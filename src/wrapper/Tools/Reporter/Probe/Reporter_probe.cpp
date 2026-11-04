#include "wrapper/Tools/Reporter/Probe/Reporter_probe.hpp"
#include "wrapper/Common/Tools/Format/Format.hpp"

#include "wrapper/Common/Tools/Type/Type.hpp"
#include "wrapper/Common/Tools/type_functions.h"
#include "wrapper/Common/Tools/type_list.hpp"

namespace py = pybind11;
using namespace py::literals;
using namespace pyspu::wrapper;

void
pyspu::wrapper::wrap_reporter_probe(py::module_& scope)
{
    auto rep_probe_class =
      py::class_<spu::tools::Reporter_probe, spu::tools::Reporter, spu::tools::Interface_get_set_n_frames>(
        scope, "Reporter_probe", R"pbdoc(
        Reporter that gathers the values of probes, one column per probe.

        Probes are attached to it when they are created (their `reporter` argument).
    )pbdoc");

    // Constructor
    rep_probe_class.def(py::init<const std::string&, const std::string&>(), "group_name"_a, "group_description"_a, R"pbdoc(
        Build a reporter.

        Args:
            group_name (str): title of the group of columns
            group_description (str): subtitle of the group of columns
    )pbdoc");
    rep_probe_class.def("register_probes", &spu::tools::Reporter_probe::register_probes, "probes"_a, R"pbdoc(
        Attach probes to the reporter.

        Args:
            probes (list[AProbe]): probes to attach
    )pbdoc");
}
