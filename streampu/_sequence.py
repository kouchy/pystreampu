# -*- coding: utf-8 -*-
from __future__ import annotations

from typing import List

from streampu._ext import exceptions
from streampu._ext.core import Socket, Task, _Sequence
from streampu._ext.set import Set


def _unique(in_list: list):
    out_list = []
    for elt in in_list:
        if id(elt) not in [id(e) for e in out_list]:
            out_list.append(elt)
    return out_list


def _get_firsts(s: Socket):
    def visit(s: Socket, visited: List[Task]):
        tsk = s.task
        visited.append(tsk)
        tsk_forwards = tsk.forwards
        all_fwd_are_outputs = True
        for fwd in tsk_forwards:
            try:
                bnd_sck = fwd.get_bound_socket()
                if bnd_sck is not None:
                    all_fwd_are_outputs = False
                    break
            except Exception:
                pass

        if len(tsk.inputs) == 0 and not tsk.is_bound() and all_fwd_are_outputs:
            return [tsk]

        out = []
        lbnd = [si.get_bound_socket() for si in tsk.inputs]
        lbnd_fwd = [si.get_bound_socket() for si in tsk_forwards]
        lbnd += lbnd_fwd
        lbnd = _unique(lbnd)
        for b in lbnd:
            try:
                if b.task not in visited:
                    lt = visit(b, visited)
                    for t in lt:
                        out.append(t)
            except Exception:
                out.append(b.task)
        return out

    return visit(s, [])


def get_cloned_modules(self, module_ref):
    """Return the copies of a module used by each thread of the sequence.

    Args:
        module_ref (Module): a module of the sequence, as created by the user
            (i.e. the module used by the thread 0)

    Returns:
        out (list): the module used by each thread, the first one being `module_ref`

    Raises:
        RuntimeError: if `module_ref` is not part of the sequence
    """
    found = False
    mid = 0
    all_modules = self.get_modules_per_threads()
    while mid < len(all_modules[0]) and not found:
        if id(all_modules[0][mid]) == id(module_ref):
            found = True
        else:
            mid += 1
    if not found:
        raise (exceptions.RuntimeError("'module_ref' can't be found in the sequence."))

    cloned_modules = []
    for tid in range(len(all_modules)):
        if isinstance(all_modules[tid][mid], type(module_ref)):
            cloned_modules.append(all_modules[tid][mid])
        else:
            raise exceptions.RuntimeError("This should never happen.")

    return cloned_modules


_Sequence.get_cloned_modules = get_cloned_modules


def get_modules(self, module_class, set_modules=True):
    """Return the modules of a given class, for all the threads of the sequence.

    Args:
        module_class (type): a module class, e.g. `streampu.Module` for all the modules
        set_modules (bool): if True, also explore the sequences held by `Set` modules

    Returns:
        out (list): the modules of the sequence that are instances of `module_class`
    """
    all_modules = [m for lst in self.get_modules_per_threads() for m in lst]
    return_list = [m for m in all_modules if isinstance(m, module_class)]
    if set_modules:
        sse_list = [mdl for mdl in all_modules if isinstance(mdl, Set)]
        for sse in sse_list:
            return_list += sse.sequence.get_module(module_class, True)
    return return_list


_Sequence.get_modules = get_modules


class Sequence(_Sequence):
    """Overlay of streampu._ext.core._Sequence."""

    @staticmethod
    def _is_socket_input(value):
        if isinstance(value, Socket):
            return True
        if isinstance(value, list):
            return len(value) > 0 and all(isinstance(v, Socket) or hasattr(v, "_mrv") for v in value)
        return hasattr(value, "_mrv")

    @staticmethod
    def _firsts_from_sockets(sockets):
        firsts = []
        if not isinstance(sockets, list):
            sockets = [sockets]
        for s_itm in sockets:
            if hasattr(s_itm, "_mrv"):
                s_itm = s_itm._mrv
            local_firsts = _get_firsts(s_itm)
            for first in local_firsts:
                if first not in firsts:
                    firsts.append(first)
        return firsts

    def __init__(self, *args, **kwargs):
        """Build a Sequence.

        A sequence can be built from:

        - a socket or a list of sockets: `Sequence(out)`, `Sequence([s1, s2])`. The first
          tasks are found by following the bindings backwards from these sockets;
        - its first task: `Sequence(task)`, or a list of first tasks;
        - its first and last tasks: `Sequence(first, last)`.

        The following positional or keyword arguments are those of the C++ constructor:
        `n_threads` (default 1), `thread_pinning` (default False),
        `sequence_pinning_policy` and `tasks_inplace`.

        Args:
            *args (Any): socket(s) or task(s) to build the sequence from, followed by the
                optional arguments of the C++ constructor
            **kwargs (Any): keyword arguments of the C++ constructor; `sockets` can be used
                to give the socket(s) to build the sequence from

        Examples:
            >>> seq = streampu.Sequence(out)        # one thread
            >>> seq = streampu.Sequence(out, 4)     # four threads
            >>> seq.exec_n_times(100)
        """
        if "sockets" in kwargs:
            sockets = kwargs.pop("sockets")
            firsts = self._firsts_from_sockets(sockets)
            super().__init__(firsts, [], [], *args, **kwargs)
        elif len(args) > 0 and self._is_socket_input(args[0]):
            firsts = self._firsts_from_sockets(args[0])
            super().__init__(firsts, [], [], *args[1:], **kwargs)
        else:
            super().__init__(*args, **kwargs)
        self.original_modules = super().get_modules_per_threads()[0]


__all__ = ["Sequence"]
