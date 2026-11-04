#include "wrapper/Module/Stateful/Set/Set.hpp"

#include "wrapper/Common/Tools/type_functions.h"
#include <map>
#include <memory>
#include <typeindex>
#include <typeinfo>

namespace py = pybind11;
using namespace py::literals;

void
pyspu::wrapper::wrap_set(py::handle scope)
{
    auto set_class = py::class_<spu::module::Set, spu::module::Stateful>(scope, "Set", "Module that wraps a sequence, so that the whole sequence can be used as a single task (`exec`).");
    set_class.def(py::init<spu::runtime::Sequence&>(), "sequence"_a, py::keep_alive<1, 2>(),
                  R"pbdoc(
        Build a set from a sequence.

        Args:
            sequence (Sequence): the sequence to wrap
    )pbdoc");
    set_class.def_property_readonly("sequence", &spu::module::Set::get_sequence, "Sequence wrapped by the set.");
}
