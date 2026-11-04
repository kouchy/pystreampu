# pyStreamPU

[![pipeline](https://gitlab.bordeaux-inp.fr/rtajan/pystreampu/badges/develop/pipeline.svg)](https://gitlab.bordeaux-inp.fr/rtajan/pystreampu/-/pipelines?ref=develop)
[![documentation](https://img.shields.io/badge/docs-GitLab%20Pages-blue)](https://rtajan.pages.bordeaux-inp.fr/pystreampu/)
[![license](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Python bindings for [StreamPU](https://github.com/aff3ct/streampu), a C++ Domain
Specific Embedded Language (DSEL) for building high-throughput, low-latency
streaming applications on multicore CPUs (originally designed for
Software-Defined Radio within the [AFF3CT](https://aff3ct.github.io/) project).

With `streampu` you describe a data-flow graph of **tasks** exchanging data
through **sockets** directly from Python, and let the StreamPU runtime execute it,
sequentially or in parallel.

## Highlights

- **NumPy interoperability without copies**: sockets expose their buffers as NumPy
  arrays and can be built from NumPy arrays.
- **Data-flow graphs from plain Python**: modules, tasks and operators
  (`+`, `*`, comparisons, reductions…) are bound together as you call them.
- **Parallel execution**: replay a graph with a multithreaded `Sequence` or split it
  into a `Pipeline`.
- **Extensible**: write your own modules in Python (optionally accelerated with
  numba, free-threaded Python supported) or in C++ with pybind11.

## A simple `streampu` program

```python
import streampu as spu

x = spu.array([1, 2, 3], dtype=spu.uint8)
y = spu.array([4, 5, 6], dtype=spu.uint8)

z = x + y
print(z)
```

This should print `[[5 7 9]]` (sockets are 2D: one row per frame).

Calling a task (here the `+` operator) executes it **and** binds its sockets into a
graph that can be replayed later:

```python
src = spu.source_random(8, dtype=spu.int64)  # random bits
inc = spu.incrementer(8, dtype=spu.int64)

out = inc.increment(src.generate()[0])       # executed once, and bound

seq = spu.Sequence(out)                       # replay the whole graph
seq.exec_n_times(10)
print(out)
```

## Getting started

### Install from the sources

Clone the repository (with its submodules)

```bash
git clone --recursive https://gitlab.bordeaux-inp.fr/rtajan/pystreampu.git
```

then install the Python interface of `StreamPU` using `pip`

```bash
pip install ./pystreampu
```

If you want more information during compilation, use the `-v` option of the `pip`
command. The compilation may take a while; set `CMAKE_BUILD_PARALLEL_LEVEL` to use
several jobs, e.g. `export CMAKE_BUILD_PARALLEL_LEVEL=4`.

### Install with fine-tuning of C++ flags

To install `streampu` compiled with custom flags, use the following syntax:

```bash
pip install -v -Ccmake.define.YOUR_CMAKE_FLAG1=CONTENT1 -Ccmake.define.YOUR_CMAKE_FLAG2=CONTENT2 .
```

where you can replace `YOUR_CMAKE_FLAG1` and `YOUR_CMAKE_FLAG2` by the flags you want
and set `CONTENT1` and `CONTENT2` values.

### Install for development

```bash
pip install -ve './pystreampu[dev,docs]'
```

This installs the linting, testing and documentation dependencies.

## Run tests

Testing the `streampu` package requires `pytest`, run the following command:

```bash
pytest --pyargs streampu
```

## Documentation

The documentation (tutorial, how-to guides, concepts and API reference) is available
at **<https://rtajan.pages.bordeaux-inp.fr/pystreampu/>**. Its sources are in `docs/`; to build it locally:

```bash
pip install './pystreampu[docs]'
mkdocs serve
```

## Contributing

The main repository is
[gitlab.bordeaux-inp.fr/rtajan/pystreampu](https://gitlab.bordeaux-inp.fr/rtajan/pystreampu).
Issues and merge requests are welcome; see `docs/dev_guidelines.md` for the coding
conventions.

## Citing

If you use StreamPU in your work, please cite (see also [`CITATION.bib`](CITATION.bib)):

```bibtex
@Article{Cassagne2023,
  author   = {A. Cassagne and R. Tajan and O. Aumage and D. Barthou and C. Leroux and C. J\'ego},
  journal  = {Wiley Concurrency and Computation: Practice and Experience (CCPE)},
  title    = {{StreamPU}: A {DSEL} for High Throughput and Low Latency Software-Defined Radio on Multicore {CPU}s},
  year     = {2023},
  month    = jul,
  number   = {23},
  pages    = {e7820},
  volume   = {35},
  doi      = {10.1002/cpe.7820},
}
```

## License

`streampu` is released under the [MIT License](LICENSE).
