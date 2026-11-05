#ifndef WRAPPER_SOCKET_CREATION_HPP_
#define WRAPPER_SOCKET_CREATION_HPP_

#include <string>

#include "wrapper/Common/Tools/Type/Type.hpp"
#include "wrapper/Common/Tools/type_functions.h"
#include "wrapper/Common/pybind11_common.h"
#include <streampu.hpp>

namespace pyspu
{
namespace wrapper
{
// Define create_socket_in, create_socket_out and create_socket_fwd(task, name, n_elmts, dtype)
// on the Python class of a module M whose socket creation takes a std::type_index
template<class M, class PyClass>
void
def_socket_creation(PyClass& cls)
{
    namespace py = pybind11;
    using namespace py::literals;
    cls.def(
      "create_socket_in",
      [](M& mdl, spu::runtime::Task& task, const std::string& name, const size_t n_elmts, const pyspu::dtype dtype)
      { return mdl.create_socket_in(task, name, n_elmts, pyspu::utils::str2typeid(dtype.get_name())); },
      "task"_a,
      "name"_a,
      "n_elmts"_a,
      "dtype"_a,
      "Create a new input socket to a task; returns its index.");
    cls.def(
      "create_socket_out",
      [](M& mdl, spu::runtime::Task& task, const std::string& name, const size_t n_elmts, const pyspu::dtype dtype)
      { return mdl.create_socket_out(task, name, n_elmts, pyspu::utils::str2typeid(dtype.get_name())); },
      "task"_a,
      "name"_a,
      "n_elmts"_a,
      "dtype"_a,
      "Create a new output socket to a task; returns its index.");
    cls.def(
      "create_socket_fwd",
      [](M& mdl, spu::runtime::Task& task, const std::string& name, const size_t n_elmts, const pyspu::dtype dtype)
      { return mdl.create_socket_fwd(task, name, n_elmts, pyspu::utils::str2typeid(dtype.get_name())); },
      "task"_a,
      "name"_a,
      "n_elmts"_a,
      "dtype"_a,
      "Create a new forward socket to a task (read and written in place); returns its index.");
}
} // namespace wrapper
} // namespace pyspu

#endif // WRAPPER_SOCKET_CREATION_HPP_
