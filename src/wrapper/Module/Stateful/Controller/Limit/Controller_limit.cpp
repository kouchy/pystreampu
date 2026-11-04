#include "wrapper/Module/Stateful/Controller/Limit/Controller_limit.hpp"

#include "wrapper/Common/Tools/Type/Type.hpp"
#include "wrapper/Common/Tools/type_functions.h"

namespace py = pybind11;
using namespace pyspu::wrapper;
using namespace py::literals;

void
pyspu::wrapper::wrap_controller_limit(py::handle scope)
{
    auto py_controller_limit_class =
      py::class_<spu::module::Controller_limit, spu::module::Controller>(scope, "Controller_limit", "Controller that outputs `init_path` for the first `limit` executions, then the other path.");
    py_controller_limit_class.def(
      py::init<const size_t, const size_t>(), "limit"_a, "init_path"_a = 0,
      R"pbdoc(
        Build a controller with a limit.

        Args:
            limit (int): number of executions before switching path
            init_path (int): first path (0 or 1)
    )pbdoc",
      py::return_value_policy::take_ownership);
}
