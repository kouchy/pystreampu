# Sockets

## Creating sockets

::: streampu._array.array
::: streampu._array.zeros
::: streampu._array.ones
::: streampu._array.arange

## Data types

| Data type | NumPy equivalent |
|-----------|------------------|
| `spu.int8`, `spu.int16`, `spu.int32`, `spu.int64` | `np.int8` … `np.int64` |
| `spu.uint8`, `spu.uint16`, `spu.uint32`, `spu.uint64` | `np.uint8` … `np.uint64` |
| `spu.float32`, `spu.float64` | `np.float32`, `np.float64` |

The NumPy equivalent of a StreamPU data type is given by its `numpy` attribute, e.g.
`spu.int16.numpy`.
