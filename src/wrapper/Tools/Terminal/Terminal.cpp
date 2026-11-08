#include "wrapper/Tools/Terminal/Terminal.hpp"

namespace py = pybind11;
using namespace py::literals;
using namespace pyspu::wrapper;

void
pyspu::wrapper::wrap_terminal(py::module_& scope)
{
    auto ter_class = py::class_<spu::tools::Terminal, pyspu::wrapper::py_Terminal>(scope, "Terminal", "Base class of the terminals, which display the reports of reporters.");
    auto sys = py::module::import("sys");
    ter_class.def(py::init<>());
    ter_class.def("legend", &spu::tools::Terminal::legend, "stream"_a = sys.attr("stdout"), R"pbdoc(
        Print the legend: titles, names and units of the columns.

        Args:
            stream (file): stream where the legend is written
    )pbdoc");
    ter_class.def("temp_report", &spu::tools::Terminal::temp_report, "stream"_a = sys.attr("stdout"), R"pbdoc(
        Print a temporary report (the line is overwritten by the next report).

        Args:
            stream (file): stream where the report is written
    )pbdoc");
    ter_class.def("final_report", &spu::tools::Terminal::final_report, "stream"_a = sys.attr("stdout"), R"pbdoc(
        Print the final report.

        Args:
            stream (file): stream where the report is written
    )pbdoc");
    ter_class.def("start_temp_report", &spu::tools::Terminal::start_temp_report, "freq"_a = std::chrono::milliseconds(500), R"pbdoc(
        Print temporary reports periodically, from a background thread.

        Args:
            freq (datetime.timedelta): period of the reports
    )pbdoc");
    ter_class.def("stop_temp_report", &spu::tools::Terminal::stop_temp_report, "Stop the periodic reports started by `start_temp_report`.");
    ter_class.def("report", &pyspu::wrapper::Publicist_Terminal::report, "stream"_a = sys.attr("stdout"), "final"_a = false, R"pbdoc(
        Print a report line with the current values of the reporters.

        Args:
            stream (file): stream where the report is written
            final (bool): True for the final report
    )pbdoc");

    auto ter_std_class = py::class_<spu::tools::Terminal_std, spu::tools::Terminal>(scope, "Terminal_std", "Terminal that prints the reports as aligned columns.");
    // keep_alive<1, 2>: the terminal keeps the list of the reporters (and so the reporters) alive,
    // it only stores pointers to them
    ter_std_class.def(py::init<const std::vector<spu::tools::Reporter*>&>(), "reporters"_a, py::keep_alive<1, 2>(), R"pbdoc(
        Build a terminal.

        The terminal keeps the reporters alive (the list given here).

        Args:
            reporters (list[Reporter]): reporters to display
    )pbdoc");
    // reference_internal: the reporters belong to their Python objects, not to the returned list
    ter_std_class.def_property_readonly("reporters", &spu::tools::Terminal_std::get_reporters, py::return_value_policy::reference_internal, "Reporters displayed by the terminal.");

    auto ter_dmp_class = py::class_<spu::tools::Terminal_dump, spu::tools::Terminal_std>(scope, "Terminal_dump", "Terminal that prints one line per report (no overwritten temporary line), e.g. to a file.");
    ter_dmp_class.def(py::init<const std::vector<spu::tools::Reporter*>&>(), "reporters"_a, py::keep_alive<1, 2>(), R"pbdoc(
        Build a terminal.

        The terminal keeps the reporters alive (the list given here).

        Args:
            reporters (list[Reporter]): reporters to display
    )pbdoc");
}