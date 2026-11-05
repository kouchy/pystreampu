"""Helpers to build C++ extensions (custom modules) against streampu."""

import os as _os


def get_cmake_dirs() -> str:
    """Return the CMake directories of the pybind11 and StreamPU versions used by `streampu`.

    Use the result as `CMAKE_PREFIX_PATH` to build a C++ extension (a custom module)
    against the same versions as the installed `streampu` package.

    Returns:
        out (str): the pybind11 and StreamPU CMake directories, separated by the path
            separator of the platform (`:`, or `;` on Windows)

    Examples:
        >>> import streampu
        >>> streampu.get_cmake_dirs()
        'path/to/site-packages/pybind11/share/cmake:path/to/site-packages/streampu/lib/cmake'
    """
    # Imported here: pybind11 is only needed to build extensions, not to use streampu
    import pybind11

    import streampu

    p11_cmake_path = _os.path.dirname(pybind11.get_cmake_dir())
    spu_cmake_path = _os.path.join(_os.path.dirname(streampu._ext.__file__), "lib", "cmake")
    return p11_cmake_path + _os.pathsep + spu_cmake_path


__all__ = ["get_cmake_dirs"]
