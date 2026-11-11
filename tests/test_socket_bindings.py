# -*- coding: utf-8 -*-
"""Tests of the socket binding accessors."""

import gc

import streampu as sp


def test_get_bound_sockets():
    """The sockets returned by `get_bound_sockets` are owned by their tasks, not by Python.

    With a wrong return value policy, Python freed the sockets of the tasks (double free).
    """
    call_auto_exec = sp.Task.call_auto_exec
    sp.Task.call_auto_exec = False
    try:
        src = sp.source_random(8, dtype=sp.uint8)
        rlys = [sp.relayer(8, dtype=sp.uint8) for _ in range(2)]
        data, *_ = src.generate()
        for rly in rlys:
            rly.relay(data)

        for _ in range(10):
            bound = src.generate["out_data"].get_bound_sockets()
            del bound
            gc.collect()

        bound = src.generate["out_data"].get_bound_sockets()
        assert len(bound) == 2
        assert bound[0] is rlys[0].relay["in"]
        assert bound[1] is rlys[1].relay["in"]
        assert rlys[0].relay["in"].get_bound_socket() is src.generate["out_data"]
        assert rlys[0].relay["out"].get_bound_sockets() == []
    finally:
        sp.Task.call_auto_exec = call_auto_exec
