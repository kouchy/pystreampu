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
        if (m_owned || t_obj)
        {
            if (Py_IsInitialized())
            {
                pyspu::wrapper::Julia_gc_safe_region gc_safe;
                pybind11::gil_scoped_acquire gil;
                if (m_owned) m_owned.release().dec_ref();
                if (t_obj) t_obj.release().dec_ref();
            }
            else
            {
                if (m_owned) m_owned.release();
                if (t_obj) t_obj.release();
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
// 3. Uses PEP 590 `PyObject_Vectorcall` with a stack-allocated `PyObject* args[3]` array instead
//    of `py::function::operator()`, avoiding `PyTuple_New(3)` allocation and pybind11 argument
//    casting on every call.
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
    return [function, cache = Codelet_call_cache()](
             spu::module::Module& m, spu::runtime::Task& t, const size_t frame_id) mutable -> int
    {
        pyspu::wrapper::Julia_gc_safe_region gc_safe;
        py::gil_scoped_acquire gil;
        if (cache.cached_m != &m || cache.cached_t != &t)
            cache.init(m, t);

        PyObject* frame_py = PyLong_FromSize_t(frame_id);
        PyObject* args[3] = { cache.m_handle.ptr(), cache.t_obj.ptr(), frame_py };
        PyObject* res = PyObject_Vectorcall(function->ptr(), args, 3, nullptr);
        Py_DECREF(frame_py);
        if (res == nullptr)
            throw py::error_already_set();

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
            if (Py_IsInitialized())
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

// Signature of the compiled Numba `@cfunc(nogil=True, fastmath=True)` trampoline:
//   int32_t trampoline(const uintptr_t* sck_ptrs,
//                      const uintptr_t* extra_ptrs,
//                      intptr_t frame_id,
//                      intptr_t n_frames_per_wave)
using numba_cfunc_t = int32_t (*)(const uintptr_t*, const uintptr_t*, intptr_t, intptr_t);

// Native C++ codelet that invokes a Numba `@cfunc(nogil=True)` trampoline directly from C++
// without acquiring the Python GIL or constructing any Python/NumPy objects at runtime.
//
// At each task execution, this codelet simply collects the raw data pointers of the task's
// data sockets (`t.sockets[0 .. n_sck-2]`, excluding the trailing `status` socket) into a
// stack-allocated array `uintptr_t sck_ptrs[32]` and calls the compiled C function pointer `fn`.
inline std::function<int(spu::module::Module&, spu::runtime::Task&, const size_t)>
numba_cfunc_codelet(const uintptr_t cfunc_addr,
                    pybind11::object keep_alive,
                    pybind11::object extra_args_packer = pybind11::none())
{
    namespace py = pybind11;
    auto fn = reinterpret_cast<numba_cfunc_t>(cfunc_addr);
    // Keep the Python `@cfunc` wrapper alive for as long as any copy of the C++ codelet exists,
    // so LLVM's JIT code memory is never freed while a Sequence/Pipeline can still call `fn`.
    auto keep_alive_ptr = std::shared_ptr<py::object>(new py::object(std::move(keep_alive)),
                                                      [](py::object* o)
                                                      {
                                                          if (Py_IsInitialized())
                                                          {
                                                              pyspu::wrapper::Julia_gc_safe_region gc_safe;
                                                              py::gil_scoped_acquire gil;
                                                              delete o;
                                                          }
                                                      });

    // Fast path for stateless Numba codelets (no `extra_args`):
    // 100% C++ execution, never touches the GIL after registration.
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
                                                      if (Py_IsInitialized())
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

} // namespace wrapper
} // namespace pyspu

#endif // WRAPPER_PYTHON_CODELET_HPP_
