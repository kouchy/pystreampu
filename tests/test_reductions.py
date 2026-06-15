"""Test reductions."""

import numpy as np

import streampu as spu


def test_reduction_sum():
    x = spu.array([1, 2, 3])
    y = spu.sum(x)
    seq = spu.Sequence.from_socket(y)
    seq.exec_seq()
    assert np.all(y.numpy == 6)


def test_reduction_prod():
    x = spu.array([1, 2, 3])
    y = spu.prod(x)
    seq = spu.Sequence.from_socket(y)
    seq.exec_seq()
    assert np.all(y.numpy == 6)


def test_reduction_max():
    x = spu.array([1, 2, 3])
    y = spu.max(x)
    seq = spu.Sequence.from_socket(y)
    seq.exec_seq()
    assert np.all(y.numpy == 3)


def test_reduction_all():
    x = spu.array([1, 1, 0])
    y = spu.all(x)
    seq = spu.Sequence.from_socket(y)
    seq.exec_seq()
    assert np.all(y.numpy == 0)


def test_reduction_any():
    x = spu.array([0, 0, 1])
    y = spu.any(x)
    seq = spu.Sequence.from_socket(y)
    seq.exec_seq()
    assert np.all(y.numpy == 1)
