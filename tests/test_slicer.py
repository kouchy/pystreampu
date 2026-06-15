"""Functional tests for the slice operator."""

import numpy as np
import pytest

from streampu import Sequence, array


def _assert_numpy(stream_arr, expected):
    """Compare a streampu array against an expected NumPy-compatible value."""
    expected_np = np.array(expected)
    assert np.array_equal(stream_arr.numpy, expected_np)


@pytest.mark.parametrize(
    "slice_obj, expected",
    [
        (slice(1, 4), [[2, 3, 4]]),
        (slice(None, 3), [[1, 2, 3]]),
        (slice(None, None, 2), [[1, 3, 5]]),
    ],
)
def test_slice_reads(slice_obj, expected):
    x = array([1, 2, 3, 4, 5])
    _assert_numpy(x[slice_obj], expected)


def test_slice_writes():
    x = array([1, 2, 3, 4, 5])

    x[1:4] = [20, 30, 40]
    _assert_numpy(x, [[1, 20, 30, 40, 5]])

    x[:3] = [10, 20, 30]
    _assert_numpy(x, [[10, 20, 30, 40, 5]])

    x[::2] = [100, 300, 400]
    _assert_numpy(x, [[100, 20, 300, 40, 400]])


def test_slice_sequence():
    x = array([1, 2, 3, 4, 5])
    xnp = x.numpy
    x[::2] = [10, 30, 50]

    seq = Sequence.from_socket(x)
    xnp[:] = [1, 2, 3, 4, 5]
    seq.exec_seq()
    _assert_numpy(x, [[10, 2, 30, 4, 50]])


def test_slice_sequence_read_write():
    x = array([1, 2, 3, 4, 5])
    xnp = x.numpy
    x[::2] = 2 * x[::2] + 1
    seq = Sequence.from_socket(x)
    xnp[:] = [1, 2, 3, 4, 5]
    seq.exec_seq()
    _assert_numpy(x, [[3, 2, 7, 4, 11]])


@pytest.mark.parametrize(
    "input_values, expected",
    [
        ([1, 2, 3, 4, 5], [[3, 2, 7, 4, 11]]),
        ([2, 4, 6, 8, 10], [[5, 4, 13, 8, 21]]),
    ],
)
def test_slice_sequence_read_write_multiple_inputs(input_values, expected):
    x = array(input_values)
    xnp = x.numpy

    x[::2] = 2 * x[::2] + 1
    seq = Sequence.from_socket(x)
    xnp[:] = input_values
    seq.exec_seq()

    _assert_numpy(x, expected)


@pytest.mark.parametrize(
    "input_values, expected",
    [
        ([1, 2, 3, 4, 5], [[3, 2, 7, 4, 11]]),
        ([2, 4, 6, 8, 10], [[5, 4, 13, 8, 21]]),
    ],
)
def test_slice_sequence_read_write_multiple_inputs_inplace(input_values, expected):
    x = array(input_values)
    xnp = x.numpy

    x[::2] *= 2
    x[::2] += 1

    seq = Sequence.from_socket(x)
    xnp[:] = input_values
    seq.exec_seq()
    _assert_numpy(x, expected)


def test_slice_int_indexing():
    x = array([1, 2, 3, 4, 5])
    assert x.numpy[0][1] == 2

    x[1] = 3
    assert x.numpy[0][1] == 3

    x[1] += 4
    assert x.numpy[0][1] == 7
