"""Test relayer allocation"""

import streampu as spu


def test_relayer_allocation():
    rly = spu.relayer(10, ns=1000, dtype=spu.int16)
    assert rly is not None
    assert rly.n_elmts == 10
    assert rly.ns == 1000


def test_relayer_invalid_dtype():
    try:
        _ = spu.relayer(10, ns=1000, dtype="float32")
        assert False, "Expected an exception for unsupported dtype"
    except TypeError:
        pass


if __name__ == "__main__":
    test_relayer_allocation()
    test_relayer_invalid_dtype()
