# Creating a plugin

A plugin is a separate Python package that extends `streampu`, typically with new
modules written in C++ (see [Writing a module in C++](cpp_module.md)) or in Python.
Plugins are discovered automatically when `streampu` is imported.

## How plugins are discovered

At import, `streampu` loads every installed package that declares an
[entry point](https://packaging.python.org/en/latest/specifications/entry-points/)
in the group `streampu.plugins`. The loaded objects are stored in the dictionary
`spu.plugins`, indexed by the name of their entry point:

```python
>>> import streampu as spu
>>> spu.plugins
{'my_plugin': <module 'my_plugin' from '...'>}
```

## Declare the entry point

In the `pyproject.toml` of the plugin package, declare the module to load:

```toml
[project]
name = "my-plugin"
dependencies = ["streampu"]

[project.entry-points."streampu.plugins"]
my_plugin = "my_plugin"
```

Once the package is installed (`pip install .`), its modules are available with:

```python
import streampu as spu

mdl = spu.plugins["my_plugin"].Adder(4)
```

## Package a C++ module as a plugin

A C++ plugin is built against the StreamPU and pybind11 versions used by the installed
`streampu` package. Their CMake configuration files are given by:

```python
>>> import streampu
>>> streampu.get_cmake_dirs()
'path/to/site-packages/pybind11/share/cmake:path/to/site-packages/streampu/lib/cmake'
```

With [scikit-build-core](https://scikit-build-core.readthedocs.io/), the build
backend used by `streampu` itself, the CMake project of
[Writing a module in C++](cpp_module.md) can be packaged by adding `streampu` to the
build requirements and passing these directories to CMake through
`CMAKE_PREFIX_PATH`.
