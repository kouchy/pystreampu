# -*- coding: utf-8 -*-
"""Zero-GIL Numba `@cfunc` trampoline generator and C++ codelet registration for `pyStreamPU`.

Architecture overview
---------------------
Standard Python codelets (`def codelet(mdl, tsk, frame_id): ...`) must acquire the Python GIL
(or synchronize with the CPython runtime), look up socket wrappers, and go through Numba's
Python `Dispatcher` to unbox `PyArrayObject` arguments on every task execution (~1-5 us overhead).

To match C++ and Julia `unsafe` codelet latency (~7 ns), this module compiles a specialized
Numba `@cfunc(nogil=True, fastmath=True)` C-ABI trampoline for each `(kernel, socket_spec, extra_spec)`
signature and registers its raw C function pointer in StreamPU via `create_codelet_cfunc`:

1. At task execution time in C++ (`numba_cfunc_codelet` in `python_codelet.hpp`):
   - C++ collects the raw `dataptr` of each data socket into a stack array `uintptr_t sck_ptrs[32]`.
   - For stateful modules with per-clone scratch buffers/tables (`numba_codelet(kernel, extra_args=...)`),
     C++ also passes `const uintptr_t* extra_ptrs`, packed once per clone on its first execution.
   - C++ calls the compiled `@cfunc` trampoline directly: no GIL, no `PyObject*`, no `PyArrayObject`.

2. Inside the LLVM `@cfunc` trampoline (`_compile_trampoline`):
   - Raw integer addresses (`uintp`) in `sck_ptrs` and `extra_ptrs` are converted to typed LLVM
     pointers via `@intrinsic` `inttoptr` instructions (0 runtime overhead) and wrapped into stack
     Numba `carray` views of shape `(n_frames_per_wave, n_cols)` (for sockets) or 1D/2D shapes
     (for extra array arguments).
   - Scalar extra arguments (`int`, `float32`, `float64`, `bool`) are bitcast back from their
     64-bit `uintp` slot in `extra_ptrs`.
   - The user's `@njit` kernel is inlined directly by LLVM inside the `@cfunc` body.
"""

from __future__ import annotations

import inspect
from typing import Any, Callable, Optional, Sequence, Tuple

import numpy as np

# Process-wide caches so identical `(kernel, sck_spec, extra_spec, extra_before_sockets)`
# signatures only run LLVM `@cfunc` compilation once.
_CFUNC_CACHE = {}
_INTTOPTR_CACHE = {}
_INTRINSICS = None


def _get_numba_primitives():
    """Lazily initialize Numba / llvmlite intrinsics (only imported when a Numba codelet is used)."""
    global _INTRINSICS
    if _INTRINSICS is not None:
        return _INTRINSICS

    from llvmlite import ir
    from numba import carray, cfunc, types
    from numba.extending import intrinsic

    # Reinterpret the low 32 bits of a `uintp` slot in `extra_ptrs` as IEEE-754 `float32`.
    @intrinsic
    def _uintp_to_f32(typingctx, val):
        sig = types.float32(types.uintp)

        def codegen(context, builder, signature, args):
            i32_val = builder.trunc(args[0], ir.IntType(32))
            return builder.bitcast(i32_val, ir.FloatType())

        return sig, codegen

    # Reinterpret a 64-bit `uintp` slot in `extra_ptrs` as IEEE-754 `float64`.
    @intrinsic
    def _uintp_to_f64(typingctx, val):
        sig = types.float64(types.uintp)

        def codegen(context, builder, signature, args):
            return builder.bitcast(args[0], ir.DoubleType())

        return sig, codegen

    dtype_map = {
        "int8": types.int8,
        "int16": types.int16,
        "int32": types.int32,
        "int64": types.int64,
        "uint8": types.uint8,
        "uint16": types.uint16,
        "uint32": types.uint32,
        "uint64": types.uint64,
        "float32": types.float32,
        "float64": types.float64,
        "bool": types.bool_,
    }

    # Emit an LLVM `inttoptr` instruction casting a raw `uintp` address to `CPointer(nb_ty)`
    # so `numba.carray(ptr, shape)` can build a stack-allocated array view without Python objects.
    def get_inttoptr(dtype_name: str):
        if dtype_name not in _INTTOPTR_CACHE:
            nb_ty = dtype_map[dtype_name]
            ptr_ty = types.CPointer(nb_ty)

            @intrinsic
            def _inttoptr(typingctx, addr):
                sig = ptr_ty(types.uintp)

                def codegen(context, builder, signature, args):
                    ll_ptr_ty = context.get_value_type(ptr_ty)
                    return builder.inttoptr(args[0], ll_ptr_ty)

                return sig, codegen

            _INTTOPTR_CACHE[dtype_name] = _inttoptr
        return _INTTOPTR_CACHE[dtype_name]

    # C ABI signature matching `numba_cfunc_t` in `python_codelet.hpp`:
    #   int32_t (const uintptr_t* sck_ptrs, const uintptr_t* extra_ptrs, intptr_t frame_id, intptr_t n_frames_per_wave)
    c_sig = types.int32(
        types.CPointer(types.uintp),
        types.CPointer(types.uintp),
        types.intp,
        types.intp,
    )

    _INTRINSICS = (carray, cfunc, types, c_sig, dtype_map, get_inttoptr, _uintp_to_f32, _uintp_to_f64)
    return _INTRINSICS


class numba_codelet:
    """Descriptor binding a Numba `@njit` kernel (and optional per-clone extra arguments) to a StreamPU Task.

    Args:
        kernel: A Numba `@njit` function returning an integer status (`0` on success).
        extra_args: Optional callable `fn(mdl, n_frames_per_wave) -> Sequence[ndarray | scalar]`
            (or `fn(mdl)`) invoked once per module clone to pack stateful workspace arrays,
            lookup tables, and scalar parameters for the kernel.
        extra_before_sockets: If True (default), `extra_args` are passed to `kernel` before
            the task's data socket views; if False, they are passed after the socket views.
    """

    _is_numba_codelet = True

    def __init__(
        self,
        kernel: Any,
        extra_args: Optional[Callable[..., Sequence[Any]]] = None,
        extra_before_sockets: bool = True,
    ):
        self.kernel = kernel
        self.extra_args = extra_args
        self.extra_before_sockets = bool(extra_before_sockets)


def _call_extra_args(fn: Callable, mdl: Any, n_frames_per_wave: int) -> Tuple[Any, ...]:
    """Call the user's `extra_args` callback with `(mdl, n_frames_per_wave)` or `(mdl,)`."""
    try:
        sig = inspect.signature(fn)
        n_params = len(sig.parameters)
    except (ValueError, TypeError):
        n_params = 2
    if n_params >= 2:
        return tuple(fn(mdl, int(n_frames_per_wave)))
    return tuple(fn(mdl))


def _describe_and_pack_extra_args(args: Sequence[Any]) -> Tuple[Tuple[Tuple[str, str], ...], list, tuple]:
    """Serialize a sequence of extra arguments (1D/2D C-contiguous NumPy arrays and scalars)
    into:
      - `spec`: hashable type descriptor tuple `(('arr1d' | 'arr2d' | 'scalar', dtype_name), ...)`
        used as part of the `@cfunc` compilation cache key,
      - `ptrs`: flat list of `uintptr_t` words passed to the C trampoline as `extra_ptrs`
        (`(data_ptr, dim0[, dim1])` for arrays, bit-cast 64-bit value for scalars),
      - `keep_alive`: tuple of references to the underlying `np.ndarray` objects so their memory
        stays valid for the lifetime of the module clone.
    """
    spec = []
    ptrs = []
    keep_alive = []
    for a in args:
        if isinstance(a, np.ndarray):
            if not a.flags["C_CONTIGUOUS"]:
                raise ValueError("All NumPy arrays passed to numba_codelet extra_args must be C-contiguous.")
            dt_name = np.dtype(a.dtype).name
            if a.ndim == 1:
                spec.append(("arr1d", dt_name))
                ptrs.append(int(a.ctypes.data))
                ptrs.append(int(a.shape[0]))
            elif a.ndim == 2:
                spec.append(("arr2d", dt_name))
                ptrs.append(int(a.ctypes.data))
                ptrs.append(int(a.shape[0]))
                ptrs.append(int(a.shape[1]))
            else:
                raise ValueError(f"Unsupported ndarray ndim={a.ndim} in numba_codelet extra_args (expected 1D or 2D).")
            keep_alive.append(a)
        elif isinstance(a, (bool, np.bool_)):
            spec.append(("scalar", "bool"))
            ptrs.append(1 if a else 0)
        elif isinstance(a, np.floating):
            dt_name = np.dtype(type(a)).name
            if dt_name == "float32":
                spec.append(("scalar", "float32"))
                ptrs.append(int(np.float32(a).view(np.uint32)))
            else:
                spec.append(("scalar", "float64"))
                ptrs.append(int(np.float64(a).view(np.uint64)))
        elif isinstance(a, float):
            spec.append(("scalar", "float64"))
            ptrs.append(int(np.float64(a).view(np.uint64)))
        elif isinstance(a, np.integer):
            dt_name = np.dtype(type(a)).name
            spec.append(("scalar", dt_name))
            ptrs.append(int(a) & 0xFFFFFFFFFFFFFFFF)
        elif isinstance(a, int):
            spec.append(("scalar", "int64"))
            ptrs.append(int(a) & 0xFFFFFFFFFFFFFFFF)
        else:
            raise TypeError(f"Unsupported extra_arg type in numba_codelet: {type(a)!r}")
    return tuple(spec), ptrs, tuple(keep_alive)


def _compile_trampoline(
    kernel: Any,
    sck_spec: Tuple[Tuple[str, int], ...],
    extra_spec: Tuple[Tuple[str, str], ...],
    extra_before_sockets: bool,
):
    """Synthesize and compile a specialized `@cfunc(nogil=True, fastmath=True)` C trampoline
    that unpacks raw pointer arrays (`sck_ptrs`, `extra_ptrs`) into `numba.carray` views and
    scalars, and calls the `@njit` `kernel`.
    """
    cache_key = (kernel, sck_spec, extra_spec, extra_before_sockets)
    if cache_key in _CFUNC_CACHE:
        return _CFUNC_CACHE[cache_key]

    carray, cfunc, types, c_sig, dtype_map, get_inttoptr, _uintp_to_f32, _uintp_to_f64 = _get_numba_primitives()

    ns = {
        "_kernel": kernel,
        "_carray": carray,
        "_uintp_to_f32": _uintp_to_f32,
        "_uintp_to_f64": _uintp_to_f64,
        "_np": np,
    }

    lines = ["def _numba_trampoline(sck_ptrs, extra_ptrs, frame_id, n_frames_per_wave):"]
    # 1. Unpack optional per-clone extra arguments (`arr1d`, `arr2d`, or `scalar`) from `extra_ptrs`.
    extra_vars = []
    offset = 0
    for idx, (kind, dt_name) in enumerate(extra_spec):
        vname = f"e_{idx}"
        extra_vars.append(vname)
        if kind == "arr1d":
            itp_name = f"_itp_{dt_name}"
            ns[itp_name] = get_inttoptr(dt_name)
            lines.append(f"    {vname} = _carray({itp_name}(extra_ptrs[{offset}]), (extra_ptrs[{offset + 1}],))")
            offset += 2
        elif kind == "arr2d":
            itp_name = f"_itp_{dt_name}"
            ns[itp_name] = get_inttoptr(dt_name)
            lines.append(
                f"    {vname} = _carray({itp_name}(extra_ptrs[{offset}]), (extra_ptrs[{offset + 1}], extra_ptrs[{offset + 2}]))"  # noqa: E501
            )
            offset += 3
        elif kind == "scalar":
            if dt_name == "bool":
                lines.append(f"    {vname} = extra_ptrs[{offset}] != 0")
            elif dt_name == "float32":
                lines.append(f"    {vname} = _uintp_to_f32(extra_ptrs[{offset}])")
            elif dt_name == "float64":
                lines.append(f"    {vname} = _uintp_to_f64(extra_ptrs[{offset}])")
            else:
                lines.append(f"    {vname} = _np.{dt_name}(extra_ptrs[{offset}])")
            offset += 1

    # 2. Unpack each task data socket into a 2D `carray` view of shape `(n_frames_per_wave, n_cols)`.
    sck_vars = []
    for idx, (dt_name, n_cols) in enumerate(sck_spec):
        vname = f"s_{idx}"
        sck_vars.append(vname)
        itp_name = f"_itp_{dt_name}"
        ns[itp_name] = get_inttoptr(dt_name)
        lines.append(f"    {vname} = _carray({itp_name}(sck_ptrs[{idx}]), (n_frames_per_wave, {int(n_cols)}))")

    # 3. Invoke the `@njit` kernel directly (inlined by LLVM).
    all_args = (extra_vars + sck_vars) if extra_before_sockets else (sck_vars + extra_vars)
    args_str = ", ".join(all_args)
    lines.append(f"    return _np.int32(_kernel({args_str}))")

    src = "\n".join(lines)
    exec(src, ns)
    tramp_py = ns["_numba_trampoline"]
    compiled_cfunc = cfunc(c_sig, nogil=True, fastmath=True)(tramp_py)
    _CFUNC_CACHE[cache_key] = compiled_cfunc
    return compiled_cfunc


def register_numba_codelet(mdl: Any, task: Any, codelet_obj: Any) -> None:
    """Compile (or fetch cached) `@cfunc` trampoline and bind it to `task` on `mdl` via `create_codelet_cfunc`."""
    if getattr(codelet_obj, "_is_numba_codelet", False):
        kernel = codelet_obj.kernel
        extra_args_fn = codelet_obj.extra_args
        extra_before_sockets = codelet_obj.extra_before_sockets
    else:
        kernel = codelet_obj
        extra_args_fn = None
        extra_before_sockets = True

    n_frames = max(1, int(mdl.n_frames))
    # Exclude the trailing `status` output socket added automatically by StreamPU.
    data_sockets = [s for s in task.sockets if s.name != "status"]
    sck_spec = tuple((s.dtype.name, int(s.n_elmts) // n_frames) for s in data_sockets)

    # Stateless path: no `extra_args` callback, C++ invokes `cfunc_obj.address` with `extra_ptrs = nullptr`.
    if extra_args_fn is None:
        cfunc_obj = _compile_trampoline(kernel, sck_spec, (), True)
        mdl.create_codelet_cfunc(task, int(cfunc_obj.address), cfunc_obj, None)
        return

    # Stateful path: inspect the initial extra arguments to determine `extra_spec` and compile
    # the specialized `@cfunc`, then pass `_packer` to C++ so each module clone lazily packs its
    # own arrays/scalars on its first execution.
    init_extra = _call_extra_args(extra_args_fn, mdl, int(mdl.n_frames_per_wave))
    extra_spec, _, _ = _describe_and_pack_extra_args(init_extra)
    cfunc_obj = _compile_trampoline(kernel, sck_spec, extra_spec, extra_before_sockets)

    def _packer(m_clone: Any, n_frames_per_wave: int):
        cur_extra = _call_extra_args(extra_args_fn, m_clone, int(n_frames_per_wave))
        _, ptrs, keep_alive = _describe_and_pack_extra_args(cur_extra)
        return ptrs, keep_alive

    mdl.create_codelet_cfunc(task, int(cfunc_obj.address), cfunc_obj, _packer)


__all__ = ["numba_codelet", "register_numba_codelet"]
