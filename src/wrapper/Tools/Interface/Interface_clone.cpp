#include "wrapper/Tools/Interface/Interface_clone.hpp"

namespace py = pybind11;
using namespace py::literals;
using namespace pyspu::wrapper;

void
pyspu::wrapper::wrap_interface_clone(py::module_& scope)
{
    auto itf_class = py::class_<spu::tools::Interface_clone,
                                pyspu::wrapper::py_Interface_clone,
                                std::unique_ptr<spu::tools::Interface_clone, py::nodelete>>(scope, "Interface_clone", "Interface of the objects that can be duplicated (e.g. on several threads).");
    itf_class.def("clone", &spu::tools::Interface_clone::clone, R"pbdoc(
        Return a copy of the object.

        Returns:
            out (Interface_clone): the copy
    )pbdoc");
}