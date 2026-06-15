```python
import streampu as spu
```

Output:

```text
No output.
```

# Module
In this section, we present some basic attributes and methods for StreamPU modules similar to the ones from the C++ API.

`spu.Module` is a shortcut for `streampu._ext.core.Module` which is a binding for the class `spu::module::Module` of the C++ API.

The Python API give access to some attributes and methods that are:
- directly bound from `streampu._ext.core.Module`
- specific to the Python API

In order to illustrate these ... an `spu.incrementer`...

```python
mdl = spu.incrementer(3)
```

Output:

```text
No output.
```

## Main attributes

- `name` (property) is the module name

```python
print(mdl.name)
```

Output:

```text
Incrementer
```

- `tasks` (read only) is the list of every task of a module.

The incrementer of our example has two tasks `increment` and `incrementf`.

```python
[t.name for t in mdl.tasks]
```

Output:

```text
['increment', 'incrementf']
```

- `n_frames` (property) is the number of frames processes at each task execution.

```python
mdl.n_frames
```

Output:

```text
1
```

## Attributes from the Python API

```python
mdl.increment
```

Output:

```text
<streampu._ext.core.Task object at 0x1085555f0>
```
