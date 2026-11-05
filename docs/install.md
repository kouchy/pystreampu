# Installation
## Create a virtual environment
To install `pystreampu` in a virtual environment, you can use the following
commands:
```
python3 -m venv env
source env/bin/activate
```

## Pre-built packages

Wheels are built for Linux (x86_64 and aarch64) and macOS (arm64 and x86_64), for
Python 3.10 to 3.14 (including the free-threaded 3.14t). There are no wheels for Windows
for now: on Windows, `pip` compiles the package from its source distribution, which needs
a C++ compiler (Visual Studio) and CMake.

## Versions

Each minor version of pyStreamPU embeds one minor version of
[StreamPU](https://github.com/aff3ct/streampu): pyStreamPU 1.1.x follows StreamPU 1.9.x.
pyStreamPU also has releases of its own, so each row gives the first version of
pyStreamPU that embeds a version of StreamPU; the following versions of pyStreamPU embed
it too, until the next row.

| pyStreamPU (from) | StreamPU |
|-------------------|----------|
| 1.1.2             | 1.9.2    |
| 1.1.1             | 1.9.1    |
| 1.1.0             | 1.9.0    |

## Install from the sources
Clone the repository
```
git clone --recursive https://github.com/rtajan/pystreampu.git
```
then install the python interface of `StreamPU` using `pip`
```
pip install ./pystreampu
```
If you want more information during compilation, use `-v` option of the `pip` command.

!!! warning
    The compilation of `streampu` may take a long time, depending on your machine. You can set the variable `CMAKE_BUILD_PARALLEL_LEVEL` to set the number of parallel jobs used during compilation. For example, to use 4 parallel jobs, you can do:
    ```
    export CMAKE_BUILD_PARALLEL_LEVEL=4
    ```

## Install with fine-tuning of C++ flags
To install `streampu` compiled with custom flags, use the following syntax:
```
pip install -Ccmake.define.YOUR_CMAKE_FLAG1=CONTENT1 -Ccmake.define.YOUR_CMAKE_FLAG2=CONTENT2 .
```
where you can replace `YOUR_CMAKE_FLAG1` and `YOUR_CMAKE_FLAG2` by the flags you want
and set `CONTENT1` and `CONTENT2` values.

## Run tests
```
pytest tests  # from the root of the repository
```

## Install for development
To install `streampu` for development, you can use the following command:
```
pip install -ve './pystreampu[dev,docs]'
```

!!! note
    This will install the development dependencies, the testing dependencies, and the documentation dependencies. You can then test the package with `pytest` and build the documentation using `mkdocs` command.
