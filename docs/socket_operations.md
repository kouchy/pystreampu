# Socket Operations (Tested Patterns)

This page documents socket operations that are exercised in the test suite,
with examples you can reuse directly.

## Create a socket from Python data

```python
import streampu as spu

x = spu.array([1, 2, 3])
print(x.numpy)  # usually shape (1, N)
```

Output:

```text
[[1 2 3]]
```

## Build expressions from sockets

Binary arithmetic operators are supported between sockets and scalars.

```python
import streampu as spu

x = spu.array([1, 2, 3])

y1 = x + 1
y2 = 1 + x
y3 = x * 2
y4 = x - 1
y5 = x / 2
```

Output:

```text
No output.
```

These expressions are lazy graph operations. Execute them through a sequence:

```python
seq = spu.Sequence.from_socket(y1)
seq.exec_seq()
print(y1.numpy)  # [[2 3 4]]
```

Output:

```text
[[2 3 4]]
```

## In-place socket updates

In-place operators are also supported and can be chained.

```python
import streampu as spu

x = spu.array([1, 2, 3])
x += 1
x += 1
x *= 2

seq = spu.Sequence.from_socket(x)
seq.exec_seq()
print(x.numpy)  # [[ 6  8 10]]
```

Output:

```text
[[16 20 24]]
```

## Unary operations

Unary operations used in tests:

- Negation: `-x`
- Bitwise not: `~x`
- Cast: `x.astype(dtype)`

```python
import streampu as spu

x = spu.array([12], dtype=spu.int32)
print((-x).numpy)
print((~x).numpy)
print(x.astype(spu.float32).numpy)
```

Output:

```text
[[-12]]
[[-13]]
[[12.]]
```

## Comparisons and bitwise operators

Comparison operators return sockets too, so they can be part of a graph:

```python
import streampu as spu

x = spu.array([1, 2, 3])

m1 = x > 1
m2 = x <= 2
m3 = x == 2
```

Output:

```text
No output.
```

Bitwise binary operators are also available (`&`, `|`, `^`, and in-place variants).

## Reductions

The following reductions are covered in tests:

- `spu.sum(x)`
- `spu.prod(x)`
- `spu.max(x)`
- `spu.all(x)`
- `spu.any(x)`

```python
import streampu as spu

x = spu.array([1, 2, 3])
y = spu.sum(x)

seq = spu.Sequence.from_socket(y)
seq.exec_seq()
print(y.numpy)  # [[6]]
```

Output:

```text
[[6]]
```

## Bind module sockets

Task/module sockets can be connected directly.

```python
import streampu as spu

src = spu.source_random(5, dtype=spu.uint32)
incr = spu.incrementer(5, dtype=spu.uint32)

# Bind incrementer input to source output
incr["increment::in"] = src["generate::out_data"]

src["generate"].exec()
incr["increment"].exec()
print(incr["increment::out"])
```

Output:

```text
[[1 2 2 1 2]]
```

You can also call `.bind(...)` on sockets in custom module code.

## Access socket buffers in codelets

Inside a codelet, socket buffers are exposed through `.numpy` and can be
read/written in place.

```python
def processing(_, t, __):
    inp = t.sock_in.numpy
    out = t.sock_out.numpy
    out[:] = inp[:] + 1
    return 0
```

Output:

```text
No output.
```

## Notes

- Most examples above come from tests under `tests/` (notably binary ops,
  unary ops, reductions, stateless module usage, and incrementer binding).
- For sequence/binary-op tests, expected `.numpy` values are typically 2D
  (`(1, N)`), not 1D.
