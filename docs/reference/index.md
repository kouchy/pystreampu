# API reference

This part of the documentation describes the functions and classes of the `streampu`
package, generated from their docstrings. For explanations and examples, see the
[tutorial](../tutorial/first_steps.md) and the [guides](../guides/socket_operations.md).

| Page | Content |
|------|---------|
| [Core classes](core.md) | `Socket`, `Task`, `Module`, data types |
| [Sockets](sockets.md) | creating sockets, data types |
| [Operators](operators.md) | arithmetic, comparison, bitwise and unary operators, reductions |
| [Modules](modules.md) | `Stateless`, `Stateful_core`, built-in modules, probes, reporters |
| [Execution](execution.md) | `Sequence` and `Pipeline` |
| [Tools](tools.md) | build helpers and plugins |

!!! note "Classes implemented in C++"
    The core classes (`Socket`, `Task`, `Module`, `Stateless`, probes…) are implemented
    in C++. Their reference is generated from the type stubs of `streampu._ext`
    (`scripts/generate_stubs.sh`). Many of them have no description yet: their
    signature is still listed.

All the functions and classes are available directly from the `streampu` package
(`import streampu as spu`, then `spu.array`, `spu.Sequence`…), whatever the module that
defines them.
