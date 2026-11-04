from __future__ import annotations

import collections.abc
import typing

import streampu._ext.core
import streampu._ext.sfl

__all__: list[str] = ["Slicer"]

class Slicer(streampu._ext.sfl.Stateful):
    """
    Module behind the indexing of sockets (`x[i]`, `x[a:b]`, `x[[i, j]]`), for reading and writing.
    """

    @typing.overload
    def __init__(
        self, sck: streampu._ext.core.Socket, slice: collections.abc.Sequence[typing.SupportsInt | typing.SupportsIndex]
    ) -> None:
        """
        Build a slicer that reads or writes some elements of a socket (used by `x[...]`).

        Args:
            sck (Socket): the socket to slice
            slice (list[int]): indices of the elements
        """

    @typing.overload
    def __init__(self, sck: streampu._ext.core.Socket, idx: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Build a slicer that reads or writes one element of a socket (used by `x[i]`).

        Args:
            sck (Socket): the socket to slice
            idx (int): index of the element
        """
