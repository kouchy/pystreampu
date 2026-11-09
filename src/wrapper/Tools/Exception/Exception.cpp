#include "wrapper/Tools/Exception/Exception.hpp"

namespace py = pybind11;
using namespace py::literals;
using namespace pyspu::wrapper;

void
pyspu::wrapper::wrap_exceptions(py::module_& scope)
{
    py::register_exception<spu::tools::cannot_allocate>(scope, "CannotAllocate").attr("__doc__") = "Memory could not be allocated.";
    py::register_exception<spu::tools::control_flow_error>(scope, "ControlFlowError").attr("__doc__") = "Error in the control flow of a sequence (switchers, loops).";
    py::register_exception<spu::tools::domain_error>(scope, "DomainError").attr("__doc__") = "A value is outside the domain of a function.";
    py::register_exception<spu::tools::invalid_argument>(scope, "InvalidArgument").attr("__doc__") = "An argument has an invalid value.";
    py::register_exception<spu::tools::julia_error>(scope, "JuliaError").attr("__doc__") = "Error raised by the Julia runtime or a Julia codelet.";
    py::register_exception<spu::tools::length_error>(scope, "LengthError").attr("__doc__") = "A size is too large.";
    py::register_exception<spu::tools::logic_error>(scope, "LogicError").attr("__doc__") = "Error in the logic of the program.";
    py::register_exception<spu::tools::out_of_range>(scope, "OutOfRange").attr("__doc__") = "An index or a value is out of the expected range.";
    py::register_exception<spu::tools::overflow_error>(scope, "OverflowError").attr("__doc__") = "Arithmetic overflow.";
    py::register_exception<spu::tools::processing_aborted>(scope, "ProcessingAborted").attr("__doc__") = "Raised to stop the processing of a sequence (e.g. by `Task.abort_processing`).";
    py::register_exception<spu::tools::range_error>(scope, "RangeError").attr("__doc__") = "A result cannot be represented.";
    py::register_exception<spu::tools::runtime_error>(scope, "RuntimeError").attr("__doc__") = "Generic StreamPU error raised during the execution.";
    py::register_exception<spu::tools::underflow_error>(scope, "UnderflowError").attr("__doc__") = "Arithmetic underflow.";
    py::register_exception<spu::tools::unimplemented_error>(scope, "UnimplementedError").attr("__doc__") = "The requested feature is not implemented.";
    py::register_exception<spu::tools::waiting_canceled>(scope, "WaitingCanceled").attr("__doc__") = "Raised when a task waiting for data is canceled (e.g. by `Task.cancel_waiting`).";
}