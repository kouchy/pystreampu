# Julia modules

This example writes modules in Julia and chains them with a C++ module, first with
immediate executions, then in a `Sequence` on 4 threads:

```
input -> increment (Julia, stateless) -> * 2 (C++) -> accumulate (Julia, stateful) -> output
```

- `julia_module.py`: the Python script;
- `codelets.jl`: the Julia types of the states and the codelet of `accumulate`.

!!! note "Work in progress"
    The Julia classes are in `streampu._ext.jl` for now (`Julia`, `Stateless_Julia`,
    `Stateful_Julia`), and a Julia module must be evaluated (`mdl.eval()`) before an
    immediate execution. Both will change: `spu.Stateless_Julia`, and automatic evaluation.

## 1. Install Julia (>= 1.10.9)

With [juliaup](https://github.com/JuliaLang/juliaup), the official installer:

```bash
brew install juliaup        # or: curl -fsSL https://install.julialang.org | sh
juliaup add 1.11
juliaup default 1.11
julia --version
```

The build looks for Julia through `JULIA_BINDIR`, the folder of the real `julia`
executable (not the `juliaup` launcher). Set it in the terminal used for the build:

```bash
export JULIA_BINDIR=$(julia --startup-file=no -e 'print(Sys.BINDIR)')
echo $JULIA_BINDIR
```

## 2. Build pyStreamPU with Julia

From the root of the repository, in a virtual environment (Python >= 3.10):

```bash
git switch streampu-1.10.0                       # branch with the Julia support
git submodule update --init --recursive          # StreamPU 1.10.0
python -m venv env-julia && source env-julia/bin/activate
pip install --upgrade pip
rm -rf build/                                    # start from a clean build folder
export CMAKE_BUILD_PARALLEL_LEVEL=8              # number of compilation jobs
pip install -v . -C cmake.define.SPU_LINK_JULIA=ON
```

In the output of the build, check these lines:

```
-- Found Julia: .../libjulia.dylib (found suitable version "1.11.x", minimum required is "1.10.9")
-- Julia library folder added to the RPATH of _ext: ...
```

Then check that the installed package has Julia (from another folder than the
repository, so that Python imports the installed package and not the sources):

```bash
cd /tmp && python -c "import streampu._ext as e; print('has_julia:', e.has_julia)" && cd -
```

## 3. Run the example

```bash
python examples/custom_julia_module/julia_module.py
```

Expected output (the split between the threads varies):

```
input              : [0 1 2 3 4 5 6 7]
after increment    : [ 3  4  5  6  7  8  9 10]
after * 2 (C++)    : [ 6  8 10 12 14 16 18 20]
after accumulate   : [ 60  80 100 120 140 160 180 200]
states of acc      : ['Accumulator(104, 1)', 'Gain(10)']

sequence: 4 clones of acc
  thread 0: ['Accumulator(26104, 251)', 'Gain(10)']
  ...
output of thread 0 : [ 60  80 100 120 140 160 180 200]

OK
```

Each thread has its own copy of `Accumulator` (made when the sequence clones the
module, so each copy starts from the state of the original: 1 call); `Gain` is shared.
The `calls` of the 4 threads add up to 1000 + 4.

## Troubleshooting

| Message | Cause | Fix |
|---|---|---|
| `Unable to detect the Julia executable` | `julia` not in the `PATH` and `JULIA_BINDIR` not set | set `JULIA_BINDIR` (step 1) |
| `Unable to find the julia shared library` or `julia.h` | `JULIA_BINDIR` is the folder of the juliaup launcher | set `JULIA_BINDIR` with `Sys.BINDIR` (step 1), `rm -rf build/` |
| `found unsuitable version` | Julia older than 1.10.9 | `juliaup add 1.11 && juliaup default 1.11` |
| `has_julia: False` | the package was built without Julia (or Python imports the sources) | `rm -rf build/`, reinstall with `-C cmake.define.SPU_LINK_JULIA=ON`, test from another folder |
| `Library not loaded: @rpath/libjulia...` at import | the RPATH of `_ext` misses the folder of libjulia | send the output of `otool -l $(python -c "import streampu._ext as e; print(e.__file__)") \| grep -A2 RPATH` |
| `The task cannot be executed because the module has not been evaluated` | `eval()` missing before an immediate execution | call `mdl.eval()` (temporary, see the note above) |
