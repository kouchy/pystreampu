"""Functional tests for Sequence with binary operators."""

import numpy as np
import pytest

import streampu as spu


@pytest.mark.parametrize(
    ("builder", "expected"),
    [
        (lambda x: x + 1, np.array([[2, 3, 4]], dtype=np.int64)),
        (lambda x: 1 + x, np.array([[2, 3, 4]], dtype=np.int64)),
    ],
    ids=["right-add", "left-add"],
)
def test_sequence_bop_add(builder, expected):
    x = spu.array([1, 2, 3])
    y = builder(x)

    seq = spu.Sequence(y)
    seq.exec_seq()

    np.testing.assert_array_equal(y.numpy, expected)


def test_sequence_bop_inplace_chained_ops():
    x = spu.array([1, 2, 3])
    x_view = x.numpy

    x += 1
    x += 1
    x *= 2

    seq = spu.Sequence(x)
    x_view[:] = [1, 2, 3]  # Reset backing values before executing the built sequence.
    seq.exec_seq()

    np.testing.assert_array_equal(x.numpy, np.array([[6, 8, 10]]))


def _first_last_graph():
    """initializer -> incrementer -> * 2 -> finalizer: the `2` is a constant (Array.read)."""
    ini, inc, fin = (
        spu.initializer(3, dtype=spu.int32),
        spu.incrementer(3, dtype=spu.int32),
        spu.finalizer(3, dtype=spu.int32),
    )
    fin.finalize(inc.increment(ini.initialize()) * 2, auto_exec=False)
    return ini, fin


@pytest.mark.parametrize("extra_args", [(), (2,), ([],), ([], 2)], ids=["default", "n_threads", "exclusions", "both"])
def test_sequence_first_last_with_constant(extra_args):
    """Sequence(first, last) also executes the constants of the graph."""
    previous = spu.Task.call_auto_exec
    spu.Task.call_auto_exec = False
    try:
        ini, fin = _first_last_graph()
        seq = spu.Sequence(ini.initialize, fin.finalize, *extra_args)
        seq.exec_seq()
    finally:
        spu.Task.call_auto_exec = previous
    np.testing.assert_array_equal(fin.finalize["in"].numpy, np.full((1, 3), 2))


def test_sequence_first_last_other_graph():
    """The constants of another graph are not added to the sequence."""
    previous = spu.Task.call_auto_exec
    spu.Task.call_auto_exec = False
    try:
        ini, fin = _first_last_graph()
        other = spu.initializer(3, dtype=spu.int32).initialize() + 5  # noqa: F841 (other graph)
        seq = spu.Sequence(ini.initialize, fin.finalize)
        names = [t.module.name for tasks in seq.get_tasks_per_types() for t in tasks]
    finally:
        spu.Task.call_auto_exec = previous
    assert names.count("Array") == 1 and names.count("Initializer") == 1, names
