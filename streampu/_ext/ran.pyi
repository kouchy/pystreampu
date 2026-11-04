from __future__ import annotations

import typing

import streampu._ext
import streampu._ext.core
import streampu._ext.sfl

__all__: list[str] = ["Range"]

class Range(streampu._ext.sfl.Stateful):
    """

    Module that produces the values `start, start + step, ...` up to `stop` (excluded),
    one per execution, like the Python `range`. It can be iterated in Python.

    """

    def __init__(
        self,
        stop: typing.SupportsInt | typing.SupportsIndex,
        start: typing.SupportsInt | typing.SupportsIndex = 0,
        step: typing.SupportsInt | typing.SupportsIndex = 1,
        dtype: streampu._ext.dtype = ...,
    ) -> None:
        """
        Build a range.

        Args:
            stop (int): end of the range (excluded)
            start (int): first value
            step (int): step between two values
            dtype (dtype): data type of the output socket
        """

    def __iter__(self) -> Range:
        """
        Restart the range from `start` and return it.
        """

    def __next__(self) -> streampu._ext.core.Socket:
        """
        Execute the range once and return its output socket.
        """

    @property
    def throw_to_stop(self) -> bool:
        """
        If True, raise StopIteration at the end of the range (to stop a Python loop).
        """

    @throw_to_stop.setter
    def throw_to_stop(self, arg1: bool) -> None: ...
