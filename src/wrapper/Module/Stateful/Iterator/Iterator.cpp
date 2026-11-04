#include "wrapper/Module/Stateful/Iterator/Iterator.hpp"

namespace py = pybind11;
using namespace pyspu::wrapper;
using namespace py::literals;

void
pyspu::wrapper::wrap_iterator(py::handle scope)
{
    auto doc_str = R"pbdoc(
        Build an iterator.

        Args:
            limit (int): number of iterations before leaving the loop
    )pbdoc";
    auto py_iterator_class =
      py::class_<spu::module::Iterator, spu::module::Stateful, spu::tools::Interface_reset>(scope, "Iterator", "Module that controls a loop: it outputs 0 for `limit` executions, then 1 to leave the loop, and starts again.");
    py_iterator_class.def(py::init<const size_t>(), "limit"_a, doc_str, py::return_value_policy::take_ownership);
    py_iterator_class.def_property("limit", &spu::module::Iterator::get_limit, &spu::module::Iterator::set_limit,
                                   "Number of iterations of the loop.");
}
