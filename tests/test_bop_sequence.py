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

    seq = spu.Sequence.from_socket(y)
    seq.exec_seq()

    np.testing.assert_array_equal(y.numpy, expected)


def test_sequence_bop_inplace_chained_ops():
    x = spu.array([1, 2, 3])
    x_view = x.numpy

    x += 1
    x += 1
    x *= 2

    seq = spu.Sequence.from_socket(x)
    x_view[:] = [1, 2, 3]  # Reset backing values before executing the built sequence.
    seq.exec_seq()

    np.testing.assert_array_equal(x.numpy, np.array([[6, 8, 10]]))
