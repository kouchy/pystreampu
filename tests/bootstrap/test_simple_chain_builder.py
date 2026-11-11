# -*- coding: utf-8 -*-
"""StreamPU Simple chain, described in a `with streampu.sequence()` block.

Same chain as `test_simple_chain.py` (kept with the explicit `streampu.Sequence(...)` API for
comparison): an initializer, 6 incrementers and a finalizer, on several threads.
"""

import argparse
import time

import pytest

import streampu

streampu.Signal_handler.init()
HW_CONCURRENCY = streampu._ext.get_hardware_concurrency()


@pytest.mark.parametrize("set_flag", [False, True])
@pytest.mark.parametrize("step_by_step", [False, True])
@pytest.mark.parametrize("copy_mode", [False, True])
@pytest.mark.parametrize("n_inter_frames", [1, 4])
@pytest.mark.parametrize("n_threads", [HW_CONCURRENCY])
def test_simple_chain_builder(n_threads: int, n_inter_frames: int, copy_mode: bool, step_by_step: bool, set_flag: bool):
    """Launch simple_chain_builder when using pytest."""
    assert simple_chain_builder(
        n_threads=n_threads,
        n_inter_frames=n_inter_frames,
        n_exec=100,
        copy_mode=copy_mode,
        step_by_step=step_by_step,
        set_flag=set_flag,
    )


def simple_chain_builder(
    n_threads: int = HW_CONCURRENCY,
    n_inter_frames: int = 1,
    sleep_time_us: int = 5,
    data_length: int = 2048,
    n_exec: int = 100,
    dot_filepath: str = "",
    copy_mode: bool = False,
    print_stats: bool = False,
    step_by_step: bool = False,
    debug: bool = False,
    set_flag: bool = False,
) -> bool:
    """Run the simple chain.

    Args:
        n_threads (int): number of threads to run in parallel
        n_inter_frames (int): number of frames to process in one task
        sleep_time_us (int): sleep time duration in one task (microseconds)
        data_length (int): size of data to process in one task (in bytes)
        n_exec (int): number of sequence executions
        dot_filepath (str): path to dot output file
        copy_mode (bool): enable to copy data in sequence (performance will be reduced)
        print_stats (bool): enable to print per task statistics (performance will be reduced)
        step_by_step (bool): enable step-by-step sequence execution (performance will be reduced)
        debug (bool): Enable task debug mode (print socket data)
        set_flag (bool): put the incrementers in a `Set` (a sub-sequence)

    Returns:
        out (bool): Test status
    """
    initializer = streampu.initializer(data_length, dtype=streampu.uint8)
    finalizer = streampu.finalizer(data_length, dtype=streampu.uint8)

    incs = []
    for s in range(6):
        inc = streampu.incrementer(data_length, dtype=streampu.uint8)
        inc.ns = sleep_time_us * 1000
        inc.name = "Inc" + str(s)
        incs.append(inc)

    # The tasks are bound (not executed) inside the blocks, and the sequences are built at their end
    if not set_flag:
        with streampu.sequence(n_threads=n_threads) as sequence_chain:
            y = initializer.initialize()
            for inc in incs:
                y = inc.increment(y)
            finalizer.finalize(y)
    else:
        with streampu.sequence() as partial_sequence:  # the sub-sequence of the Set
            y = incs[0].increment()
            for inc in incs[1:]:
                y = inc.increment(y)
        theset = streampu.Set(partial_sequence.sequence)
        with streampu.sequence(n_threads=n_threads) as sequence_chain:
            finalizer.finalize(theset.exec(initializer.initialize()))

    print(sequence_chain)

    sequence_chain.n_frames = n_inter_frames
    sequence_chain.no_copy_mode = not copy_mode

    if dot_filepath:
        sequence_chain.export_dot(dot_filepath)

    for mdl in sequence_chain.get_modules(streampu.Module, False):
        for tsk in mdl.tasks:
            tsk.reset()
            tsk.debug = debug
            tsk.set_debug_limit(16)
            tsk.stats = print_stats
            tsk.fast = True

    for tid, cur_initializer in enumerate(sequence_chain.get_cloned_modules(initializer)):
        for f in range(n_inter_frames):
            cur_initializer.data_init[f][:] = tid * n_inter_frames + f

    start = time.time_ns()
    if not step_by_step:
        sequence_chain.exec_n_times(n_exec)
    else:
        counter = 0
        while counter < n_exec / n_threads:
            for tid in range(n_threads):
                while sequence_chain.exec_step(tid):
                    pass
            counter += 1
    duration = (time.time_ns() - start) / 1000000.0
    print(f"Sequence elapsed time: {duration} ms")

    tests_passed = True
    for tid, cur_finalizer in enumerate(sequence_chain.get_cloned_modules(finalizer)):
        for f in range(n_inter_frames):
            final_data = cur_finalizer.final_data[f]
            expected = (len(incs) + tid * n_inter_frames + f) % 256
            for d in range(len(final_data)):
                if final_data[d] != expected:
                    print(f"# expected = {expected} - obtained = {final_data[d]} (d = {d}, tid = {tid})")
                    tests_passed = False
    if print_stats:
        sequence_chain.show_stats(True, False)

    if tests_passed:
        print(f"#{streampu.rang.style.bold}{streampu.rang.fg.green} Tests passed! {streampu.rang.style.reset}")
    else:
        print(f"#{streampu.rang.style.bold}{streampu.rang.fg.red} Tests failed :-( {streampu.rang.style.reset}")
    return tests_passed


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Simple chain described in a 'with streampu.sequence()' block.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("-t", "--n-threads", type=int, dest="n_threads", default=HW_CONCURRENCY)
    parser.add_argument("-f", "--n-inter-frames", type=int, dest="n_inter_frames", default=1)
    parser.add_argument("-s", "--sleep-time", type=int, dest="sleep_time_us", default=5)
    parser.add_argument("-d", "--data-length", type=int, dest="data_length", default=2048)
    parser.add_argument("-e", "--n-exec", type=int, dest="n_exec", default=100000)
    parser.add_argument("-o", "--dot-filepath", type=str, dest="dot_filepath", default="")
    parser.add_argument("-c", "--copy-mode", action="store_true", dest="copy_mode")
    parser.add_argument("-p", "--print-stats", action="store_true", dest="print_stats")
    parser.add_argument("-b", "--step-by-step", action="store_true", dest="step_by_step")
    parser.add_argument("-g", "--debug", action="store_true", dest="debug")
    parser.add_argument("-l", "--set-flag", action="store_true", dest="set_flag")

    simple_chain_builder(**vars(parser.parse_args()))
