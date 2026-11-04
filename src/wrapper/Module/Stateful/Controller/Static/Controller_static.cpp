#include "wrapper/Module/Stateful/Controller/Static/Controller_static.hpp"

#include "wrapper/Common/Tools/Type/Type.hpp"
#include "wrapper/Common/Tools/type_functions.h"

namespace py = pybind11;
using namespace pyspu::wrapper;
using namespace py::literals;

void
pyspu::wrapper::wrap_controller_static(py::handle scope)
{
    auto py_controller_static_class =
      py::class_<spu::module::Controller_static, spu::module::Controller>(scope, "Controller_static", "Controller that always outputs the same path (it can be changed with `path`).");
    py_controller_static_class.def(
      py::init<const size_t>(), "init_path"_a = 0,
      R"pbdoc(
        Build a static controller.

        Args:
            init_path (int): path to output
    )pbdoc",
      py::return_value_policy::take_ownership);
}
