#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Polyglot Empty-Task Sequence Runtime Overhead Micro-Benchmark (`test_sequence_overhead.py`).

Exact polyglot counterpart of `tests/benchmarks/sequence_overhead.cpp` from StreamPU, supporting:
  - `CPP`       : Native C++ empty codelet (`empty_kernel_arity<N>` with `noinline` + `asm volatile`)
  - `JL_UNSAFE` : Julia `Stateless_Julia` (`jl_safe = False`, `@cfunction` fast trampoline)
  - `JL_SAFE`   : Julia `Stateless_Julia` (`jl_safe = True`, exception-catching `@cfunction` trampoline)
  - `PY_NUMBA`  : Numba `@njit(nogil=True, fastmath=True)` compiled to a zero-GIL `@cfunc` trampoline
  - `PY_NUMPY`  : Python codelet materializing each task socket's cached 2D NumPy `.wave` view
  - `PY_RAW`    : Pure Python codelet materializing each task socket's cached 1D `.memoryview`

Supports the same CLI flags (`-e`, `-d`, `-b`, `-C`, `-r`, `-R`, `-F`), the same 2-line per-case
granularity (`ns/stm` and `ns/tsk`), and automatic switching between:
  - Mode 1 (Multi-Backend Average Comparison) when multiple backends are active
  - Mode 2 (Single-Backend Full HDR Real-Time Percentiles: `AVG`, `TICKS`, `STD`, `P50`..`P99.99`, `MAX`)
    when a single backend is selected via `-b <BACKEND>`.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from typing import Callable, Dict, List, Optional, Sequence as PySequence, Tuple

import numpy as np

import streampu as spu
from streampu._ext.core import _Sequence

try:
    from numba import njit

    HAS_NUMBA = True
except ImportError:
    njit = None
    HAS_NUMBA = False

HAS_JULIA = spu.julia.available()


# ==================================================================================================
# 1. Data Structures & Table Formatting (matching `sequence_overhead.cpp`)
# ==================================================================================================

@dataclass
class SeqBenchResult:
    name: str = ""
    backend: str = ""
    n_tasks: int = 0
    ns_per_frame: float = -1.0
    ns_per_task: float = -1.0
    ticks_per_frame: float = 0.0
    ticks_per_task: float = 0.0
    std_ns_per_frame: float = 0.0
    p50_ns_per_frame: float = 0.0
    p99_ns_per_frame: float = 0.0
    p999_ns_per_frame: float = 0.0
    p9999_ns_per_frame: float = 0.0
    max_ns_per_frame: float = 0.0

    @classmethod
    def from_dict(cls, name: str, backend: str, d: dict) -> "SeqBenchResult":
        return cls(
            name=name,
            backend=backend,
            n_tasks=int(d["n_tasks"]),
            ns_per_frame=float(d["ns_per_frame"]),
            ns_per_task=float(d["ns_per_task"]),
            ticks_per_frame=float(d["ticks_per_frame"]),
            ticks_per_task=float(d["ticks_per_task"]),
            std_ns_per_frame=float(d["std_ns_per_frame"]),
            p50_ns_per_frame=float(d["p50_ns_per_frame"]),
            p99_ns_per_frame=float(d["p99_ns_per_frame"]),
            p999_ns_per_frame=float(d["p999_ns_per_frame"]),
            p9999_ns_per_frame=float(d["p9999_ns_per_frame"]),
            max_ns_per_frame=float(d["max_ns_per_frame"]),
        )


def fmt_ns(ns_val: float) -> str:
    return f"{ns_val:9.2f} ns"


def print_multi_header(title: str, cols: PySequence[str]):
    col_hdr = " | ".join(f"{c:>12}" for c in cols)
    sep_line = "-+-".join("-" * 12 for _ in cols)
    total_w = 57 + 4 + len(col_hdr)
    bold = spu.rang.style.bold
    reset = spu.rang.style.reset
    print("#")
    print(f"# {bold}{'=' * total_w}{reset}")
    print(f"#  {bold}{title}{reset}")
    print(f"# {bold}{'-' * total_w}{reset}")
    print(f"#  {bold}{'BENCHMARK CASE':<39} | TASKS | UNIT   || {col_hdr}{reset}")
    print(f"#  {bold}{'-' * 39}-+-------+--------++-{sep_line}{reset}")


def print_multi_row(label: str, n_tasks: int, results: PySequence[SeqBenchResult]):
    lbl = label[:39]
    # Line 1: Per Stream (ns/stm)
    cells_stm = [
        f"{'N/A':>12}" if r.ns_per_frame < 0.0 else f"{fmt_ns(r.ns_per_frame):>12}"
        for r in results
    ]
    print(f"#  {lbl:<39} | {n_tasks:5d} | ns/stm || " + " | ".join(cells_stm))

    # Line 2: Per Task (ns/tsk)
    cells_tsk = [
        f"{'N/A':>12}" if r.ns_per_task < 0.0 else f"{fmt_ns(r.ns_per_task):>12}"
        for r in results
    ]
    print(f"#  {'':<39} | {n_tasks:5d} | ns/tsk || " + " | ".join(cells_tsk))


def print_single_rt_header(title: str, backend: str):
    hdr_line = (
        "BENCHMARK CASE                          | TASKS | UNIT   ||   AVG(ns) |     TICKS ||   STD(ns) | "
        "  P50(ns) |   P99(ns) | P99.9(ns) |P99.99(ns) |   MAX(ns)"
    )
    sep_line = (
        "----------------------------------------+-------+--------++-----------+-----------++-----------+-"
        "----------+-----------+-----------+-----------+----------"
    )
    total_w = 1 + len(hdr_line)
    bold = spu.rang.style.bold
    reset = spu.rang.style.reset
    print("#")
    print(f"# {bold}{'=' * total_w}{reset}")
    print(f"#  {bold}{title} [Backend: {backend}]{reset}")
    print(f"# {bold}{'-' * total_w}{reset}")
    print(f"#  {bold}{hdr_line}{reset}")
    print(f"#  {bold}{sep_line}{reset}")


def print_single_rt_row(label: str, r: SeqBenchResult):
    if r.ns_per_task < 0.0:
        return
    d = float(max(1, r.n_tasks))
    lbl = label[:39]

    # Line 1: Per Stream (ns/stm)
    print(
        f"#  {lbl:<39} | {r.n_tasks:5d} | ns/stm || "
        f"{r.ns_per_frame:9.2f} | {r.ticks_per_frame:9.2f} || "
        f"{r.std_ns_per_frame:9.2f} | {r.p50_ns_per_frame:9.2f} | "
        f"{r.p99_ns_per_frame:9.2f} | {r.p999_ns_per_frame:9.2f} | "
        f"{r.p9999_ns_per_frame:9.2f} | {r.max_ns_per_frame:9.2f}"
    )

    # Line 2: Per Task (ns/tsk)
    print(
        f"#  {'':<39} | {r.n_tasks:5d} | ns/tsk || "
        f"{r.ns_per_task:9.2f} | {r.ticks_per_task:9.2f} || "
        f"{r.std_ns_per_frame / d:9.2f} | {r.p50_ns_per_frame / d:9.2f} | "
        f"{r.p99_ns_per_frame / d:9.2f} | {r.p999_ns_per_frame / d:9.2f} | "
        f"{r.p9999_ns_per_frame / d:9.2f} | {r.max_ns_per_frame / d:9.2f}"
    )


def print_header(title: str, backends: PySequence[str]):
    if len(backends) == 1:
        print_single_rt_header(title, backends[0])
    else:
        print_multi_header(title, backends)


def print_row(label: str, n_tasks: int, results: PySequence[SeqBenchResult]):
    if len(results) == 1:
        print_single_rt_row(label, results[0])
    else:
        print_multi_row(label, n_tasks, results)


# ==================================================================================================
# 2. Empty Codelets for Numba, Julia, NumPy (`.wave`) and Pure Python (`.memoryview`)
# ==================================================================================================

_NUMBA_EMPTY_CACHE: Dict[int, object] = {}
_JL_EMPTY_DEFINED: set[int] = set()
_PY_MV_EMPTY_CACHE: Dict[int, Callable] = {}
_PY_NP_EMPTY_CACHE: Dict[int, Callable] = {}


def get_numba_empty_kernel(n_scks: int):
    """Return a cached `@njit(nogil=True, fastmath=True)` empty kernel accepting `n_scks` socket views."""
    if not HAS_NUMBA:
        raise RuntimeError("Numba is not installed in the current Python environment.")
    if n_scks not in _NUMBA_EMPTY_CACHE:
        args_str = ", ".join(f"s{i}" for i in range(n_scks))
        ns = {"njit": njit, "np": np}
        src = (
            "@njit(nogil=True, fastmath=True)\n"
            f"def _empty_nb_{n_scks}({args_str}):\n"
            "    return np.int32(0)\n"
        )
        exec(src, ns)
        _NUMBA_EMPTY_CACHE[n_scks] = ns[f"_empty_nb_{n_scks}"]
    return _NUMBA_EMPTY_CACHE[n_scks]


def get_julia_empty_codelet(n_scks: int) -> Tuple[str, str]:
    """Return `(julia_code, func_name)` for an empty Julia codelet taking `n_scks` sockets + `(f, w)`."""
    if not HAS_JULIA:
        raise RuntimeError("pyStreamPU is not compiled with Julia support (SPU_LINK_JULIA=ON).")
    fn_name = f"_spu_bench_empty_jl_{n_scks}"
    if n_scks not in _JL_EMPTY_DEFINED:
        sck_args = ", ".join(f"s{i}" for i in range(n_scks))
        all_args = f"{sck_args}, f, w" if sck_args else "f, w"
        code = f"{fn_name}({all_args}) = Int32(0)"
        spu.julia.eval(code)
        _JL_EMPTY_DEFINED.add(n_scks)
    return "", fn_name


def _empty_py_bare(mdl, tsk, frame_id):
    return 0


def get_py_mv_empty_codelet(n_scks: int) -> Callable:
    """Return a pure-Python codelet that materializes `tsk[f's{i}'].memoryview` for each data socket."""
    if n_scks not in _PY_MV_EMPTY_CACHE:
        if n_scks == 0:
            _PY_MV_EMPTY_CACHE[0] = _empty_py_bare
        else:
            lines = [f"def _empty_py_mv_{n_scks}(mdl, tsk, fid):"]
            for i in range(n_scks):
                lines.append(f'    _ = tsk["s{i}"].memoryview')
            lines.append("    return 0")
            ns: Dict[str, Callable] = {}
            exec("\n".join(lines), ns)
            _PY_MV_EMPTY_CACHE[n_scks] = ns[f"_empty_py_mv_{n_scks}"]
    return _PY_MV_EMPTY_CACHE[n_scks]


def get_py_numpy_empty_codelet(n_scks: int) -> Callable:
    """Return a Python codelet that materializes `tsk[f's{i}'].wave` (2D NumPy view) for each data socket."""
    if n_scks not in _PY_NP_EMPTY_CACHE:
        if n_scks == 0:
            _PY_NP_EMPTY_CACHE[0] = _empty_py_bare
        else:
            lines = [f"def _empty_py_np_{n_scks}(mdl, tsk, fid):"]
            for i in range(n_scks):
                lines.append(f'    _ = tsk["s{i}"].wave')
            lines.append("    return 0")
            ns: Dict[str, Callable] = {}
            exec("\n".join(lines), ns)
            _PY_NP_EMPTY_CACHE[n_scks] = ns[f"_empty_py_np_{n_scks}"]
    return _PY_NP_EMPTY_CACHE[n_scks]


# ==================================================================================================
# 3. Polyglot Empty-Task Module & Sequence Builders
# ==================================================================================================

ALL_BACKENDS = ("CPP", "JL_UNSAFE", "JL_SAFE", "PY_NUMBA", "PY_NUMPY", "PY_RAW")
DEFAULT_BACKENDS = (
    ("CPP",)
    + (("JL_UNSAFE", "JL_SAFE") if HAS_JULIA else ())
    + (("PY_NUMBA",) if HAS_NUMBA else ())
    + ("PY_NUMPY", "PY_RAW")
)

_BACKEND_ALIASES = {
    "JL": "JL_UNSAFE",
    "PY": "PY_RAW",
}


def parse_backends(backends_str: str) -> List[str]:
    out = []
    for item in backends_str.split(","):
        bu = item.strip().upper()
        if not bu:
            continue
        bu = _BACKEND_ALIASES.get(bu, bu)
        if bu == "PY_NUMBA" and not HAS_NUMBA:
            continue
        if bu in ("JL_UNSAFE", "JL_SAFE") and not HAS_JULIA:
            continue
        if bu in ALL_BACKENDS:
            out.append(bu)
    return out


def make_empty_module(
    backend: str,
    socket_spec: PySequence[Tuple[str, str]],
    data_length: int,
    n_frames: int = 1,
    n_frames_per_wave: int = 1,
    capture_mode: int = 0,
):
    b = _BACKEND_ALIASES.get(backend.upper(), backend.upper())
    n_scks = len(socket_spec)

    if b in ("JL_UNSAFE", "JL_SAFE"):
        if not HAS_JULIA:
            raise RuntimeError("pyStreamPU is not compiled with Julia support (SPU_LINK_JULIA=ON).")
        mdl = spu.Stateless_Julia()
        mdl.n_frames = n_frames
        mdl.n_frames_per_wave = n_frames_per_wave
        mdl.jl_safe = b == "JL_SAFE"
        t = mdl.create_task("exec")
        t.replicable = True
        for direction, name in socket_spec:
            if direction == "IN":
                mdl.create_socket_in(t, name, data_length, spu.uint8)
            elif direction == "OUT":
                mdl.create_socket_out(t, name, data_length, spu.uint8)
            elif direction == "FWD":
                mdl.create_socket_fwd(t, name, data_length, spu.uint8)
            else:
                raise ValueError(f"Unknown direction: {direction}")
        code, fn_name = get_julia_empty_codelet(n_scks)
        mdl.create_codelet(t, code, fn_name)
        return mdl

    mdl = spu.Stateless()
    mdl.n_frames = n_frames
    mdl.n_frames_per_wave = n_frames_per_wave
    t = mdl.create_task("exec")
    t.replicable = True
    for direction, name in socket_spec:
        if direction == "IN":
            mdl.create_socket_in(t, name, data_length, spu.uint8)
        elif direction == "OUT":
            mdl.create_socket_out(t, name, data_length, spu.uint8)
        elif direction == "FWD":
            mdl.create_socket_fwd(t, name, data_length, spu.uint8)
        else:
            raise ValueError(f"Unknown direction: {direction}")

    if b == "CPP":
        mdl.create_codelet_empty(t, capture_mode)
    elif b == "PY_NUMBA":
        mdl.create_codelet(t, get_numba_empty_kernel(n_scks))
    elif b == "PY_BARE":
        mdl.create_codelet(t, _empty_py_bare)
    elif b == "PY_RAW":
        mdl.create_codelet(t, get_py_mv_empty_codelet(n_scks))
    elif b == "PY_NUMPY":
        mdl.create_codelet(t, get_py_numpy_empty_codelet(n_scks))
    else:
        raise ValueError(f"Unsupported backend: {backend}")

    return mdl


def build_chain(
    backends: PySequence[str],
    topology: str,
    data_length: int,
    n_scks_per_task: int = 1,
    n_threads: int = 1,
    no_copy_mode: bool = True,
    fast_mode: bool = True,
    stats_mode: bool = False,
    n_frames: int = 1,
    n_frames_per_wave: int = 1,
    capture_mode: int = 0,
):
    chain_len = len(backends)
    mods = []

    for i, b in enumerate(backends):
        if topology == "0SCK":
            spec = []
        elif topology == "SFWD":
            if i == 0:
                spec = [("OUT", f"s{s}") for s in range(n_scks_per_task)]
            elif i + 1 < chain_len:
                spec = [("FWD", f"s{s}") for s in range(n_scks_per_task)]
            else:
                spec = [("IN", f"s{s}") for s in range(n_scks_per_task)]
        elif topology == "SINOUT":
            if i == 0:
                spec = [("OUT", "s0")]
            elif i + 1 < chain_len:
                spec = [("IN", "s0"), ("OUT", "s1")]
            else:
                spec = [("IN", "s0")]
        else:
            raise ValueError(f"Unknown topology: {topology}")

        m = make_empty_module(
            b,
            spec,
            data_length=data_length,
            n_frames=n_frames,
            n_frames_per_wave=n_frames_per_wave,
            capture_mode=capture_mode,
        )
        m.custom_name = f"{b}_{i}"
        mods.append(m)

    for i in range(chain_len - 1):
        t_cur = mods[i]["exec"]
        t_nxt = mods[i + 1]["exec"]
        if topology == "0SCK":
            t_nxt.bind(t_cur)
        elif topology == "SFWD":
            for s in range(n_scks_per_task):
                t_nxt[f"s{s}"].bind(t_cur[f"s{s}"])
        elif topology == "SINOUT":
            out_name = "s0" if i == 0 else "s1"
            t_nxt["s0"].bind(t_cur[out_name])

    seq = spu.Sequence(mods[0]["exec"], n_threads=n_threads)
    seq.n_frames = n_frames
    seq.no_copy_mode = no_copy_mode
    for m_group in seq.get_modules_per_types():
        for m in m_group:
            m.n_frames = n_frames
            m.n_frames_per_wave = n_frames_per_wave
    for t_group in seq.get_tasks_per_types():
        for t in t_group:
            t.fast = fast_mode
            t.stats = stats_mode

    return seq, mods


def choose_n_exec(base_n_exec: int, backends: PySequence[str], scale: float = 1.0) -> int:
    has_py = any(b.upper() in ("PY", "PY_RAW", "PY_BARE", "PY_NUMPY") for b in backends)
    has_jl_safe = any(b.upper() == "JL_SAFE" for b in backends)
    raw = max(1, int(base_n_exec * scale))
    if base_n_exec < 5000:
        return raw
    if has_py or has_jl_safe:
        return max(5000, min(raw, 50000))
    return max(10000, raw)


def measure_sequence_bench(
    name: str,
    backend: str,
    seq: spu.Sequence,
    n_exec: int,
    collect_rt_percentiles: bool,
    n_warmup: int = 256,
    rt_skip: int = 0,
    with_statuses: bool = False,
    task_divisor_override: int = 0,
    per_thread: bool = False,
) -> SeqBenchResult:
    d = _Sequence.measure_bench(
        seq,
        n_exec,
        collect_rt_percentiles,
        n_warmup,
        rt_skip,
        with_statuses,
        task_divisor_override,
        per_thread,
    )
    return SeqBenchResult.from_dict(name, backend, d)


# ==================================================================================================
# 4. Benchmark Suite Sections (1..7, matching `sequence_overhead.cpp`)
# ==================================================================================================

def run_all_benchmarks(
    n_exec: int = 300000,
    data_length: int = 64,
    backends_str: str = ",".join(DEFAULT_BACKENDS),
    csv_path: str = "",
    n_warmup: int = 256,
    show_full_rt_tables: bool = False,
    rt_skip: int = 0,
    rt_frames: bool = False,
) -> List[Dict[str, object]]:
    spu.Signal_handler.init()
    backends = parse_backends(backends_str)
    if not backends:
        raise ValueError(f"No valid backends selected from '{backends_str}'.")

    if HAS_JULIA and any(b in ("JL_UNSAFE", "JL_SAFE") for b in backends):
        spu.julia.init(256)

    single_backend_rt_mode = len(backends) == 1
    has_cpp = "CPP" in backends
    has_numba = "PY_NUMBA" in backends
    has_py_any = any(b in ("PY_NUMPY", "PY_RAW") for b in backends)
    csv_rows: List[Dict[str, object]] = []

    def append_csv(section: str, case_name: str, r: SeqBenchResult):
        csv_rows.append(
            {
                "section": section,
                "case": case_name,
                "backend": r.backend,
                "n_tasks": r.n_tasks,
                "ns_per_frame": r.ns_per_frame,
                "ns_per_task": r.ns_per_task,
                "ticks_per_frame": r.ticks_per_frame,
                "ticks_per_task": r.ticks_per_task,
                "std_ns_per_frame": r.std_ns_per_frame,
                "p50_ns_per_frame": r.p50_ns_per_frame,
                "p99_ns_per_frame": r.p99_ns_per_frame,
                "p999_ns_per_frame": r.p999_ns_per_frame,
                "p9999_ns_per_frame": r.p9999_ns_per_frame,
                "max_ns_per_frame": r.max_ns_per_frame,
            }
        )

    print("#######################################################################")
    print("# StreamPU Empty-Task Runtime Overhead Benchmark (sequence_overhead)  #")
    print("#######################################################################")
    print(f"#   - base n_exec  = {n_exec} (scaled for JL_SAFE / PY / long chains)")
    print(f"#   - data_length  = {data_length} bytes")
    print(f"#   - n_warmup     = {n_warmup}")
    print(f"#   - rt_skip      = {rt_skip}")
    print(f"#   - has_julia    = {'true' if HAS_JULIA else 'false'}")
    print(f"#   - has_numba    = {'true' if HAS_NUMBA else 'false'}")
    print(f"#   - backends     = {', '.join(backends)}")
    print(
        "#   - display mode = "
        + (
            "Single-Backend Full RT Percentiles (AVG, STD, P50..P99.99, MAX)"
            if single_backend_rt_mode
            else "Multi-Backend Average Comparison (pass -b <BACKEND> for RT percentiles)"
        )
    )

    # ----------------------------------------------------------------------------------------------
    # SECTION 1: Baseline & Socket Types (8 empty tasks per sequence)
    # ----------------------------------------------------------------------------------------------
    print_header("1. BASELINE & SOCKET TYPES (8 empty tasks per sequence)", backends)

    if has_cpp or has_py_any:
        bare_cpp_r = SeqBenchResult()
        if has_cpp:
            d_bare = _Sequence.bench_bare_cpp_call(n_exec, 8, single_backend_rt_mode, n_warmup, rt_skip)
            bare_cpp_r = SeqBenchResult.from_dict("Bare call (C++ noinline)", "CPP", d_bare)
            append_csv("1_socket_types", "Bare call (C++ noinline)", bare_cpp_r)

        bare_py_r = SeqBenchResult()
        if has_py_any:
            seq_py_bare, mods_py_bare = build_chain(["PY_BARE"] * 8, "SFWD", data_length)
            ne_py_bare = choose_n_exec(n_exec, ["PY_BARE"])
            bare_py_r = measure_sequence_bench(
                "Bare call (PY return 0)", "PY_RAW", seq_py_bare, ne_py_bare, single_backend_rt_mode, n_warmup, rt_skip
            )
            del seq_py_bare, mods_py_bare

        baseline_cells = []
        for b in backends:
            if b == "CPP":
                baseline_cells.append(bare_cpp_r)
            elif b in ("PY_NUMPY", "PY_RAW"):
                r_copy = SeqBenchResult(**{**bare_py_r.__dict__, "backend": b})
                baseline_cells.append(r_copy)
                append_csv("1_socket_types", "Bare call (PY return 0)", r_copy)
            else:
                baseline_cells.append(SeqBenchResult())
        print_row("Bare call (C++ noinline / PY return 0)", 8, baseline_cells)

    cases_sec1 = [
        ("0-socket task-bound chain (status only)", "0SCK", True),
        ("SFWD chain (1x OUT, 6x FWD, 1x IN)", "SFWD", True),
        ("SIN+SOUT chain (no_copy_mode=true)", "SINOUT", True),
        ("SIN+SOUT chain (no_copy_mode=false)", "SINOUT", False),
    ]
    for label, topo, no_copy in cases_sec1:
        row_vals = []
        for b in backends:
            seq, mods = build_chain([b] * 8, topo, data_length, no_copy_mode=no_copy)
            ne = choose_n_exec(n_exec, [b])
            res = measure_sequence_bench(label, b, seq, ne, single_backend_rt_mode, n_warmup, rt_skip)
            row_vals.append(res)
            append_csv("1_socket_types", label, res)

            if show_full_rt_tables and topo == "SFWD" and b in ("CPP", "JL_UNSAFE", "PY_NUMBA"):
                _Sequence.reset_rt_stats(seq)
                _Sequence.set_rt_stats(seq, True, rt_skip)
                _Sequence.exec_n_times(seq, ne, False, False)
                _Sequence.show_rt_stats(seq, True, rt_frames)

            del seq, mods
        print_row(label, 8, row_vals)

    # ----------------------------------------------------------------------------------------------
    # SECTION 2: Number of Sockets per Task (1, 2, 4, 8, 16 sockets, SFWD no_copy_mode=true)
    # ----------------------------------------------------------------------------------------------
    print_header("2. NUMBER OF SOCKETS PER TASK (8 tasks, SFWD no_copy_mode=true)", backends)
    for n_scks in (1, 2, 4, 8, 16):
        label = f"{n_scks} socket(s) per task"
        row_vals = []
        for b in backends:
            seq, mods = build_chain([b] * 8, "SFWD", data_length, n_scks_per_task=n_scks, no_copy_mode=True)
            ne = choose_n_exec(n_exec, [b])
            res = measure_sequence_bench(label, b, seq, ne, single_backend_rt_mode, n_warmup, rt_skip)
            row_vals.append(res)
            append_csv("2_n_sockets", label, res)
            del seq, mods
        print_row(label, 8, row_vals)

    # ----------------------------------------------------------------------------------------------
    # SECTION 3: C++ Lambda Capture, Julia Stateful Args & Numba extra_args (8 tasks, SFWD)
    # ----------------------------------------------------------------------------------------------
    print_header("3. C++ LAMBDA CAPTURE & JULIA/NUMBA STATEFUL ARGS (8 tasks, SFWD)", backends)
    if has_cpp:
        capture_cases = [
            (0, "0-byte capture [] (fast_codelet)"),
            (1, "8-byte capture [ptr] (fast_codelet)"),
            (2, "16-byte capture [2x size_t] (fast)"),
            (3, "64-byte capture [8x size_t] (fast max)"),
            (4, "Non-trivial capture (std::function)"),
        ]
        for cap_mode, label in capture_cases:
            seq, mods = build_chain(["CPP"] * 8, "SFWD", data_length, capture_mode=cap_mode)
            ne = choose_n_exec(n_exec, ["CPP"])
            res = measure_sequence_bench(label, "CPP", seq, ne, single_backend_rt_mode, n_warmup, rt_skip)
            row_vals = [res if b == "CPP" else SeqBenchResult() for b in backends]
            print_row(label, 8, row_vals)
            append_csv("3_cpp_capture_and_jl_state", label, res)
            del seq, mods

    if HAS_JULIA and any(b in ("JL_UNSAFE", "JL_SAFE") for b in backends):
        spu.julia.eval(
            """
            if !isdefined(Main, :_SpuEmptyBenchState)
                mutable struct _SpuEmptyBenchState
                    v::Int64
                end
            end
            """
        )
        for n_states in (0, 1, 2):
            for n_consts in (0, 2):
                label = f"Stateful_Julia: {n_states} state(s), {n_consts} const(s)"
                fn_name = f"_spu_bench_st_{n_states}_{n_consts}"
                st_args = "".join(f"stt_{st}, " for st in range(n_states))
                cst_args = "".join(f"cst_{c}, " for c in range(n_consts))
                spu.julia.eval(f"{fn_name}({st_args}s0, {cst_args}rnt_frame_id, rnt_n_frames_per_wave) = Int32(0)")

                row_vals = []
                for b in backends:
                    if b not in ("JL_UNSAFE", "JL_SAFE"):
                        row_vals.append(SeqBenchResult())
                        continue
                    mods = []
                    for i in range(8):
                        m = spu.Stateful_Julia()
                        m.jl_safe = b == "JL_SAFE"
                        for st in range(n_states):
                            m.create_state(f"_SpuEmptyBenchState({st})", False)
                        t = m.create_task("exec")
                        if i == 0:
                            m.create_socket_out(t, "s0", data_length, spu.uint8)
                        elif i < 7:
                            m.create_socket_fwd(t, "s0", data_length, spu.uint8)
                        else:
                            m.create_socket_in(t, "s0", data_length, spu.uint8)
                        for c in range(n_consts):
                            m.create_constant(t, c, spu.uint32)
                        m.create_codelet(t, "", fn_name)
                        mods.append(m)
                    for i in range(7):
                        mods[i + 1]["exec"]["s0"].bind(mods[i]["exec"]["s0"])

                    seq = spu.Sequence(mods[0]["exec"], 1)
                    seq.no_copy_mode = True
                    for t_group in seq.get_tasks_per_types():
                        for t in t_group:
                            t.fast = True

                    ne = choose_n_exec(n_exec, [b])
                    res = measure_sequence_bench(label, b, seq, ne, single_backend_rt_mode, n_warmup, rt_skip)
                    row_vals.append(res)
                    append_csv("3_cpp_capture_and_jl_state", label, res)
                    del seq, mods
                print_row(label, 8, row_vals)

    if HAS_NUMBA and has_numba:
        for n_states in (0, 1, 2):
            for n_consts in (0, 2):
                label = f"Numba extra: {n_states} state(s), {n_consts} const(s)"
                n_extra = n_states + n_consts
                arg_list = ["s0"] + [f"e{k}" for k in range(n_extra)]
                ns_nb = {"njit": njit, "np": np}
                fn_nb_name = f"_nb_bench_st_{n_states}_{n_consts}"
                exec(
                    f"@njit(nogil=True, fastmath=True)\n"
                    f"def {fn_nb_name}({', '.join(arg_list)}):\n"
                    f"    return np.int32(0)\n",
                    ns_nb,
                )
                nb_kernel = ns_nb[fn_nb_name]

                mods = []
                state_keepalive = []
                for i in range(8):
                    m = spu.Stateless()
                    t = m.create_task("exec")
                    if i == 0:
                        m.create_socket_out(t, "s0", data_length, spu.uint8)
                    elif i < 7:
                        m.create_socket_fwd(t, "s0", data_length, spu.uint8)
                    else:
                        m.create_socket_in(t, "s0", data_length, spu.uint8)

                    extras = [np.zeros(8, dtype=np.int64) for _ in range(n_states)] + [
                        int(c) for c in range(n_consts)
                    ]
                    state_keepalive.append(extras)
                    m.create_codelet(
                        t,
                        spu.numba_codelet(
                            nb_kernel,
                            extra_args=(lambda ex=extras: (lambda _m, _w: ex))(),
                            extra_before_sockets=False,
                        ),
                    )
                    mods.append(m)

                for i in range(7):
                    mods[i + 1]["exec"]["s0"].bind(mods[i]["exec"]["s0"])

                seq = spu.Sequence(mods[0]["exec"], 1)
                seq.no_copy_mode = True
                for t_group in seq.get_tasks_per_types():
                    for t in t_group:
                        t.fast = True

                ne = choose_n_exec(n_exec, ["PY_NUMBA"])
                res = measure_sequence_bench(label, "PY_NUMBA", seq, ne, single_backend_rt_mode, n_warmup, rt_skip)
                row_vals = [res if b == "PY_NUMBA" else SeqBenchResult() for b in backends]
                print_row(label, 8, row_vals)
                append_csv("3_cpp_capture_and_jl_state", label, res)
                del seq, mods, state_keepalive

    # ----------------------------------------------------------------------------------------------
    # SECTION 4: Task & Sequence Execution Modes (8 empty tasks, SFWD)
    # ----------------------------------------------------------------------------------------------
    print_header("4. TASK & SEQUENCE EXECUTION MODES (8 empty tasks, SFWD)", backends)
    mode_cases = [
        ("fast=true, _exec_without_statuses", True, False, False, 1.0),
        ("fast=true, _exec (with statuses)", True, True, False, 1.0),
        ("fast=false (full checks & fill)", False, False, False, 1.0),
        ("stats=true (per-task steady_clock)", True, False, True, 0.25),
    ]
    for label, fast_m, with_st, stats_m, scale in mode_cases:
        row_vals = []
        for b in backends:
            seq, mods = build_chain([b] * 8, "SFWD", data_length, fast_mode=fast_m, stats_mode=stats_m)
            ne = choose_n_exec(n_exec, [b], scale=scale)
            res = measure_sequence_bench(
                label, b, seq, ne, single_backend_rt_mode, n_warmup, rt_skip, with_statuses=with_st
            )
            row_vals.append(res)
            append_csv("4_exec_modes", label, res)
            del seq, mods
        print_row(label, 8, row_vals)

    # ----------------------------------------------------------------------------------------------
    # SECTION 5: Sequence Chain Length Scaling (2, 4, 8, 16, 32, 64, 128 tasks)
    # ----------------------------------------------------------------------------------------------
    print_header("5. SEQUENCE CHAIN LENGTH SCALING (amortization of Sequence loop)", backends)
    for chain_len in (2, 4, 8, 16, 32, 64, 128):
        label = f"Chain length = {chain_len} tasks"
        scale = 8.0 / float(chain_len)
        row_vals = []
        for b in backends:
            seq, mods = build_chain([b] * chain_len, "SFWD", data_length)
            ne = choose_n_exec(n_exec, [b], scale=scale)
            res = measure_sequence_bench(label, b, seq, ne, single_backend_rt_mode, n_warmup, rt_skip)
            row_vals.append(res)
            append_csv("5_chain_length", label, res)
            del seq, mods
        print_row(label, chain_len, row_vals)

    # ----------------------------------------------------------------------------------------------
    # SECTION 6: Multi-Wave Execution (8 tasks, n_waves = 1, 2, 4, 8)
    # ----------------------------------------------------------------------------------------------
    print_header("6. MULTI-WAVE EXECUTION (8 tasks, n_frames = n_waves, n_frames_per_wave ou fpw = 1)", backends)
    for n_waves in (1, 2, 4, 8):
        label = f"n_waves = {n_waves} (n_frames={n_waves}, fpw=1)"
        scale = 1.0 / float(n_waves)
        row_vals = []
        for b in backends:
            seq, mods = build_chain([b] * 8, "SFWD", data_length, n_frames=n_waves, n_frames_per_wave=1)
            ne = choose_n_exec(n_exec, [b], scale=scale)
            res = measure_sequence_bench(
                label, b, seq, ne, single_backend_rt_mode, n_warmup, rt_skip, task_divisor_override=8 * n_waves
            )
            row_vals.append(res)
            append_csv("6_multi_wave", label, res)
            del seq, mods
        print_row(label, 8 * n_waves, row_vals)

    # ----------------------------------------------------------------------------------------------
    # SECTION 7: Multi-Thread, Heterogeneous & Control Flow
    # ----------------------------------------------------------------------------------------------
    print_header("7. MULTI-THREAD EFFECTIVE LATENCY & CONTROL FLOW", backends)
    for n_threads in (1, 2, 4):
        label = f"Threads = {n_threads} (homogeneous 8 tasks)"
        row_vals = []
        for b in backends:
            seq, mods = build_chain([b] * 8, "SFWD", data_length, n_threads=n_threads)
            ne = choose_n_exec(n_exec, [b], scale=float(n_threads))
            res = measure_sequence_bench(
                label, b, seq, ne, single_backend_rt_mode, n_warmup, rt_skip, per_thread=True
            )
            row_vals.append(res)
            append_csv("7_multithread_and_ctrl", label, res)
            del seq, mods
        print_row(label, 8, row_vals)

    # Heterogeneous chains (CPP+JL_UNSAFE, CPP+PY_NUMBA, CPP+JL_UNSAFE+PY_NUMBA)
    het_configs = []
    if HAS_JULIA and has_cpp and "JL_UNSAFE" in backends:
        het_configs.append(
            ("CPP+JL_UNSAFE", ["CPP", "JL_UNSAFE"] * 4, "mixed CPP + JL_UNSAFE")
        )
    if HAS_NUMBA and has_cpp and has_numba:
        het_configs.append(
            ("CPP+PY_NUMBA", ["CPP", "PY_NUMBA"] * 4, "mixed CPP + PY_NUMBA")
        )
    if HAS_JULIA and HAS_NUMBA and has_cpp and "JL_UNSAFE" in backends and has_numba:
        het_configs.append(
            (
                "CPP+JL+PY_NUMBA",
                ["CPP", "PY_NUMBA", "JL_UNSAFE", "CPP", "PY_NUMBA", "JL_UNSAFE", "CPP", "PY_NUMBA"],
                "mixed CPP + JL_UNSAFE + PY_NUMBA",
            )
        )

    for het_tag, het_pattern, het_desc in het_configs:
        for n_threads in (1, 4):
            seq, mods = build_chain(het_pattern, "SFWD", data_length, n_threads=n_threads)
            ne = choose_n_exec(n_exec, het_pattern, scale=float(n_threads))
            label = f"Heterogeneous ({het_tag}, t={n_threads})"
            res = measure_sequence_bench(label, "MIXED", seq, ne, False, n_warmup, rt_skip, per_thread=True)
            print(f"#  {label[:39]:<39} |     8 | ns/stm || {fmt_ns(res.ns_per_frame):>12} ({het_desc})")
            print(f"#  {'':<39} |     8 | ns/tsk || {fmt_ns(res.ns_per_task):>12} ({het_desc})")
            append_csv("7_multithread_and_ctrl", label, res)
            del seq, mods

    # Switcher commute + select control flow (6 tasks executed along path 0: ctrl_gen, src, commute, branch0, select, snk)
    for no_copy in (True, False):
        label = f"Switcher commute+select ({'no_copy=true)' if no_copy else 'no_copy=false)'}"
        row_vals = []
        for b in backends:
            src = make_empty_module(b, [("OUT", "s0")], data_length)
            ctrl_gen = spu.Stateless()
            t_ctrl = ctrl_gen.create_task("exec")
            ctrl_gen.create_socket_out(t_ctrl, "ctrl", 1, spu.int8)
            ctrl_gen.create_codelet_empty(t_ctrl, -1)

            switcher = spu.Switcher(2, data_length, spu.uint8)
            branch0 = make_empty_module(b, [("IN", "s0"), ("OUT", "s1")], data_length)
            branch1 = make_empty_module(b, [("IN", "s0"), ("OUT", "s1")], data_length)
            snk = make_empty_module(b, [("IN", "s0")], data_length)

            src["exec"].bind(ctrl_gen["exec"])
            switcher["commute"]["in_data"].bind(src["exec"]["s0"])
            switcher["commute"]["in_ctrl"].bind(ctrl_gen["exec"]["ctrl"])
            branch0["exec"]["s0"].bind(switcher["commute"]["out_data0"])
            branch1["exec"]["s0"].bind(switcher["commute"]["out_data1"])
            switcher["select"]["in_data0"].bind(branch0["exec"]["s1"])
            switcher["select"]["in_data1"].bind(branch1["exec"]["s1"])
            snk["exec"]["s0"].bind(switcher["select"]["out_data"])

            seq = spu.Sequence(ctrl_gen["exec"], 1)
            seq.no_copy_mode = no_copy
            for t_group in seq.get_tasks_per_types():
                for t in t_group:
                    t.fast = True

            ne = choose_n_exec(n_exec, [b])
            res = measure_sequence_bench(
                label, b, seq, ne, single_backend_rt_mode, n_warmup, rt_skip, task_divisor_override=6
            )
            row_vals.append(res)
            append_csv("7_multithread_and_ctrl", label, res)
            del seq, src, ctrl_gen, switcher, branch0, branch1, snk
        print_row(label, 6, row_vals)

    if csv_path:
        fieldnames = [
            "section",
            "case",
            "backend",
            "n_tasks",
            "ns_per_frame",
            "ns_per_task",
            "ticks_per_frame",
            "ticks_per_task",
            "std_ns_per_frame",
            "p50_ns_per_frame",
            "p99_ns_per_frame",
            "p999_ns_per_frame",
            "p9999_ns_per_frame",
            "max_ns_per_frame",
        ]
        with open(csv_path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(csv_rows)
        print(f"# Wrote CSV results to {csv_path}")

    print("#")
    print(
        f"# {spu.rang.style.bold}{spu.rang.fg.green}"
        f"Empty-task sequence overhead breakdown completed!{spu.rang.style.reset}"
    )
    return csv_rows


# ==================================================================================================
# 5. Pytest Smoke Test & CLI Entrypoint
# ==================================================================================================

def test_sequence_overhead():
    """Fast pytest smoke test verifying all sections and available backends of `test_sequence_overhead`."""
    rows = run_all_benchmarks(n_exec=50, data_length=64, n_warmup=16)
    assert len(rows) > 0
    assert all(float(r["ns_per_task"]) > 0.0 for r in rows)


def parse_args():
    default_backends_str = ",".join(DEFAULT_BACKENDS)
    parser = argparse.ArgumentParser(
        description="StreamPU Empty-Task Sequence Runtime Overhead Benchmark (C++ / Julia / Numba / NumPy / Python).",
        add_help=True,
    )
    parser.add_argument(
        "-e",
        "--n-exec",
        type=int,
        default=300000,
        help="Base number of sequence executions per benchmark [300000]",
    )
    parser.add_argument(
        "-d",
        "--data-length",
        type=int,
        default=64,
        help="Socket buffer length in bytes [64]",
    )
    parser.add_argument(
        "-b",
        "--backends",
        type=str,
        default=default_backends_str,
        help=f"Backends (1 backend => full RT percentiles/MAX) [{default_backends_str}]",
    )
    parser.add_argument(
        "-C",
        "--csv",
        type=str,
        default="",
        help="Optional path to export benchmark results as CSV [none]",
    )
    parser.add_argument(
        "-W",
        "--warmup",
        type=int,
        default=256,
        help="Number of warmup streams before each benchmark [256]",
    )
    parser.add_argument(
        "-r",
        "--rt-stats",
        action="store_true",
        default=False,
        help="Also print full tools::Stats::show_rt tables [false]",
    )
    parser.add_argument(
        "-R",
        "-k",
        "--rt-skip",
        type=int,
        default=0,
        help="Number of initial frames to skip in RT [0]",
    )
    parser.add_argument(
        "-F",
        "--rt-frames",
        action="store_true",
        default=False,
        help="Display RT throughput in frames/s [false]",
    )
    return parser.parse_args()


if __name__ == "__main__":
    cli_args = parse_args()
    run_all_benchmarks(
        n_exec=cli_args.n_exec,
        data_length=cli_args.data_length,
        backends_str=cli_args.backends,
        csv_path=cli_args.csv,
        n_warmup=cli_args.warmup,
        show_full_rt_tables=cli_args.rt_stats,
        rt_skip=cli_args.rt_skip,
        rt_frames=cli_args.rt_frames,
    )
