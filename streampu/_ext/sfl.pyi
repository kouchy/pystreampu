from __future__ import annotations

import typing

import streampu._ext
import streampu._ext.core

__all__: list[str] = ["Stateful", "Stateful_core"]

class Stateful(streampu._ext.core.Module):
    """
    Stateful modules are modules that cannot be cloned due to internal state.
    """

class Stateful_core(Stateful):
    """
    Stateful_core is the class that will contain the 'core' of python stateful modules. It inherits from Stateful, and implements the clone method by cloning the python state of the Module's body as well as its own state.
    """

    @typing.overload
    def __init__(self) -> None:
        """
        Build an empty module: add tasks with `create_task`, and implement `clone`.
        """

    @typing.overload
    def __init__(self, arg0: Stateful_core) -> None:
        """
        Build a copy of another module.
        """

    def clone(self) -> typing.Any:
        """
        Return a copy of the module, used to duplicate it on several threads.

        Override it in Python subclasses: create the new instance without calling
        `__init__` (StreamPU copies the tasks, sockets and codelets) and copy the Python
        state.

        Returns:
            out (Stateful_core): the copy
        """

    def create_codelet(self, task: streampu._ext.core.Task, codelet: typing.Any) -> None:
        """
        Set the function executed by a task (its codelet).

        The codelet is called as `codelet(module, task, frame_id)` and must return 0 on
        success. Inside it, the data of the sockets are reached with `task.<name>.numpy`;
        outputs must be written in place (`out[:] = ...`).
        Alternatively, `codelet` may be a Numba `@njit` function taking the task's data
        sockets as 2D NumPy views (`wave`), or a `streampu.numba_codelet(...)` descriptor,
        which is compiled into a GIL-free `@cfunc` trampoline called directly from C++.

        Args:
            task (Task): a task created with `create_task`
            codelet (Callable): the function to execute
        """

    def create_codelet_cfunc(
        self,
        task: streampu._ext.core.Task,
        cfunc_addr: typing.SupportsInt | typing.SupportsIndex,
        keep_alive: typing.Any = None,
        extra_args_packer: typing.Any = None,
    ) -> None: ...
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
