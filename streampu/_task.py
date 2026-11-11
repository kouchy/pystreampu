# -*- coding: utf-8 -*-
"""Add some magic functions to the class Task."""

from __future__ import annotations

from typing import Any, Union

import numpy as np

from streampu import _context_manager
from streampu._ext import exceptions as exc
from streampu._ext.core import Socket, Task
from streampu._typing import SocketLike

Task.call_auto_exec = True


def _setattr_impl(self: Task, attr: str, value: Any) -> Union[tuple, Socket, None]:
    """Overload __setattr__ of streampu._ext.core.Task.

    Args:
        self (Task): A Task
        attr (str): attribute name
        value (Any): Value to set
    """
    for s in self.sockets:
        if s.name == attr:
            self[attr].bind(value)
            return
    object.__setattr__(self, attr, value)


def _getattr_impl(self: Task, attr: str) -> Union[tuple, Socket, None]:
    """Overload __getattr__ of streampu._ext.core.Task.

    task.<socket_name> returns the socket named `socket_name` of the task.
    Note: `Task.__getitem__` (and `Codelet_call_cache::init`) caches the resolved `Socket`
    in `self.__dict__[attr]`, so subsequent `task.<socket_name>` accesses hit `self.__dict__`
    directly in C without calling `__getattr__`.

    Args:
        self (Task): A Task
        attr (str): socket name

    Returns:
        out (Socket): the task socket named 'sck_name'
    """
    for s in self.sockets:
        if s.name == attr:
            return self[attr]

    return object.__getattribute__(self, attr)


def _dir_impl(self: Task) -> dict:
    new_dir = object.__dir__(self)
    for sckt in self.sockets:
        new_dir.append(sckt.name)
    return new_dir


def _call_impl(
    self: Task,
    *args: tuple[SocketLike],
    raw_data=False,
    auto_exec=True,
    **kwargs: dict[str, SocketLike],
) -> Union[Socket, tuple[Socket], None]:
    out_dir = Socket.directions.OUT

    inputs = [sckt for sckt in self.sockets if sckt.direction != out_dir]
    outputs = [sckt for sckt in self.sockets if sckt.direction == out_dir]
    outputs = [sckt for sckt in outputs if sckt.name != "status"]

    _context_manager.store_task(self)

    for i, arg in enumerate(args):
        inputs[i].reset()
        inputs[i].bind(arg, raw_data=raw_data)

    for key, sckt in kwargs.items():
        if key in ["raw_data", "auto_exec"]:
            continue
        self[key].reset()
        self[key].bind(sckt, raw_data=raw_data)

    if Task.call_auto_exec and auto_exec:
        try:
            self.exec()
        except exc.ProcessingAborted:
            pass

    if raw_data:
        out = tuple(np.array(sckt, copy=False) for sckt in outputs)
        if len(out) == 1:
            out = out[0]

        return out

    # Return a tuple of Sockets except that does not contain the status socket
    # If only one output socket, return this socket
    out = tuple(sckt for sckt in outputs)
    if len(out) > 1:
        return out

    if len(out) == 1:
        return out[0]

    return None


_task_bind = Task.bind


def _bind_impl(self: Task, out: Union[Task, Socket], priority: int = -1) -> None:
    """Bind the task to a task or a socket, to force an order of execution.

    The task will be executed after `out` (a task, or the task owning the socket `out`).
    Inside `streampu.stage`, the dependency is recorded to split the pipeline.

    Args:
        self (Task): the task to execute after `out`
        out (Task | Socket): the task, or an output/forward socket of the task, to execute
            before `self`
        priority (int): priority of the binding, -1 for the default one
    """
    _context_manager.store_control(self, out if isinstance(out, Task) else out.task)
    _task_bind(self, out, priority)


Task.bind = _bind_impl
Task.__call__ = _call_impl
Task.__getattr__ = _getattr_impl
Task.__setattr__ = _setattr_impl
Task.__dir__ = _dir_impl

__all__ = ["Task"]
