# -*- coding: utf-8 -*-
"""Functional tests for binary operators."""

import numpy as np

import streampu as spu
from streampu import array


def _make_pair(dtype, lhs=12.6, rhs=13.2):
    """Create matching NumPy and streampu arrays for binary operation tests."""
    x = np.array([lhs], dtype=dtype.numpy)
    y = np.array([rhs], dtype=dtype.numpy)
    return x, y, array(x), dtype(y)


def _assert_stream_equals_numpy(stream_arr, numpy_arr):
    """Assert that a streampu array and a NumPy array hold the same values."""
    assert np.allclose(stream_arr.numpy, numpy_arr)


def test_bop_add(dtype):
    """Test 'add' binary operator.

    Args:
        dtype (streampu._ext.dtype): Data type
    """
    x, y, px, py = _make_pair(dtype)
    _assert_stream_equals_numpy(px + py, x + y)
    _assert_stream_equals_numpy(px + py, spu.add(px, py))

    y = x + 1
    py = px + 1
    _assert_stream_equals_numpy(py, y)
    _assert_stream_equals_numpy(spu.add(px, 1), y)

    y = 1 + x
    py = 1 + px
    _assert_stream_equals_numpy(py, y)
    _assert_stream_equals_numpy(spu.add(1, px), y)


def test_bop_sub(signed_dtype):
    """Test 'sub' binary operator.

    Args:
        signed_dtype (streampu._ext.dtype): Signed data type
    """
    x, y, px, py = _make_pair(signed_dtype)
    _assert_stream_equals_numpy(px - py, x - y)
    _assert_stream_equals_numpy(spu.sub(px, py), x - y)

    y = x - 1
    py = px - 1
    _assert_stream_equals_numpy(py, y)
    _assert_stream_equals_numpy(spu.sub(px, 1), y)

    y = 1 - x
    py = 1 - px
    _assert_stream_equals_numpy(py, y)
    _assert_stream_equals_numpy(spu.sub(1, px), y)


def test_bop_mul(dtype):
    """Test 'mul' binary operator.

    Args:
        dtype (streampu._ext.dtype): Data type
    """
    x, y, px, py = _make_pair(dtype)
    _assert_stream_equals_numpy(px * py, x * y)
    _assert_stream_equals_numpy(spu.mul(px, py), x * y)

    y = x * 2
    py = px * 2
    _assert_stream_equals_numpy(py, y)
    _assert_stream_equals_numpy(spu.mul(px, 2), y)

    y = 2 * x
    py = 2 * px
    _assert_stream_equals_numpy(py, y)
    _assert_stream_equals_numpy(spu.mul(2, px), y)


def test_bop_div(float_dtype):
    """Test 'div' binary operator.

    Args:
        float_dtype (streampu._ext.dtype): Float data type
    """
    x, y, px, py = _make_pair(float_dtype)
    _assert_stream_equals_numpy(px / py, x / y)
    _assert_stream_equals_numpy(spu.div(px, py), x / y)

    z = x / 2
    pz = px / 2
    _assert_stream_equals_numpy(pz, z)
    _assert_stream_equals_numpy(spu.div(px, 2), z)

    z = 2 / x
    pz = 2 / px
    _assert_stream_equals_numpy(pz, z)
    _assert_stream_equals_numpy(spu.div(2, px), z)


def test_bop_div2(int_dtype):
    """Test 'div2' binary operator.

    Args:
        int_dtype (streampu._ext.dtype): Integer data type
    """
    x = np.array([12], dtype=int_dtype.numpy)
    y = np.array([2], dtype=int_dtype.numpy)
    z = x // y

    px = array(x)
    py = array(y)
    pz = px / py
    _assert_stream_equals_numpy(pz, z)
    _assert_stream_equals_numpy(spu.div(px, py), z)


def test_bop_gt(float_dtype):
    """Test 'gt' binary operator.

    Args:
        float_dtype (streampu._ext.dtype): Float data type
    """
    x, y, px, py = _make_pair(float_dtype)
    _assert_stream_equals_numpy(px > py, x > y)
    _assert_stream_equals_numpy(spu.greater(px, py), x > y)

    z = x > 12
    pz = px > 12
    _assert_stream_equals_numpy(pz, z)
    _assert_stream_equals_numpy(spu.greater(px, 12), z)

    z = 13 > x
    pz = 13 > px
    _assert_stream_equals_numpy(pz, z)
    _assert_stream_equals_numpy(spu.greater(13, px), z)


def test_bop_lt(float_dtype):
    """Test 'lt' binary operator.

    Args:
        float_dtype (streampu._ext.dtype): Float Data type
    """
    x, y, px, py = _make_pair(float_dtype)
    _assert_stream_equals_numpy(px < py, x < y)
    _assert_stream_equals_numpy(spu.less(px, py), x < y)


def test_bop_ge(float_dtype):
    """Test 'ge' binary operator.

    Args:
        float_dtype (streampu._ext.dtype): Float data type
    """
    x, y, px, py = _make_pair(float_dtype)
    _assert_stream_equals_numpy(px >= py, x >= y)
    _assert_stream_equals_numpy(spu.greater_equal(px, py), x >= y)


def test_bop_le(float_dtype):
    """Test 'le' binary operator.

    Args:
        float_dtype (streampu._ext.dtype): Float data type
    """
    x, y, px, py = _make_pair(float_dtype)
    _assert_stream_equals_numpy(px <= py, x <= y)
    _assert_stream_equals_numpy(spu.less_equal(px, py), x <= y)


def test_bop_eq(int_dtype):
    """Test 'eq' binary operator.

    Args:
        int_dtype (streampu._ext.dtype): Integer data type
    """
    x, y, px, py = _make_pair(int_dtype)
    _assert_stream_equals_numpy(px == py, x == y)
    _assert_stream_equals_numpy(spu.equal(px, py), x == y)


def test_bop_neq(int_dtype):
    """Test 'neq' binary operator.

    Args:
        int_dtype (streampu._ext.dtype): Integer data type
    """
    x, y, px, py = _make_pair(int_dtype)
    _assert_stream_equals_numpy(px != py, x != y)
    _assert_stream_equals_numpy(spu.not_equal(px, py), x != y)


def test_bop_add_const(dtype):
    """Test 'add' binary operator with constant.

    Args:
        dtype (streampu._ext.dtype): Data type
    """
    x = np.array([12.6], dtype=dtype.numpy)
    y = dtype.numpy([13.2])
    z = x + y

    px = array(x)
    pz = px + y
    _assert_stream_equals_numpy(pz, z)
    _assert_stream_equals_numpy(spu.add(px, y), z)


def test_bop_sub_const(signed_dtype):
    """Test 'sub' binary operator with constant.

    Args:
        signed_dtype (streampu._ext.dtype): Signed data type
    """
    x = np.array([12.6], dtype=signed_dtype.numpy)
    y = signed_dtype.numpy([13.2])
    z = x - y

    px = array(x)
    pz = px - y
    _assert_stream_equals_numpy(pz, z)
    _assert_stream_equals_numpy(spu.sub(px, y), z)


def test_bop_mul_const(dtype):
    """Test 'mul' binary operator with constant.

    Args:
        dtype (streampu._ext.dtype): Data type
    """
    x = np.array([12.6], dtype=dtype.numpy)
    y = dtype.numpy([13.2])
    z = x * y

    px = array(x)
    pz = px * y
    _assert_stream_equals_numpy(pz, z)
    _assert_stream_equals_numpy(spu.mul(px, y), z)


if __name__ == "__main__":
    test_bop_gt(spu.float32)
