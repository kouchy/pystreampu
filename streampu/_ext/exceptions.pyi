from __future__ import annotations

__all__: list[str] = [
    "CannotAllocate",
    "ControlFlowError",
    "DomainError",
    "InvalidArgument",
    "JuliaError",
    "LengthError",
    "LogicError",
    "OutOfRange",
    "OverflowError",
    "ProcessingAborted",
    "RangeError",
    "RuntimeError",
    "UnderflowError",
    "UnimplementedError",
    "WaitingCanceled",
]

class CannotAllocate(Exception):
    """
    Memory could not be allocated.
    """

class ControlFlowError(Exception):
    """
    Error in the control flow of a sequence (switchers, loops).
    """

class DomainError(Exception):
    """
    A value is outside the domain of a function.
    """

class InvalidArgument(Exception):
    """
    An argument has an invalid value.
    """

class JuliaError(Exception):
    """
    Error raised by the Julia runtime or a Julia codelet.
    """

class LengthError(Exception):
    """
    A size is too large.
    """

class LogicError(Exception):
    """
    Error in the logic of the program.
    """

class OutOfRange(Exception):
    """
    An index or a value is out of the expected range.
    """

class OverflowError(Exception):
    """
    Arithmetic overflow.
    """

class ProcessingAborted(Exception):
    """
    Raised to stop the processing of a sequence (e.g. by `Task.abort_processing`).
    """

class RangeError(Exception):
    """
    A result cannot be represented.
    """

class RuntimeError(Exception):
    """
    Generic StreamPU error raised during the execution.
    """

class UnderflowError(Exception):
    """
    Arithmetic underflow.
    """

class UnimplementedError(Exception):
    """
    The requested feature is not implemented.
    """

class WaitingCanceled(Exception):
    """
    Raised when a task waiting for data is canceled (e.g. by `Task.cancel_waiting`).
    """
