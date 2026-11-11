# -*- coding: utf-8 -*-
"""Tests of the description of a pipeline stage by stage (`streampu.pipeline` / `streampu.stage`)."""

import filecmp
import os

import pytest

import streampu as sp
from streampu import _context_manager

DATA_LENGTH = 64


@pytest.fixture
def files(tmp_path):
    in_path = str(tmp_path / "file.in")
    out_path = str(tmp_path / "file.out")
    with open(in_path, "wb") as fout:
        fout.write(os.urandom(8 * 1024))
    return in_path, out_path


def _chain(in_path, out_path, n_relays=3):
    src = sp.source_user_binary(DATA_LENGTH, in_path, auto_reset=False, dtype=sp.uint8)
    snk = sp.sink_user_binary(DATA_LENGTH, out_path, dtype=sp.uint8)
    rlys = [sp.relayer(DATA_LENGTH, dtype=sp.uint8) for _ in range(n_relays)]
    return src, snk, rlys


def _names(tasks):
    return [f"{t.module.name}::{t.name}" for t in tasks]


def _stage_modules(pip, stage_id, module_class):
    return [m for m in pip.stages[stage_id].get_modules_per_threads()[0] if isinstance(m, module_class)]


def _assert_clean_context(auto_exec=True):
    assert sp.Task.call_auto_exec is auto_exec
    assert not isinstance(_context_manager.current_context, (sp.PipelineBuilder, sp.Stage))


def test_three_stages(files):
    in_path, out_path = files
    src, snk, rlys = _chain(*files)

    with sp.pipeline(buffer_size=4) as pip:
        assert sp.Task.call_auto_exec is False
        with sp.stage():
            data, cnt = src.generate()
        with sp.stage(n_threads=2):
            for rly in rlys:
                data = rly.relay(data)
        with sp.stage(active_waiting=True):
            snk.send_count(data, cnt)

    _assert_clean_context()
    assert isinstance(pip.pipeline, sp.Pipeline)

    firsts, lasts, excl = pip._sep_stages[0]
    assert _names(firsts) == _names(lasts) == ["Source_user_binary::generate"]
    assert _names(excl) == ["Relayer::relay", "Sink_user_binary::send_count"]
    firsts, lasts, excl = pip._sep_stages[1]
    assert firsts[0] is rlys[0].relay and lasts[0] is rlys[-1].relay
    assert len(firsts) == len(lasts) == 1
    assert _names(excl) == ["Sink_user_binary::send_count"]
    firsts, lasts, excl = pip._sep_stages[2]
    assert firsts[0] is snk.send_count and lasts[0] is snk.send_count and excl == []

    # attributes and methods are forwarded to the pipeline
    pip.n_frames = 2
    assert pip.n_frames == 2
    assert len(pip.stages) == 3
    assert len(pip.stages[1].get_modules_per_threads()) == 2
    pip.exec()
    assert filecmp.cmp(in_path, out_path)


def test_same_stages_as_explicit_api(files):
    """The stages deduced from the blocks are the ones written with `streampu.Pipeline(...)`."""
    in_path, out_path = files

    src, snk, rlys = _chain(*files)
    sp.Task.call_auto_exec = False
    data, cnt = src.generate()
    for rly in rlys:
        data = rly.relay(data)
    snk.send_count(data, cnt)
    sp.Task.call_auto_exec = True
    ref = sp.Pipeline(
        [src.generate],
        [snk.send_count],
        [
            [[src.generate], [src.generate], []],
            [[rlys[0].relay], [rlys[-1].relay], []],
            [[snk.send_count], [snk.send_count], []],
        ],
        [1, 2, 1],
        [4, 4],
        [False, False],
    )
    ref_tasks = [_names(s.get_tasks_per_threads()[0]) for s in ref.stages]
    ref.exec()
    assert filecmp.cmp(in_path, out_path)
    del ref
    os.remove(out_path)

    src, snk, rlys = _chain(*files)
    with sp.pipeline(buffer_size=4) as pip:
        with sp.stage():
            data, cnt = src.generate()
        with sp.stage(n_threads=2):
            for rly in rlys:
                data = rly.relay(data)
        with sp.stage():
            snk.send_count(data, cnt)
    assert [_names(s.get_tasks_per_threads()[0]) for s in pip.stages] == ref_tasks
    pip.exec()
    assert filecmp.cmp(in_path, out_path)


def test_branch_needs_exclusions(files):
    """A task of the stage 0 feeds a task of the stage 0 and a task of the stage 1.

    Without exclusion, the exploration of the stage 0 would also enter the task of the stage 1.
    """
    in_path, out_path = files
    src, snk, rlys = _chain(*files, n_relays=2)

    with sp.pipeline() as pip:
        with sp.stage():
            data, cnt = src.generate()
            rlys[0].relay(data)  # output not used
        with sp.stage():
            data = rlys[1].relay(data)
        with sp.stage():
            snk.send_count(data, cnt)

    firsts, lasts, excl = pip._sep_stages[0]
    assert firsts[0] is src.generate and lasts[0] is rlys[0].relay
    assert any(t is rlys[1].relay for t in excl)
    assert len(_stage_modules(pip, 0, type(rlys[0]))) == 1
    assert _stage_modules(pip, 1, type(rlys[1]))[0] is rlys[1]
    pip.exec()
    assert filecmp.cmp(in_path, out_path)


def test_first_with_inputs_from_two_stages(files):
    """A task fed by the previous stage and by its own stage is a first of its stage."""
    in_path, out_path = files
    src, snk, rlys = _chain(*files, n_relays=2)

    with sp.pipeline() as pip:
        with sp.stage():
            data, cnt = src.generate()
        with sp.stage():
            data = rlys[0].relay(data)
            # `cnt` comes from the stage 0, `data` from the stage 1
            snk.send_count(data, cnt)

    firsts, lasts, _ = pip._sep_stages[1]
    assert firsts[0] is rlys[0].relay and firsts[1] is snk.send_count
    assert len(firsts) == 2
    assert lasts[0] is snk.send_count and len(lasts) == 1
    pip.exec()
    assert filecmp.cmp(in_path, out_path)


def test_control_dependency(files):
    """`Task.bind` inside a stage is taken into account to split the stage."""
    in_path, out_path = files
    src, snk, rlys = _chain(*files, n_relays=2)

    with sp.pipeline() as pip:
        with sp.stage():
            data, cnt = src.generate()
        with sp.stage():
            rlys[0].relay(data)  # output not used
            out = rlys[1].relay(data)
            rlys[1].relay.bind(rlys[0].relay)
        with sp.stage():
            snk.send_count(out, cnt)

    firsts, lasts, _ = pip._sep_stages[1]
    assert len(firsts) == 2 and len(lasts) == 1
    assert lasts[0] is rlys[1].relay  # rlys[0].relay is consumed by the binding
    pip.exec()
    assert filecmp.cmp(in_path, out_path)


def test_socket_binding_inside_stage(files):
    """A task whose sockets are bound (without calling the task) belongs to the stage."""
    in_path, out_path = files
    src, snk, rlys = _chain(*files, n_relays=1)

    with sp.pipeline() as pip:
        with sp.stage():
            data, cnt = src.generate()
        with sp.stage():
            rlys[0].relay["in"].bind(data)
        with sp.stage():
            snk.send_count.in_data = rlys[0].relay.out
            snk.send_count.in_count = cnt

    assert pip.stages_description[1].tasks[0] is rlys[0].relay
    assert pip.stages_description[2].tasks[0] is snk.send_count
    pip.exec()
    assert filecmp.cmp(in_path, out_path)


def test_source_declared_out_of_the_stages(files):
    """A task without input declared before the stages joins the stage of its first consumer."""
    in_path, out_path = files
    src, snk, rlys = _chain(*files, n_relays=1)

    with sp.pipeline() as pip:
        data, cnt = src.generate()
        with sp.stage():
            data = rlys[0].relay(data)
        with sp.stage():
            snk.send_count(data, cnt)

    assert pip._sep_stages[0][0][0] is src.generate
    assert pip._pipeline_firsts[0] is src.generate
    pip.exec()
    assert filecmp.cmp(in_path, out_path)


def test_buffer_parameters():
    src = sp.source_random(DATA_LENGTH, dtype=sp.uint8)
    rly = sp.relayer(DATA_LENGTH, dtype=sp.uint8)
    snk = sp.sink_no(DATA_LENGTH, dtype=sp.uint8)

    with sp.pipeline(buffer_size=8, active_waiting=True) as pip:
        with sp.stage():
            data, *_ = src.generate()
        with sp.stage(buffer_size=2):
            data = rly.relay(data)
        with sp.stage(active_waiting=False):
            snk.send(data)

    assert "size=2, active_waiting=True" in repr(pip)
    assert "size=8, active_waiting=False" in repr(pip)


# ---------------------------------------------------------------------------------------- errors


def test_error_task_out_of_stage():
    src = sp.source_random(DATA_LENGTH, dtype=sp.uint8)
    rly = sp.relayer(DATA_LENGTH, dtype=sp.uint8)
    with pytest.raises(sp.exceptions.RuntimeError, match="outside of a 'streampu.stage'"):
        with sp.pipeline():
            with sp.stage():
                data, *_ = src.generate()
            rly.relay(data)
    _assert_clean_context()


def test_error_stage_out_of_pipeline():
    with pytest.raises(sp.exceptions.RuntimeError, match="inside a 'with streampu.pipeline"):
        with sp.stage():
            pass
    _assert_clean_context()


def test_error_nested():
    with pytest.raises(sp.exceptions.RuntimeError, match="cannot be nested"):
        with sp.pipeline():
            with sp.stage():
                with sp.stage():
                    pass
    with pytest.raises(sp.exceptions.RuntimeError, match="cannot be nested"):
        with sp.pipeline():
            with sp.pipeline():
                pass
    _assert_clean_context()


def test_error_buffer_on_first_stage():
    with pytest.raises(sp.exceptions.InvalidArgument, match="first stage has no input buffer"):
        with sp.pipeline():
            with sp.stage(buffer_size=4):
                pass
    _assert_clean_context()


def test_error_task_in_two_stages():
    src = sp.source_random(DATA_LENGTH, dtype=sp.uint8)
    rly = sp.relayer(DATA_LENGTH, dtype=sp.uint8)
    with pytest.raises(sp.exceptions.RuntimeError, match="already in the stage 1"):
        with sp.pipeline():
            with sp.stage():
                data, *_ = src.generate()
            with sp.stage():
                data = rly.relay(data)
            with sp.stage():
                rly.relay(data)
    _assert_clean_context()


def test_error_backward_dependency():
    src = sp.source_random(DATA_LENGTH, dtype=sp.uint8)
    rlys = [sp.relayer(DATA_LENGTH, dtype=sp.uint8) for _ in range(2)]
    with pytest.raises(sp.exceptions.RuntimeError, match="of a later stage"):
        with sp.pipeline():
            with sp.stage():
                data, *_ = src.generate()
                rlys[0].relay["in"].bind(data)
            with sp.stage():
                rlys[1].relay(data)
            # stage 0 consumes the output of stage 1
            rlys[0].relay.bind(rlys[1].relay)
    _assert_clean_context()


def test_error_empty():
    with pytest.raises(sp.exceptions.RuntimeError, match="at least one"):
        with sp.pipeline():
            pass
    with pytest.raises(sp.exceptions.RuntimeError, match="does not contain any task"):
        with sp.pipeline():
            with sp.stage():
                pass
    _assert_clean_context()


def test_error_not_built():
    pip = sp.pipeline()
    with pytest.raises(sp.exceptions.RuntimeError, match="built at the end"):
        pip.exec()


def test_auto_exec_restored_after_error():
    sp.Task.call_auto_exec = True
    with pytest.raises(KeyError):
        with sp.pipeline():
            with sp.stage():
                raise KeyError("user error")
    _assert_clean_context(True)
