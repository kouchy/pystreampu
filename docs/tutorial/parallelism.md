# Running in parallel

StreamPU extracts two kinds of parallelism from a streaming application
([Cassagne et al., 2023](https://doi.org/10.1002/cpe.7820)):

- **spatial parallelism**: the whole sequence is duplicated on several threads, each
  thread processing its own frames;
- **temporal parallelism**: the graph is split into a **pipeline** of stages that run
  concurrently, like an assembly line.

Both are available from Python. The execution itself happens in C++ and the Python GIL
is released while a sequence or a pipeline runs.

## Duplicating a sequence on several threads

### Describe the graph

We build a chain of six incrementers between an `initializer` (which outputs constant
data) and a `finalizer` (which keeps the last data it received). Each incrementer
sleeps 5 µs per execution (`ns=5000`) to simulate some work.

```python
import time
import streampu as spu

data_length = 2048
n_threads = 4

initializer = spu.initializer(data_length, dtype=spu.uint8)
incs = [spu.incrementer(data_length, ns=5000, dtype=spu.uint8) for _ in range(6)]
finalizer = spu.finalizer(data_length, dtype=spu.uint8)

x = initializer.initialize()
y = x
for inc in incs:
    y = inc.increment(y)
finalizer.finalize(y)
```

### Build a multithreaded sequence

The second argument of `spu.Sequence` is the number of threads:

```python
seq = spu.Sequence(x.task, n_threads)
```

When `n_threads > 1`, StreamPU **clones** every module of the graph so that each thread
works on its own copy. All the built-in modules used here can be cloned, as well as the
[`Stateless` modules written in Python](../guides/python_module.md).

!!! warning
    Some modules cannot be cloned, typically sources and sinks that read or write a
    file (`source_user_binary`, `sink_user_binary`…). They cannot be part of a
    multithreaded sequence: use a [pipeline](#splitting-the-graph-into-a-pipeline)
    to keep them on a single thread.

### Work with the clones

The modules you created are the ones of the first thread. To reach the copies used by
every thread, use `get_cloned_modules`. Here, each thread gets different initial data:

```python
for tid, ini in enumerate(seq.get_cloned_modules(initializer)):
    ini.data_init[0][:] = tid   # first (and only) frame of this thread
```

Then run the sequence and measure its duration:

```python
start = time.perf_counter()
seq.exec_n_times(1000)
print(f"Elapsed: {time.perf_counter() - start:.3f} s")

for tid, fin in enumerate(seq.get_cloned_modules(finalizer)):
    print(tid, fin.final_data[0][:4])   # each thread outputs tid + 6
```

The chain sleeps 6 × 5 µs per execution, so 1000 executions take about 30 ms on one
thread. With 4 threads, it ideally drops to 30 / 4 ≈ 7.5 ms. Try
different values of `n_threads` to see how the duration evolves on your machine
(`spu._ext.get_hardware_concurrency()` gives the number of hardware threads).

### Useful options

| Option | Effect |
|--------|--------|
| `seq.n_frames = 4` | each execution processes 4 frames per thread |
| `seq.no_copy_mode = True` | avoid data copies between tasks when possible |
| `spu.Sequence(..., thread_pinning=True)` | pin each thread to a core |

## Splitting the graph into a pipeline

A pipeline cuts the graph into **stages**. Each stage is a sequence running on its own
thread(s), and consecutive stages exchange frames through synchronization buffers. This
is the way to combine non-clonable modules (sources, sinks…) with a multithreaded
processing.

### Describe the graph

This time the data is read from a file by `source_user_binary`, goes through six
`relayer` modules (which copy their input to their output after a short sleep), and is
written to another file by `sink_user_binary`.

```python
import os
import streampu as spu

spu.Signal_handler.init()

data_length = 2048
n_threads = 4

with open("file.in", "wb") as f:          # some data to process
    f.write(os.urandom(data_length * 100))

source = spu.source_user_binary(data_length, "file.in", auto_reset=False, dtype=spu.uint8)
sink = spu.sink_user_binary(data_length, "file.out", dtype=spu.uint8)
rlys = [spu.relayer(data_length, ns=5000, dtype=spu.uint8) for _ in range(6)]

spu.Task.call_auto_exec = False   # describe the graph without executing it
data, count = source.generate()
for rly in rlys:
    data = rly.relay(data)
sink.send_count(data, count)
spu.Task.call_auto_exec = True
```

!!! note
    Here, the automatic execution of the tasks is disabled while the graph is described.
    Otherwise, calling `source.generate()` would already consume the first frame of the
    file.

### Build and run the pipeline

```python
pipeline = spu.Pipeline(
    [source.generate],    # first tasks of the graph
    [sink.send_count],    # last tasks of the graph
    [                     # stages: [first tasks, last tasks, excluded tasks]
        [[source.generate], [source.generate], []],
        [[rlys[0].relay], [rlys[-1].relay], []],
        [[sink.send_count], [sink.send_count], []],
    ],
    [1, n_threads, 1],    # number of threads per stage
    [16, 16],             # size of the buffers between consecutive stages
    [False, False],       # active waiting between stages
)
pipeline.exec()
```

The pipeline has three stages: the source on one thread, the six relayers duplicated on
`n_threads` threads, and the sink on one thread. `pipeline.exec()` returns when the
source reaches the end of the file (`auto_reset=False`). The output file is then
identical to the input file.

Like a sequence, a pipeline offers `n_frames`, `export_dot(...)`, `show_stats()` and
`get_modules(...)`. Its `stages` property gives access to the sequence of each stage.

## Python modules and the GIL

The built-in modules are written in C++ and run in parallel without any restriction.
Modules written in Python (see [Writing a module in Python](../guides/python_module.md))
execute Python code in each thread: with a regular Python interpreter, the GIL lets only
one of them run at a time. With a free-threaded Python (3.14t, run with `PYTHON_GIL=0`),
they can run truly in parallel. The example `examples/custom_python_module` compares
these configurations.
