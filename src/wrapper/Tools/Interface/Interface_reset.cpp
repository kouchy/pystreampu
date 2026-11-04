#include "wrapper/Tools/Interface/Interface_reset.hpp"

namespace py = pybind11;
using namespace py::literals;
using namespace pyspu::wrapper;

void
pyspu::wrapper::wrap_interface_reset(py::module_& scope)
{
    auto itf_class =
      py::class_<spu::tools::Interface_reset, pyspu::wrapper::py_Interface_reset>(scope, "Interface_reset", "Interface of the objects that can be reset to their initial state.");
    itf_class.def("reset", &spu::tools::Interface_reset::reset, "Reset the object to its initial state.");
}