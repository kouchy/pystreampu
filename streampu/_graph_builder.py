# -*- coding: utf-8 -*-
"""Common part of `streampu.pipeline` and `streampu.sequence`: describe a graph in a `with` block."""

from typing import Any, Dict, List

from streampu._context_manager import _Context, _context_manager
from streampu._ext import exceptions
from streampu._ext.core import Task
from streampu._sequence import _bound_sockets

# `Task.bind` as bound from C++. Inside a `with streampu.pipeline()` or `with streampu.sequence()`
# block only, it is replaced by `_recording_bind`, which records the dependency: outside the block,
# `Task.bind` (and its stub, generated from the imported package) stays the C++ method.
_task_bind = Task.bind


def _recording_bind(self: Task, *args, **kwargs):
    out = args[0] if args else kwargs.get("s_out", kwargs.get("t_out"))
    if out is not None:
        _context_manager.store_control(self, out if isinstance(out, Task) else out.task)
    return _task_bind(self, *args, **kwargs)


def _task_label(tsk: Task) -> str:
    return f"'{tsk.module.name}::{tsk.name}'"


def _index(tasks: List[Task], tsk: Task) -> int:
    for i, t in enumerate(tasks):
        if t is tsk:
            return i
    return -1


class _BuilderScope(_Context):
    """A context opened by a graph builder (the builder itself, or a pipeline stage)."""


class _GraphBuilder(_BuilderScope):
    """Base of `PipelineBuilder` and `SequenceBuilder`.

    During the `with` block, the tasks are only bound (`Task.call_auto_exec` is False) and the
    `Task.bind` dependencies are recorded. At the end of the block, `_build()` creates the object
    (`Pipeline` or `Sequence`), to which the builder then forwards the attributes and methods.
    """

    _LOCAL = ("type",)
    _KIND = ""  # "pipeline" or "sequence": name of the block and of the property of the built object

    def __init__(self, name: str):
        super().__init__(name)
        self._controls: Dict[int, List[Task]] = {}
        self._saved_auto_exec = True
        self._built: Any = None
        self._entered = False

    # ------------------------------------------------------------------ context protocol
    def __enter__(self):
        if self._entered:
            raise exceptions.RuntimeError(f"A 'streampu.{self._KIND}' can be described only once.")
        if isinstance(_context_manager.current_context, _BuilderScope):
            raise exceptions.RuntimeError(
                "'streampu.pipeline' and 'streampu.sequence' blocks cannot be nested "
                f"(a 'streampu.{self._KIND}' block is opened inside another block)."
            )
        self._entered = True
        self._saved_auto_exec = Task.call_auto_exec
        Task.call_auto_exec = False
        Task.bind = _recording_bind
        _context_manager.open_context(self)
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        _context_manager.close_context(self)
        Task.bind = _task_bind
        Task.call_auto_exec = self._saved_auto_exec
        if exc_type is None:
            self._build()

    def _build(self) -> None:
        raise NotImplementedError

    # ------------------------------------------------------------------ recording
    def _store_control(self, tsk: Task, producer: Task) -> None:
        self._controls.setdefault(id(tsk), []).append(producer)

    def _producers(self, tsk: Task) -> List[Task]:
        """Tasks that `tsk` depends on: the data bindings and the `Task.bind` dependencies."""
        out = []
        for t in [s.task for s in _bound_sockets(tsk)] + self._controls.get(id(tsk), []):
            if _index(out, t) < 0:
                out.append(t)
        return out

    def _attach_sources(self, groups: List[List[Task]]) -> List[List[Task]]:
        """Add to each group the tasks without input declared out of the block that feed it.

        A task without input (a source, a constant created before the block...) joins the group of
        its first consumer, at its beginning. A task with inputs declared out of the block raises an
        error.

        Args:
            groups (list[list[Task]]): the tasks recorded in the block (one list per stage)

        Returns:
            out (list[list[Task]]): the groups with the attached tasks
        """
        known = {id(t) for tasks in groups for t in tasks}
        attached: List[List[Task]] = [[] for _ in groups]
        for k, tasks in enumerate(groups):
            for t in tasks:
                for p in self._producers(t):
                    if id(p) in known:
                        continue
                    if self._producers(p):
                        raise exceptions.RuntimeError(
                            f"Task {_task_label(t)} depends on the task {_task_label(p)}, which is not "
                            f"declared in the 'streampu.{self._KIND}' block."
                        )
                    attached[k].append(p)
                    known.add(id(p))
        return [attached[k] + tasks for k, tasks in enumerate(groups)]

    # ------------------------------------------------------------------ forwarding
    def _get_built(self) -> Any:
        if self._built is None:
            raise exceptions.RuntimeError(
                f"The {self._KIND} is built at the end of the 'with streampu.{self._KIND}()' block."
            )
        return self._built

    def __getattr__(self, name: str) -> Any:
        # only called when `name` is not an attribute of the builder
        if name.startswith("_"):
            raise AttributeError(name)
        return getattr(self._get_built(), name)

    def __setattr__(self, name: str, value: Any) -> None:
        if name.startswith("_") or name in self._LOCAL:
            object.__setattr__(self, name, value)
        else:
            setattr(self._get_built(), name, value)

    def __dir__(self) -> list:
        out = list(object.__dir__(self))
        if self._built is not None:
            out += [n for n in dir(self._built) if n not in out]
        return out


__all__: List[str] = []
