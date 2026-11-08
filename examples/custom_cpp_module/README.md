# Custom C++ module for StreamPU
## Build the example
To build the example, run the following commands:
```bash
mkdir build && cd build
CMAKE_PREFIX_PATH=$(python -c "import streampu; print(streampu.get_cmake_dirs())") cmake ..
make
```

## Use the built Module
```python
import sys
sys.path.insert(0, "../build")

import my_module

import streampu as spu

mdl = my_module.Adder(4)
x = spu.array([1, 2, 3, 4], dtype=spu.float64)
y = mdl.add_one(x)

print(y)
```
This should print `[[2. 3. 4. 5.]]`.

## Typing of the modules returned by streampu

`streampu` returns `spu::module::Module*` in several places (for instance the modules of a `Sequence`, which are
clones of yours when `n_threads > 1`). pybind11 types them after their dynamic type: if this exact class is not
registered (an extension that only registers abstract bases, or a concrete class built by a factory), the object
falls back to `streampu.Module` and loses the methods of your classes.

Register a downcaster to fix that: it receives the object and returns the most derived class *you registered*
(`wrapper/Common/Tools/Module_downcast.hpp`, installed with the pystreampu headers in
`<streampu>/include/pystreampu`).

```cpp
#include "wrapper/Common/Tools/Module_downcast.hpp" // before any other use of pybind11 in the translation unit

static const void* my_downcaster(const spu::module::Module* m, const std::type_info*& type)
{
    // try the most derived registered classes first
    if (auto p = pyspu::downcast_to<My_base_int>(m, type)) return p;
    return nullptr;
}

PYBIND11_MODULE(my_module, m)
{
    // ... register the classes, then:
    pyspu::register_module_downcaster(&my_downcaster);
}
```

The registry lives in the pybind11 internals, so it is shared with `streampu` although each extension links its own
copy of the static StreamPU library. `PYSPU_HAS_MODULE_DOWNCAST_REGISTRY` is defined when the installed pystreampu
provides it.
