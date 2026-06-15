# Extending StreamPu with custom C++ module

By following this tutorial, you will be able to add your own module to StreamPU and use it in python with pybind11. 

We will start from an example of a module, Adder, which add 1 to all the element of an array.

#### Example of C++ header for a module

```python
#ifndef ADDER_HPP_
#define ADDER_HPP_

#include <streampu.hpp>

class Adder : public spu::module::Stateful   //inherite from Stateful
{
  protected:
    int n_elmts;

  public:
    Adder(const int n_elmts);
    virtual ~Adder() = default;

    void add(const double* input, double* output) const;

};

#endif // ADDER_HPP_
```

Output:

```text
Traceback (most recent call last):
  File "<stdin>", line 26, in execute_block
  File "/opt/homebrew/Cellar/python@3.12/3.12.11/Frameworks/Python.framework/Versions/3.12/lib/python3.12/ast.py", line 52, in parse
    return compile(source, filename, mode, flags,
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<unknown>", line 6
    class Adder : public spu::module::Stateful   //inherite from Stateful
                         ^^^
SyntaxError: invalid syntax
```

#### Example of C++ source code for a module

```python
#include "Adder.hpp"

Adder::Adder(const int n_elmts)
  : Stateful()
  , n_elmts(n_elmts)
{
    const std::string name = "Adder";
    this->set_name(name);

    auto& p = this->create_task("add");
    size_t ps_input  = this->template create_socket_in <double>(p, "input",  this->n_elmts);
    size_t ps_output = this->template create_socket_out<double>(p, "output", this->n_elmts);

    this->create_codelet(p,[ps_input, ps_output](spu::module::Module& m, spu::runtime::Task& t, const size_t frame_id) -> int
        {
            auto& adder = static_cast<Adder&>(m);
            double* input  = (double*)(t[ps_input ].get_dataptr());
            double* output = (double*)(t[ps_output].get_dataptr());

            adder.add(input, output);
            return spu::runtime::status_t::SUCCESS;
        });
}

void
Adder::add(const double* input, double* output) const
{
    for (int i = 0; i<this->n_elmts;i++)
        output[i] = input[i] + 1;
}
```

Output:

```text
Traceback (most recent call last):
  File "<stdin>", line 26, in execute_block
  File "/opt/homebrew/Cellar/python@3.12/3.12.11/Frameworks/Python.framework/Versions/3.12/lib/python3.12/ast.py", line 52, in parse
    return compile(source, filename, mode, flags,
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<unknown>", line 3
    Adder::Adder(const int n_elmts)
          ^
SyntaxError: invalid syntax
```

In order to use this example module Adder in python, we need to wrap/bind it with pybind11 

#### Example of a wrapper

```python
#include "Adder.hpp"
#include <pybind11/pybind11.h>
#include <streampu.hpp>

namespace py = pybind11;
using namespace py::literals;

// Create a	python module using PYBIND11, here our module will be named my_module
PYBIND11_MODULE(my_module, m){
	auto pyspu_stateful = (py::object) py::module_::import("streampu").attr("Stateful");
	py::class_<Adder, spu::module::Stateful>(m,"Adder")
    .def(py::init<const int>(),"n_elmts"_a);
}
```

Output:

```text
Traceback (most recent call last):
  File "<stdin>", line 26, in execute_block
  File "/opt/homebrew/Cellar/python@3.12/3.12.11/Frameworks/Python.framework/Versions/3.12/lib/python3.12/ast.py", line 52, in parse
    return compile(source, filename, mode, flags,
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<unknown>", line 5
    namespace py = pybind11;
              ^^
SyntaxError: invalid syntax
```

#### Building the Example as a C++ Project With CMake

We will provide you the CMakeLists.txt file in order to build your example project

Make sure to create a build folder before running any cmake command

```python
custom_module/
  Adder.cpp
  Adder.hpp
  wrapper.cpp
  CMakeLists.txt
  build/
```

Output:

```text
Traceback (most recent call last):
  File "<stdin>", line 26, in execute_block
  File "/opt/homebrew/Cellar/python@3.12/3.12.11/Frameworks/Python.framework/Versions/3.12/lib/python3.12/ast.py", line 52, in parse
    return compile(source, filename, mode, flags,
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<unknown>", line 1
    custom_module/
                  ^
SyntaxError: invalid syntax
```

The module build is called my_module-lib

```python
cmake_minimum_required(VERSION 3.2)
cmake_policy(SET CMP0054 NEW)
project (my_module)

# Enable C++11
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Link with the "Threads library (required to link with AFF3CT after)
set(CMAKE_THREAD_PREFER_PTHREAD ON)
set(THREADS_PREFER_PTHREAD_FLAG ON)
set(PYBIND11_NEWPYTHON ON)

find_package(Threads REQUIRED)
find_package(pybind11 REQUIRED)
find_package(cpptrace REQUIRED)
find_package(streampu REQUIRED)

file(GLOB SOURCES "${CMAKE_CURRENT_SOURCE_DIR}/src/*.cpp")

#add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/pybind11/)
pybind11_add_module(my_module-lib MODULE ${SOURCES})

set_target_properties(my_module-lib PROPERTIES
                      OUTPUT_NAME my_module
                      POSITION_INDEPENDENT_CODE ON) # set -fpic

target_link_libraries     (my_module-lib PRIVATE spu::spu-static-lib)
target_include_directories(my_module-lib PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/Adder.hpp)
```

Output:

```text
Traceback (most recent call last):
  File "<stdin>", line 26, in execute_block
  File "/opt/homebrew/Cellar/python@3.12/3.12.11/Frameworks/Python.framework/Versions/3.12/lib/python3.12/ast.py", line 52, in parse
    return compile(source, filename, mode, flags,
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<unknown>", line 1
    cmake_minimum_required(VERSION 3.2)
                           ^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
```

Activate your python environnement where you install streampu before running the script python below in build/ in order to create the Makefile

```python
CMAKE_PREFIX_PATH=$(python -c "import streampu; print(streampu.get_cmake_dirs())") cmake ..
```

Output:

```text
Traceback (most recent call last):
  File "<stdin>", line 26, in execute_block
  File "/opt/homebrew/Cellar/python@3.12/3.12.11/Frameworks/Python.framework/Versions/3.12/lib/python3.12/ast.py", line 52, in parse
    return compile(source, filename, mode, flags,
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<unknown>", line 1
    CMAKE_PREFIX_PATH=$(python -c "import streampu; print(streampu.get_cmake_dirs())") cmake ..
                      ^
SyntaxError: invalid syntax
```

Building the project will create a .so file that you can import in python

see the example below

```python
import my_module

mdl = my_module.Adder(10)
pprint.pp(my_module.Adder.mro())
print(mdl.tasks)
```

Output:

```text
Traceback (most recent call last):
  File "<stdin>", line 32, in execute_block
  File "<doc-cell>", line 1, in <module>
ModuleNotFoundError: No module named 'my_module'
```

In order to import your module you need to add it to the Python Path, by adding these lines before your module import in python

```python
import sys
import pprint

sys.path.insert(0, "/path/to/build")

import streampu
```

Output:

```text
No output.
```

Or by exporting the path of your file.so in the PYTHONPATH variable

```python
export PYTHONPATH=$PYTHONPATH:/path/to/build
```

Output:

```text
Traceback (most recent call last):
  File "<stdin>", line 26, in execute_block
  File "/opt/homebrew/Cellar/python@3.12/3.12.11/Frameworks/Python.framework/Versions/3.12/lib/python3.12/ast.py", line 52, in parse
    return compile(source, filename, mode, flags,
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<unknown>", line 1
    export PYTHONPATH=$PYTHONPATH:/path/to/build
           ^^^^^^^^^^
SyntaxError: invalid syntax
```
