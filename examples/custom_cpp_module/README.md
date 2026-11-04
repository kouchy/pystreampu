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
