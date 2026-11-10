#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Polyglot Empty-Task Pipeline Overhead Benchmark for pyStreamPU.

Direct polyglot equivalent of ``tests/benchmarks/pipeline_overhead.cpp`` in StreamPU.
Isolates the pure runtime scheduling, inter-stage synchronization (``Adaptor_m_to_n``),
zero-copy buffer swapping vs copying, and multi-stage / multi-thread scaling overhead
of ``spu.Pipeline`` across all supported task languages:
  1. C++          : Native C++ codelet with non-inlinable empty kernel + compiler barrier
  2. Julia Unsafe : ``Stateless_Julia(jl_safe=False)`` direct ``@cfunction`` trampoline (if compiled with Julia)
  3. Julia Safe   : ``Stateless_Julia(jl_safe=True)`` GC-safe/thread-adoption trampoline (if compiled with Julia)
  4. Python Numba : ``@njit(nogil=True, fastmath=True)`` C-ABI ``@cfunc`` trampoline
  5. Python NumPy : Standard Python codelet accessing socket 2D NumPy views (``sck.wave``)
  6. Python Raw   : Standard Python codelet accessing socket 1D PEP 3118 memoryviews (``sck.memoryview``)

Can be executed either directly as a standalone benchmark CLI (matching ``pipeline_overhead``)
or via ``pytest``:
  python tests/benchmarks/test_pipeline_overhead.py --n-exec 50000
  python tests/benchmarks/test_pipeline_overhead.py -b CPP
  python tests/benchmarks/test_pipeline_overhead.py -b PY_NUMBA
  pytest tests/benchmarks/test_pipeline_overhead.py -s
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from typing import Callable, Dict, List, Sequence as PySequence, Tuple
import numpy as np

try:
    from numba import njit

    HAS_NUMBA = True
except ImportError:
    HAS_NUMBA = False

import streampu as spu

HAS_JULIA = bool(hasattr(spu, "julia") and spu.julia.available())


# ==================================================================================================
# 1. Data Structures & Table Formatting (matching tests/benchmarks/pipeline_overhead.cpp)
# ==================================================================================================


@dataclass
class PipeBenchResult:
    name: str
    backend: str
    n_stages: int = 0
    stage_ns_per_task: float = -1.0
    stage_std_ns_per_task: float = 0.0
    stage_p50_ns_per_task: float = 0.0
    stage_p99_ns_per_task: float = 0.0
    stage_p999_ns_per_task: float = 0.0
    stage_p9999_ns_per_task: float = 0.0
    stage_max_ns_per_task: float = 0.0
    out_ns_per_stream: float = -1.0
    e2e_avg_ns: float = -1.0
    e2e_std_ns: float = -1.0
    e2e_p50_ns: float = -1.0
    e2e_p99_ns: float = -1.0
    e2e_p999_ns: float = -1.0
    e2e_p9999_ns: float = -1.0
    e2e_max_ns: float = -1.0


@dataclass
class PipeCsvRow:
    section: str
    case_name: str
    res: PipeBenchResult


def fmt_ns(ns_val: float) -> str:
    if ns_val < 0.0:
        return f"{'N/A':>12}"
    return f"{ns_val:9.2f} ns"


def print_multi_header(title: str, cols: PySequence[str]):
    col_hdr = " | ".join(f"{c:>12}" for c in cols)
    sep_line = "-+-".join("-" * 12 for _ in cols)
    total_w = 60 + 4 + len(col_hdr)
    print("#")
    print(f"# {'=' * total_w}")
    print(f"#  {title}")
    print(f"# {'-' * total_w}")
    print(f"#  {'PIPELINE BENCHMARK CASE':<39} | STGS | METRIC     || {col_hdr}")
    print(f"#  {'-' * 39}-+------+------------++-{sep_line}")


def print_multi_row(label: str, n_stages: int, results: PySequence[PipeBenchResult]):
    # Line 1: End-to-End latency per stream (E2E ns/stm)
    cells_e2e = " | ".join(fmt_ns(r.e2e_avg_ns) for r in results)
    print(f"#  {label[:39]:<39} | {n_stages:4d} | E2E ns/stm || {cells_e2e}")

    # Line 2: Stage latency per task (STG ns/tsk)
    cells_stg = " | ".join(fmt_ns(r.stage_ns_per_task) for r in results)
    print(f"#  {'':<39} | {n_stages:4d} | STG ns/tsk || {cells_stg}")


def print_single_rt_header(title: str, backend: str):
    hdr_line = (
        "PIPELINE BENCHMARK CASE                 | STGS | METRIC     ||    AVG(ns) | OUT NS/STM ||    STD(ns) | "
        "   P50(ns) |    P99(ns) |  P99.9(ns) | P99.99(ns) |    MAX(ns)"
    )
    sep_line = (
        "----------------------------------------+------+------------++------------+------------++------------+-"
        "-----------+------------+------------+------------+-----------"
    )
    total_w = 1 + len(hdr_line)
    print("#")
    print(f"# {'=' * total_w}")
    print(f"#  {title} [Backend: {backend}]")
    print(f"# {'-' * total_w}")
    print(f"#  {hdr_line}")
    print(f"#  {sep_line}")


def print_single_rt_row(label: str, r: PipeBenchResult):
    if r.stage_ns_per_task < 0.0:
        return

    # Line 1: End-to-End pipeline stream latency (E2E ns/stm)
    print(
        f"#  {label[:39]:<39} | {r.n_stages:4d} | E2E ns/stm || "
        f"{r.e2e_avg_ns:10.2f} | {r.out_ns_per_stream:10.2f} || "
        f"{r.e2e_std_ns:10.2f} | {r.e2e_p50_ns:10.2f} | "
        f"{r.e2e_p99_ns:10.2f} | {r.e2e_p999_ns:10.2f} | "
        f"{r.e2e_p9999_ns:10.2f} | {r.e2e_max_ns:10.2f}"
    )

    # Line 2: Stage execution latency per task (STG ns/tsk)
    print(
        f"#  {'':<39} | {r.n_stages:4d} | STG ns/tsk || "
        f"{r.stage_ns_per_task:10.2f} | {r.out_ns_per_stream:10.2f} || "
        f"{r.stage_std_ns_per_task:10.2f} | {r.stage_p50_ns_per_task:10.2f} | "
        f"{r.stage_p99_ns_per_task:10.2f} | {r.stage_p999_ns_per_task:10.2f} | "
        f"{r.stage_p9999_ns_per_task:10.2f} | {r.stage_max_ns_per_task:10.2f}"
    )


def print_section_header(title: str, backends: PySequence[str]):
    if len(backends) == 1:
        print_single_rt_header(title, backends[0])
    else:
        print_multi_header(title, backends)


def print_section_row(label: str, n_stages: int, results: PySequence[PipeBenchResult]):
    if len(results) == 1:
        print_single_rt_row(label, results[0])
    else:
        print_multi_row(label, n_stages, results)


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
    fn_name = f"_spu_pipe_empty_jl_{n_scks}"
    if n_scks not in _JL_EMPTY_DEFINED:
        sck_args = ", ".join(f"s{i}" for i in range(n_scks))
        all_args = f"{sck_args}, rnt_frame_id, rnt_n_frames_per_wave" if sck_args else "rnt_frame_id, rnt_n_frames_per_wave"
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
# 3. Polyglot Empty-Task Pipeline Builder & Measurement Helpers
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


def choose_pipe_n_exec(base_n_exec: int, backend: str, active_wait: bool) -> int:
    cur = base_n_exec
    if not active_wait:
        cur = min(cur, 25000)
    if backend == "JL_SAFE":
        cur = min(cur, 25000)
    if backend in ("PY_NUMPY", "PY_RAW"):
        cur = min(cur, 2500)
    return max(16, cur)


def make_pipe_empty_module(backend: str, stage_idx: int, task_idx: int, role: str, n_scks: int, data_length: int):
    b = _BACKEND_ALIASES.get(backend.upper(), backend.upper())
    if b in ("JL_UNSAFE", "JL_SAFE"):
        if not HAS_JULIA:
            raise RuntimeError("pyStreamPU is not compiled with Julia support (SPU_LINK_JULIA=ON).")
        mdl = spu.Stateless_Julia()
        mdl.custom_name = f"{b}_S{stage_idx}_{task_idx}"
        mdl.jl_safe = b == "JL_SAFE"
        t = mdl.create_task("exec")
        t.replicable = True
        for s in range(n_scks):
            sname = f"s{s}"
            if role == "FIRST":
                mdl.create_socket_out(t, sname, data_length, spu.uint8)
            elif role == "MID":
                mdl.create_socket_fwd(t, sname, data_length, spu.uint8)
            else:
                mdl.create_socket_in(t, sname, data_length, spu.uint8)
        code, fn_name = get_julia_empty_codelet(n_scks)
        mdl.create_codelet(t, code, fn_name)
        return mdl

    mdl = spu.Stateless()
    mdl.custom_name = f"{b}_S{stage_idx}_{task_idx}"
    t = mdl.create_task("exec")
    t.replicable = True
    for s in range(n_scks):
        sname = f"s{s}"
        if role == "FIRST":
            mdl.create_socket_out(t, sname, data_length, spu.uint8)
        elif role == "MID":
            mdl.create_socket_fwd(t, sname, data_length, spu.uint8)
        else:
            mdl.create_socket_in(t, sname, data_length, spu.uint8)

    if b == "CPP":
        mdl.create_codelet_empty(t, 0)
    elif b == "PY_NUMBA":
        mdl.create_codelet(t, get_numba_empty_kernel(n_scks))
    elif b == "PY_NUMPY":
        mdl.create_codelet(t, get_py_numpy_empty_codelet(n_scks))
    elif b == "PY_RAW":
        mdl.create_codelet(t, get_py_mv_empty_codelet(n_scks))
    else:
        raise ValueError(f"Unsupported backend: {backend}")
    return mdl


def run_linear_pipeline_case(
    name: str,
    backend: str,
    n_stages: int,
    tasks_per_stage: int,
    threads_per_stage: PySequence[int],
    buffer_size: int,
    active_wait: bool,
    no_copy_mode: bool,
    data_length: int,
    n_exec: int,
    n_scks_per_task: int = 1,
    show_rt_table: bool = False,
    n_warmup: int = 256,
    n_skip_frames: int = 0,
    rt_frames: bool = False,
) -> PipeBenchResult:
    total_tasks = n_stages * tasks_per_stage
    mods = []
    for i in range(total_tasks):
        role = "FIRST" if i == 0 else ("MID" if i + 1 < total_tasks else "LAST")
        m = make_pipe_empty_module(
            backend,
            stage_idx=i // tasks_per_stage,
            task_idx=i % tasks_per_stage,
            role=role,
            n_scks=n_scks_per_task,
            data_length=data_length,
        )
        mods.append(m)

    for s in range(n_scks_per_task):
        sname = f"s{s}"
        for i in range(total_tasks - 1):
            mods[i + 1]["exec"][sname].bind(mods[i]["exec"][sname])

    sep_stages = []
    for s in range(n_stages):
        first_t = mods[s * tasks_per_stage]["exec"]
        last_t = mods[(s + 1) * tasks_per_stage - 1]["exec"]
        sep_stages.append(([first_t], [last_t], []))

    buf_sizes = [buffer_size] * (n_stages - 1)
    waits = [active_wait] * (n_stages - 1)

    pipe = spu.Pipeline(
        [mods[0]["exec"]],
        [mods[-1]["exec"]],
        sep_stages,
        list(threads_per_stage),
        buf_sizes,
        waits,
    )
    for stg in pipe.stages:
        stg.no_copy_mode = no_copy_mode

    cur_exec = choose_pipe_n_exec(n_exec, backend, active_wait)
    d = pipe.measure_bench(n_exec=cur_exec, n_warmup=n_warmup, n_skip_frames=n_skip_frames)

    if show_rt_table:
        print("#")
        pipe.show_rt_stats(display_thr=True, display_in_frames=rt_frames)

    pipe.unbind_adaptors()
    for s in range(n_scks_per_task):
        sname = f"s{s}"
        for i in range(total_tasks - 1):
            mods[i + 1]["exec"][sname].unbind(mods[i]["exec"][sname])

    return PipeBenchResult(
        name=name,
        backend=backend,
        n_stages=int(d["n_stages"]),
        stage_ns_per_task=float(d["stage_ns_per_task"]),
        stage_std_ns_per_task=float(d["stage_std_ns_per_task"]),
        stage_p50_ns_per_task=float(d["stage_p50_ns_per_task"]),
        stage_p99_ns_per_task=float(d["stage_p99_ns_per_task"]),
        stage_p999_ns_per_task=float(d["stage_p999_ns_per_task"]),
        stage_p9999_ns_per_task=float(d["stage_p9999_ns_per_task"]),
        stage_max_ns_per_task=float(d["stage_max_ns_per_task"]),
        out_ns_per_stream=float(d["out_ns_per_stream"]),
        e2e_avg_ns=float(d["e2e_avg_ns"]),
        e2e_std_ns=float(d["e2e_std_ns"]),
        e2e_p50_ns=float(d["e2e_p50_ns"]),
        e2e_p99_ns=float(d["e2e_p99_ns"]),
        e2e_p999_ns=float(d["e2e_p999_ns"]),
        e2e_p9999_ns=float(d["e2e_p9999_ns"]),
        e2e_max_ns=float(d["e2e_max_ns"]),
    )


# ==================================================================================================
# 4. Main Benchmark Suite (6 Sections matching pipeline_overhead.cpp)
# ==================================================================================================


def run_benchmark_suite(
    n_exec: int = 50000,
    data_length: int = 64,
    backends: PySequence[str] = DEFAULT_BACKENDS,
    csv_path: str = "",
    n_warmup: int = 256,
    show_full_rt_tables: bool = False,
    n_skip_frames: int = 0,
    rt_frames: bool = False,
):
    backends = [
        b
        for b in backends
        if (b != "PY_NUMBA" or HAS_NUMBA) and (b not in ("JL_UNSAFE", "JL_SAFE") or HAS_JULIA)
    ]
    if not backends:
        raise ValueError("No valid backends selected.")

    if HAS_JULIA and any(b in ("JL_UNSAFE", "JL_SAFE") for b in backends):
        spu.julia.init(256)

    active_backends_joined = ", ".join(backends)
    print("#######################################################################")
    print("# StreamPU Empty-Task Pipeline Overhead Benchmark (pipeline_overhead) #")
    print("#######################################################################")
    print(f"#   - base n_exec   = {n_exec} (scaled for passive wait / JL_SAFE / Python)")
    print(f"#   - data_length   = {data_length} bytes")
    print(f"#   - n_warmup      = {n_warmup}")
    print(f"#   - rt_skip       = {n_skip_frames}")
    print(f"#   - has_julia     = {'true' if HAS_JULIA else 'false'}")
    print(f"#   - has_numba     = {'true' if HAS_NUMBA else 'false'}")
    print(f"#   - backends      = {active_backends_joined}")
    if len(backends) == 1:
        print("#   - display_mode  = Single-Backend Full RT Percentiles (E2E ns/stm + STG ns/tsk)")
    else:
        print("#   - display_mode  = Multi-Backend Average Comparison (use -b <BACKEND> for full RT percentiles)")

    csv_rows: List[PipeCsvRow] = []

    # ==============================================================================================
    # SECTION 1: Waiting Strategy: Active Spin-Wait vs Passive Condition Variable (2 stages)
    # ==============================================================================================
    print_section_header("1. WAITING STRATEGY: ACTIVE SPIN-WAIT vs PASSIVE CONDVAR (2 stages)", backends)
    for bsize in (1, 16):
        for active in (True, False):
            act_str = "active_wait=true" if active else "active_wait=false"
            label = f"{act_str}, buffer_size={bsize}"
            row_res = []
            for b in backends:
                rt_label = f"{act_str}, buf={bsize} ({b})"
                r = run_linear_pipeline_case(
                    rt_label,
                    b,
                    n_stages=2,
                    tasks_per_stage=2,
                    threads_per_stage=[1, 1],
                    buffer_size=bsize,
                    active_wait=active,
                    no_copy_mode=True,
                    data_length=data_length,
                    n_exec=n_exec,
                    n_scks_per_task=1,
                    show_rt_table=False,
                    n_warmup=n_warmup,
                    n_skip_frames=n_skip_frames,
                    rt_frames=rt_frames,
                )
                row_res.append(r)
                csv_rows.append(PipeCsvRow("1_waiting_strategy", label, r))
            print_section_row(label, 2, row_res)

    # ==============================================================================================
    # SECTION 2: Inter-Stage FIFO Buffer Size (buffer_size = 1, 2, 4, 8, 16, 64; 2 stages)
    # ==============================================================================================
    print_section_header("2. INTER-STAGE FIFO BUFFER SIZE (2 stages, active_wait=true, no_copy=true)", backends)
    for bsize in (1, 2, 4, 8, 16, 64):
        label = f"buffer_size = {bsize} slot(s)"
        row_res = []
        for b in backends:
            r = run_linear_pipeline_case(
                f"{label} ({b})",
                b,
                n_stages=2,
                tasks_per_stage=2,
                threads_per_stage=[1, 1],
                buffer_size=bsize,
                active_wait=True,
                no_copy_mode=True,
                data_length=data_length,
                n_exec=n_exec,
                n_scks_per_task=1,
                show_rt_table=False,
                n_warmup=n_warmup,
                n_skip_frames=n_skip_frames,
                rt_frames=rt_frames,
            )
            row_res.append(r)
            csv_rows.append(PipeCsvRow("2_buffer_size", label, r))
        print_section_row(label, 2, row_res)

    # ==============================================================================================
    # SECTION 3: Number of Pipeline Stages (2, 3, 4, 8 stages in series; buffer_size = 1 and 16)
    # ==============================================================================================
    print_section_header("3. NUMBER OF PIPELINE STAGES IN SERIES (active_wait=true, no_copy=true)", backends)
    for bsize in (1, 16):
        for n_stg in (2, 3, 4, 8):
            label = f"{n_stg} stages (buffer_size={bsize})"
            thrs = [1] * n_stg
            row_res = []
            for b in backends:
                show_rt = show_full_rt_tables and (
                    n_stg == 4 and bsize == 1 and b in ("CPP", "JL_UNSAFE", "PY_NUMBA")
                )
                r = run_linear_pipeline_case(
                    f"{label} ({b})",
                    b,
                    n_stages=n_stg,
                    tasks_per_stage=2,
                    threads_per_stage=thrs,
                    buffer_size=bsize,
                    active_wait=True,
                    no_copy_mode=True,
                    data_length=data_length,
                    n_exec=n_exec,
                    n_scks_per_task=1,
                    show_rt_table=show_rt,
                    n_warmup=n_warmup,
                    n_skip_frames=n_skip_frames,
                    rt_frames=rt_frames,
                )
                row_res.append(r)
                csv_rows.append(PipeCsvRow("3_n_stages", label, r))
            print_section_row(label, n_stg, row_res)

    # ==============================================================================================
    # SECTION 4: Data-Parallel Multi-Threading on Middle Stage (1->N->1 Adaptor_m_to_n contention)
    # ==============================================================================================
    print_section_header("4. DATA-PARALLEL MULTI-THREADING (3 stages: 1 -> N -> 1 threads, active_wait)", backends)
    for mid_t in (1, 2, 4):
        label = f"3 stages: 1 -> {mid_t} -> 1 thread(s) (buf=16)"
        row_res = []
        for b in backends:
            rt_label = f"3 stages: 1->{mid_t}->1 threads ({b})"
            r = run_linear_pipeline_case(
                rt_label,
                b,
                n_stages=3,
                tasks_per_stage=2,
                threads_per_stage=[1, mid_t, 1],
                buffer_size=16,
                active_wait=True,
                no_copy_mode=True,
                data_length=data_length,
                n_exec=n_exec,
                n_scks_per_task=1,
                show_rt_table=False,
                n_warmup=n_warmup,
                n_skip_frames=n_skip_frames,
                rt_frames=rt_frames,
            )
            row_res.append(r)
            csv_rows.append(PipeCsvRow("4_multithread_stage", label, r))
        print_section_row(label, 3, row_res)

    # ==============================================================================================
    # SECTION 5: Copy Mode vs Zero-Copy Mode across Payload Sizes (64 B, 1 KB, 16 KB, 64 KB)
    # ==============================================================================================
    print_section_header("5. ZERO-COPY (swap_buffers) vs COPY (std::copy) ACROSS PAYLOAD SIZES", backends)
    for bytes_len in (64, 1024, 16384, 65536):
        for no_copy in (True, False):
            nc_str = "no_copy=true" if no_copy else "no_copy=false"
            label = f"{nc_str}, payload={bytes_len} B"
            row_res = []
            for b in backends:
                r = run_linear_pipeline_case(
                    f"{label} ({b})",
                    b,
                    n_stages=2,
                    tasks_per_stage=2,
                    threads_per_stage=[1, 1],
                    buffer_size=4,
                    active_wait=True,
                    no_copy_mode=no_copy,
                    data_length=bytes_len,
                    n_exec=n_exec,
                    n_scks_per_task=1,
                    show_rt_table=False,
                    n_warmup=n_warmup,
                    n_skip_frames=n_skip_frames,
                    rt_frames=rt_frames,
                )
                row_res.append(r)
                csv_rows.append(PipeCsvRow("5_copy_vs_zerocopy", label, r))
            print_section_row(label, 2, row_res)

    # ==============================================================================================
    # SECTION 6: Number of Sockets Crossing Adaptor_m_to_n Boundary (1, 2, 4, 8 sockets)
    # ==============================================================================================
    print_section_header("6. NUMBER OF SOCKETS CROSSING ADAPTOR BOUNDARY (2 stages, active_wait, buf=4)", backends)
    for n_scks in (1, 2, 4, 8):
        label = f"{n_scks} socket(s) across Adaptor_m_to_n"
        row_res = []
        for b in backends:
            r = run_linear_pipeline_case(
                f"{label} ({b})",
                b,
                n_stages=2,
                tasks_per_stage=2,
                threads_per_stage=[1, 1],
                buffer_size=4,
                active_wait=True,
                no_copy_mode=True,
                data_length=data_length,
                n_exec=n_exec,
                n_scks_per_task=n_scks,
                show_rt_table=False,
                n_warmup=n_warmup,
                n_skip_frames=n_skip_frames,
                rt_frames=rt_frames,
            )
            row_res.append(r)
            csv_rows.append(PipeCsvRow("6_adaptor_sockets", label, r))
        print_section_row(label, 2, row_res)

    if csv_path:
        with open(csv_path, "w", encoding="utf-8") as ofs:
            ofs.write(
                "section,case,backend,n_stages,stage_ns_per_task,stage_std_ns_per_task,stage_p50_ns_per_task,"
                "stage_p99_ns_per_task,stage_p999_ns_per_task,stage_p9999_ns_per_task,stage_max_ns_per_task,"
                "out_ns_per_stream,e2e_avg_ns,e2e_std_ns,e2e_p50_ns,e2e_p99_ns,e2e_p999_ns,e2e_p9999_ns,e2e_max_ns\n"
            )
            for row in csv_rows:
                r = row.res
                ofs.write(
                    f'{row.section},"{row.case_name}",{r.backend},{r.n_stages},'
                    f"{r.stage_ns_per_task},{r.stage_std_ns_per_task},{r.stage_p50_ns_per_task},"
                    f"{r.stage_p99_ns_per_task},{r.stage_p999_ns_per_task},{r.stage_p9999_ns_per_task},"
                    f"{r.stage_max_ns_per_task},{r.out_ns_per_stream},{r.e2e_avg_ns},{r.e2e_std_ns},"
                    f"{r.e2e_p50_ns},{r.e2e_p99_ns},{r.e2e_p999_ns},{r.e2e_p9999_ns},{r.e2e_max_ns}\n"
                )
        print(f"# Wrote CSV results to {csv_path}")

    print("#")
    print("# Empty-task pipeline overhead breakdown completed!")


def test_pipeline_overhead():
    """Pytest entry point running a fast smoke-test pass of the polyglot pipeline overhead suite."""
    run_benchmark_suite(n_exec=64, data_length=64, backends=DEFAULT_BACKENDS, n_warmup=16)


def main():
    default_backends_str = ",".join(DEFAULT_BACKENDS)
    parser = argparse.ArgumentParser(
        description="pyStreamPU Polyglot Empty-Task Pipeline Overhead Benchmark (matching pipeline_overhead.cpp)"
    )
    parser.add_argument(
        "-e",
        "--n-exec",
        type=int,
        default=50000,
        help="Base number of pipeline frames per benchmark [50000]",
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
        help=(
            f"Comma-separated list of backends [{default_backends_str}] "
            "(Specify a single backend e.g. -b CPP or -b PY_NUMBA to display full RT percentiles + MAX for every case)"
        ),
    )
    parser.add_argument(
        "-C",
        "--csv",
        type=str,
        default="",
        help="Optional path to export benchmark results (CSV) [none]",
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
        help="Display RT throughput in frames/s [false]",
    )
    args = parser.parse_args()
    backends = parse_backends(args.backends)
    if not backends:
        raise SystemExit(f"# No valid backends selected from '{args.backends}'.")

    run_benchmark_suite(
        n_exec=args.n_exec,
        data_length=args.data_length,
        backends=backends,
        csv_path=args.csv,
        n_warmup=args.warmup,
        show_full_rt_tables=args.rt_stats,
        n_skip_frames=args.rt_skip,
        rt_frames=args.rt_frames,
    )


if __name__ == "__main__":
    main()
