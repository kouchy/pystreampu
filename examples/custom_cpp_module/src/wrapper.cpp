#include "Adder.hpp"
#include <pybind11/pybind11.h>
#include <streampu.hpp>

namespace py = pybind11;
using namespace py::literals;

// Create a	python module using PYBIND11, here our module will be named pyaf
PYBIND11_MODULE(my_module, m)
{
    auto pyspu_stateful = (py::object)py::module_::import("streampu");
    // Each extension linked with the static StreamPU library has its own copy of the
    // allocator settings: enable the automatic allocation of the task sockets here too,
    // as streampu does for its own modules.
    spu::tools::Buffer_allocator::set_task_autoalloc(true);
    m.attr("spu") = pyspu_stateful;
    py::class_<Adder, spu::module::Stateful>(m, "Adder").def(py::init<const int>(), "n_elmts"_a);
}
