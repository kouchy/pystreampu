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
// Per-Socket-wrapper cache of the `numpy` and `wave` 2D NumPy `ndarray` views.
//
// Why this cache exists:
// - Previously, every access to `sck.wave` or `sck.numpy` inside a Python codelet constructed
//   a brand-new `py::capsule`, a new `py::buffer_info` (with heap-allocated `shape` and `strides`
//   vectors), and a new `PyArrayObject` via NumPy's C-API (~800 ns per socket access).
// - By enabling `py::dynamic_attr()` on `Socket`, each Python `Socket` wrapper has an instance
//   `__dict__` where we store a `PyCapsule` owning a `Socket_view_cache` (automatically freed when
//   the Python `Socket` wrapper is garbage-collected).
// - On subsequent accesses with the same dimensions `(n_row, n_col)`, we reuse the cached
//   `py::array` directly. If the underlying C++ socket `dataptr` changed (e.g., when advancing to
//   a new wave within a multi-wave buffer or after rebinding), we update the `PyArrayObject`'s
//   internal `data` pointer in place (`array_proxy(arr)->data = dataptr`) in a single pointer
//   store, with zero allocations.
struct Socket_view_cache
{
    struct Entry
    {
        size_t rows = 0;
        size_t cols = 0;
        void* ptr = nullptr;
        py::array arr;
    };
    Entry wave;
    Entry numpy;
};

// Retrieve (or lazily allocate) the `Socket_view_cache` attached to `self_h.__dict__`.
inline Socket_view_cache*
get_socket_view_cache(py::handle self_h)
{
    static PyObject* k_cache_key = PyUnicode_InternFromString("_spu_view_cache");
    PyObject** dict_ptr = _PyObject_GetDictPtr(self_h.ptr());
    if (dict_ptr == nullptr) return nullptr;
    if (*dict_ptr == nullptr)
    {
        *dict_ptr = PyDict_New();
        if (*dict_ptr == nullptr) return nullptr;
    }
    PyObject* cap = PyDict_GetItemWithError(*dict_ptr, k_cache_key);
    if (cap != nullptr)
        return static_cast<Socket_view_cache*>(PyCapsule_GetPointer(cap, "spu_socket_view_cache"));

    auto* cache = new Socket_view_cache();
    py::capsule py_cap(cache, "spu_socket_view_cache", [](void* p) { delete static_cast<Socket_view_cache*>(p); });
    PyDict_SetItem(*dict_ptr, k_cache_key, py_cap.ptr());
    return cache;
}

// Fast-path getter for `Socket.wave` (`is_wave = true`) and `Socket.numpy` (`is_wave = false`).
inline py::array
get_cached_socket_array(py::handle self_h, const spu::runtime::Socket& self, const bool is_wave)
{
    void* dataptr = self.get_dataptr();
    if (dataptr == nullptr)
        return py::array(py::buffer_info(nullptr, self.get_datatype_size(), type_map[self.get_datatype()], {}));

    const auto& mdl = self.get_task().get_module();
    const size_t n_frames = mdl.get_n_frames();
    const size_t n_row = is_wave ? mdl.get_n_frames_per_wave() : n_frames;
    const size_t n_col = self.get_n_elmts() / n_frames;

    if (Socket_view_cache* cache = get_socket_view_cache(self_h))
    {
        auto& entry = is_wave ? cache->wave : cache->numpy;
        // Fast path: dimensions match the cached `ndarray` view; only patch `data` if `dataptr` moved.
        if (entry.rows == n_row && entry.cols == n_col && entry.arr)
        {
            if (entry.ptr != dataptr)
            {
                py::detail::array_proxy(entry.arr.ptr())->data = static_cast<char*>(dataptr);
                entry.ptr = dataptr;
            }
            return entry.arr;
        }

        // Slow path (first access, or after `n_frames` / `n_frames_per_wave` changed):
        // allocate the 2D `ndarray` view once and cache it. Input sockets (`SIN`) are marked read-only.
        py::capsule buffer_handle([]() {});
        const size_t dt_size = (size_t)self.get_datatype_size();
        entry.arr = py::array(
          py::buffer_info(dataptr,
                          (ssize_t)dt_size,
                          type_map[self.get_datatype()],
                          2,
                          { n_row, n_col },
                          { dt_size * n_col, dt_size },
                          self.get_type() == socket_t::SIN),
          buffer_handle);
        entry.rows = n_row;
        entry.cols = n_col;
        entry.ptr = dataptr;
        return entry.arr;
    }

    py::capsule buffer_handle([]() {});
    const size_t dt_size = (size_t)self.get_datatype_size();
    return py::array(
      py::buffer_info(dataptr,
                      (ssize_t)dt_size,
                      type_map[self.get_datatype()],
                      2,
                      { n_row, n_col },
                      { dt_size * n_col, dt_size },
                      self.get_type() == socket_t::SIN),
      buffer_handle);
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
    py_socket.def_property_readonly(
      "wave",
      [](py::handle self_h) -> py::array
      {
          const auto& self = self_h.cast<const spu::runtime::Socket&>();
          return get_cached_socket_array(self_h, self, true);
      },
      "NumPy view (without copy) of the frames of the current wave (`n_frames_per_wave` rows).");

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

    py_socket.def_property_readonly(
      "numpy",
      [](py::handle self_h) -> py::array
      {
          const auto& self = self_h.cast<const spu::runtime::Socket&>();
          return get_cached_socket_array(self_h, self, false);
      },
      "NumPy view of the data of the socket (no copy), with one row per frame.");

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
