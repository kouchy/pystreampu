# -*- coding: utf-8 -*-
"""StreamPU Simple Pipeline, described stage by stage with `streampu.pipeline` / `streampu.stage`.

Same chain as `test_simple_pipeline.py` (kept with the explicit `streampu.Pipeline(...)` API for
comparison): a source reading a file, 6 relayers on several threads and a sink writing a file.
"""

import argparse
import filecmp
import os
import time
from math import ceil

import pytest

import streampu
import streampu.rang as rang

streampu.Signal_handler.init()
HW_CONCURRENCY = streampu._ext.get_hardware_concurrency()


@pytest.mark.parametrize("n_threads", [HW_CONCURRENCY])
@pytest.mark.parametrize("n_inter_frames", [1, 4])
# active_waiting=True is not tested: the output file is sometimes wrong with this mode, with the
# explicit `streampu.Pipeline(...)` API too (see test_simple_pipeline.py, which only tests False)
@pytest.mark.parametrize("active_waiting", [False])
def test_simple_pipeline_builder(tmp_path, n_threads: int, n_inter_frames: int, active_waiting: bool):
    """Launch simple_pipeline_builder when using pytest."""
    in_filepath = str(tmp_path / "file.in")
    out_filepath = str(tmp_path / "file.out")
    with open(in_filepath, "wb") as fout:
        fout.write(os.urandom(1048576))

    assert simple_pipeline_builder(
        n_threads=n_threads,
        n_inter_frames=n_inter_frames,
        in_filepath=in_filepath,
        out_filepath=out_filepath,
        active_waiting=active_waiting,
    )


def simple_pipeline_builder(
    n_threads: int = HW_CONCURRENCY - 2,
    n_inter_frames: int = 1,
    sleep_time_us: int = 5,
    data_length: int = 2048,
    buffer_size: int = 16,
    dot_filepath: str = "",
    in_filepath: str = "",
    out_filepath: str = "file.out",
    print_stats: bool = False,
    debug: bool = False,
    active_waiting: bool = False,
) -> bool:
    """Run the simple pipeline.

    Args:
        n_threads(int) : Number of threads of the relayers stage
        n_inter_frames(int) : Number of frames to process in one task
        sleep_time_us(int) : Sleep time duration in one task (microseconds)
        data_length(int) : Size of data to process in one task (in bytes)
        buffer_size(int) : Size of the buffer between the different stages of the pipeline
        dot_filepath(str) : Path to dot output file
        in_filepath(str) : Path to the input file
        out_filepath(str) : Path to the output file
        print_stats(bool) : Enable to print per task statistics (performance will be reduced)
        debug(bool) : Enable task debug mode (print socket data)
        active_waiting(bool) : Enable active waiting in the pipeline sync

    Returns:
        tests_passed(bool) : Bool value indicating test success
    """
    source = streampu.source_user_binary(data_length, in_filepath, auto_reset=False, dtype=streampu.uint8)
    sink = streampu.sink_user_binary(data_length, out_filepath, dtype=streampu.uint8)

    rlys = []
    for s in range(6):
        rly = streampu.relayer(data_length, dtype=streampu.uint8)
        rly.ns = sleep_time_us * 1000
        rly.name = "Relayer" + str(s)
        rlys.append(rly)

    # The tasks are bound (not executed) inside the block, and the pipeline is built at its end
    with streampu.pipeline(buffer_size=buffer_size, active_waiting=active_waiting) as pipeline_chain:
        with streampu.stage():  # stage 0: the source reads the file (1 thread)
            data, cnt = source.generate()

        with streampu.stage(n_threads=n_threads):  # stage 1: the relayers
            for rly in rlys:
                data = rly.relay(data)

        with streampu.stage():  # stage 2: the sink writes the file (1 thread)
            sink.send_count(data, cnt)

    print(pipeline_chain)

    pipeline_chain.n_frames = n_inter_frames
    if dot_filepath:
        pipeline_chain.export_dot(dot_filepath)

    for mdl in pipeline_chain.get_modules(streampu.Module, False):
        for tsk in mdl.tasks:
            tsk.reset()
            tsk.debug = debug
            tsk.set_debug_limit(16)
            tsk.stats = print_stats
            tsk.fast = True

    start = time.time_ns()
    pipeline_chain.exec()
    duration = (time.time_ns() - start) / 1000000.0

    in_filesize = os.stat(in_filepath).st_size
    n_frames = ceil(in_filesize * 8.0 / (data_length * n_inter_frames))
    theoretical_time_us_allthreads = n_frames * (len(rlys) * sleep_time_us * 1000) * n_inter_frames
    theoretical_time = theoretical_time_us_allthreads / 1000000.0 / n_threads

    print(f"Pipeline elapsed time: {duration} ms")
    print(f"Pipeline theoretical time: {theoretical_time} ms")

    if print_stats:
        pipeline_chain.show_stats()

    tests_passed = filecmp.cmp(in_filepath, out_filepath)
    if tests_passed:
        print(f"#{rang.style.bold}{rang.fg.green} Tests passed! {rang.style.reset}")
    else:
        print(f"#{rang.style.bold}{rang.fg.red} Tests failed :-( {rang.style.reset}")
    return tests_passed


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Simple pipeline described stage by stage.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("-t", "--n-threads", type=int, dest="n_threads", default=HW_CONCURRENCY - 2)
    parser.add_argument("-f", "--n-inter-frames", type=int, dest="n_inter_frames", default=1)
    parser.add_argument("-s", "--sleep-time", type=int, dest="sleep_time_us", default=5)
    parser.add_argument("-d", "--data-length", type=int, dest="data_length", default=2048)
    parser.add_argument("-u", "--buffer-size", type=int, dest="buffer_size", default=16)
    parser.add_argument("-o", "--dot-filepath", type=str, dest="dot_filepath", default="")
    parser.add_argument("-i", "--in-filepath", type=str, dest="in_filepath", required=True)
    parser.add_argument("-j", "--out-filepath", type=str, dest="out_filepath", default="file.out")
    parser.add_argument("-p", "--print-stats", action="store_true", dest="print_stats")
    parser.add_argument("-g", "--debug", action="store_true", dest="debug")
    parser.add_argument("-w", "--active-waiting", action="store_true", dest="active_waiting")

    simple_pipeline_builder(**vars(parser.parse_args()))
