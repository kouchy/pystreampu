"""Test delayer allocation"""

import streampu as spu


def test_delayer_allocation():
    dly = spu.delayer(10, init_val=0, dtype=spu.int16)
    assert dly is not None


def test_delayer_invalid_dtype():
    try:
        _ = spu.delayer(10, init_val=0, dtype="float32")
        assert False, "Expected an exception for unsupported dtype"
    except TypeError:
        pass


if __name__ == "__main__":
    test_delayer_allocation()
    test_delayer_invalid_dtype()
