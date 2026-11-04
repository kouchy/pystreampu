#include "wrapper/Tools/Interface/Interface_set_seed.hpp"

namespace py = pybind11;
using namespace py::literals;
using namespace pyspu::wrapper;

void
pyspu::wrapper::wrap_interface_set_seed(py::module_& scope)
{
    auto itf_class =
      py::class_<spu::tools::Interface_set_seed,
                 pyspu::wrapper::py_Interface_set_seed,
                 std::unique_ptr<spu::tools::Interface_set_seed, py::nodelete>>(scope, "Interface_set_seed", "Interface of the objects that use a random generator.");

    itf_class.def("set_seed", &spu::tools::Interface_set_seed::set_seed, "seed"_a, R"pbdoc(
        Set the seed of the random generator.

        Args:
            seed (int): the new seed
    )pbdoc");
}