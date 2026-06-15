"""Test min and max operations on sockets."""

import numpy as np

import streampu as spu


def test_minmax_1():
    x = spu.array([3, 1, 4, 1, 5])
    x_min = spu.min(x)
    x_max = spu.max(x)
    assert np.array_equal(x_min.numpy, [[1]])
    assert np.array_equal(x_max.numpy, [[5]])


def test_minmax_2():
    x = spu.array([3, 1, 4, 1, 5])
    y = spu.array([2, 7, 1, 8, 2])
    z_min = spu.min(x, y)
    z_max = spu.max(x, y)

    assert np.array_equal(z_min.numpy, [[2, 1, 1, 1, 2]])
    assert np.array_equal(z_max.numpy, [[3, 7, 4, 8, 5]])


def test_minmax_3():
    x = spu.array([3, 1, 4, 1, 5])
    y = spu.array([2, 7, 1, 8, 2])
    z = spu.array([8, 2, 3, 0, 6])

    z_min = spu.min(x, y, z)
    z_max = spu.max(x, y, z)

    seq = spu.Sequence.from_socket([z_min, z_max])
    seq.exec_seq()

    assert np.array_equal(z_min.numpy, [[2, 1, 1, 0, 2]])
    assert np.array_equal(z_max.numpy, [[8, 7, 4, 8, 6]])


if __name__ == "__main__":
    test_minmax_1()
    test_minmax_2()
    test_minmax_3()
