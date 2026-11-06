from __future__ import annotations

import typing

import streampu._ext
import streampu._ext.core
import streampu._ext.sfl

__all__: list[str] = ["Julia", "Module_Julia", "Stateful_Julia", "Stateless_Julia"]

class Julia:
    """

    The Julia runtime used by the Julia modules (`Stateless_Julia`, `Stateful_Julia`).

    All the methods are static. Julia is started automatically when the first Julia
    module is created; call `Julia.init` before to choose the number of GC root slots.
    The code evaluated by `eval` and `eval_file` is evaluated in the `Main` module of
    Julia, where the codelets are looked up.

    """

    @staticmethod
    def eval(code: str) -> None:
        """
        Evaluate Julia code in the `Main` module (starts Julia if needed).

        Args:
            code (str): Julia code

        Raises:
            spu.exceptions.RuntimeError: if the evaluation raises a Julia exception
        """

    @staticmethod
    def eval_file(path: typing.Any) -> None:
        """
        Evaluate a Julia file in the `Main` module (starts Julia if needed).

        Args:
            path (str | os.PathLike): path of the `.jl` file

        Raises:
            spu.exceptions.RuntimeError: if the file cannot be read, or if its evaluation
                raises a Julia exception
        """

    @staticmethod
    def get_n_proxies() -> int:
        """
        Number of GC root slots per thread.
        """

    @staticmethod
    def init(n_proxies: typing.SupportsInt | typing.SupportsIndex = 256) -> None:
        """
        Start the Julia runtime, if it is not started yet (it is never started twice).

        Args:
            n_proxies (int): number of GC root slots per thread
        """

    @staticmethod
    def is_init() -> bool:
        """
        True if the Julia runtime has been started.
        """

class Module_Julia:
    """

    Base class of the Julia modules (`Stateless_Julia`, `Stateful_Julia`): the methods
    that set the Julia codelets and constants of their tasks. It cannot be built.

    A Julia codelet is a Julia function called with, in this order: the states of the
    module (`Stateful_Julia` only), the sockets of the task (in their creation order, as
    1D Julia vectors of `n_elmts * n_frames_per_wave` elements, without copy), the
    constants of the task, then `frame_id` and `n_frames_per_wave` (`UInt32`). It
    returns 0 on success.

    """

    def create_codelet(self, task: streampu._ext.core.Task, code: str = "", function_name: str = "") -> None:
        """
        Set the Julia codelet of a task.

        Args:
            task (Task): a task of this module
            code (str): Julia code that defines the function; empty if the function is
                already defined (see `Julia.eval`)
            function_name (str): name of the Julia function; by default, the name of the task
        """

    def create_codelet_file(self, task: streampu._ext.core.Task, path: typing.Any, function_name: str = "") -> None:
        """
        Set the Julia codelet of a task from a `.jl` file.

        Args:
            task (Task): a task of this module
            path (str | os.PathLike): file that defines the function
            function_name (str): name of the Julia function; by default, the name of the task
        """

    def create_constant(self, task: streampu._ext.core.Task, value: typing.Any, dtype: typing.Any = None) -> None:
        """
        Add a constant argument to the codelet of a task, after its sockets. Create the
        constants before the codelet.

        Args:
            task (Task): a task of this module
            value (bool | int | float | numpy scalar): value of the constant
            dtype (dtype | None): Julia type of the constant (`spu.int32` gives `Int32`...).
                Without it: `Bool` for a bool, `Int64` for an int, `Float64` for a float,
                the type of a NumPy scalar.
        """

    def eval(self) -> None:
        """
        Evaluate the Julia code of the module (states and codelets). It is done
        automatically: at the first immediate execution of a task, and by a `Sequence` or a
        `Pipeline` for each of its threads.

        Raises:
            spu.exceptions.RuntimeError: if the module has already been evaluated, or has no
                codelet
        """

    def is_eval(self) -> bool:
        """
        True if the Julia code of the module has been evaluated.
        """

    @property
    def jl_safe(self) -> bool:
        """
        If True (default), a Julia exception in a codelet is caught and raised as a Python
        spu.exceptions.RuntimeError with the Julia stack trace. False calls the codelets directly (faster).
        """

    @jl_safe.setter
    def jl_safe(self, arg1: bool) -> None: ...

class Stateful_Julia(streampu._ext.sfl.Stateful, Module_Julia):
    """

    Module with Julia states whose codelets are written in Julia.

    The codelet of a task is called with the states of the module (in their creation
    order), the sockets of the task, its constants, then `frame_id` and
    `n_frames_per_wave` (see `Module_Julia`). The tasks of a module share its states.
    When a `Sequence` or a `Pipeline` clones the module, each clone gets a `deepcopy`
    of a state, or the same object if the state is shared.

    """

    def __init__(self, jl_safe: bool = True) -> None:
        """
        Build an empty Julia module (starts Julia if needed): add states with
        `create_state` and tasks with `create_task`.

        Args:
            jl_safe (bool): raise the Julia exceptions of the codelets as Python exceptions
        """

    def create_socket_fwd(
        self,
        task: streampu._ext.core.Task,
        name: str,
        n_elmts: typing.SupportsInt | typing.SupportsIndex,
        dtype: streampu._ext.dtype,
    ) -> int:
        """
        Create a new forward socket to a task (read and written in place); returns its index.
        """

    def create_socket_in(
        self,
        task: streampu._ext.core.Task,
        name: str,
        n_elmts: typing.SupportsInt | typing.SupportsIndex,
        dtype: streampu._ext.dtype,
    ) -> int:
        """
        Create a new input socket to a task; returns its index.
        """

    def create_socket_out(
        self,
        task: streampu._ext.core.Task,
        name: str,
        n_elmts: typing.SupportsInt | typing.SupportsIndex,
        dtype: streampu._ext.dtype,
    ) -> int:
        """
        Create a new output socket to a task; returns its index.
        """

    def create_state(self, constructor: str, shared: bool = False, code: str = "") -> None:
        """
        Add a state to the module. Create the states before the codelets. The code that
        defines the type of the state is evaluated at once (in the `Main` module of Julia).

        Args:
            constructor (str): Julia expression that builds the state, e.g. `"Acc(0)"`
            shared (bool): False: each clone gets a `deepcopy` of the state; True: the clones
                share the same object
            code (str): Julia code that defines the type of the state
        """

    def create_state_file(self, constructor: str, path: typing.Any, shared: bool = False) -> None:
        """
        Add a state to the module, whose type is defined in a `.jl` file (evaluated at once,
        in the `Main` module of Julia).

        Args:
            constructor (str): Julia expression that builds the state
            path (str | os.PathLike): file that defines the type of the state
            shared (bool): False: each clone gets a `deepcopy` of the state; True: the clones
                share the same object
        """

    def create_task(self, name: str) -> streampu._ext.core.Task:
        """
        Create a new task.
        """

    def get_states(self) -> list[str]:
        """
        Representation of the states of the module, as `repr` gives it in Julia. The states
        exist once the module has been evaluated.

        Returns:
            list[str]: one string per state
        """

    @property
    def n_frames_per_wave(self) -> int:
        """
        Number of frames processed by each call of the codelets (by default, all the frames).
        """

    @n_frames_per_wave.setter
    def n_frames_per_wave(self, arg1: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Stateless_Julia(streampu._ext.core.Module, Module_Julia):
    """

    Module without state whose codelets are written in Julia.

    The codelet of a task is called with the sockets of the task, its constants, then
    `frame_id` and `n_frames_per_wave` (see `Module_Julia`).

    """

    def __init__(self, jl_safe: bool = True) -> None:
        """
        Build an empty Julia module (starts Julia if needed): add tasks with `create_task`.

        Args:
            jl_safe (bool): raise the Julia exceptions of the codelets as Python exceptions
        """

    def create_socket_fwd(
        self,
        task: streampu._ext.core.Task,
        name: str,
        n_elmts: typing.SupportsInt | typing.SupportsIndex,
        dtype: streampu._ext.dtype,
    ) -> int:
        """
        Create a new forward socket to a task (read and written in place); returns its index.
        """

    def create_socket_in(
        self,
        task: streampu._ext.core.Task,
        name: str,
        n_elmts: typing.SupportsInt | typing.SupportsIndex,
        dtype: streampu._ext.dtype,
    ) -> int:
        """
        Create a new input socket to a task; returns its index.
        """

    def create_socket_out(
        self,
        task: streampu._ext.core.Task,
        name: str,
        n_elmts: typing.SupportsInt | typing.SupportsIndex,
        dtype: streampu._ext.dtype,
    ) -> int:
        """
        Create a new output socket to a task; returns its index.
        """

    def create_task(self, name: str) -> streampu._ext.core.Task:
        """
        Create a new task.
        """

    @property
    def n_frames_per_wave(self) -> int:
        """
        Number of frames processed by each call of the codelets (by default, all the frames).
        """

    @n_frames_per_wave.setter
    def n_frames_per_wave(self, arg1: typing.SupportsInt | typing.SupportsIndex) -> None: ...
