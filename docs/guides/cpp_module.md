# Writing a module in C++

StreamPU can be extended with modules written in C++. They run at full speed, without
the GIL, and can keep a state. This guide builds a module `Adder` with a task
`add_one` that adds 1 to each element of an array of `double`, then makes it
available in Python.

The complete project is in the folder
[`examples/custom_cpp_module`](https://gitlab.bordeaux-inp.fr/rtajan/pystreampu/-/tree/develop/examples/custom_cpp_module)
of the repository; the code shown on this page is included from it.

```text
custom_cpp_module/
  src/
    Adder.hpp
    Adder.cpp
    wrapper.cpp
  tests/
    test_custom_cpp_module.py
  CMakeLists.txt
```

## Declare the module

The class `Adder` inherits from `spu::module::Stateful`. The number of elements of the
arrays is given to the constructor, and the actual processing is done by the method
`add_one`:

```c++
--8<-- "examples/custom_cpp_module/src/Adder.hpp"
```

## Implement the module

The constructor declares the task and its sockets, then the **codelet**, the function
executed by the task:

1. `create_task("add_one")` creates the task;
2. `create_socket_in<double>` and `create_socket_out<double>` create its input and
   output sockets of `n_elmts` elements, and return their indexes;
3. `create_codelet` registers a lambda of type
   `int(spu::module::Module&, spu::runtime::Task&, const size_t)`. It recovers the
   module and the data pointers of the sockets, calls `add_one` and returns a status.

```c++
--8<-- "examples/custom_cpp_module/src/Adder.cpp"
```

## Wrap the module with pybind11

Only the constructor needs to be wrapped: the tasks and sockets created by the
constructor are exposed automatically by `streampu`.

```c++
--8<-- "examples/custom_cpp_module/src/wrapper.cpp"
```

Two lines of the module initialization are required:

- `py::module_::import("streampu")` registers the base class `spu::module::Stateful`
  with pybind11 before `Adder` is declared;
- `spu::tools::Buffer_allocator::set_task_autoalloc(true)` enables the automatic
  allocation of the socket buffers. `streampu` does it for its own modules, but your
  extension is linked with its own copy of the static StreamPU library, and therefore
  with its own copy of this setting. Without it, executing a task fails with
  *"some of the inputs/output sockets are not fed"*.

## Build the project

The project must be compiled against the StreamPU and pybind11 versions used by the
installed `streampu` package. `streampu.get_cmake_dirs()` gives the corresponding CMake
directories:

```python
>>> import streampu
>>> streampu.get_cmake_dirs()
'path/to/your/site-packages/pybind11/share/cmake:path/to/your/site-packages/streampu/lib/cmake'
```

Pass them to CMake through `CMAKE_PREFIX_PATH`:

```bash
cd examples/custom_cpp_module
mkdir build && cd build
CMAKE_PREFIX_PATH=$(python -c "import streampu; print(streampu.get_cmake_dirs())") cmake ..
make
```

??? example "CMakeLists.txt"
    ```cmake
    --8<-- "examples/custom_cpp_module/CMakeLists.txt"
    ```

## Use the module

The build creates a Python extension `my_module` in the `build` folder. Add this
folder to the Python path, either in the script:

```python
import sys
sys.path.insert(0, "/path/to/build")
```

or in the environment:

```bash
export PYTHONPATH=$PYTHONPATH:/path/to/build
```

The module is then used like any StreamPU module:

```python
>>> import my_module
>>> import streampu as spu
>>> mdl = my_module.Adder(4)
>>> x = spu.array([1, 2, 3, 4], dtype=spu.float64)
>>> y = mdl.add_one(x)
>>> y
socket([[2. 3. 4. 5.]], dtype=float64, name=output, task=Adder.add_one)
```

To distribute such a module as a Python package, see
[Creating a plugin](plugins.md).
