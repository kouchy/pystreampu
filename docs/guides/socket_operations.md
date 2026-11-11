# Working with sockets

Sockets can be combined with the usual Python operators. Each operation creates a
small StreamPU module (adder, comparator, reducer…), binds it to its operands and
executes it. The result is a new socket that can be used in turn, so that a whole
computation can be written as plain Python expressions and then replayed by a
[Sequence](../tutorial/sequence.md).

```python
>>> import streampu as spu
```

## Create sockets

| Function | Result |
|----------|--------|
| `spu.array(data, dtype=None)` | socket holding `data` (list, scalar or NumPy array) |
| `spu.zeros(n, dtype=spu.float32)` | `n` zeros |
| `spu.ones(n, dtype=spu.float32)` | `n` ones |
| `spu.arange(start, stop, step=1, dtype=spu.float32)` | evenly spaced values, like `np.arange` |

```python
>>> spu.array([1, 2, 3])
socket([[1 2 3]], dtype=int64, name=data, task=Array.read)
>>> spu.array([1, 2, 3], dtype=spu.float32)
socket([[1. 2. 3.]], dtype=float32, name=data, task=Array.read)
```

All these functions also accept an `n_frames` argument to replicate the data on
several frames.

!!! note
    The available data types are `spu.int8`, `spu.int16`, `spu.int32`, `spu.int64`,
    `spu.uint8`, `spu.uint16`, `spu.uint32`, `spu.uint64`, `spu.float32` and
    `spu.float64`. Without `dtype`, `spu.array` keeps the NumPy type of the data.

!!! warning
    `spu.array` is designed for 1D data. A 2D list is interpreted as one row per frame.

## Arithmetic operators

`+`, `-`, `*` and `/` work between two sockets of the same size, or between a socket
and a scalar, on either side:

```python
>>> x = spu.array([1, 2, 3])
>>> (x + 1).numpy
array([[2, 3, 4]], dtype=int64)
>>> (10 - x).numpy
array([[9, 8, 7]], dtype=int64)
>>> (x * x).numpy
array([[1, 4, 9]], dtype=int64)
```

The result has the data type of the first socket, and the other operand is converted
to this type. As a consequence, **dividing integer sockets performs an integer
division**:

```python
>>> x = spu.array([12, 7], dtype=spu.int32)
>>> (x / 2).numpy
array([[6, 3]], dtype=int32)
>>> (x.astype(spu.float32) / 2).numpy
array([[6. , 3.5]], dtype=float32)
```

Each operator also exists as a function, which accepts an `output_dtype` argument:
`spu.add`, `spu.sub`, `spu.mul` and `spu.div`.

## In-place operators

`+=`, `-=`, `*=`, `/=`, `&=`, `|=` and `^=` modify the data of the socket itself
instead of creating a new socket:

```python
>>> x = spu.array([1, 2, 3])
>>> x += 1
>>> x *= 2
>>> x.numpy
array([[4, 6, 8]], dtype=int64)
```

!!! warning
    In-place operations are replayed by a sequence on data that has already been
    modified. See [A sequence replays the graph](../tutorial/sequence.md#a-sequence-replays-the-graph).

## Comparisons

`==`, `!=`, `<`, `<=`, `>` and `>=` return a socket of `0` and `1`, with the data type
of the first operand:

```python
>>> x = spu.array([1, 2, 3])
>>> (x > 1).numpy
array([[0, 1, 1]], dtype=int64)
>>> (x == 2).numpy
array([[0, 1, 0]], dtype=int64)
```

Function forms: `spu.equal`, `spu.not_equal`, `spu.less`, `spu.less_equal`,
`spu.greater`, `spu.greater_equal`.

## Bitwise operators

`&`, `|`, `^` and `~` work on integer sockets (functions `spu.bitwise_and`,
`spu.bitwise_or`, `spu.bitwise_xor` and `spu.bitwise_not`):

```python
>>> x = spu.array([12], dtype=spu.int32)
>>> (~x).numpy
array([[-13]], dtype=int32)
```

## Unary operations

| Operation | Function |
|-----------|----------|
| `-x` | `spu.neg(x)` |
| `abs(x)` | `spu.abs(x)` |
| `~x` | `spu.bitwise_not(x)` |
| `x.astype(dtype)` | `spu.cast(x, dtype)` |

```python
>>> x = spu.array([12], dtype=spu.int32)
>>> (-x).numpy
array([[-12]], dtype=int32)
>>> x.astype(spu.float32).numpy
array([[12.]], dtype=float32)
```

## Reductions, minimum and maximum

`spu.sum`, `spu.prod`, `spu.min`, `spu.max`, `spu.all` and `spu.any` reduce a socket
to a single value:

```python
>>> x = spu.array([3, 1, 4, 1, 5])
>>> spu.sum(x).numpy
array([[14]], dtype=int64)
>>> spu.max(x).numpy
array([[5]], dtype=int64)
```

Given several sockets, `spu.min` and `spu.max` compute the element-wise minimum or
maximum:

```python
>>> y = spu.array([2, 7, 1, 8, 2])
>>> spu.min(x, y).numpy
array([[2, 1, 1, 1, 2]], dtype=int64)
```

## Slicing

Sockets support reading and writing with an index, a slice or a list of indices:

```python
>>> x = spu.array([1, 2, 3, 4, 5])
>>> x[1:4].numpy
array([[2, 3, 4]], dtype=int64)
>>> x[::2] = [10, 30, 50]
>>> x.numpy
array([[10,  2, 30,  4, 50]], dtype=int64)
```

Reading and writing can be combined, for instance to transform every other element:

```python
>>> x = spu.array([1, 2, 3, 4, 5])
>>> x[::2] = 2 * x[::2] + 1
>>> x.numpy
array([[ 3,  2,  7,  4, 11]], dtype=int64)
```

## Mixing operators and modules

The sockets produced by operators are regular sockets: they can be given to any task,
and the outputs of any task can be used with operators.

```python
>>> src = spu.source_random(8, dtype=spu.int64)
>>> inc = spu.incrementer(8, dtype=spu.int64)
>>> out_data, _ = src.generate()
>>> y = 2 * inc.increment(out_data) - 1
>>> seq = spu.Sequence(y)
>>> seq.exec_seq()
```

Here `y` is computed from fresh random bits at each execution of `seq`.

## Inspecting and changing the bindings

A socket knows what it is bound to:

| Method | Result |
|--------|--------|
| `s_in.get_bound_socket()` | the output socket an input socket is bound to |
| `s_out.get_bound_sockets()` | the list of input sockets bound to an output socket |
| `s_in.unbind(s_out)` | remove the binding between `s_in` and `s_out` |
| `s.has_data()` | `True` for an output socket (its memory is allocated) and for a bound input socket |
| `task.is_bound()` | `True` when the task was bound to another one with `Task.bind` |
| `task.can_exec()` | `True` when every socket of the task has data |

```python
>>> a = spu.incrementer(4, dtype=spu.int32)
>>> b = spu.incrementer(4, dtype=spu.int32)
>>> y = a.increment(spu.array([1, 2, 3, 4], dtype=spu.int32))
>>> z = b.increment(y)
>>> b.increment["in"].get_bound_socket() is y
True
>>> [s.task.name for s in y.get_bound_sockets()]
['increment']
>>> b.increment["in"].unbind(y)
0
>>> y.get_bound_sockets()
[]
```

Besides `numpy`, two views give access to the data without copy: `s.wave`, a NumPy
array of the frames processed by one execution (`n_frames_per_wave` rows), and
`s.memoryview`, a flat Python `memoryview` of the same elements.
