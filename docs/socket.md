# Socket

```python
import streampu as spu
import numpy as np
```

Output:

```text
No output.
```

## Python interface

```python
x = spu.array([1,2,3,4])
print(x)
```

Output:

```text
[[1 2 3 4]]
```

## NumPy interface
### From NumPy to StreamPu

```python
l = np.array([1,2,3,4], np.float32)
x = spu.array(l)
print("A", x.dtype, "socket containing the data", x)
print(repr(x))
```

Output:

```text
A float32 socket containing the data [[1. 2. 3. 4.]]
socket([[1. 2. 3. 4.]], dtype=float32, name=data, task=Array.read)
```

```python
l[2] = 1
x
```

Output:

```text
socket([[1. 2. 1. 4.]], dtype=float32, name=data, task=Array.read)
```

### From StreamPu to Numpy

```python
src = spu.source_random(8, dtype = spu.int64)
x,_ = src.generate()
px = x.numpy
print(px)
```

Output:

```text
[[0 1 1 0 1 1 1 1]]
```

```python
src.generate.exec()
x
```

Output:

```text
socket([[1 1 1 0 0 1 0 0]], dtype=int64, name=out_data, task=Source_random.generate)
```
