"""Minimal example of a module written in Python with a state: keep one sample out of F."""

import streampu as spu
from streampu._ext.sfl import Stateful_core


class Downsampler(Stateful_core):
    """Stateful module with one task, `downsample`, that keeps one sample out of `F`.

    The parameter `F` is stored as a Python attribute of the module: it is its state.
    """

    def __init__(self, N, F=1, dtype=spu.float32):
        super().__init__()
        self.F = F

        task = self.create_task("downsample")
        self.create_socket_in(task, "input", N, dtype)
        self.create_socket_out(task, "output", N // F, dtype)
        self.create_codelet(task, Downsampler._downsample)

    @staticmethod
    def _downsample(mdl, tsk, frame_id):
        # `mdl` is the module that executes the task: the original one or one of its clones.
        # Always read the state from `mdl`, never from a `self` captured when the codelet was created.
        out = tsk["output"].numpy
        out[:] = tsk["input"].numpy[:, : out.shape[1] * mdl.F : mdl.F]
        return 0

    def clone(self):
        # Called by StreamPU to duplicate the module on several threads. Only the Python state
        # is copied here: the tasks, sockets and codelets are copied by StreamPU itself, so
        # `__init__` must not be called again. `type(self)` keeps the class of subclasses.
        other = type(self).__new__(type(self))
        Stateful_core.__init__(other)
        other.F = self.F
        return other
