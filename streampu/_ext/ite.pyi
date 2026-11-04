from __future__ import annotations

import typing

import streampu._ext.interfaces
import streampu._ext.sfl

__all__: list[str] = ["Iterator"]

class Iterator(streampu._ext.sfl.Stateful, streampu._ext.interfaces.Interface_reset):
    """
    Module that controls a loop: it outputs 0 for `limit` executions, then 1 to leave the loop, and starts again.
    """

    def __init__(self: typing.Iterator, limit: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Build an iterator.

        Args:
            limit (int): number of iterations before leaving the loop
        """

    @property
    def limit(self) -> int:
        """
        Number of iterations of the loop.
        """

    @limit.setter
    def limit(self, arg1: typing.SupportsInt | typing.SupportsIndex) -> None: ...
