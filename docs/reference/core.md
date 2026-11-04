# Core classes

These classes are implemented in C++ and exposed with pybind11. Their methods are those
of the corresponding [StreamPU](https://aff3ct.github.io/streampu) classes, plus a few
Python methods added by `streampu` (calling a task, operators on sockets…).

## Socket

::: streampu._ext.core.Socket

## Task

::: streampu._ext.core.Task

## Module

::: streampu._ext.core.Module

## Data types

::: streampu._ext.dtype

## Tools

### help

```python
spu.help(obj, verbose=False)
```

Print the tasks and sockets of a module (`obj` is a `Module`), the sockets of a task
(`obj` is a `Task`) or the description of a socket (`obj` is a `Socket`).

::: streampu._ext.Signal_handler

::: streampu._ext.FormatFlags
