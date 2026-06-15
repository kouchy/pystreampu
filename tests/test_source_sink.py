"""Test sink and source with user binary data."""

import numpy as np

import streampu as spu
from streampu import sink_no, sink_user_binary


def test_sink_no():
    snk_no = sink_no(14, dtype=spu.uint8)
    assert snk_no is not None


def test_source_random():
    from streampu import source_random

    src = source_random(8, seed=0, dtype=spu.uint8)
    data, data_len = src.generate()
    assert data_len == len(data) == 8


def test_source_user(tmp_path):
    from streampu import source_user

    filename = tmp_path / "tmp.txt"

    msg = "Hello, world!"

    msg_bits = np.unpackbits(
        np.frombuffer(msg.encode("utf-8"), dtype=np.uint8),
        bitorder="little",
    )

    with filename.open("w") as f:
        f.write("1 \n" + str(len(msg_bits)) + "\n")
        for bit in msg_bits:
            f.write(str(bit) + " ")

    src = source_user(len(msg_bits), str(filename), dtype=spu.int32)
    data, data_len = src.generate()
    bits = np.array(data.numpy, dtype=np.uint8).reshape(-1)
    packed = np.packbits(bits, bitorder="little")

    assert bytes(packed).decode("utf-8") == msg
    assert data_len == len(msg_bits)


def test_sink_user_binary(tmp_path):
    filename = tmp_path / "tmp.txt"
    msg = "Hello, world!"

    msg_bits = np.unpackbits(
        np.frombuffer(msg.encode("utf-8"), dtype=np.uint8),
        bitorder="little",
    )

    snk = sink_user_binary(msg_bits.size, str(filename), dtype=spu.uint8)
    snk.send(msg_bits)

    with filename.open("rb") as f:
        assert f.read() == msg.encode("utf-8")


def test_source_user_binary(tmp_path):
    from streampu import source_user_binary

    msg = b"Hello, world!"
    filename = tmp_path / "tmp.txt"

    with filename.open("wb") as f:
        f.write(msg)

    src = source_user_binary(len(msg) * 8, str(filename), dtype=spu.uint8)

    data, data_len = src.generate()
    bits = np.array(data.numpy).reshape(-1)
    packed = np.packbits(bits, bitorder="little")

    assert bytes(packed) == msg
    assert data_len == len(msg) * 8
