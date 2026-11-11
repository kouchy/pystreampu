# Real-time statistics

The [statistics per task](profiling.md#statistics-per-task) give the average time spent
in each task. A real-time application also needs the **distribution** of the latency of
each frame: its median, but also its rare worst cases (jitter). Sequences and pipelines
can record this distribution in an HDR histogram, with a very low overhead.

## Latency of a sequence

Enable the collection with `set_rt_stats(True)` **before** the execution, then display
the result with `show_rt_stats()`:

```python
import streampu as spu

ini = spu.initializer(256, dtype=spu.int32)
incs = [spu.incrementer(256, ns=2000, dtype=spu.int32) for _ in range(3)]
fin = spu.finalizer(256, dtype=spu.int32)
with spu.sequence() as seq:
    x = ini.initialize()
    for inc in incs:
        x = inc.increment(x)
    fin.finalize(x)

seq.set_rt_stats(True, n_skip_frames=10)   # ignore the first 10 executions (warm-up)
seq.exec_n_times(1000)
seq.show_rt_stats()
```

The table ends with the statistics of the whole sequence (columns shortened here):

```text
#        MODULE NAME |       TASK NAME ||    CALLS ||  AVERAGE |  STD DEV |  MINIMUM |      P50 |      P99 |   P99.99 |  MAXIMUM ||  AVERAGE |   1% LOW | ...
#                    |                 ||          ||     (us) |     (us) |     (us) |     (us) |     (us) |     (us) |     (us) || (strm/s) | (strm/s) | ...
# -------------------|-----------------||----------||----------|----------|----------|----------|----------|----------|----------||----------|----------|
#           SEQUENCE |     * (5 tasks) ||      990 ||     6.37 | 1.84e-01 |     6.31 |     6.38 |     6.42 |    12.13 |    12.13 || 1.57e+05 | 1.56e+05 | ...
```

- the **latency** columns give the duration of one execution of the whole sequence:
  average, standard deviation, minimum, percentiles (P50: median; P99: 1 execution out of
  100 is slower…) and maximum;
- the **throughput** columns give the number of executions per second (`strm/s`): its
  average, and its "lows", the throughput during the slowest 1 %, 0.1 % and 0.01 % of
  the executions. `show_rt_stats(display_in_frames=True)` gives it in frames per second
  (with [`n_frames`](../tutorial/sequence.md#process-several-frames-at-once) frames per
  execution).

Here, the three incrementers sleep 2 µs each: one execution takes 6.4 µs, and the worst
one 12 µs.

The same values are available as a dictionary, to be stored or plotted:

```python
stats = seq.get_rt_stats()
print(stats["n_calls"], stats["p50_ns"], stats["p99_ns"])   # 990 6384.06 6448.06
```

Its keys are `n_calls`, `n_tasks`, `avg_ns`, `std_ns`, `min_ns`, `p10_ns`, `p25_ns`,
`p50_ns`, `p75_ns`, `p90_ns`, `p99_ns`, `p999_ns`, `p9999_ns` and `max_ns` (durations in
nanoseconds). `seq.reset_rt_stats()` clears the histogram, and `seq.set_rt_stats(False)`
stops the collection.

!!! note
    With several threads, each thread records its own executions, and the statistics
    merge all of them.

## Latency of a pipeline

The examples of this section use `pip`, the pipeline of
[Running in parallel](../tutorial/parallelism.md#describe-the-pipeline-stage-by-stage)
(a source reading a file, six relayers on 4 threads and a sink, with buffers of 16
frames). On a pipeline, `show_rt_stats()` prints two tables:

- one line **per stage**: the time spent by a stage to process a frame, without the time
  spent waiting for the buffers;
- one line **`PIPELINE E2E`** (end to end): the time between the start of the first stage
  and the end of the last stage for the same frame, buffers included. This is the latency
  seen by the user of the application.

```python
pip.set_rt_stats(True, n_skip_frames=10)
pip.exec()
pip.show_rt_stats()
```

```text
#       STAGE 0 (1t) |       * (2 tasks) ||      790 || 5.68e-01 |     1.02 | ...
#       STAGE 1 (4t) |       * (8 tasks) ||      760 ||    31.75 |     2.06 | ...
#       STAGE 2 (1t) |       * (2 tasks) ||      790 ||     3.36 |     2.16 | ...
# ...
#       PIPELINE E2E |        end-to-end ||      790 ||   583.44 |    82.38 | ...
```

Here, a frame needs about 36 µs of processing (0.6 + 31.8 + 3.4 µs), but spends 580 µs
on average in the pipeline: the source fills the buffers much faster than the relayers
empty them, so most of this time is spent waiting in the buffers.

`pip.get_rt_stats()` returns the same values: `stages` (one dictionary per stage, with the
keys of a sequence), the `e2e_*_ns` keys for the end-to-end latency, and
`out_ns_per_stream`, the average time between two frames at the output.

## Emulating a source with a fixed rate

In a real application, the frames often arrive at a fixed rate (a sensor, a radio…),
not as fast as the first stage can produce them. `set_rt_pacing(period_ns)` makes the
first stage of a pipeline start a new frame every `period_ns` nanoseconds, and measures
the end-to-end latency from this nominal arrival time:

```python
pip.set_rt_stats(True)
pip.set_rt_pacing(50_000)       # one frame every 50 µs (20,000 frames per second)
pip.exec()
stats = pip.get_rt_stats()
print(stats["out_ns_per_stream"], stats["e2e_avg_ns"])   # about 50,000 and 48,000
```

The pacing is only applied while the real-time statistics are enabled. `set_rt_pacing(0)`
disables it, and `get_rt_pacing()` returns the current period.

With a frame every 50 µs, the pipeline keeps up: the buffers stay almost empty, and the
end-to-end latency drops from 580 µs to 48 µs. Increasing the rate until the latency
grows shows the maximum rate that the pipeline can sustain.

## Benchmarking in one call

`measure_bench` runs some warm-up executions, then measures a given number of
executions, and returns the statistics as a dictionary:

```python
res = seq.measure_bench(10_000)                 # sequence: n_warmup=256 by default
print(res["ns_per_frame"], res["p99_ns_per_frame"])

res = pip.measure_bench(10_000, n_warmup=100)   # pipeline
print(res["e2e_p50_ns"], res["out_ns_per_stream"])
```

For a sequence, the dictionary gives the time per frame (`ns_per_frame`, its percentiles
`p50_ns_per_frame`… `max_ns_per_frame`) and per task (`ns_per_task`). For a pipeline, it
gives the time per task of the stages (`stage_*_ns_per_task`), the end-to-end latency
(`e2e_*_ns`) and the output period (`out_ns_per_stream`).
