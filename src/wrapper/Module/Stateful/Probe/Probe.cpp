#include "wrapper/Module/Stateful/Probe/Probe.hpp"

#include "wrapper/Common/Tools/Type/Type.hpp"
#include "wrapper/Common/Tools/Format/Format.hpp"
#include "wrapper/Common/Tools/type_functions.h"
#include "wrapper/Common/Tools/type_list.hpp"


#include "wrapper/Module/Stateful/Probe/Latency/Probe_latency.hpp"
#include "wrapper/Module/Stateful/Probe/Occurrence/Probe_occurrence.hpp"
#include "wrapper/Module/Stateful/Probe/Throughput/Probe_throughput.hpp"
#include "wrapper/Module/Stateful/Probe/Time/Probe_time.hpp"
#include "wrapper/Module/Stateful/Probe/Timestamp/Probe_timestamp.hpp"

namespace py = pybind11;
using namespace py::literals;

void
pyspu::wrapper::wrap_probe(py::handle scope)
{
    // AProbe has a protected destructor
    auto aprobe_class = py::class_<spu::module::AProbe,
                                   spu::module::Stateful,
                                   spu::tools::Interface_reset,
                                   std::unique_ptr<spu::module::AProbe, py::nodelete>>(scope, "AProbe", "Base class of the probes: modules that observe the graph and fill a column of a `Reporter_probe`.");

    aprobe_class.def_property("str_display", &spu::module::AProbe::get_str_display, &spu::module::AProbe::set_str_display,
                              "If True, display the probed values as a string of characters.");


    using lT = tl::type_list<ALL_DTYPES>;
    lT::for_each(
      [&](auto t)
      {
          using T = typename decltype(t)::type;
          std::string T_str = spu::runtime::type_to_string[typeid(T)];
          auto probe_class = py::class_<spu::module::Probe<T>, spu::module::AProbe, pyspu::wrapper::py_Probe<T>>(
            scope, std::string("Probe_" + T_str).c_str());
          // probe_class.def(py::init<const int, const std::string &>(), "size"_a,
          // "col_name"_a, py::return_value_policy::take_ownership);
          probe_class.def("set_col_unit", &spu::module::Probe<T>::set_col_unit, "unit"_a, R"pbdoc(
        Set the unit displayed under the name of the column.

        Args:
            unit (str): the unit, e.g. "(s)"
    )pbdoc");
          probe_class.def("set_col_buff_size", &spu::module::Probe<T>::set_col_buff_size, "buffer_size"_a, R"pbdoc(
        Set the number of values kept by the probe between two reports.

        Args:
            buffer_size (int): number of values
    )pbdoc");
          probe_class.def(
            "set_col_fmtflags",
            [](spu::module::Probe<T>& self, const pyspu::fmtflags ff)
            { self.set_col_fmtflags(static_cast<std::ios_base::fmtflags>(ff)); },
            "ff"_a,
            R"pbdoc(
        Set the format of the values of the column.

        Args:
            ff (FormatFlags): format flags, e.g. `FormatFlags.fixed | FormatFlags.showpoint`
    )pbdoc");
          probe_class.def("set_col_prec", &spu::module::Probe<T>::set_col_prec, "precision"_a, R"pbdoc(
        Set the number of decimals of the values of the column.

        Args:
            precision (int): number of decimals
    )pbdoc");
          probe_class.def("set_col_size", &spu::module::Probe<T>::set_col_size, "col_size"_a, R"pbdoc(
        Set the width of the column.

        Args:
            col_size (int): width, in characters
    )pbdoc");
          probe_class.def("register_reporter", &spu::module::Probe<T>::register_reporter, "reporter"_a, py::keep_alive<1, 2>(), R"pbdoc(
        Attach the probe to a reporter (if it was not given at creation).

        Args:
            reporter (Reporter_probe): the reporter
    )pbdoc");
          probe_class.def("get_col_name", &spu::module::Probe<T>::get_col_name, "Return the name of the column of the probe.");

          py::class_<spu::module::Probe_value<T>, spu::module::Probe<T>>(scope,
                                                                         std::string("Probe_value_" + T_str).c_str())
            .def(py::init<const int, const std::string&, spu::tools::Reporter_probe*>(),
                 "size"_a,
                 "col_name"_a,
                 "reporter"_a,
                 py::keep_alive<1, 2>(),
                 R"pbdoc(
        Build a probe that reports the values of a socket (use `streampu.probe_value`).

        Args:
            size (int): number of elements of the probed socket
            col_name (str): name of the column
            reporter (Reporter_probe): reporter of the probe
    )pbdoc",
                 py::return_value_policy::take_ownership);
      });

    pyspu::wrapper::wrap_probe_latency(scope);
    pyspu::wrapper::wrap_probe_occurrence(scope);
    pyspu::wrapper::wrap_probe_throughput(scope);
    pyspu::wrapper::wrap_probe_time(scope);
    pyspu::wrapper::wrap_probe_timestamp(scope);
}
