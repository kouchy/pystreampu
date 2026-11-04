from __future__ import annotations

import collections.abc
import typing

import streampu._ext
import streampu._ext.core

__all__: list[str] = ["Stateless"]

class Stateless(streampu._ext.core.Module):
    """

    Class Stateless

    Stateless modules are modules that can be cloned automatically.
    """

    def __init__(self) -> None:
        """
        Build an empty module: add tasks with `create_task`.
        """

    def create_codelet(
        self,
        task: streampu._ext.core.Task,
        codelet: collections.abc.Callable[
            [streampu._ext.core.Module, streampu._ext.core.Task, typing.SupportsInt | typing.SupportsIndex], int
        ],
    ) -> None:
        """
        Set the function executed by a task (its codelet).

        The codelet is called as `codelet(module, task, frame_id)` and must return 0 on
        success. Inside it, the data of the sockets are reached with `task.<name>.numpy`;
        outputs must be written in place (`out[:] = ...`).

        Args:
            task (Task): a task created with `create_task`
            codelet (Callable): the function to execute
        """

    def create_socket_fwd(
        self,
        task: streampu._ext.core.Task,
        name: str,
        n_elmts: typing.SupportsInt | typing.SupportsIndex,
        dtype: streampu._ext.dtype,
    ) -> int:
        """
        Create a new forward socket to a task.
        """

    def create_socket_in(
        self,
        task: streampu._ext.core.Task,
        name: str,
        n_elmts: typing.SupportsInt | typing.SupportsIndex,
        dtype: streampu._ext.dtype,
    ) -> int:
        """
        Create a new input socket to a task.
        """

    def create_socket_out(
        self,
        task: streampu._ext.core.Task,
        name: str,
        n_elmts: typing.SupportsInt | typing.SupportsIndex,
        dtype: streampu._ext.dtype,
    ) -> int:
        """
        Create a new output socket to a task.
        """

    def create_task(self, name: str) -> streampu._ext.core.Task:
        """
        Create a new task.

        Args:
            name (str): name of the task

        Returns:
            Task: newly created task.
        """

    @property
    def n_frames_per_wave(self) -> int:
        """
        Number of frames processed by each call of the codelets (by default, all the frames).
        """

    @n_frames_per_wave.setter
    def n_frames_per_wave(self, arg1: typing.SupportsInt | typing.SupportsIndex) -> None: ...
