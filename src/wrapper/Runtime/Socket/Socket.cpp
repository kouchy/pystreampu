#include <map>
#include <memory>
#include <sstream>
#include <string>
#include <typeinfo>

#include "wrapper/Runtime/Socket/Socket.hpp"
#include "wrapper/Common/Tools/Type/Type.hpp"

namespace py = pybind11;
using namespace py::literals;
using namespace pyspu::wrapper;
using namespace spu::runtime;

std::map<std::type_index, std::string> type_map = { { typeid(int8_t), py::format_descriptor<int8_t>::format() },
                                                    { typeid(int16_t), py::format_descriptor<int16_t>::format() },
                                                    { typeid(int32_t), py::format_descriptor<int32_t>::format() },
                                                    { typeid(int64_t), py::format_descriptor<int64_t>::format() },
                                                    { typeid(uint8_t), py::format_descriptor<uint8_t>::format() },
                                                    { typeid(uint16_t), py::format_descriptor<uint16_t>::format() },
                                                    { typeid(uint32_t), py::format_descriptor<uint32_t>::format() },
                                                    { typeid(uint64_t), py::format_descriptor<uint64_t>::format() },
                                                    { typeid(float), py::format_descriptor<float>::format() },
                                                    { typeid(double), py::format_descriptor<double>::format() } };

namespace
{
static const char* const k_socket_cache_cap_name = "spu_socket_view_cache";

// Per-Socket-wrapper cache of the `numpy` and `wave` 2D NumPy `ndarray` views.
//
// Why this cache exists:
// - Previously, every access to `sck.wave` or `sck.numpy` inside a Python codelet constructed
//   a brand-new `py::capsule`, a new `py::buffer_info` (with heap-allocated `shape` and `strides`
//   vectors), and a new `PyArrayObject` via NumPy's C-API (~800 ns per socket access).
// - By enabling `py::dynamic_attr()` on `Socket`, each Python `Socket` wrapper has an instance
//   `__dict__` where we store a `PyCapsule` owning a `Socket_view_cache` (automatically freed when
//   the Python `Socket` wrapper is garbage-collected).
// - The cache also stores raw C++ pointers to `Socket` and `Module` (`sck` and `mdl`) so the
//   `tp_getattro` hook (`socket_tp_getattro`) bypasses `pybind11::cpp_function` and
//   `pybind11::cast<const Socket&>()` completely on the fast path.
// - On subsequent accesses with the same dimensions `(n_row, n_col)`, we reuse the cached
//   `py::array` directly. If the underlying C++ socket `dataptr` changed (e.g., when advancing to
//   a new wave within a multi-wave buffer or after rebinding), we update the `PyArrayObject`'s
//   internal `data` pointer in place (`array_proxy(arr)->data = dataptr`) in a single pointer
//   store, with zero allocations.
struct Socket_view_cache
{
    const spu::runtime::Socket* sck = nullptr;
    const spu::module::Module* mdl = nullptr;
    struct Entry
    {
        size_t n_frames = 0;
        size_t n_elmts = 0;
        size_t rows = 0;
        size_t cols = 0;
        void* ptr = nullptr;
        py::array arr;
        void* mv_ptr = nullptr;
        py::array arr_1d;
        py::object mv;
    };
    Entry wave;
    Entry numpy;
};

// Retrieve (or lazily allocate) the `Socket_view_cache` attached to `self_obj.__dict__`.
inline Socket_view_cache*
get_socket_view_cache(PyObject* self_obj)
{
    static PyObject* k_cache_key = PyUnicode_InternFromString("_spu_view_cache");
    PyObject** dict_ptr = _PyObject_GetDictPtr(self_obj);
    if (dict_ptr == nullptr) return nullptr;
    if (*dict_ptr != nullptr)
    {
        PyObject* cap = PyDict_GetItemWithError(*dict_ptr, k_cache_key);
        if (cap != nullptr)
            return static_cast<Socket_view_cache*>(PyCapsule_GetPointer(cap, k_socket_cache_cap_name));
    }
    else
    {
        *dict_ptr = PyDict_New();
        if (*dict_ptr == nullptr) return nullptr;
    }

    const auto& self = py::handle(self_obj).cast<const spu::runtime::Socket&>();
    auto* cache = new Socket_view_cache();
    cache->sck = &self;
    cache->mdl = &self.get_task().get_module();
    py::capsule py_cap(cache, k_socket_cache_cap_name, [](void* p) { delete static_cast<Socket_view_cache*>(p); });
    PyDict_SetItem(*dict_ptr, k_cache_key, py_cap.ptr());
    return cache;
}

// Fast-path C getter for `Socket.wave` (`is_wave = true`) and `Socket.numpy` (`is_wave = false`).
inline PyObject*
get_cached_socket_array_ptr(PyObject* self_obj, const bool is_wave)
{
    try
    {
        Socket_view_cache* cache = get_socket_view_cache(self_obj);
        const spu::runtime::Socket& self =
          (cache != nullptr && cache->sck != nullptr) ? *cache->sck : py::handle(self_obj).cast<const spu::runtime::Socket&>();

        void* dataptr = self.get_dataptr();
        if (dataptr == nullptr)
        {
            py::array empty_arr(py::buffer_info(nullptr, self.get_datatype_size(), type_map.at(self.get_datatype()), {}));
            return empty_arr.release().ptr();
        }

        const auto& mdl = (cache != nullptr && cache->mdl != nullptr) ? *cache->mdl : self.get_task().get_module();
        const size_t n_frames = mdl.get_n_frames();
        const size_t n_row = is_wave ? mdl.get_n_frames_per_wave() : n_frames;
        const size_t n_elmts = self.get_n_elmts();

        if (cache != nullptr)
        {
            auto& entry = is_wave ? cache->wave : cache->numpy;
            // Fast path: dimensions match the cached `ndarray` view (no integer division); only patch `data` if `dataptr` moved.
            if (entry.n_frames == n_frames && entry.rows == n_row && entry.n_elmts == n_elmts && entry.arr)
            {
                if (entry.ptr != dataptr)
                {
                    py::detail::array_proxy(entry.arr.ptr())->data = static_cast<char*>(dataptr);
                    entry.ptr = dataptr;
                }
                return Py_NewRef(entry.arr.ptr());
            }

            // Slow path (first access, or after `n_frames` / `n_frames_per_wave` changed):
            // allocate the 2D `ndarray` view once and cache it. Input sockets (`SIN`) are marked read-only.
            const size_t n_col = n_elmts / n_frames;
            py::capsule buffer_handle([]() {});
            const size_t dt_size = (size_t)self.get_datatype_size();
            entry.arr = py::array(
              py::buffer_info(dataptr,
                              (ssize_t)dt_size,
                              type_map.at(self.get_datatype()),
                              2,
                              { n_row, n_col },
                              { dt_size * n_col, dt_size },
                              self.get_type() == socket_t::SIN),
              buffer_handle);
            entry.n_frames = n_frames;
            entry.n_elmts = n_elmts;
            entry.rows = n_row;
            entry.cols = n_col;
            entry.ptr = dataptr;
            return Py_NewRef(entry.arr.ptr());
        }

        const size_t n_col = n_elmts / n_frames;
        py::capsule buffer_handle([]() {});
        const size_t dt_size = (size_t)self.get_datatype_size();
        py::array arr(
          py::buffer_info(dataptr,
                          (ssize_t)dt_size,
                          type_map.at(self.get_datatype()),
                          2,
                          { n_row, n_col },
                          { dt_size * n_col, dt_size },
                          self.get_type() == socket_t::SIN),
          buffer_handle);
        return arr.release().ptr();
    }
    catch (py::error_already_set& e)
    {
        e.restore();
        return nullptr;
    }
    catch (const std::exception& e)
    {
        PyErr_SetString(PyExc_RuntimeError, e.what());
        return nullptr;
    }
}

// Fast-path C getter for `Socket.memoryview`: returns a cached 1D `memoryview` of the current
// wave (`n_frames_per_wave * n_cols` elements), avoiding `memoryview(sck.wave).cast(...)`
// allocations on every task execution in pure-Python codelets.
inline PyObject*
get_cached_socket_memoryview_ptr(PyObject* self_obj)
{
    try
    {
        Socket_view_cache* cache = get_socket_view_cache(self_obj);
        if (cache == nullptr || cache->sck == nullptr)
        {
            PyObject* wave_obj = get_cached_socket_array_ptr(self_obj, true);
            if (wave_obj == nullptr) return nullptr;
            PyObject* mv = PyMemoryView_FromObject(wave_obj);
            Py_DECREF(wave_obj);
            return mv;
        }

        const spu::runtime::Socket& self = *cache->sck;
        void* dataptr = self.get_dataptr();
        if (dataptr == nullptr)
        {
            PyErr_SetString(PyExc_RuntimeError, "Socket has no allocated data.");
            return nullptr;
        }

        const spu::module::Module& mdl = *cache->mdl;
        const size_t n_frames = mdl.get_n_frames();
        const size_t n_row = mdl.get_n_frames_per_wave();
        const size_t n_elmts = self.get_n_elmts();
        auto& entry = cache->wave;

        if (entry.n_frames == n_frames && entry.rows == n_row && entry.n_elmts == n_elmts && entry.mv)
        {
            if (entry.mv_ptr != dataptr)
            {
                if (entry.arr_1d)
                    py::detail::array_proxy(entry.arr_1d.ptr())->data = static_cast<char*>(dataptr);
                PyMemoryView_GET_BUFFER(entry.mv.ptr())->buf = dataptr;
                entry.mv_ptr = dataptr;
            }
            return Py_NewRef(entry.mv.ptr());
        }

        const size_t n_col = n_elmts / n_frames;
        const size_t total_wave_elmts = n_row * n_col;
        py::capsule buffer_handle([]() {});
        const size_t dt_size = (size_t)self.get_datatype_size();
        entry.arr_1d = py::array(
          py::buffer_info(dataptr,
                          (ssize_t)dt_size,
                          type_map.at(self.get_datatype()),
                          1,
                          { total_wave_elmts },
                          { dt_size },
                          self.get_type() == socket_t::SIN),
          buffer_handle);
        PyObject* mv_raw = PyMemoryView_FromObject(entry.arr_1d.ptr());
        if (mv_raw == nullptr) return nullptr;
        entry.mv = py::reinterpret_steal<py::object>(mv_raw);
        entry.n_frames = n_frames;
        entry.n_elmts = n_elmts;
        entry.rows = n_row;
        entry.cols = n_col;
        entry.mv_ptr = dataptr;
        return Py_NewRef(entry.mv.ptr());
    }
    catch (py::error_already_set& e)
    {
        e.restore();
        return nullptr;
    }
    catch (const std::exception& e)
    {
        PyErr_SetString(PyExc_RuntimeError, e.what());
        return nullptr;
    }
}

// New reference returned by a fast getter, or the pending Python error raised as a C++ exception
inline PyObject*
check_new_ref(PyObject* obj)
{
    if (obj == nullptr) throw py::error_already_set();
    return obj;
}

getattrofunc orig_socket_getattro = nullptr;
PyObject* k_wave_attr = nullptr;
PyObject* k_numpy_attr = nullptr;
PyObject* k_memoryview_attr = nullptr;

// Fast C `tp_getattro` slot for `Socket`: compares `name` by pointer identity against the
// interned strings `"wave"`, `"numpy"`, and `"memoryview"` before falling back to
// `PyObject_GenericGetAttr`, bypassing `_PyType_Lookup` and descriptor dispatch.
PyObject*
socket_tp_getattro(PyObject* self, PyObject* name)
{
    if (name == k_wave_attr)
        return get_cached_socket_array_ptr(self, true);
    if (name == k_numpy_attr)
        return get_cached_socket_array_ptr(self, false);
    if (name == k_memoryview_attr)
        return get_cached_socket_memoryview_ptr(self);
    return orig_socket_getattro(self, name);
}
} // namespace

void
pyspu::wrapper::wrap_socket(py::handle scope)
{
    py::class_<Socket, spu::tools::Interface_reset, spu::runtime::Socket_Publicist> py_socket(
      scope, "Socket", py::buffer_protocol(), py::dynamic_attr(), R"pbdoc(
        Data exchanged between tasks.

        A socket belongs to a task and has a name, a data type (`dtype`), a number of
        elements and a direction (input, output or forward). Its data is a 2D array with
        one row per frame, accessible without copy through `numpy`.

        Python operators (`+`, `<`, `&`, `x[::2]`...) can be used on sockets: each one
        creates a module, binds it to its operands and executes it.
    )pbdoc");

    py::enum_<socket_t>(py_socket, "directions", "Enumeration of socket directions")
      .value("IN", socket_t::SIN, "Input socket")
      .value("OUT", socket_t::SOUT, "Output socket")
      .value("FWD", socket_t::SFWD, "Forward socket");

    py_socket.def_buffer(
      [](Socket& s) -> py::buffer_info
      {
          if (s.get_dataptr() == nullptr)
              return py::buffer_info(nullptr, s.get_datatype_size(), type_map[s.get_datatype()], 0);

          size_t n_frames = s.get_task().get_module().get_n_frames();
          size_t n_row = n_frames;
          size_t n_col = s.get_n_elmts() / n_frames;

          return py::buffer_info(s.get_dataptr(),            /* Pointer to buffer */
                                 s.get_datatype_size(),      /* Size of one scalar */
                                 type_map[s.get_datatype()], /* Python struct-style format descriptor */
                                 2,                          /* Number of dimensions */
                                 { n_row, n_col },           /* Buffer dimensions */
                                 { (size_t)s.get_datatype_size() * n_col, (size_t)s.get_datatype_size() },
                                 s.get_type() == socket_t::SIN);
      });
    // `wave`, `numpy` and `memoryview` are pybind11 properties (seen by pybind11-stubgen and
    // `help()`), but they are only reached by introspection: `tp_getattro` is hooked so that
    // reading them on an instance (`sck.wave`, `sck.numpy`, `sck.memoryview`) resolves the
    // interned name by pointer identity, without `_PyType_Lookup` and descriptor dispatch.
    py_socket.def_property_readonly(
      "wave",
      [](py::handle self) -> py::array
      { return py::reinterpret_steal<py::array>(check_new_ref(get_cached_socket_array_ptr(self.ptr(), true))); },
      "NumPy view (without copy) of the frames of the current wave (`n_frames_per_wave` rows).");
    py_socket.def_property_readonly(
      "numpy",
      [](py::handle self) -> py::array
      { return py::reinterpret_steal<py::array>(check_new_ref(get_cached_socket_array_ptr(self.ptr(), false))); },
      "NumPy view of the data of the socket (no copy), with one row per frame.");
    py_socket.def_property_readonly(
      "memoryview",
      [](py::handle self) -> py::memoryview
      { return py::reinterpret_steal<py::memoryview>(check_new_ref(get_cached_socket_memoryview_ptr(self.ptr()))); },
      "1D memoryview (without copy) of the elements of the current wave.");
    {
        k_wave_attr = PyUnicode_InternFromString("wave");
        k_numpy_attr = PyUnicode_InternFromString("numpy");
        k_memoryview_attr = PyUnicode_InternFromString("memoryview");
        auto* sck_type = reinterpret_cast<PyTypeObject*>(py_socket.ptr());
        if (sck_type->tp_getattro != nullptr)
        {
            orig_socket_getattro = sck_type->tp_getattro;
            sck_type->tp_getattro = &socket_tp_getattro;
        }
        PyType_Modified(sck_type);
    }

    py_socket.def_property_readonly("task", &spu::runtime::Socket::get_task, "Task owning the socket.");
    py_socket.def_property_readonly("n_elmts", &spu::runtime::Socket::get_n_elmts, "Total number of elements, for all the frames.");
    py_socket.def("get_bound_sockets", &spu::runtime::Socket::get_bound_sockets, "Return the sockets bound to this socket (for output sockets only).");
    py_socket.def_property_readonly(
      "dtype",
      [](const spu::runtime::Socket& self) { return pyspu::dtype::get(self.get_datatype_string()); },
      "Data type.");
    py_socket.def("get_bound_socket",
    [](const spu::runtime::Socket& self) { return &self.get_bound_socket(); },
    "Return the socket this socket is bound to (for input sockets only).", py::return_value_policy::reference);

    py_socket.def(
      "has_data",
      [](const spu::runtime::Socket& self) { return self.get_dataptr() != nullptr; },
      "Return True if the socket has data allocated.");
    py_socket.def_property_readonly(
      "dataaddr",
      [](const spu::runtime::Socket& self)
      {
          std::stringstream ss;
          ss << self.get_dataptr();
          return ss.str();
      },
      "Return the socket data address as str.");

    py_socket.def("__bool__",
                  [](const spu::runtime::Socket& sckt)
                  {
                        size_t n_frames = sckt.get_task().get_module().get_n_frames();
                        size_t n = sckt.get_n_elmts() / n_frames;
                        if (n > n_frames)
                        {
                            std::stringstream message;
                            message << "The truth value of an array with more than one element is "
                                        "ambiguous.";
                            throw spu::tools::runtime_error(message.str());
                        }
                        if (sckt.get_datatype() == typeid(int8_t))
                            return (bool)(static_cast<int8_t*>(sckt.get_dataptr())[0]);
                        else if (sckt.get_datatype() == typeid(int16_t))
                            return (bool)(static_cast<int16_t*>(sckt.get_dataptr())[0]);
                        else if (sckt.get_datatype() == typeid(int32_t))
                            return (bool)(static_cast<int32_t*>(sckt.get_dataptr())[0]);
                        else if (sckt.get_datatype() == typeid(int64_t))
                            return (bool)(static_cast<int64_t*>(sckt.get_dataptr())[0]);
                        else if (sckt.get_datatype() == typeid(uint8_t))
                            return (bool)(static_cast<uint8_t*>(sckt.get_dataptr())[0]);
                        else if (sckt.get_datatype() == typeid(uint16_t))
                            return (bool)(static_cast<uint16_t*>(sckt.get_dataptr())[0]);
                        else if (sckt.get_datatype() == typeid(uint32_t))
                            return (bool)(static_cast<uint32_t*>(sckt.get_dataptr())[0]);
                        else if (sckt.get_datatype() == typeid(uint64_t))
                            return (bool)(static_cast<uint64_t*>(sckt.get_dataptr())[0]);
                        else if (sckt.get_datatype() == typeid(float))
                            return (bool)(static_cast<float*>(sckt.get_dataptr())[0]);
                        else if (sckt.get_datatype() == typeid(double))
                            return (bool)(static_cast<double*>(sckt.get_dataptr())[0]);
                        else
                        {
                        std::stringstream message;
                        message << "Unknown socket type '" << sckt.get_datatype_string() << "'.";
                        throw spu::tools::unimplemented_error(message.str());
                        }
                  });
    py_socket.def("unbind", &spu::runtime::Socket::unbind, "s_out"_a, R"pbdoc(
        Unbind the socket from the socket `s_out`.

        Args:
            s_out (Socket): the output or forward socket this socket is bound to
    )pbdoc");
    py_socket.def(
      "_bind",
      [](spu::runtime::Socket& self, spu::runtime::Socket& s_out, const int priority) { self.bind(s_out, priority); },
      "Binds the socket to socket 's_out' with priority 'priority'.",
      "s_out"_a,
      "priority"_a = -1);

    py_socket.def(
      "_bind",
      [](spu::runtime::Socket& self, py::array& arr)
      {
          size_t n_row = (size_t)self.get_task().get_module().get_n_frames();
          size_t n_col = (size_t)self.get_n_elmts() / n_row;

          py::buffer_info buffer = arr.request();

          if (n_row > 1 && buffer.ndim == 2)
          {
              if ((size_t)buffer.shape[0] != n_row || (size_t)buffer.shape[1] != n_col)
              {
                  std::stringstream message;
                  message << "The shape of the array must match the socket one.";
                  message << "Socket shape: " << n_row << " x " << n_col << ".";
                  message << "Array shape: " << buffer.shape[0] << " x " << buffer.shape[1] << ".\n";
                  throw spu::tools::runtime_error(message.str());
              }
          }
          else if (n_row == 1 && buffer.ndim == 1)
          {
              if ((size_t)buffer.shape[0] != n_col)
              {
                  std::stringstream message;
                  message << "The shape of the array must match the socket one.";
                  message << "Socket shape: " << 1 << " x " << n_col << ".";
                  message << "Array shape: " << 1 << " x " << buffer.shape[0] << ".\n";
                  throw spu::tools::runtime_error(message.str());
              }
          }

          py::array py_self = py::cast(self);
          if (!arr.dtype().is(py_self.dtype()))
          {
              std::stringstream message;
              message << "The dtype of the array must match the socket one.\n";
              message << "Socket dtype: " << py_self.dtype().attr("name").cast<std::string>() << ".\n";
              message << "Array dtype: " << arr.dtype().attr("name").cast<std::string>() << ".\n";
              throw spu::tools::runtime_error(message.str());
          }

          self.bind(buffer.ptr);
      },
      "Binds the socket to the numpy array 'array' data.",
      "array"_a);
    py_socket.def_property_readonly("name", &spu::runtime::Socket::get_name, "Name of the socket in its task.");
    py_socket.def_property_readonly("direction", &spu::runtime::Socket::get_type, "Direction of the socket (`Socket.directions.IN`, `OUT` or `FWD`).");
};
