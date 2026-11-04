#include "wrapper/Tools/Signal_handler/Signal_handler.hpp"

#include "wrapper/Common/pybind11_common.h"

namespace py = pybind11;
using namespace py::literals;
using namespace pyspu::wrapper;

void
pyspu::wrapper::wrap_signal_handler(py::module_& scope)
{
    auto signal_handler_class = py::class_<spu::tools::Signal_handler>(scope, "Signal_handler", R"pbdoc(
        Handler of the SIGINT (Ctrl+C) and SIGSEGV signals.

        After `Signal_handler.init()`, a first Ctrl+C sets a flag that stops the running
        sequences cleanly; a second one kills the program.
    )pbdoc");
    signal_handler_class.def_static("is_sigint", &spu::tools::Signal_handler::is_sigint, "Return True if SIGINT (Ctrl+C) has been received since the last reset.");
    signal_handler_class.def_static("is_sigsegv", &spu::tools::Signal_handler::is_sigsegv, "Return True if SIGSEGV has been received since the last reset.");
    signal_handler_class.def_static("init", &spu::tools::Signal_handler::init, "Install the StreamPU handlers of SIGINT and SIGSEGV.");
    signal_handler_class.def_static("reset_sigint", &spu::tools::Signal_handler::reset_sigint, "Clear the SIGINT flag.");
    signal_handler_class.def_static("reset_sigsegv", &spu::tools::Signal_handler::reset_sigsegv, "Clear the SIGSEGV flag.");
}