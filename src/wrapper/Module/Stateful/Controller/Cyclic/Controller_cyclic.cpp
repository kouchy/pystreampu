#include "wrapper/Module/Stateful/Controller/Cyclic/Controller_cyclic.hpp"

#include "wrapper/Common/Tools/Type/Type.hpp"
#include "wrapper/Common/Tools/type_functions.h"

namespace py = pybind11;
using namespace pyspu::wrapper;
using namespace py::literals;

void
pyspu::wrapper::wrap_controller_cyclic(py::handle scope)
{
    auto py_controller_cyclic_class =
      py::class_<spu::module::Controller_cyclic, spu::module::Controller>(scope, "Controller_cyclic", "Controller that cycles through the paths: 0, 1, ..., n_paths - 1, 0, ...");
    py_controller_cyclic_class.def(
      py::init<const size_t, const size_t>(), "n_paths"_a, "init_path"_a = 0,
      R"pbdoc(
        Build a cyclic controller.

        Args:
            n_paths (int): number of paths
            init_path (int): first path
    )pbdoc",
      py::return_value_policy::take_ownership);

    py_controller_cyclic_class.def_property(
      "path", &spu::module::Controller_cyclic::get_path, &spu::module::Controller_cyclic::set_path,
      "Index of the current path.");
    py_controller_cyclic_class.def("set_n_paths", &spu::module::Controller_cyclic::set_n_paths, "n_paths"_a,
      R"pbdoc(
        Change the number of paths.

        Args:
            n_paths (int): number of paths
    )pbdoc");
}
