# -*- coding: utf-8 -*-
"""Functional tests for Stateful_core (modules written in Python with a state)."""

import numpy as np

import streampu as spu


class Scaler(spu.Stateful_core):
    """Multiply the input by `k`, the state of the module."""

    def __init__(self, N, k, dtype):
        super().__init__()
        self.k = k
        tsk = self.create_task("scale")
        self.create_socket_in(tsk, "input", N, dtype)
        self.create_socket_out(tsk, "output", N, dtype)
        self.create_codelet(tsk, Scaler._scale)

    @staticmethod
    def _scale(mdl, tsk, frame_id):
        tsk["output"].numpy[:] = tsk["input"].numpy * mdl.k
        return 0

    def clone(self):
        other = type(self).__new__(type(self))
        spu.Stateful_core.__init__(other)
        other.k = self.k
        return other


def test_public_api():
    """Stateful_core is available from the streampu package."""
    from streampu._ext.sfl import Stateful_core

    assert spu.Stateful_core is Stateful_core


def test_stateful_core_exec():
    """A task of a Stateful_core module is executed with the state of the module."""
    mdl = Scaler(4, 3, spu.int32)
    y = mdl.scale(spu.array([1, 2, 3, 4], dtype=spu.int32))
    np.testing.assert_array_equal(y.numpy, np.array([[3, 6, 9, 12]], dtype=np.int32))


def test_stateful_core_clones():
    """In a multithreaded sequence, every clone has the class and the state of the module."""
    mdl = Scaler(4, 2, spu.int32)
    y = mdl.scale(spu.array([1, 2, 3, 4], dtype=spu.int32))
    seq = spu.Sequence(y + 1, 3)
    seq.exec_n_times(10)

    clones = seq.get_cloned_modules(mdl)
    assert len(clones) == 3
    assert all(type(c) is Scaler for c in clones)
    assert [c.k for c in clones] == [2, 2, 2]
