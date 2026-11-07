from __future__ import annotations

import collections.abc
import typing

import streampu._ext.interfaces
import streampu._ext.terminal
from streampu._typing import SocketLike

__all__: list[str] = ["Module", "Socket", "Task"]

class Module(streampu._ext.interfaces.Interface_clone, streampu._ext.interfaces.Interface_get_set_n_frames):
    """

    Base class of the StreamPU modules: an object that holds tasks.

    The tasks of a module are reached by name, `module["task"]` or `module.task`,
    and their sockets with `module["task::socket"]`. A module processes `n_frames`
    frames per execution of its tasks. `spu.help(module)` prints its tasks and their
    sockets.

    """

    def __call__(
        self, *args: tuple[SocketLike], raw_data: bool = False, **kwargs: dict[str, SocketLike]
    ) -> Socket | tuple[Socket] | None: ...
    def __getattr__(self, attr: str) -> Task | Socket:
        """
        Overload __getattr__ of streampu._ext.core.Module.

        module[task_name] will return the task named `task_name` of the module.

        module[task_name::socket_name] will return the socket named `socket_name`
        of the task `task_name` of the module.

        Args:
            self (Module): A Module
            attr (str): attribute name

        Returns:
            out (Task): if attr is formatted as 'task_name'
            out (Socket): if attr is formatted as 'task_name::socket_name'


        """

    def __getitem__(self, key: str) -> typing.Any:
        """
        Return the task or the socket corresponding to the key.

        Args:
            key (str): key representing a task or a socket.
              If key is of the form "task_name" then the task with the name
              "task_name" is returned.
              If key is of the form "task_name::socket_name" then the socket
              with the name "socket_name" of the task named "task_name"
              is returned.

        Returns:
            Task | Socket : task or socket described by the key.
        """

    def __setitem__(self, attr: str, tsk_sck: Task | Socket) -> None:
        """
        Bind self[attr] to the socket sck.

        Args:
            self (Module): A Module
            attr (str): attribute name (should name a task or a socket)
            tsk_sck (Task|Socket): socket to bind self[attr].

        """

    @property
    def clonable(self) -> bool:
        """
        True if the module can be duplicated on several threads.
        """

    @property
    def name(self) -> str:
        """
        Name of the module (can be changed, e.g. to tell modules apart in the statistics).
        """

    @name.setter
    def name(self, arg1: str) -> None: ...
    @property
    def stateful(self) -> bool:
        """
        True if the module keeps a state between executions.
        """

    @property
    def stateless(self) -> bool:
        """
        True if the module does not keep any state (it can then be cloned automatically).
        """

    @property
    def tasks(self) -> list[Task]:
        """
        Tasks of the module.
        """

class Socket(streampu._ext.interfaces.Interface_reset):
    """

    Data exchanged between tasks.

    A socket belongs to a task and has a name, a data type (`dtype`), a number of
    elements and a direction (input, output or forward). Its data is a 2D array with
    one row per frame, accessible without copy through `numpy`.

    Python operators (`+`, `<`, `&`, `x[::2]`...) can be used on sockets: each one
    creates a module, binds it to its operands and executes it.

    """

    class directions:
        """
        Enumeration of socket directions

        Members:

          IN : Input socket

          OUT : Output socket

          FWD : Forward socket
        """

        FWD: typing.ClassVar[Socket.directions]  # value = <directions.FWD: 2>
        IN: typing.ClassVar[Socket.directions]  # value = <directions.IN: 0>
        OUT: typing.ClassVar[Socket.directions]  # value = <directions.OUT: 1>
        __members__: typing.ClassVar[
            dict[str, Socket.directions]
        ]  # value = {'IN': <directions.IN: 0>, 'OUT': <directions.OUT: 1>, 'FWD': <directions.FWD: 2>}
        def __eq__(self, other: typing.Any) -> bool: ...
        def __getstate__(self) -> int: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None: ...
        def __int__(self) -> int: ...
        def __ne__(self, other: typing.Any) -> bool: ...
        def __repr__(self) -> str: ...
        def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None: ...
        def __str__(self) -> str: ...
        @property
        def name(self) -> str: ...
        @property
        def value(self) -> int: ...

    def __abs__(self) -> Socket:
        """
        Compute abs(self).

        Args:
            self (Socket): input data

        Returns:
            out (Socket):  abs(self)

        """

    def __add__(self, value: SocketLike) -> Socket:
        """
        Compute self + value.

        Args:
            self (Socket): input data
            value (SocketLike): a value

        Returns:
            out (Socket):  self + value

        """

    def __and__(self, value: SocketLike) -> Socket:
        """
        Compute self & value.

        Args:
            self (Socket): input data
            value (SocketLike): a value

        Returns:
            out (Socket):  self & value

        """

    def __bool__(self) -> bool: ...
    def __buffer__(self, flags):
        """
        Return a buffer object that exposes the underlying memory of the object.
        """

    def __eq__(self, value: SocketLike) -> Socket:
        """
        Compute value == self.

        Args:
            self (Socket): input data
            value (SocketLike): a value

        Returns:
            out (Socket):  value == self

        """

    def __ge__(self, value: SocketLike) -> Socket:
        """
        Compute self >= value.

        Args:
            self (Socket): input data
            value (SocketLike): a value

        Returns:
            out (Socket):  self >= value

        """

    def __getitem__(self, key: slice | int | list) -> Socket:
        """
        Read data at place key inside a socket.

        Args:
            self (Socket): input data
            key (int|slice|list): place to read (as for a 1D NumPy array)

        Returns:
            out (Socket): self[key]

        Raises:
            IndexError: if an index is out of the frame (this also ends `iter(socket)`)
            TypeError: if `key` is not an index, a slice or a list of indices

        """

    def __gt__(self, value: SocketLike) -> Socket:
        """
        Compute self > value.

        Args:
            self (Socket): input data
            value (SocketLike): a value

        Returns:
            out (Socket):  self > value

        """

    def __iadd__(self, value: SocketLike) -> Socket:
        """
        Compute self += value.

        Args:
            self (Socket): input data
            value (SocketLike): a value

        Returns:
            out (Socket):  updated self (in-place operation)

        """

    def __iand__(self, value: SocketLike) -> Socket:
        """
        Compute self &= value.

        Args:
            self (Socket): input data
            value (SocketLike): a value

        Returns:
            out (Socket):  updated self (in-place operation)

        """

    def __imul__(self, value: SocketLike) -> Socket:
        """
        Compute self = self * value with in-place operation.

        Args:
            self (Socket): input data
            value (SocketLike): a value

        Returns:
            out (Socket):  updated self (in-place operation)

        """

    def __invert__(self) -> Socket:
        """
        Compute ~self.

        Args:
            self (Socket): input data

        Returns:
            out (Socket):  ~self

        """

    def __ior__(self, value: SocketLike) -> Socket:
        """
        Compute self = self | value with in-place operation.

        Args:
            self (Socket): input data
            value (SocketLike): a value

        Returns:
            out (Socket):  updated self (in-place operation)

        """

    def __isub__(self, value: SocketLike) -> Socket:
        """
        Compute self -= value.

        Args:
            self (Socket): input data
            value (SocketLike): a value

        Returns:
            out (Socket):  updated self (in-place operation)

        """

    def __iter__(self):
        """
        Iterate over the elements of a frame: `self[0]`, `self[1]`, ..., `self[len(self) - 1]`.

        Args:
            self (Socket): input data

        Yields:
            out (Socket): one socket per element

        """

    def __itruediv__(self, value: SocketLike) -> Socket:
        """
        Compute self /= value.

        Args:
            self (Socket): input data
            value (SocketLike): a value

        Returns:
            out (Socket):  updated self (in-place operation)

        """

    def __ixor__(self, value: SocketLike) -> Socket:
        """
        Compute self ^= value.

        Args:
            self (Socket): input data
            value (SocketLike): a value

        Returns:
            out (Socket):  updated self (in-place operation)

        """

    def __le__(self, value: SocketLike) -> Socket:
        """
        Compute self <= value.

        Args:
            self (Socket): input data
            value (SocketLike): a value

        Returns:
            out (Socket):  self <= value

        """

    def __len__(self) -> int:
        """
        Return the size of one frame.

        Args:
            self (Socket): A socket

        Returns:
            out (int): size of one frame

        """

    def __lt__(self, value: SocketLike) -> Socket:
        """
        Compute self < value.

        Args:
            self (Socket): input data
            value (SocketLike): a value

        Returns:
            out (Socket):  self < value

        """

    def __mul__(self, value: SocketLike) -> Socket:
        """
        Compute self * value.

        Args:
            self (Socket): input data
            value (SocketLike): a value

        Returns:
            out (Socket):  self * value

        """

    def __ne__(self, value: SocketLike) -> Socket:
        """
        Compute self != value.

        Args:
            self (Socket): input data
            value (SocketLike): a value

        Returns:
            out (Socket):  self != value

        """

    def __neg__(self) -> Socket:
        """
        Compute -self.

        Args:
            self (Socket): input data

        Returns:
            out (Socket):  -self

        """

    def __or__(self, value: SocketLike) -> Socket:
        """
        Compute self | value.

        Args:
            self (Socket): input data
            value (SocketLike): a value

        Returns:
            out (Socket):  self | value

        """

    def __radd__(self, value: SocketLike) -> Socket:
        """
        Compute value + self.

        Args:
            self (Socket): input data
            value (SocketLike): a value

        Returns:
            out (Socket):  value + self

        """

    def __rand__(self, value: SocketLike) -> Socket:
        """
        Compute value & self.

        Args:
            self (Socket): input data
            value (SocketLike): a value

        Returns:
            out (Socket):  value & value

        """

    def __release_buffer__(self, buffer):
        """
        Release the buffer object that exposes the underlying memory of the object.
        """

    def __repr__(self) -> str:
        """
        Return a socket representation.

        Args:
            self (Socket): A socket

        Returns:
            out (str): a str representing the socket

        """

    def __req__(self, value: SocketLike) -> Socket:
        """
        Compute self == value.

        Args:
            self (Socket): input data
            value (SocketLike): a value

        Returns:
            out (Socket):  self == value

        """

    def __rge__(self, value: SocketLike) -> Socket:
        """
        Compute value >= self.

        Args:
            self (Socket): input data
            value (SocketLike): a value

        Returns:
            out (Socket):  value >= self

        """

    def __rgt__(self, value: SocketLike) -> Socket:
        """
        Compute value > self.

        Args:
            self (Socket): input data
            value (SocketLike): a value

        Returns:
            out (Socket):  value > self

        """

    def __rle__(self, value: SocketLike) -> Socket:
        """
        Compute value <= self.

        Args:
            self (Socket): input data
            value (SocketLike): a value

        Returns:
            out (Socket):  value <= self

        """

    def __rlt__(self, value: SocketLike) -> Socket:
        """
        Compute value < self.

        Args:
            self (Socket): input data
            value (SocketLike): a value

        Returns:
            out (Socket):  value < self

        """

    def __rmul__(self, value: SocketLike) -> Socket:
        """
        Compute value * self.

        Args:
            self (Socket): input data
            value (SocketLike): a value

        Returns:
            out (Socket):  value * self

        """

    def __rneq__(self, value: SocketLike) -> Socket:
        """
        Compute value != self.

        Args:
            self (Socket): input data
            value (SocketLike): a value

        Returns:
            out (Socket):  value != self

        """

    def __ror__(self, value: SocketLike) -> Socket:
        """
        Compute value | self.

        Args:
            self (Socket): input data
            value (SocketLike): a value

        Returns:
            out (Socket):  value | self

        """

    def __rsub__(self, value: SocketLike) -> Socket:
        """
        Compute value - self.

        Args:
            self (Socket): input data
            value (SocketLike): a value

        Returns:
            out (Socket):  value - self

        """

    def __rtruediv__(self, value: SocketLike) -> Socket:
        """
        Compute value / self.

        Args:
            self (Socket): input data
            value (SocketLike): a value

        Returns:
            out (Socket):  value / self

        """

    def __rxor__(self, value: SocketLike) -> Socket:
        """
        Compute value ^ self.

        Args:
            self (Socket): input data
            value (SocketLike): a value

        Returns:
            out (Socket):  value ^ self

        """

    def __setitem__(self, key: int | slice | list, data: SocketLike) -> Socket:
        """
        Write data at place key inside a socket.

        Args:
            self (Socket): input data
            key (int|slice|list): place to write the new data (as for a 1D NumPy array)
            data (SocketLike): new data

        Raises:
            IndexError: if an index is out of the frame
            TypeError: if `key` is not an index, a slice or a list of indices

        """

    def __str__(self) -> str:
        """
        Return the socket as a str.

        Args:
            self (Socket): A socket

        Returns:
            out (str): str representing the socket's data

        """

    def __sub__(self, value: SocketLike) -> Socket:
        """
        Compute self - value.

        Args:
            self (Socket): input data
            value (SocketLike): a value

        Returns:
            out (Socket):  self - value

        """

    def __truediv__(self, value: SocketLike) -> Socket:
        """
        Compute self / value.

        Args:
            self (Socket): input data
            value (SocketLike): a value

        Returns:
            out (Socket):  self / value

        """

    def __xor__(self, value: SocketLike) -> Socket:
        """
        Compute self ^ value.

        Args:
            self (Socket): input data
            value (SocketLike): a value

        Returns:
            out (Socket):  self ^ value

        """

    @typing.overload
    def _bind(self, s_out: Socket, priority: typing.SupportsInt | typing.SupportsIndex = -1) -> None:
        """
        Binds the socket to socket 's_out' with priority 'priority'.
        """

    @typing.overload
    def _bind(self, array: numpy.ndarray) -> None:
        """
        Binds the socket to the numpy array 'array' data.
        """

    def astype(self, output_dtype: numpy.dtype[typing.Any]) -> Socket:
        """
        Cast socket to dtype.

        Args:
            self (Socket): input data
            output_dtype (dtype): output data type

        Returns:
            out (Socket):  output_dtype(self)

        """

    def bind(self, s_out: SocketLike, priority: int = -1, raw_data: bool = False) -> None:
        """
        Binds self to s_out.

        If s_out is not a `Socket`, s_out is converted to a `Socket` first.

        Args:
            self (Socket): A socket
            s_out (SocketLike): Socket to bind
            priority (int): Priority of the bind.
            raw_data (bool): if True converts data to a Socket

        """

    def get_bound_socket(self) -> Socket:
        """
        Return the socket this socket is bound to (for input sockets only).
        """

    def get_bound_sockets(self) -> list[Socket]:
        """
        Return the sockets bound to this socket (for output sockets only).
        """

    def has_data(self) -> bool:
        """
        Return True if the socket has data allocated.
        """

    def unbind(self, s_out: Socket) -> int:
        """
        Unbind the socket from the socket `s_out`.

        Args:
            s_out (Socket): the output or forward socket this socket is bound to
        """

    @property
    def dataaddr(self) -> str:
        """
        Return the socket data address as str.
        """

    @property
    def direction(self) -> Socket.directions:
        """
        Direction of the socket (`Socket.directions.IN`, `OUT` or `FWD`).
        """

    @property
    def dtype(self) -> ...:
        """
        Data type.
        """

    @property
    def n_elmts(self) -> int:
        """
        Total number of elements, for all the frames.
        """

    @property
    def name(self) -> str:
        """
        Name of the socket in its task.
        """

    @property
    def numpy(self) -> numpy.ndarray:
        """
        NumPy view of the data of the socket (no copy), with one row per frame.
        """

    @property
    def task(self) -> ...:
        """
        Task owning the socket.
        """

    @property
    def wave(self) -> numpy.ndarray:
        """
        NumPy view (without copy) of the frames of the current wave (`n_frames_per_wave` rows).
        """

class Task:
    """

    A processing step of a module: the code executed by a node of the data-flow graph.

    A task reads its input sockets, writes its output sockets and modifies its forward
    sockets. Its sockets are reached by name: `task["name"]` or `task.name`.

    Calling a task, `task(*sockets)`, binds the given sockets to its input and forward
    sockets (in the order of `task.sockets`), executes it once and returns its output
    sockets (without `status`).

    """

    class Status:
        """
        Enumeration of tasks return code.

        Members:

          SUCCESS : Success code

          FAILURE : Failure code

          FAILURE_STOP : Failure stop code

          UNKNOWN : Unknown code
        """

        FAILURE: typing.ClassVar[Task.Status]  # value = <Status.FAILURE: 1>
        FAILURE_STOP: typing.ClassVar[Task.Status]  # value = <Status.FAILURE_STOP: -1>
        SUCCESS: typing.ClassVar[Task.Status]  # value = <Status.SUCCESS: 0>
        UNKNOWN: typing.ClassVar[Task.Status]  # value = <Status.UNKNOWN: -2>
        __members__: typing.ClassVar[
            dict[str, Task.Status]
        ]  # value = {'SUCCESS': <Status.SUCCESS: 0>, 'FAILURE': <Status.FAILURE: 1>, 'FAILURE_STOP': <Status.FAILURE_STOP: -1>, 'UNKNOWN': <Status.UNKNOWN: -2>}
        def __eq__(self, other: typing.Any) -> bool: ...
        def __getstate__(self) -> int: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None: ...
        def __int__(self) -> int: ...
        def __ne__(self, other: typing.Any) -> bool: ...
        def __repr__(self) -> str: ...
        def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None: ...
        def __str__(self) -> str: ...
        @property
        def name(self) -> str: ...
        @property
        def value(self) -> int: ...

    call_auto_exec: typing.ClassVar[bool] = True
    def __call__(
        self, *args: tuple[SocketLike], raw_data=False, auto_exec=True, **kwargs: dict[str, SocketLike]
    ) -> Socket | tuple[Socket] | None: ...
    def __getattr__(self, attr: str) -> tuple | Socket | None:
        """
        Overload __getattr__ of streampu._ext.core.Task.

        task[socket_name] will return the socket named `socket_name`
        of the task.

        Args:
            self (Task): A Task
            attr (str): socket name

        Returns:
            out (Socket): the task socket named 'sck_name'

        """

    def __getitem__(self, arg0: str) -> typing.Any: ...
    def __setattr__(self, attr: str, value: typing.Any) -> tuple | Socket | None:
        """
        Overload __setattr__ of streampu._ext.core.Task.

        Args:
            self (Task): A Task
            attr (str): attribute name
            value (Any): Value to set

        """

    def abort_processing(self) -> None:
        """
        Raise a `ProcessingAborted` exception, to stop the processing from a codelet.

        Raises:
            ProcessingAborted: always
        """

    @typing.overload
    def bind(self, s_out: Socket, priority: typing.SupportsInt | typing.SupportsIndex = -1) -> None:
        """
        Bind the task to a socket, to force an order of execution without exchanging data.

        The task will be executed after the task that owns `s_out`.

        Args:
            s_out (Socket): an output or forward socket of another task
            priority (int): priority of the binding, -1 for the default one
        """

    @typing.overload
    def bind(self, t_out: Task, priority: typing.SupportsInt | typing.SupportsIndex = -1) -> None:
        """
        Bind the task to another task, to force an order of execution without exchanging data.

        Args:
            t_out (Task): the task to execute before this one
            priority (int): priority of the binding, -1 for the default one
        """

    def can_exec(self) -> bool:
        """
        Tell whether the task can be executed.

        Returns:
            out (bool): True if every socket of the task has data (input sockets bound,
                output sockets allocated)
        """

    def cancel_waiting(self) -> None:
        """
        Raise a `WaitingCanceled` exception, to stop a task that waits for data.

        Raises:
            WaitingCanceled: always
        """

    def exec(self, frame_id: typing.SupportsInt | typing.SupportsIndex = -1, managed_memory: bool = True) -> None:
        """
        Execute the task once.

        Args:
            frame_id (int): index of the frame to process, or -1 to process all the frames
                of the module (`n_frames`)
            managed_memory (bool): let StreamPU manage the memory of the sockets

        Raises:
            RuntimeError: if some sockets have no data (see `can_exec`)
        """

    def interrupt_processing(self) -> None:
        """
        Raise a `ProcessingAborted` exception (same as `abort_processing`).

        Raises:
            ProcessingAborted: always
        """

    def is_bound(self) -> bool:
        """
        Tell whether the task is bound to another task or socket with `bind`.

        Returns:
            out (bool): True if the task has been bound with `Task.bind`
        """

    def reset(self) -> None:
        """
        Reset the statistics of the task (`n_calls`, durations).
        """

    def set_debug_frame_max(self, limit: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Set the maximum number of frames printed in debug mode.

        Args:
            limit (int): maximum number of frames
        """

    def set_debug_hex(self, debug_hex: bool) -> None:
        """
        Print the data in hexadecimal in debug mode.

        Args:
            debug_hex (bool): True to print in hexadecimal
        """

    def set_debug_limit(self, limit: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Set the maximum number of elements printed per socket in debug mode.

        Args:
            limit (int): maximum number of elements
        """

    def set_debug_precision(self, prec: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Set the number of decimals of the floating-point values printed in debug mode.

        Args:
            prec (int): number of decimals
        """

    @property
    def avg_duration(self) -> float:
        """
        Average duration of an execution, in seconds (0 if `stats` is False).
        """

    @property
    def debug(self) -> bool:
        """
        If True, print the content of the sockets at each execution.
        """

    @debug.setter
    def debug(self, arg1: bool) -> None: ...
    @property
    def fast(self) -> bool:
        """
        If True, skip some checks at each execution, for speed.
        """

    @fast.setter
    def fast(self, arg1: bool) -> None: ...
    @property
    def forwards(self) -> list[Socket]:
        """
        Forward sockets of the task.
        """

    @property
    def inputs(self) -> list[Socket]:
        """
        Input sockets of the task.
        """

    @property
    def max_duration(self) -> float:
        """
        Maximum duration of an execution, in seconds (0 if `stats` is False).
        """

    @property
    def min_duration(self) -> float:
        """
        Minimum duration of an execution, in seconds (0 if `stats` is False).
        """

    @property
    def module(self) -> ...:
        """
        Module that owns the task.
        """

    @property
    def n_calls(self) -> int:
        """
        Number of executions since the last `reset`.
        """

    @property
    def name(self) -> str:
        """
        Name of the task.
        """

    @property
    def outputs(self) -> list[Socket]:
        """
        Output sockets of the task, including `status`.
        """

    @property
    def replicable(self) -> bool:
        """
        If True, the task can be duplicated on several threads (its module must be clonable).
        """

    @replicable.setter
    def replicable(self, arg1: bool) -> None: ...
    @property
    def sockets(self) -> list[Socket]:
        """
        All the sockets of the task, in their order of creation.
        """

    @property
    def stats(self) -> bool:
        """
        If True, measure the duration of each execution (see `avg_duration`...).
        """

    @stats.setter
    def stats(self, arg1: bool) -> None: ...
    @property
    def total_duration(self) -> float:
        """
        Total time spent in the task, in seconds (0 if `stats` is False).
        """

class _Pipeline(streampu._ext.interfaces.Interface_get_set_n_frames):
    """

    C++ pipeline of StreamPU: a graph split into stages that run concurrently.

    Each stage is a sequence with its own number of threads; consecutive stages exchange
    frames through buffers (adaptor modules). Use `streampu.Pipeline`.

    """

    def __getitem__(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> _Sequence: ...
    def __init__(
        self,
        firsts: collections.abc.Sequence[Task],
        lasts: collections.abc.Sequence[Task],
        sep_stages: collections.abc.Sequence[
            tuple[collections.abc.Sequence[Task], collections.abc.Sequence[Task], collections.abc.Sequence[Task]]
        ] = [],
        n_threads: collections.abc.Sequence[typing.SupportsInt | typing.SupportsIndex] = [],
        synchro_buffer_sizes: collections.abc.Sequence[typing.SupportsInt | typing.SupportsIndex] = [],
        synchro_active_waiting: collections.abc.Sequence[bool] = [],
        thread_pinning: collections.abc.Sequence[bool] = [],
        puids: collections.abc.Sequence[collections.abc.Sequence[typing.SupportsInt | typing.SupportsIndex]] = [],
    ) -> None:
        """
        Build a pipeline.

        Args:
            firsts (list[Task]): first tasks of the graph
            lasts (list[Task]): last tasks of the graph
            sep_stages (list): for each stage, `[first tasks, last tasks, excluded tasks]`
            n_threads (list[int]): number of threads of each stage
            synchro_buffer_sizes (list[int]): size of the buffer between each pair of
                consecutive stages
            synchro_active_waiting (list[bool]): active waiting between each pair of
                consecutive stages (faster, but uses a core)
            thread_pinning (list[bool]): pin the threads of each stage
            puids (list[list[int]]): processing units of the threads of each stage
        """

    def bind_adaptors(self) -> None:
        """
        Bind the adaptors that connect the stages (done when the pipeline is built).
        """

    def exec(self) -> None:
        """
        Execute the pipeline until a module is done (e.g. a source at the end of its file) or SIGINT is received.
        """

    def export_dot(self, file_name: str) -> None:
        """
        Export the graph of the pipeline in the Graphviz DOT format.

        Args:
            file_name (str): path of the DOT file to write
        """

    def get_modules_per_threads(self) -> list[list[Module]]:
        """
        Return the modules of each thread, for all the stages.
        """

    def get_modules_per_types(self) -> list[list[Module]]:
        """
        Return the modules grouped by type, for all the stages.
        """

    def get_original_modules(self) -> list[list[Module]]:
        """
        Return the modules created by the user, one list per stage (without the clones and adaptors).
        """

    def get_tasks_per_threads(self) -> list[list[Task]]:
        """
        Return the tasks of each thread, for all the stages.
        """

    def get_tasks_per_types(self) -> list[list[Task]]:
        """
        Return the tasks grouped by type, for all the stages.
        """

    def is_bound_adaptors(self) -> bool:
        """
        Return True if the adaptors are bound.
        """

    def show_stats(self, stream: ... = ...) -> None:
        """
        Print the statistics of the tasks, one table per stage (enable them first with
        `task.stats = True`).

        Args:
            stream (file): stream where the statistics are written
        """

    def unbind_adaptors(self) -> None:
        """
        Unbind the adaptors and restore the original bindings of the tasks.
        """

    @property
    def auto_stop(self) -> bool:
        """
        If True, the pipeline stops by itself when a module is done.
        """

    @auto_stop.setter
    def auto_stop(self, arg1: bool) -> None: ...
    @property
    def first_tasks(self) -> list[list[Task]]:
        """
        First tasks of the pipeline.
        """

    @property
    def last_tasks(self) -> list[list[Task]]:
        """
        Last tasks of the pipeline.
        """

    @property
    def stages(self) -> list[_Sequence]:
        """
        Sequences of the stages of the pipeline.
        """

class _Sequence(
    streampu._ext.interfaces.Interface_clone,
    streampu._ext.interfaces.Interface_get_set_n_frames,
    streampu._ext.interfaces.Interface_is_done,
):
    """

    C++ sequence of StreamPU: a graph of bound tasks, executed on one or several threads.

    Use `streampu.Sequence`, which can also be built from sockets.

    """

    @typing.overload
    def __init__(
        self,
        first: Task,
        n_threads: typing.SupportsInt | typing.SupportsIndex = 1,
        thread_pinning: bool = False,
        sequence_pinning_policy: str = "",
        tasks_inplace: bool = True,
    ) -> None:
        """
        Build a sequence from its first task(s), and possibly its last tasks and the tasks
        to exclude.

        Args:
            n_threads (int): number of threads; the modules are cloned for each thread
            thread_pinning (bool): pin each thread to a processing unit
            sequence_pinning_policy (str): pinning policy, see the StreamPU documentation
            tasks_inplace (bool): execute the tasks in place when possible
        """

    @typing.overload
    def __init__(
        self,
        first: Task,
        last: Task,
        n_threads: typing.SupportsInt | typing.SupportsIndex = 1,
        thread_pinning: bool = False,
        sequence_pinning_policy: str = "",
        tasks_inplace: bool = True,
    ) -> None:
        """
        Build a sequence from its first task(s), and possibly its last tasks and the tasks
        to exclude.

        Args:
            n_threads (int): number of threads; the modules are cloned for each thread
            thread_pinning (bool): pin each thread to a processing unit
            sequence_pinning_policy (str): pinning policy, see the StreamPU documentation
            tasks_inplace (bool): execute the tasks in place when possible
        """

    @typing.overload
    def __init__(
        self,
        firsts: collections.abc.Sequence[Task],
        n_threads: typing.SupportsInt | typing.SupportsIndex = 1,
        thread_pinning: bool = False,
        sequence_pinning_policy: str = "",
        tasks_inplace: bool = True,
    ) -> None:
        """
        Build a sequence from its first task(s), and possibly its last tasks and the tasks
        to exclude.

        Args:
            n_threads (int): number of threads; the modules are cloned for each thread
            thread_pinning (bool): pin each thread to a processing unit
            sequence_pinning_policy (str): pinning policy, see the StreamPU documentation
            tasks_inplace (bool): execute the tasks in place when possible
        """

    @typing.overload
    def __init__(
        self,
        firsts: collections.abc.Sequence[Task],
        lasts: collections.abc.Sequence[Task],
        exclusions: collections.abc.Sequence[Task],
        n_threads: typing.SupportsInt | typing.SupportsIndex = 1,
        thread_pinning: bool = False,
        sequence_pinning_policy: str = "",
        tasks_inplace: bool = True,
    ) -> None:
        """
        Build a sequence from its first task(s), and possibly its last tasks and the tasks
        to exclude.

        Args:
            n_threads (int): number of threads; the modules are cloned for each thread
            thread_pinning (bool): pin each thread to a processing unit
            sequence_pinning_policy (str): pinning policy, see the StreamPU documentation
            tasks_inplace (bool): execute the tasks in place when possible
        """

    @typing.overload
    def exec(self) -> None:
        """
        Execute the sequence until a module of the sequence is done (e.g. a source at the
        end of its file) or SIGINT (Ctrl+C) is received.
        """

    @typing.overload
    def exec(
        self, terminal: streampu._ext.terminal.Terminal_dump, stream: ... = ..., force_report: bool = False
    ) -> None:
        """
        Execute the sequence until a module is done or SIGINT is received, and print a
        report of the probes with `terminal` after each execution.

        Args:
            terminal (Terminal_dump): terminal displaying the reporters
            stream (file): stream where the report is written
            force_report (bool): report after every execution, even when the last task
                did not run
        """

    @typing.overload
    def exec_n_times(self, n_exec: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Execute the sequence `n_exec` times in total, shared between the threads.

        Args:
            n_exec (int): number of executions
        """

    @typing.overload
    def exec_n_times(
        self,
        n_exec: typing.SupportsInt | typing.SupportsIndex,
        terminal: streampu._ext.terminal.Terminal_dump,
        stream: ... = ...,
        force_report: bool = False,
    ) -> None:
        """
        Execute the sequence `n_exec` times and print a report of the probes with
        `terminal` after each execution.

        Args:
            n_exec (int): number of executions
            terminal (Terminal_dump): terminal displaying the reporters
            stream (file): stream where the report is written
            force_report (bool): report after every execution, even when the last task
                did not run
        """

    def exec_seq(
        self,
        tid: typing.SupportsInt | typing.SupportsIndex = 0,
        frame_id: typing.SupportsInt | typing.SupportsIndex = -1,
    ) -> None:
        """
        Execute the sequence of one thread once, sequentially.

        Args:
            tid (int): index of the thread whose sequence is executed
            frame_id (int): index of the frame to process, or -1 for all the frames
        """

    def exec_step(
        self,
        tid: typing.SupportsInt | typing.SupportsIndex = 0,
        frame_id: typing.SupportsInt | typing.SupportsIndex = -1,
    ) -> Task:
        """
        Execute the next task of the sequence of one thread, for step-by-step debugging.

        Args:
            tid (int): index of the thread
            frame_id (int): index of the frame to process, or -1 for all the frames

        Returns:
            out (Task | None): the executed task, or None when a full execution of the
                sequence is over
        """

    def export_dot(self, file_name: str) -> None:
        """
        Export the graph of the sequence in the Graphviz DOT format.

        Args:
            file_name (str): path of the DOT file to write
        """

    def get_cloned_modules(self, module_ref):
        """
        Return the copies of a module used by each thread of the sequence.

        Args:
            module_ref (Module): a module of the sequence, as created by the user
                (i.e. the module used by the thread 0)

        Returns:
            out (list): the module used by each thread, the first one being `module_ref`

        Raises:
            RuntimeError: if `module_ref` is not part of the sequence

        """

    def get_modules(self, module_class, set_modules=True):
        """
        Return the modules of a given class, for all the threads of the sequence.

        Args:
            module_class (type): a module class, e.g. `streampu.Module` for all the modules
            set_modules (bool): if True, also explore the sequences held by `Set` modules

        Returns:
            out (list): the modules of the sequence that are instances of `module_class`

        """

    def get_modules_per_threads(self) -> list[list[Module]]:
        """
        Return the modules of each thread: a list (one per thread) of lists of modules.
        """

    def get_modules_per_types(self) -> list[list[Module]]:
        """
        Return the modules grouped by type: a list (one per original module) of the modules of all the threads.
        """

    def get_tasks_per_threads(self) -> list[list[Task]]:
        """
        Return the tasks of each thread: a list (one per thread) of lists of tasks.
        """

    def get_tasks_per_types(self) -> list[list[Task]]:
        """
        Return the tasks grouped by type: a list (one per original task) of the tasks of all the threads.
        """

    def show_stats(self, ordered: bool = False, display_thr: bool = True, stream: ... = ...) -> None:
        """
        Print the statistics of the tasks (enable them first with `task.stats = True`).

        Args:
            ordered (bool): sort the tasks by decreasing duration
            display_thr (bool): display the throughput columns
            stream (file): stream where the statistics are written
        """

    @property
    def first_tasks(self) -> list[list[Task]]:
        """
        First tasks of the sequence, one list per thread.
        """

    @property
    def last_tasks(self) -> list[list[Task]]:
        """
        Last tasks of the sequence, one list per thread.
        """

    @property
    def no_copy_mode(self) -> bool:
        """
        If True, avoid the data copies between tasks when possible.
        """

    @no_copy_mode.setter
    def no_copy_mode(self, arg1: bool) -> None: ...
