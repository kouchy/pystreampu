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
[StreamPU](https://github.com/aff3ct/streampu): pyStreamPU 1.2.x follows StreamPU 1.10.x.
pyStreamPU also has releases of its own, so each row gives the first version of
pyStreamPU that embeds a version of StreamPU; the following versions of pyStreamPU embed
it too, until the next row.

| pyStreamPU (from) | StreamPU |
|-------------------|----------|
| 1.2.0             | 1.10.0   |
| 1.1.4             | 1.9.4    |
| 1.1.3             | 1.9.3    |
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

## Julia modules

The modules written in Julia (`spu.Stateless_Julia`, `spu.Stateful_Julia`, see
[Writing a module in Julia](guides/julia_module.md)) need pyStreamPU compiled with Julia:
they are not in the packages of PyPI.

1. Install Julia (>= 1.10.9), for instance with [juliaup](https://github.com/JuliaLang/juliaup):
   ```
   curl -fsSL https://install.julialang.org | sh   # or: brew install juliaup
   juliaup add 1.11 && juliaup default 1.11
   ```
2. Give the folder of the `julia` executable to the build (with juliaup, `julia` in the
   `PATH` is a launcher):
   ```
   export JULIA_BINDIR=$(julia --startup-file=no -e 'print(Sys.BINDIR)')
   ```
3. Build pyStreamPU from its sources with the option `SPU_LINK_JULIA`, from PyPI:
   ```
   pip install streampu --no-binary streampu -C cmake.define.SPU_LINK_JULIA=ON
   ```
   or from a clone of the repository:
   ```
   pip install ./pystreampu -C cmake.define.SPU_LINK_JULIA=ON
   ```
4. Check (from another folder than the repository):
   ```
   python -c "import streampu as spu; print(spu.julia.available())"
   ```

The build prints `Found Julia: ...` and `Julia library folder added to the RPATH of _ext`;
`_ext` is linked to `libjulia` of this installation of Julia.

!!! warning "Rebuild pyStreamPU after an update of Julia"
    The compiled extension of pyStreamPU records the absolute path of the folder of
    `libjulia` (its RPATH) and is built against the headers of this version of Julia. If
    this installation of Julia is updated, moved or removed (for instance when juliaup
    replaces 1.11.7 by 1.11.8 and deletes the old one), `import streampu` fails with
    `Library not loaded: @rpath/libjulia...` (macOS) or
    `libjulia.so...: cannot open shared object file` (Linux), or the Julia modules may
    misbehave. Rebuild pyStreamPU (steps 2 and 3) after each update of Julia, with
    `--force-reinstall --no-cache-dir` and the `build/` folder removed when building from
    a clone. To keep a version of Julia for pyStreamPU, pin it with juliaup
    (`juliaup add 1.11.7 && juliaup default 1.11.7`).

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
