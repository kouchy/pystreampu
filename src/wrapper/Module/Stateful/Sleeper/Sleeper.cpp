#include "wrapper/Module/Stateful/Sleeper/Sleeper.hpp"

namespace py = pybind11;
using namespace pyspu::wrapper;
using namespace py::literals;

void
pyspu::wrapper::wrap_sleeper(py::handle scope)
{
    auto doc_str = R"pbdoc(
        Build a sleeper.

        Args:
            ns (int): sleep duration per execution, in nanoseconds
    )pbdoc";
    auto py_sleeper_class = py::class_<spu::module::Sleeper, spu::module::Stateful>(scope, "Sleeper", "Module whose task only sleeps, e.g. to emulate some work.");

    py_sleeper_class.def(py::init<const size_t>(), "ns"_a = 0, doc_str, py::return_value_policy::take_ownership);
    py_sleeper_class.def_property("ns", &spu::module::Sleeper::get_ns, &spu::module::Sleeper::set_ns,
                                  "Sleep duration per execution, in nanoseconds.");
}
