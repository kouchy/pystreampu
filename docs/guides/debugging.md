# Debugging and stopping

This guide gathers the tools to follow what a sequence does, to understand the errors
raised by StreamPU, and to stop an execution.

## Printing the sockets

The `debug` property of a task prints its sockets at each execution (see
[First steps](../tutorial/first_steps.md#debug-mode-activation)). A few methods of the task
control what is printed:

| Method | Effect |
|--------|--------|
| `task.set_debug_limit(n)` | print at most `n` elements per socket |
| `task.set_debug_precision(n)` | print the floating-point values with `n` decimals |
| `task.set_debug_hex(True)` | print the integers in hexadecimal |
| `task.set_debug_frame_max(n)` | print at most `n` frames per socket |

```python
>>> import numpy as np
>>> x = spu.array(np.linspace(0, 1, 40, dtype=np.float32))
>>> y = x * 3
>>> y.task.debug = True
>>> y.task.set_debug_limit(4)
>>> y.task.set_debug_precision(2)
>>> y.task.exec()
# Binaryop<mul>::perform(const float32 in0[40], const float32 in1[1], float32 out[40])
# {IN}  in0 = [ 0.00,  0.03,  0.05,  0.08, ...]
# {IN}  in1 = [ 3.00]
# {OUT} out = [ 0.00,  0.08,  0.15,  0.23, ...]
# Returned status: [0 'SUCCESS']
#
```

To enable the debug mode on a whole sequence, loop over its tasks:

```python
for task in seq.get_tasks_per_threads()[0]:   # tasks of the thread 0
    task.debug = True
    task.set_debug_limit(8)
```

## Executing step by step

`seq.exec_step(tid)` executes **one task** of the thread `tid`, the next one in the order
of the sequence, and returns `True`. Once the last task has been executed, the next call
returns `False` (the execution of the sequence is complete), and the call after starts a
new execution:

```python
while seq.exec_step(0):     # one execution of the sequence, task by task
    pass
```

With the debug mode enabled, this shows the data after each task. For a sequence on
several threads, call it for each `tid`.

## Errors

The errors raised by StreamPU (wrong arguments, unbound sockets…) are exceptions of the
module `spu.exceptions`. Their message gives the C++ file, line and function that raised
it, followed by a stack trace:

```python
>>> try:
...     spu.incrementer(0)
... except spu.exceptions.InvalidArgument as e:
...     print(str(e).splitlines()[0])
In the '.../Incrementer.cpp' file at line 23 ('Incrementer' function): "'n_elmts' has to be greater than 0 ('n_elmts' = 0).":
```

| Exception | Raised when |
|-----------|-------------|
| `InvalidArgument` | an argument has a wrong value (size, data type…) |
| `RuntimeError` | an operation is not possible in the current state (unbound socket, wrong graph…) |
| `LengthError`, `OutOfRange`, `RangeError`, `DomainError` | a size or an index is out of its bounds |
| `ControlFlowError` | a [`Switcher`](control_flow.md) is not consistent: a `commute` without its `select`, or the two tasks in different pipeline stages |
| `LogicError` | an internal inconsistency |
| `CannotAllocate`, `OverflowError`, `UnderflowError` | a memory or arithmetic limit is reached |
| `UnimplementedError` | the feature is not implemented for these arguments |
| `ProcessingAborted`, `WaitingCanceled` | a task stopped the processing, or a waiting task was canceled (used internally to stop pipelines) |
| `JuliaError` | an error in a Julia codelet (see [Writing a module in Julia](julia_module.md#errors)) |

!!! warning
    These exceptions derive from `Exception` only: `spu.exceptions.RuntimeError` is not
    the Python `RuntimeError`, and `spu.exceptions.InvalidArgument` is not a `ValueError`.
    Catch them by their class in `spu.exceptions`.

An exception raised by a Python codelet (`ValueError`…) goes through StreamPU unchanged,
whether the task is called directly or executed by a sequence.

## Stopping an execution

| Call | Stops |
|------|-------|
| `seq.exec_n_times(n)` | after `n` executions in total, shared between the threads |
| `seq.exec_n_times(n, per_thread=True)` | after `n / n_threads` executions on each thread |
| `seq.exec()`, `pipeline.exec()` | when a module is done (`is_done()`), for instance a source that reached the end of its file (`auto_reset=False`), or on `Ctrl+C` |

`seq.exec()` has no other stop condition: with a source that never ends, only `Ctrl+C`
stops it. Call `spu.Signal_handler.init()` at the beginning of the program, so that a
first `Ctrl+C` stops the running sequence or pipeline cleanly (a second one kills the
program):

```python
spu.Signal_handler.init()
seq.exec()                        # runs until the end of the file, or Ctrl+C
if spu.Signal_handler.is_sigint():
    print("interrupted")
    spu.Signal_handler.reset_sigint()
```

A pipeline stops by itself when one of its modules is done. Set
`pipeline.auto_stop = False` to keep it running until `Ctrl+C`.
