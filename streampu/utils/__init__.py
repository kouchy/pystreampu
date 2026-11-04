import os.path as _osp

import pybind11 as _p11

import streampu as _spu


def get_cmake_dirs() -> str:
    """Return the CMake directories of the pybind11 and StreamPU versions used by `streampu`.

    Use the result as `CMAKE_PREFIX_PATH` to build a C++ extension (a custom module or a
    plugin) against the same versions as the installed `streampu` package.

    Returns:
        out (str): the pybind11 and StreamPU CMake directories, separated by `:`

    Examples:
        >>> import streampu
        >>> streampu.get_cmake_dirs()
        'path/to/site-packages/pybind11/share/cmake:path/to/site-packages/streampu/lib/cmake'
    """
    p11_cmake_path = _osp.dirname(_p11.get_cmake_dir())
    spu_cmake_path = _osp.join(_osp.dirname(_spu._ext.__file__), "lib", "cmake")
    return p11_cmake_path + ":" + spu_cmake_path


__all__ = ["get_cmake_dirs"]
