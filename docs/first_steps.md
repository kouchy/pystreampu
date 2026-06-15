# First steps
This section presents the first steps for playing with [StreamPU](https://aff3ct.github.io/streampu) in Python.
It covers the following key concepts of [StreamPU](https://aff3ct.github.io/streampu):
- module
- task
- socket

At the end of this section, you should be able to :
- Create a module
- Get information about the task of a module
- Bind two sockets
- Execute a task of a module
- Read the values of a socket
- Activate the debug mode of a task

## Import StreamPU

As every Python package `StreamPU`is imported using the `import` interface.

```python
import streampu as spu
```

Output:

```text
No output.
```

## Build a module
Basically, a `module` is a device that can process data.
A data processing is called a `task` in the StreamPU DSEL language.
Modules can store several tasks as well as shared data for the different tasks or for different executions of the same tasks.
Tasks exchange data through `sockets`.

For example suppose that we want to randomly generate `8` bits from a Bernoulli distribution.

```python
src = spu.source_random(8, dtype = spu.int64)
```

Output:

```text
No output.
```

If you want to have some information about the tasks of `src` you can use `help`or `spu.help`.

```python
spu.help(src)
```

Output:

```text
# module:
# |- name: Source_random
# |- short name: Source
# |- n_frames: 1
# |- tasks:
# |  |- name: generate
# |  |  |- sockets out:
# |  |  |  |- out_data: { n_elts = 8, datatype = int64 }
# |  |  |  |- out_count: { n_elts = 1, datatype = uint32 }
# |  |  |  |- status: { n_elts = 1, datatype = int32 }
```

In this log, we see that `src` has one `task` named `generate` that has 3 outputs: 
- `out_data`: 8 elements of type `int64`
- `out_count`: 1 element of type `uint32`
- `status`: 1 element of type `int32`

We will access the task `tsk`of a module `mdl` using the syntax `mdl['tsk']`.
Similarly, the socket `sck`of the task `tsk` of a module `mdl` can be accessed using `mdl['tsk::sck']`

## Execute a Task

To fill these sockets, let us execute the task `generate` of `src`.

```python
src['generate'].exec()
```

Output:

```text
No output.
```

The generated bits, contained in the socket `out_data` can be read.

```python
print(src['generate::out_data'])
```

Output:

```text
[[0 1 1 0 1 1 1 1]]
```

## Second module building

We now want to incerement the bits of `out_data`. To do so, we start by building an `incrementer` (which is a also a `module`).

```python
inc = spu.incrementer(8, dtype=spu.int64)
```

Output:

```text
No output.
```

When asking for more details about `inc` we can see that it has two tasks named `increment` and `incrementf`.
We will use `increment`.
The task `increment` has one input socket called `in`.

```python
spu.help(inc)
```

Output:

```text
# module:
# |- name: Incrementer
# |- short name: Incrementer
# |- n_frames: 1
# |- tasks:
# |  |- name: increment
# |  |  |- sockets in:
# |  |  |  |- in: { n_elts = 8, datatype = int64 }
# |  |  |- sockets out:
# |  |  |  |- out: { n_elts = 8, datatype = int64 }
# |  |  |  |- status: { n_elts = 1, datatype = int32 }
# |  |- name: incrementf
# |  |  |- sockets in:
# |  |  |  |- fwd: { n_elts = 8, datatype = int64 }
# |  |  |- sockets out:
# |  |  |  |- status: { n_elts = 1, datatype = int32 }
```

## Module binding 

To link the source `src` and the incrementer `inc`, the output socket `out_data` of the task `generate` of the module `src` should be "bound" to the input socket `in` of the task `increment` of the module `inc`.

```python
inc['increment::in'] = src['generate::out_data']
```

Output:

```text
No output.
```

This line is schematically equivalent to the following figure.

<img src="/assets/src_inc_binding.svg" width = "250"/>

## Tasks execution

Now we can execute the tasks of each module.

```python
src['generate'].exec()
inc['increment'].exec()

print("Output of source:", src['generate::out_data'])
print("Output of incrementer:", inc['increment::out'])
```

Output:

```text
Output of source: [[1 1 1 0 0 1 0 0]]
Output of incrementer: [[2 2 2 1 1 2 1 1]]
```

## Debug mode activation

You can see that the data is automatically transfered from the output of `generate` to the input of `increment`. 
The data printing can also be handled automatically by setting the `debug` property of the tasks to `true`.

```python
src['generate'].debug = True
inc['increment'].debug = True
src['generate'].exec()
inc['increment'].exec()
```

Output:

```text
# [1m[32mSource_random[0m::[1m[35mgenerate[0m([1m[34mint64[0m out_data[8], [1m[34muint32[0m out_count[1])
# {OUT} out_data  = [    0,     0,     0,     1,     0,     1,     1,     0]
# {OUT} out_count = [    8]
# Returned status: [0 'SUCCESS']
#
# [1m[32mIncrementer[0m::[1m[35mincrement[0m([1m[34mconst int64[0m in[8], [1m[34mint64[0m out[8])
# {IN}  in  = [    0,     0,     0,     1,     0,     1,     1,     0]
# {OUT} out = [    1,     1,     1,     2,     1,     2,     2,     1]
# Returned status: [0 'SUCCESS']
#
```
