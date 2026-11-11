# -*- coding: utf-8 -*-
"""Tests of the description of a sequence in a `with streampu.sequence()` block."""

import types

import numpy as np
import pytest

import streampu as sp
from streampu import _context_manager

DATA_LENGTH = 8


def _chain(n_incs=3):
    ini = sp.initializer(DATA_LENGTH, dtype=sp.uint8)
    incs = [sp.incrementer(DATA_LENGTH, dtype=sp.uint8) for _ in range(n_incs)]
    fin = sp.finalizer(DATA_LENGTH, dtype=sp.uint8)
    return ini, incs, fin


def _modules(seq, module_class):
    return [m for m in seq.get_modules_per_threads()[0] if isinstance(m, module_class)]


def _assert_clean_context(auto_exec=True):
    assert sp.Task.call_auto_exec is auto_exec
    assert not isinstance(_context_manager.current_context, (sp.SequenceBuilder, sp.PipelineBuilder, sp.Stage))
    assert not isinstance(sp.Task.bind, types.FunctionType)


def test_simple_chain():
    ini, incs, fin = _chain()
    with sp.sequence() as seq:
        assert sp.Task.call_auto_exec is False
        x = ini.initialize()
        for inc in incs:
            x = inc.increment(x)
        fin.finalize(x)
    _assert_clean_context()

    assert isinstance(seq.sequence, sp.Sequence)
    assert seq.tasks[0] is ini.initialize
    assert seq._firsts_tasks == [ini.initialize]
    assert seq._lasts_tasks == [fin.finalize]
    assert seq._exclusions == []
    assert len(_modules(seq.sequence, sp.Module)) == 5

    ini.data_init[0][:] = 10
    seq.exec_n_times(1)  # forwarded to the Sequence
    assert np.all(np.array(fin.final_data[0]) == 13)


def test_same_sequence_as_explicit_api():
    ini, incs, fin = _chain()
    with sp.sequence() as seq:
        x = ini.initialize()
        for inc in incs:
            x = inc.increment(x)
        fin.finalize(x)

    ini2, incs2, fin2 = _chain()
    sp.Task.call_auto_exec = False
    x = ini2.initialize()
    for inc in incs2:
        x = inc.increment(x)
    fin2.finalize(x)
    sp.Task.call_auto_exec = True
    explicit = sp.Sequence(ini2.initialize, fin2.finalize)

    # the C++ sequence collects its modules in a set of pointers: their order depends on the
    # memory addresses, so the modules are compared without order
    names = sorted(type(m).__name__ for m in seq.get_modules_per_threads()[0])
    names2 = sorted(type(m).__name__ for m in explicit.get_modules_per_threads()[0])
    assert names == names2
    # the order of execution of the tasks is the same
    tasks = [f"{type(t.module).__name__}::{t.name}" for t in seq.get_tasks_per_threads()[0]]
    tasks2 = [f"{type(t.module).__name__}::{t.name}" for t in explicit.get_tasks_per_threads()[0]]
    assert tasks == tasks2
    assert [t.name for t in seq.first_tasks[0]] == [t.name for t in explicit.first_tasks[0]]
    assert [t.name for t in seq.last_tasks[0]] == [t.name for t in explicit.last_tasks[0]]


def test_options_and_forwarding():
    ini, incs, fin = _chain()
    with sp.sequence(n_threads=3, tasks_inplace=False) as seq:
        fin.finalize(incs[0].increment(ini.initialize()))

    assert len(seq.get_cloned_modules(seq.get_modules_per_threads()[0][0])) == 3
    seq.n_frames = 2  # forwarded
    assert seq.sequence.n_frames == 2
    assert "exec_n_times" in dir(seq)
    assert "n_threads=3" in repr(seq)


def test_constants_created_in_the_block():
    ini, _, fin = _chain(0)
    with sp.sequence() as seq:
        x = ini.initialize()
        fin.finalize(x + 1)  # `+ 1` creates a constant (Array.read) and an addition

    assert len(seq._firsts_tasks) == 2  # the initializer and the constant
    ini.data_init[0][:] = 4
    seq.exec_n_times(1)
    assert np.all(np.array(fin.final_data[0]) == 5)


def test_source_declared_before_the_block():
    ini, incs, fin = _chain(1)
    sp.Task.call_auto_exec = False
    x = ini.initialize()
    sp.Task.call_auto_exec = True

    with sp.sequence() as seq:
        fin.finalize(incs[0].increment(x))

    assert seq.tasks[0] is ini.initialize
    assert seq._firsts_tasks == [ini.initialize]


def test_consumers_out_of_the_block_are_excluded():
    ini, incs, fin = _chain(1)
    # a whole graph described before the block...
    sp.Task.call_auto_exec = False
    fin.finalize(incs[0].increment(ini.initialize()))
    sp.Task.call_auto_exec = True

    # ...of which only the beginning makes the sequence
    with sp.sequence() as seq:
        incs[0].increment(ini.initialize())

    assert seq._lasts_tasks == [incs[0].increment]
    assert seq._exclusions == [fin.finalize]
    assert len(_modules(seq.sequence, sp.Module)) == 2  # no finalizer


def test_control_dependency():
    ini, incs, fin = _chain(2)
    with sp.sequence() as seq:
        x = ini.initialize()
        incs[0].increment(x)
        y = incs[1].increment(x)
        incs[1].increment.bind(incs[0].increment)
        fin.finalize(y)
    _assert_clean_context()

    assert seq._firsts_tasks == [ini.initialize]
    assert seq._lasts_tasks == [fin.finalize]  # incs[0].increment is consumed by the binding


def test_control_dependency_keywords():
    ini, incs, fin = _chain(2)
    with sp.sequence() as seq:
        x = ini.initialize()
        a = incs[0].increment(x)
        fin.finalize(incs[1].increment(x))
        fin.finalize.bind(t_out=incs[0].increment)
        fin.finalize.bind(s_out=a, priority=-1)

    assert seq._lasts_tasks == [fin.finalize]


def test_error_empty():
    with pytest.raises(sp.exceptions.RuntimeError, match="does not contain any task"):
        with sp.sequence():
            pass
    _assert_clean_context()


def test_error_not_built():
    seq = sp.sequence()
    with pytest.raises(sp.exceptions.RuntimeError, match="built at the end"):
        seq.exec()


def test_error_described_twice():
    ini, incs, fin = _chain(1)
    seq = sp.sequence()
    with seq:
        fin.finalize(incs[0].increment(ini.initialize()))
    with pytest.raises(sp.exceptions.RuntimeError, match="only once"):
        with seq:
            pass


def test_error_n_threads():
    with pytest.raises(sp.exceptions.InvalidArgument, match="strictly greater than 0"):
        sp.sequence(n_threads=0)


def test_error_dependency_out_of_the_block():
    ini, incs, fin = _chain(2)
    sp.Task.call_auto_exec = False
    x = incs[0].increment(ini.initialize())  # a task with an input, out of the block
    sp.Task.call_auto_exec = True
    with pytest.raises(sp.exceptions.RuntimeError, match="not declared in the 'streampu.sequence' block"):
        with sp.sequence():
            fin.finalize(incs[1].increment(x))
    _assert_clean_context()


@pytest.mark.parametrize("outer", ["sequence", "pipeline"])
@pytest.mark.parametrize("inner", ["sequence", "pipeline"])
def test_error_nested(outer, inner):
    with pytest.raises(sp.exceptions.RuntimeError, match="cannot be nested"):
        with getattr(sp, outer)():
            with getattr(sp, inner)():
                pass
    _assert_clean_context()


def test_error_sequence_in_a_stage():
    with pytest.raises(sp.exceptions.RuntimeError, match="cannot be nested"):
        with sp.pipeline():
            with sp.stage():
                with sp.sequence():
                    pass
    _assert_clean_context()


def test_error_stage_in_a_sequence():
    with pytest.raises(sp.exceptions.RuntimeError, match="inside a 'with streampu.pipeline"):
        with sp.sequence():
            with sp.stage():
                pass
    _assert_clean_context()


def test_auto_exec_restored_after_error():
    sp.Task.call_auto_exec = False
    with pytest.raises(ZeroDivisionError):
        with sp.sequence():
            1 / 0
    _assert_clean_context(auto_exec=False)
    sp.Task.call_auto_exec = True
