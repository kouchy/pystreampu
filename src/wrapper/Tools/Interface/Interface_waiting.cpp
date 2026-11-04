#include "wrapper/Tools/Interface/Interface_waiting.hpp"

namespace py = pybind11;
using namespace py::literals;
using namespace pyspu::wrapper;

void
pyspu::wrapper::wrap_interface_waiting(py::module_& scope)
{
    auto itf_class =
      py::class_<spu::tools::Interface_waiting, spu::tools::Interface_reset, pyspu::wrapper::py_Interface_waiting>(
        scope, "Interface_waiting", "Interface of the objects that can block while waiting for data (e.g. pipeline adaptors).");

    itf_class.def("send_cancel_signal", &spu::tools::Interface_waiting::send_cancel_signal, "Ask the waiting tasks to stop waiting.");
    itf_class.def("wake_up", &spu::tools::Interface_waiting::wake_up, "Wake up the waiting tasks.");
    itf_class.def("cancel_waiting", &spu::tools::Interface_waiting::cancel_waiting, "Send the cancel signal and wake up the waiting tasks.");
}