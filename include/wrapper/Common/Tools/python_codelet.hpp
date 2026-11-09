#ifndef WRAPPER_PYTHON_CODELET_HPP_
#define WRAPPER_PYTHON_CODELET_HPP_

#include <cstdint>
#include <functional>
#include <memory>
#include <utility>
#include <vector>

#include "wrapper/Common/pybind11_common.h"
#include "wrapper/Julia/gc_region.hpp"
#include <streampu.hpp>

namespace pyspu
{
namespace wrapper
{

inline bool
is_python_alive()
{
#if PY_VERSION_HEX >= 0x030D0000
    return Py_IsInitialized() && !Py_IsFinalizing();
#else
    return Py_IsInitialized() && !_Py_IsFinalizing();
#endif
}

// Keep the Python `PyThreadState` alive for the lifetime of each C++ worker thread (`Sequence`
// or `Pipeline` `std::thread`) instead of allocating and destroying a fresh `PyThreadState`
// (`PyThreadState_New` + `PyThreadState_DeleteCurrent`, ~1.4 us overhead) on every single task
// execution. When the C++ `std::thread` exits, the `thread_local` destructor releases the extra
// reference so `pybind11::gil_scoped_acquire` cleanly deletes the `PyThreadState`.
struct Thread_state_keeper
{
    bool held = false;

    void ensure(pybind11::gil_scoped_acquire& gil)
    {
        if (!held)
        {
            if (PyGILState_GetThisThreadState() == nullptr)
            {
                gil.inc_ref();
                held = true;
            }
        }
    }

    ~Thread_state_keeper()
    {
        if (held && is_python_alive())
        {
            pyspu::wrapper::Julia_gc_safe_region gc_safe;
            pybind11::gil_scoped_acquire gil;
            gil.dec_ref();
        }
    }
};

inline void
keep_worker_thread_state_alive(pybind11::gil_scoped_acquire& gil)
{
    static thread_local Thread_state_keeper keeper;
    keeper.ensure(gil);
}

// Per-codelet-instance cache of the Python wrapper objects passed to a Python codelet
// `codelet(module, task, frame_id) -> int`.
//
// Why this cache exists:
// - Without caching, every execution of a Python codelet would call `py::cast(&m, ...)` and
//   `py::cast(&t, ...)`, performing two global hash-table lookups in pybind11's
//   `registered_instances` map (plus mutex/shard locks under free-threaded Python), and for
//   cloned `Stateless` modules (which have no preexisting Python wrapper) it would allocate and
//   destroy a temporary Python `Stateless` instance on every single frame/wave.
// - When StreamPU duplicates a module across threads (`Sequence` or `Pipeline`), each clone
//   copies the `std::function` of its codelets. The copy constructor of `Codelet_call_cache`
//   intentionally resets `cached_m` and `cached_t` to `nullptr` so that each thread/clone lazily
//   initializes and owns its own cached Python wrappers on its first execution.
// - During `init()`, we also pre-populate `t_obj.__dict__` with interned `Socket` names mapped to
//   their Python `Socket` wrappers: consequently, both `t.<socket_name>` (attribute lookup in
//   `__dict__` before `__getattr__`) and `t["<socket_name>"]` (`PyDict_GetItemWithError` in
//   `Task::__getitem__`) resolve in O(1) without allocating a `std::vector<Socket*>` or scanning
//   socket names at runtime.
struct Codelet_call_cache
{
    const spu::module::Module* cached_m = nullptr;
    const spu::runtime::Task* cached_t = nullptr;
    pybind11::handle m_handle; // Borrowed or owned handle passed as `args[0]` (`module`)
    pybind11::object m_owned;  // Non-empty only when `m` had no Python wrapper (e.g. C++ clone of `Stateless`)
    pybind11::object t_obj;    // Owned reference to the Python `Task` wrapper passed as `args[1]` (`task`)
    pybind11::object zero_py;  // Cached `PyLong(0)` for `frame_id == 0` and fast return-value comparison
    PyObject* args[3] = { nullptr, nullptr, nullptr };

    Codelet_call_cache() = default;

    // When a module is cloned by StreamPU (`Module::deep_copy`), its codelet `std::function` is
    // copied: start with an empty cache so the clone binds to its own `Module&` and `Task&`.
    Codelet_call_cache(const Codelet_call_cache&)
      : cached_m(nullptr)
      , cached_t(nullptr)
    {
    }
    Codelet_call_cache& operator=(const Codelet_call_cache&)
    {
        reset();
        return *this;
    }

    // Safely release any held Python references with the GIL held (and inside a Julia GC-safe
    // region if the destroying thread was adopted by Julia).
    void reset()
    {
        cached_m = nullptr;
        cached_t = nullptr;
        m_handle = pybind11::handle();
        args[0] = args[1] = args[2] = nullptr;
        if (m_owned || t_obj || zero_py)
        {
            if (is_python_alive())
            {
                pyspu::wrapper::Julia_gc_safe_region gc_safe;
                pybind11::gil_scoped_acquire gil;
                if (m_owned) m_owned.release().dec_ref();
                if (t_obj) t_obj.release().dec_ref();
                if (zero_py) zero_py.release().dec_ref();
            }
            else
            {
                if (m_owned) m_owned.release();
                if (t_obj) t_obj.release();
                if (zero_py) zero_py.release();
            }
        }
    }

    ~Codelet_call_cache() { reset(); }

    void init(spu::module::Module& m, spu::runtime::Task& t)
    {
        namespace py = pybind11;
        m_owned = py::object();
        py::object m_tmp = py::cast(&m, py::return_value_policy::reference);
        // Important subtlety to avoid a reference cycle on `Stateful_core`:
        // - If `Py_REFCNT(m_tmp) == 1`, `py::cast` just created a brand-new Python wrapper (for
        //   example on a C++-cloned `Stateless` module). We must keep `m_owned` alive so the
        //   wrapper is not destroyed at the end of `init()`.
        // - If `Py_REFCNT(m_tmp) > 1`, a Python object already owns `m` (e.g. a `Stateful_core`
        //   subclass in Python). Holding a strong reference to `m` inside `m`'s own codelet
        //   would create an uncollectable cycle (`PyObject -> C++ Module -> Task -> std::function -> PyObject`),
        //   so we only store a borrowed `py::handle` (`m_handle`).
        if (Py_REFCNT(m_tmp.ptr()) == 1)
        {
            m_owned = std::move(m_tmp);
            m_handle = m_owned;
        }
        else
        {
            m_handle = m_tmp.ptr();
        }

        t_obj = py::cast(&t, py::return_value_policy::reference);
        zero_py = py::reinterpret_steal<py::object>(PyLong_FromLong(0));
        args[0] = m_handle.ptr();
        args[1] = t_obj.ptr();
        args[2] = zero_py.ptr();

        // Pre-populate the Python `Task` instance's `__dict__` with all its sockets keyed by
        // interned socket name (`in`, `out`, ...). This makes both `t.in` and `t["in"]` hit
        // `t_obj.__dict__` directly in C without iterating over `t.sockets`.
        PyObject** dict_ptr = _PyObject_GetDictPtr(t_obj.ptr());
        if (dict_ptr != nullptr)
        {
            if (*dict_ptr == nullptr) *dict_ptr = PyDict_New();
            if (*dict_ptr != nullptr)
            {
                for (auto& sck : t.sockets)
                {
                    PyObject* key = PyUnicode_InternFromString(sck->get_name().c_str());
                    if (key != nullptr)
                    {
                        py::object py_sck = py::cast(sck.get(), py::return_value_policy::reference);
                        PyDict_SetItem(*dict_ptr, key, py_sck.ptr());
                        Py_DECREF(key);
                    }
                }
            }
        }

        cached_m = &m;
        cached_t = &t;
    }
};

// C++ codelet that calls a Python function `codelet(module, task, frame_id) -> int`.
//
// Latency optimizations on this path:
// 1. Enters a Julia GC-safe region before acquiring the Python GIL so Python and Julia codelets
//    can coexist in multi-threaded Sequences/Pipelines without deadlocking the Julia GC.
// 2. Reuses the per-clone `Codelet_call_cache` so `m` and `t` are only wrapped once per clone.
// 3. Uses PEP 590 `PyObject_Vectorcall` with a pre-populated `PyObject* args[3]` array (reusing
//    the cached `PyLong(0)` when `frame_id == 0`), and checks `res == cache.zero_py.ptr()` by
//    pointer identity before falling back to `PyLong_AsLong`.
inline std::function<int(spu::module::Module&, spu::runtime::Task&, const size_t)>
python_codelet(const pybind11::function& codelet)
{
    namespace py = pybind11;
    auto function = std::shared_ptr<py::function>(new py::function(codelet),
                                                  [](py::function* f)
                                                  {
                                                      if (Py_IsInitialized())
                                                      {
                                                          pyspu::wrapper::Julia_gc_safe_region gc_safe;
                                                          py::gil_scoped_acquire gil;
                                                          delete f;
                                                      }
                                                  });
    PyObject* fn_ptr = function->ptr();
    return [function, fn_ptr, cache = Codelet_call_cache()](
             spu::module::Module& m, spu::runtime::Task& t, const size_t frame_id) mutable -> int
    {
        pyspu::wrapper::Julia_gc_safe_region gc_safe;
        py::gil_scoped_acquire gil;
        keep_worker_thread_state_alive(gil);
        if (cache.cached_m != &m || cache.cached_t != &t)
            cache.init(m, t);

        PyObject* res;
        if (frame_id == 0)
        {
            res = PyObject_Vectorcall(fn_ptr, cache.args, 3, nullptr);
        }
        else
        {
            PyObject* frame_py = PyLong_FromSize_t(frame_id);
            PyObject* call_args[3] = { cache.args[0], cache.args[1], frame_py };
            res = PyObject_Vectorcall(fn_ptr, call_args, 3, nullptr);
            Py_DECREF(frame_py);
        }
        if (res == nullptr)
            throw py::error_already_set();

        if (res == cache.zero_py.ptr())
        {
            Py_DECREF(res);
            return 0;
        }

        const long ret = PyLong_AsLong(res);
        Py_DECREF(res);
        if (ret == -1 && PyErr_Occurred())
            throw py::error_already_set();
        return static_cast<int>(ret);
    };
}

// Per-clone cache of packed extra arguments (raw buffer pointers, shapes, scalars) for stateful
// Numba `@cfunc` codelets (`spu.numba_codelet(kernel, extra_args=...)`).
//
// When a `Stateful_core` module is cloned across threads in a `Sequence` or `Pipeline`, each
// clone owns distinct scratch buffers (e.g. per-thread decoder workspaces). On the first call
// (or if `n_frames_per_wave` changes), `extra_args_packer(m_clone, n_frames_per_wave)` is called
// once under the GIL to extract the flat `uintptr_t` array (`extra_ptrs`) and keep the underlying
// NumPy arrays alive in `keep_alive`. All subsequent calls read `extra_ptrs.data()` with zero
// GIL and zero Python overhead.
struct Numba_extra_cache
{
    const spu::module::Module* cached_m = nullptr;
    size_t cached_w = 0;
    std::vector<uintptr_t> extra_ptrs;
    pybind11::object keep_alive;

    Numba_extra_cache() = default;
    Numba_extra_cache(const Numba_extra_cache&)
      : cached_m(nullptr)
      , cached_w(0)
    {
    }
    Numba_extra_cache& operator=(const Numba_extra_cache&)
    {
        reset();
        return *this;
    }

    void reset()
    {
        cached_m = nullptr;
        cached_w = 0;
        extra_ptrs.clear();
        if (keep_alive)
        {
            if (is_python_alive())
            {
                pyspu::wrapper::Julia_gc_safe_region gc_safe;
                pybind11::gil_scoped_acquire gil;
                keep_alive.release().dec_ref();
            }
            else
            {
                keep_alive.release();
            }
        }
    }

    ~Numba_extra_cache() { reset(); }
};

// Signature of the general compiled Numba `@cfunc(nogil=True, fastmath=True)` trampoline:
//   int32_t trampoline(const uintptr_t* sck_ptrs,
//                      const uintptr_t* extra_ptrs,
//                      intptr_t frame_id,
//                      intptr_t n_frames_per_wave)
using numba_cfunc_t = int32_t (*)(const uintptr_t*, const uintptr_t*, intptr_t, intptr_t);

// Maximum number of data sockets passed directly as individual `uintptr_t` parameters
// (`int32_t (*)(uintptr_t p_0, ..., uintptr_t p_{N-1}, intptr_t n_frames_per_wave)`)
// via C++17 `std::index_sequence` expansion without a stack `sck_ptrs` array or loop
// (matching `SPU_MAX_DIRECT_TRAMPOLINE_ARGS = 16` in `Module_Julia.cpp`).
static constexpr size_t k_max_direct_numba_sockets = 16;

template<size_t>
using Uintptr_arg_t = uintptr_t;

// Native C++ codelet that invokes a Numba `@cfunc(nogil=True)` trampoline directly from C++
// without acquiring the Python GIL or constructing any Python/NumPy objects at runtime.
inline std::function<int(spu::module::Module&, spu::runtime::Task&, const size_t)>
numba_cfunc_codelet(const uintptr_t cfunc_addr,
                    pybind11::object keep_alive,
                    pybind11::object extra_args_packer = pybind11::none())
{
    namespace py = pybind11;
    auto fn = reinterpret_cast<numba_cfunc_t>(cfunc_addr);
    auto keep_alive_ptr = std::shared_ptr<py::object>(new py::object(std::move(keep_alive)),
                                                      [](py::object* o)
                                                      {
                                                          if (is_python_alive())
                                                          {
                                                              pyspu::wrapper::Julia_gc_safe_region gc_safe;
                                                              py::gil_scoped_acquire gil;
                                                              delete o;
                                                          }
                                                      });

    if (extra_args_packer.is_none())
    {
        return [fn, keep_alive_ptr](spu::module::Module& m, spu::runtime::Task& t, const size_t frame_id) -> int
        {
            const size_t n_sck = t.sockets.size();
            const size_t n_data_sck = n_sck > 0 ? n_sck - 1 : 0; // exclude trailing `status` socket
            uintptr_t sck_ptrs[32];
            for (size_t i = 0; i < n_data_sck; ++i)
                sck_ptrs[i] = reinterpret_cast<uintptr_t>(t.sockets[i]->get_dataptr());
            return static_cast<int>(fn(sck_ptrs,
                                       nullptr,
                                       static_cast<intptr_t>(frame_id),
                                       static_cast<intptr_t>(m.get_n_frames_per_wave())));
        };
    }

    // Path for stateful Numba codelets with per-clone extra arguments (`extra_args_packer`):
    // packs the clone's extra arguments once on the first execution of each clone, then runs
    // completely GIL-free on all subsequent executions.
    auto packer_ptr = std::shared_ptr<py::object>(new py::object(std::move(extra_args_packer)),
                                                  [](py::object* o)
                                                  {
                                                      if (is_python_alive())
                                                      {
                                                          pyspu::wrapper::Julia_gc_safe_region gc_safe;
                                                          py::gil_scoped_acquire gil;
                                                          delete o;
                                                      }
                                                  });

    return [fn, keep_alive_ptr, packer_ptr, cache = Numba_extra_cache()](
             spu::module::Module& m, spu::runtime::Task& t, const size_t frame_id) mutable -> int
    {
        const size_t w = m.get_n_frames_per_wave();
        if (cache.cached_m != &m || cache.cached_w != w)
        {
            pyspu::wrapper::Julia_gc_safe_region gc_safe;
            py::gil_scoped_acquire gil;
            keep_worker_thread_state_alive(gil);
            py::object m_py = py::cast(&m, py::return_value_policy::reference);
            py::tuple packed = (*packer_ptr)(m_py, w);
            cache.extra_ptrs = packed[0].cast<std::vector<uintptr_t>>();
            cache.keep_alive = packed[1];
            cache.cached_m = &m;
            cache.cached_w = w;
        }
        const size_t n_sck = t.sockets.size();
        const size_t n_data_sck = n_sck > 0 ? n_sck - 1 : 0; // exclude trailing `status` socket
        uintptr_t sck_ptrs[32];
        for (size_t i = 0; i < n_data_sck; ++i)
            sck_ptrs[i] = reinterpret_cast<uintptr_t>(t.sockets[i]->get_dataptr());
        return static_cast<int>(fn(sck_ptrs,
                                   cache.extra_ptrs.data(),
                                   static_cast<intptr_t>(frame_id),
                                   static_cast<intptr_t>(w)));
    };
}

template<typename Mdl, size_t... Is>
inline void
bind_numba_fast_arity(Mdl& mdl, spu::runtime::Task& task, const uintptr_t cfunc_addr, std::index_sequence<Is...>)
{
    using fn_t = int32_t (*)(Uintptr_arg_t<Is>..., intptr_t);
    auto fn = reinterpret_cast<fn_t>(cfunc_addr);
    mdl.create_codelet(
      task,
      [fn](spu::module::Module& m, spu::runtime::Task& t, const size_t) -> int
      {
          (void)t;
          return static_cast<int>(fn(reinterpret_cast<uintptr_t>(t.sockets[Is]->get_dataptr())...,
                                     static_cast<intptr_t>(m.get_n_frames_per_wave())));
      });
}

template<typename Mdl, size_t I = 0>
inline void
dispatch_numba_fast_arity(Mdl& mdl, spu::runtime::Task& task, const uintptr_t cfunc_addr, const size_t n_data_sck)
{
    if (n_data_sck == I)
    {
        bind_numba_fast_arity(mdl, task, cfunc_addr, std::make_index_sequence<I>{});
        return;
    }
    if constexpr (I + 1 <= k_max_direct_numba_sockets)
    {
        dispatch_numba_fast_arity<Mdl, I + 1>(mdl, task, cfunc_addr, n_data_sck);
    }
    else
    {
        auto fn = reinterpret_cast<numba_cfunc_t>(cfunc_addr);
        mdl.create_codelet(
          task,
          [fn](spu::module::Module& m, spu::runtime::Task& t, const size_t frame_id) -> int
          {
              const size_t ns = t.sockets.size();
              const size_t nd = ns > 0 ? ns - 1 : 0;
              uintptr_t sck_ptrs[32];
              for (size_t i = 0; i < nd; ++i)
                  sck_ptrs[i] = reinterpret_cast<uintptr_t>(t.sockets[i]->get_dataptr());
              return static_cast<int>(fn(sck_ptrs,
                                         nullptr,
                                         static_cast<intptr_t>(frame_id),
                                         static_cast<intptr_t>(m.get_n_frames_per_wave())));
          });
    }
}

// Register a compiled Numba `@cfunc` trampoline on `task`:
// - When `extra_args_packer` is `None` (stateless codelet), registers a trivially-copyable
//   8-byte lambda capturing only the C function pointer `fn` directly with `mdl.create_codelet`,
//   activating StreamPU's `Task::call_fast_codelet` (`fast_codelet_fn`) flat C dispatch without
//   `std::function` indirection, and unpacking `0..16` socket pointers directly via `std::index_sequence`.
// - The `@cfunc` object is kept alive in `_CFUNC_CACHE` in `streampu._numba`.
template<typename Mdl>
inline void
register_numba_cfunc_codelet(Mdl& mdl,
                             spu::runtime::Task& task,
                             const uintptr_t cfunc_addr,
                             pybind11::object keep_alive,
                             pybind11::object extra_args_packer = pybind11::none())
{
    if (!extra_args_packer.is_none())
    {
        mdl.create_codelet(
          task, numba_cfunc_codelet(cfunc_addr, std::move(keep_alive), std::move(extra_args_packer)));
        return;
    }

    // Note: `Module::create_codelet` appends the trailing `"status"` socket to `task.sockets`,
    // so before `mdl.create_codelet` runs, `task.sockets` only contains the data sockets.
    const size_t n_sck = task.sockets.size();
    const size_t n_data_sck =
      (n_sck > 0 && task.sockets.back()->get_name() == "status") ? (n_sck - 1) : n_sck;
    dispatch_numba_fast_arity(mdl, task, cfunc_addr, n_data_sck);
}

#if defined(_MSC_VER)
#define SPU_PY_BENCH_NOINLINE __declspec(noinline)
#else
#define SPU_PY_BENCH_NOINLINE __attribute__((noinline))
#endif

// Empty out-of-line C++ kernels with compiler register/memory barriers (matching `sequence_overhead.cpp`)
// so the C++ compiler cannot inline, constant-fold, or dead-code-eliminate the function call or the
// socket pointer materializations in `register_empty_cpp_codelet`.
SPU_PY_BENCH_NOINLINE inline void
empty_kernel_0(const size_t frame_id) noexcept
{
#if defined(__GNUC__) || defined(__clang__)
    asm volatile("" : : "r"(frame_id) : "memory");
#else
    (void)frame_id;
#endif
}

SPU_PY_BENCH_NOINLINE inline void
empty_kernel_1(const void* p0, const size_t frame_id) noexcept
{
#if defined(__GNUC__) || defined(__clang__)
    asm volatile("" : : "r"(p0), "r"(frame_id) : "memory");
#else
    (void)p0;
    (void)frame_id;
#endif
}

SPU_PY_BENCH_NOINLINE inline void
empty_kernel_2(const void* p0, const void* p1, const size_t frame_id) noexcept
{
#if defined(__GNUC__) || defined(__clang__)
    asm volatile("" : : "r"(p0), "r"(p1), "r"(frame_id) : "memory");
#else
    (void)p0;
    (void)p1;
    (void)frame_id;
#endif
}

inline void
clobber_ptr(const void* p) noexcept
{
#if defined(__GNUC__) || defined(__clang__)
    asm volatile("" : : "r"(p) : "memory");
#else
    (void)p;
#endif
}

template<typename... Ptrs>
SPU_PY_BENCH_NOINLINE inline void
empty_kernel_arity(const size_t frame_id, Ptrs... ptrs) noexcept
{
#if defined(__GNUC__) || defined(__clang__)
    asm volatile("" : : "r"(frame_id) : "memory");
#else
    (void)frame_id;
#endif
    (clobber_ptr(ptrs), ...);
}

SPU_PY_BENCH_NOINLINE inline void
empty_kernel_n(const void* const* ptrs, const size_t n_ptrs, const size_t frame_id) noexcept
{
#if defined(__GNUC__) || defined(__clang__)
    asm volatile("" : : "r"(ptrs), "r"(n_ptrs), "r"(frame_id) : "memory");
#else
    (void)ptrs;
    (void)n_ptrs;
    (void)frame_id;
#endif
}

template<typename Mdl, size_t... Is>
inline void
bind_empty_cpp_fast_arity(Mdl& mdl, spu::runtime::Task& task, std::index_sequence<Is...>)
{
    mdl.create_codelet(
      task,
      [](spu::module::Module&, spu::runtime::Task& tsk, const size_t fid) -> int
      {
          (void)tsk;
          empty_kernel_arity(fid, tsk.sockets[Is]->get_dataptr()...);
          return spu::runtime::status_t::SUCCESS;
      });
}

template<typename Mdl, size_t I = 0>
inline void
dispatch_empty_cpp_fast_arity(Mdl& mdl, spu::runtime::Task& task, const size_t n_data_sck)
{
    if (n_data_sck == I)
    {
        bind_empty_cpp_fast_arity(mdl, task, std::make_index_sequence<I>{});
        return;
    }
    if constexpr (I + 1 <= k_max_direct_numba_sockets)
    {
        dispatch_empty_cpp_fast_arity<Mdl, I + 1>(mdl, task, n_data_sck);
    }
    else
    {
        mdl.create_codelet(
          task,
          [n_data_sck](spu::module::Module&, spu::runtime::Task& tsk, const size_t fid) -> int
          {
              const void* ptrs[32];
              for (size_t s = 0; s < n_data_sck; ++s)
                  ptrs[s] = tsk.sockets[s]->get_dataptr();
              empty_kernel_n(ptrs, n_data_sck, fid);
              return spu::runtime::status_t::SUCCESS;
          });
    }
}

// Register a native C++ empty codelet on `task` (for `test_sequence_overhead.py` / `test_pipeline_overhead.py`):
// - `capture_mode == -1`: `Switcher` control-generator codelet (`ctrl[0] = 0; empty_kernel_1(ctrl, fid)`).
// - `capture_mode == 0`: optimal `0..16`-socket variadic expansion (`fast_codelet_fn`).
// - `capture_mode == 1`: 8-byte capture `[ptr]` (`fast_codelet_fn`).
// - `capture_mode == 2`: 16-byte capture `[2x size_t]` (`fast_codelet_fn`).
// - `capture_mode == 3`: 64-byte capture `[8x size_t]` (`fast_codelet_fn` max inline storage).
// - `capture_mode == 4`: Non-trivial capture `[std::shared_ptr<size_t>]` (`std::function` fallback).
template<typename Mdl>
inline void
register_empty_cpp_codelet(Mdl& mdl, spu::runtime::Task& task, const int capture_mode = 0)
{
    const size_t n_sck = task.sockets.size();
    const size_t n_data_sck =
      (n_sck > 0 && task.sockets.back()->get_name() == "status") ? (n_sck - 1) : n_sck;

    if (capture_mode == -1)
    {
        mdl.create_codelet(
          task,
          [](spu::module::Module&, spu::runtime::Task& tsk, const size_t fid) -> int
          {
              int8_t* ctrl = static_cast<int8_t*>(tsk.sockets[0]->get_dataptr());
              ctrl[0] = 0;
              empty_kernel_1(ctrl, fid);
              return spu::runtime::status_t::SUCCESS;
          });
        return;
    }

    if (capture_mode == 1)
    {
        void* dummy_ptr = &mdl;
        mdl.create_codelet(
          task,
          [dummy_ptr](spu::module::Module&, spu::runtime::Task& tsk, const size_t fid) -> int
          {
              empty_kernel_2(tsk.sockets[0]->get_dataptr(), dummy_ptr, fid);
              return spu::runtime::status_t::SUCCESS;
          });
        return;
    }
    if (capture_mode == 2)
    {
        size_t s0 = 0, s1 = 1;
        mdl.create_codelet(
          task,
          [s0, s1](spu::module::Module&, spu::runtime::Task& tsk, const size_t fid) -> int
          {
              empty_kernel_1(tsk.sockets[s0]->get_dataptr(), fid + s1);
              return spu::runtime::status_t::SUCCESS;
          });
        return;
    }
    if (capture_mode == 3)
    {
        struct Cap64
        {
            size_t a[8];
        } cap = { { 0, 1, 2, 3, 4, 5, 6, 7 } };
        mdl.create_codelet(
          task,
          [cap](spu::module::Module&, spu::runtime::Task& tsk, const size_t fid) -> int
          {
              empty_kernel_1(tsk.sockets[cap.a[0]]->get_dataptr(), fid + cap.a[7]);
              return spu::runtime::status_t::SUCCESS;
          });
        return;
    }
    if (capture_mode == 4)
    {
        std::shared_ptr<size_t> sp(new size_t(0));
        mdl.create_codelet(
          task,
          [sp](spu::module::Module&, spu::runtime::Task& tsk, const size_t fid) -> int
          {
              empty_kernel_1(tsk.sockets[*sp]->get_dataptr(), fid);
              return spu::runtime::status_t::SUCCESS;
          });
        return;
    }

    dispatch_empty_cpp_fast_arity(mdl, task, n_data_sck);
}

} // namespace wrapper
} // namespace pyspu

#endif // WRAPPER_PYTHON_CODELET_HPP_
