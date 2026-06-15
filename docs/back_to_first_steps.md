```python
import streampu as spu
```

Output:

```text
No output.
```

# Back to the first steps
Now that you are familiar with the [StreamPU](https://aff3ct.github.io/streampu) concepts of
- module
- task
- socket
we will show how the previous steps can be simplified.

## Build the modules
We keep the same example: suppose that we want to randomly generate `8` bits from a Bernoulli distribution and increment these bits.

```python
src = spu.source_random(8, dtype = spu.int64)
inc = spu.incrementer(8, dtype=spu.int64)
```

Output:

```text
No output.
```

```python
x,_ = src.generate()
y = inc.increment(x)

print("Output of source:", x)
print("Output of incrementer:", y)
```

Output:

```text
Output of source: [[0 1 1 0 1 1 1 1]]
Output of incrementer: [[1 2 2 1 2 2 2 2]]
```

```python
src.generate.exec()
inc.increment.exec()
print("Output of source:", x)
print("Output of incrementer:", y)
```

Output:

```text
Output of source: [[1 1 1 0 0 1 0 0]]
Output of incrementer: [[2 2 2 1 1 2 1 1]]
```
