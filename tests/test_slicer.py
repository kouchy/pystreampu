"""Functional tests for the slice operator."""

import itertools

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

    seq = Sequence(x)
    xnp[:] = [1, 2, 3, 4, 5]
    seq.exec_seq()
    _assert_numpy(x, [[10, 2, 30, 4, 50]])


def test_slice_sequence_read_write():
    x = array([1, 2, 3, 4, 5])
    xnp = x.numpy
    x[::2] = 2 * x[::2] + 1
    seq = Sequence(x)
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
    seq = Sequence(x)
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

    seq = Sequence(x)
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


def test_iteration_stops_at_the_end_of_the_frame():
    """iter(socket) gives the elements of a frame and stops (it was infinite, past the end)."""
    s = array([1, 0, 1])
    items = list(itertools.islice(iter(s), 8))
    assert len(items) == 3
    assert [int(i.numpy[0, 0]) for i in items] == [1, 0, 1]
    assert [int(i.numpy[0, 0]) for i in s] == [1, 0, 1]


@pytest.mark.parametrize("key, expected", [(-1, [[5]]), (-5, [[1]]), (np.int64(2), [[3]]), ([0, -1], [[1, 5]])])
def test_negative_and_numpy_indices(key, expected):
    x = array([1, 2, 3, 4, 5])
    _assert_numpy(x[key], expected)


@pytest.mark.parametrize("key", [5, -6, [0, 5], [-6]])
def test_index_out_of_bounds(key):
    x = array([1, 2, 3, 4, 5])
    with pytest.raises(IndexError):
        x[key]
    with pytest.raises(IndexError):
        x[key] = 0


@pytest.mark.parametrize("key", [1.5, "a", [0.5]])
def test_invalid_index(key):
    x = array([1, 2, 3, 4, 5])
    with pytest.raises(TypeError):
        x[key]


def test_negative_index_write():
    x = array([1, 2, 3, 4, 5])
    x[-1] = 50
    _assert_numpy(x, [[1, 2, 3, 4, 50]])
