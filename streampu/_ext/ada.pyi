from __future__ import annotations

import typing

import streampu._ext
import streampu._ext.interfaces
import streampu._ext.sfl

__all__: list[str] = ["Adaptor_m_to_n"]

class Adaptor_m_to_n(streampu._ext.sfl.Stateful, streampu._ext.interfaces.Interface_waiting):
    """
    Module inserted by a pipeline between two stages: it buffers the frames from m threads to n threads.
    """

    @property
    def dtype(self) -> streampu._ext.dtype:
        """
        Data type of the buffered sockets.
        """

    @property
    def n_bytes(self, arg1: typing.SupportsInt | typing.SupportsIndex) -> int:
        """
        Number of bytes of each buffered socket.
        """

    @property
    def n_elmts(self, arg1: typing.SupportsInt | typing.SupportsIndex) -> int:
        """
        Number of elements of each buffered socket.
        """

    @property
    def n_frames(self) -> int:
        """
        Number of frames per execution.
        """

    @n_frames.setter
    def n_frames(self, arg1: typing.SupportsInt | typing.SupportsIndex) -> None: ...
