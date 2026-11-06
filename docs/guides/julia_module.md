# Writing a module in Julia

The codelets of a module can be written in [Julia](https://julialang.org/). A Julia module
is used like any other module: its tasks are executed immediately, or chained with Python
and C++ modules in a `Sequence` or a `Pipeline`, where StreamPU runs it on several threads.
The data of the sockets are shared with Julia without copy.

!!! warning "pyStreamPU compiled with Julia"
    The Julia modules are not in the packages of PyPI: pyStreamPU must be compiled with
    Julia (>= 1.10.9) installed, see [Julia modules](../install.md#julia-modules) in the
    installation page. `spu.julia.available()` tells whether the installed package has them.

The complete example of this page is in
[`examples/custom_julia_module`](https://github.com/rtajan/pystreampu/tree/develop/examples/custom_julia_module).

## A module without state

`spu.Stateless_Julia` is the Julia counterpart of `spu.Stateless`: create the tasks and
their sockets, then give the Julia code of each codelet.

```python
import numpy as np
import streampu as spu

inc = spu.Stateless_Julia()
t = inc.create_task("increment")
inc.create_socket_in(t, "in", 8, spu.int32)
inc.create_socket_out(t, "out", 8, spu.int32)
inc.create_constant(t, 3, spu.int32)
inc.create_codelet(t, """
function increment(sck_in, sck_out, step, rnt_frame_id, rnt_n_frames_per_wave)
    @inbounds for i in eachindex(sck_in)
        sck_out[i] = sck_in[i] + step
    end
    return 0
end
""")

y = inc.increment(spu.array(np.arange(8, dtype=np.int32)))
print(y.numpy)  # [[ 3  4  5  6  7  8  9 10]]
```

Julia is started when the first Julia module is created, and the Julia code of a module is
evaluated at its first execution (by a `Sequence` or a `Pipeline`, once per thread).

### Arguments of a codelet

A codelet is a Julia function named after its task (or the `function_name` given to
`create_codelet`). It is called with, in this order:

| Arguments | Julia type | Content |
|---|---|---|
| states (`Stateful_Julia` only) | the types of the states | in their creation order, see below |
| sockets | `Vector{T}` | the sockets of the task, in their creation order: 1D vectors of `n_elmts × n_frames_per_wave` elements, without copy |
| constants | see below | the constants of the task, in their creation order |
| `rnt_frame_id` | `UInt32` | index of the first frame of the call |
| `rnt_n_frames_per_wave` | `UInt32` | number of frames of the call |

It returns `0` on success. The outputs are written in place (`sck_out[i] = ...`,
`sck_out .= ...`). The element type `T` of a socket follows its `dtype`: `spu.int32`
gives `Int32`, `spu.float64` gives `Float64`, and so on.

### Constants

`create_constant(task, value, dtype=None)` adds a scalar argument after the sockets. It
must be called before `create_codelet`.

| `value` | `dtype` | Julia type |
|---|---|---|
| any | `spu.int8` … `spu.uint64`, `spu.float32`, `spu.float64` | `Int8` … `UInt64`, `Float32`, `Float64` |
| `bool` | `None` | `Bool` |
| `int` | `None` | `Int64` |
| `float` | `None` | `Float64` |
| NumPy scalar (`np.float32(1.5)`) | `None` | its type (`Float32`) |

### Where the code comes from

- `create_codelet(task, code)`: the Julia code that defines the function;
- `create_codelet_file(task, path)`: a `.jl` file that defines it;
- `create_codelet(task)`: the function is already defined, for instance by
  `spu.julia.eval(code)` or `spu.julia.eval_file(path)`.

All the Julia code is evaluated in the `Main` module of Julia, shared by all the modules:
two codelets cannot have the same name with different definitions.

## A module with states

`spu.Stateful_Julia` adds states: Julia objects passed to all the codelets of the module,
before the sockets.

```python
acc = spu.Stateful_Julia()
acc.create_state("Accumulator(0)", code="""
mutable struct Accumulator
    total::Int64
end
""")
acc.create_state("Gain(Int32(10))", shared=True, code="""
struct Gain
    factor::Int32
end
""")
t = acc.create_task("accumulate")
acc.create_socket_in(t, "in", 8, spu.int32)
acc.create_socket_out(t, "out", 8, spu.int32)
acc.create_codelet(t, """
function accumulate(acc::Accumulator, gain::Gain, sck_in, sck_out, rnt_frame_id, rnt_n_frames_per_wave)
    @inbounds for i in eachindex(sck_in)
        acc.total += sck_in[i]
        sck_out[i] = sck_in[i] * gain.factor
    end
    return 0
end
""")
```

- `create_state(constructor, shared=False, code="")`: `constructor` is the Julia
  expression that builds the state; `code` defines its type. The type is defined at once,
  so that the codelets can use it in their arguments (`acc::Accumulator`).
  `create_state_file(constructor, path, shared=False)` takes the type from a file.
- When a `Sequence` or a `Pipeline` clones the module for its threads, each clone gets a
  `deepcopy` of a state (`shared=False`: no lock needed), or the same object
  (`shared=True`: for large or read-only data).
- `get_states()` returns the states as text (`repr` of Julia), for instance to inspect the
  clones of a sequence:

```python
z = acc.accumulate(inc.increment(x))
seq = spu.Sequence(z, 4)
seq.exec_n_times(1000)
for clone in seq.get_cloned_modules(acc):
    print(clone.get_states())  # ['Accumulator(…)', 'Gain(10)']
```

## Julia, Python and C++ in the same graph

Julia modules can be chained with Python and C++ modules, in a `Sequence` or a `Pipeline`.
StreamPU runs the threads (or the stages of a pipeline) that contain Julia modules with
threads adopted by Julia; pyStreamPU makes the Python codelets of these threads release
Julia's garbage collector while they wait for the GIL, so that they do not block it.

For the best performance:

- avoid allocating memory in the codelets (pre-allocate it in a state with
  `shared=False`): the garbage collector of Julia stops all the Julia threads;
- do not use `Threads.@threads` or Julia tasks (`@spawn`, `println`...) in the codelets:
  StreamPU handles the threads;
- the first execution of a codelet compiles it: run a first execution before measuring
  times.

## Errors

By default (`jl_safe=True`), a Julia exception in a codelet is raised in Python as a
`spu.exceptions.RuntimeError` that contains the Julia message and stack trace; so is an
error in the code given to `spu.julia.eval`, `create_state` or `create_state_file`.
`Stateless_Julia(jl_safe=False)` (or `mdl.jl_safe = False`) calls the codelets directly,
which is faster once they are debugged.

## Limitations

- Julia is started in the thread that creates the first Julia module: create it from the
  main thread of Python.
- Julia is not stopped when Python exits (its exit hooks do not run).
- Python 3.14t (without GIL) with Julia has not been tested yet.
