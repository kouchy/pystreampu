"""Test task features."""

import numpy as np

import streampu as spu


def test_accessing_tasks_and_sockets():
    src = spu.source_random(8, seed=0, dtype=spu.uint8)

    src.name = "my_source"
    assert src.name == "my_source"

    generate0 = src.generate
    generate1 = src["generate"]
    generate2 = src.tasks[0]
    assert generate0 is generate1
    assert generate1 is generate2

    x0, x0_len = src.generate()
    assert generate0["out_data"] is x0
    assert generate0["out_count"] is x0_len

    x2 = src["generate::out_data"]
    x2_len = src["generate::out_count"]
    assert x2 is x0
    assert x2_len is x0_len

    xr, xr_len = src.generate(raw_data=True)
    assert np.array_equal(xr, x0)
    assert np.array_equal(xr_len, x0_len)

    # Socket access remains stable across both task-level and module-level lookups.
    assert src.generate["out_data"] is src["generate::out_data"]
    assert src.generate["out_count"] is src["generate::out_count"]

    dir_generate = dir(generate0)
    assert "out_data" in dir_generate
    assert "out_count" in dir_generate

    dir_src = dir(src)
    assert "generate" in dir_src


if __name__ == "__main__":
    test_accessing_tasks_and_sockets()
