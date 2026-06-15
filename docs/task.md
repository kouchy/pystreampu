# Task

In this section we present some functionalities of `task` objects.

```python
import streampu as spu
src = spu.source_random(8, dtype = spu.int64)
generate = src["generate"]
```

Output:

```text
No output.
```

If you want to have some information about the tasks of `src` you can use `help`or `spu.help`.

```python
generate.module

generate.inputs
generate.outputs
generate.forwards

generate.stats
generate.avg_duration, generate.min_duration, generate.max_duration
generate.n_calls
generate.reset

generate.debug

generate.exec



generate.out_data
__call__
```

Output:

```text
Traceback (most recent call last):
  File "<stdin>", line 33, in execute_block
  File "<doc-cell>", line 19, in <module>
NameError: name '__call__' is not defined. Did you mean: '__name__'?
```
