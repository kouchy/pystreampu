"""Julia runtime of the Julia modules (`spu.Stateless_Julia`, `spu.Stateful_Julia`).

The Julia modules need pyStreamPU compiled with Julia (Julia >= 1.10.9):

    pip install streampu --no-binary streampu -C cmake.define.SPU_LINK_JULIA=ON

`available()` tells whether the installed package has them. Julia is started
automatically when the first Julia module is created: `init()` is only needed to choose
the number of GC root slots. The code given to `eval` and `eval_file` is evaluated in the
`Main` module of Julia, where the codelets are looked up.

Examples:
    >>> import streampu as spu
    >>> if spu.julia.available():
    ...     spu.julia.eval("double(x) = 2x")
"""

import os
from typing import Union

from streampu import _ext

__all__ = ["available", "init", "is_init", "eval", "eval_file"]

# Names of the classes of the Julia support, exported by the streampu package
_CLASSES = ("Julia", "Module_Julia", "Stateless_Julia", "Stateful_Julia")

_NOT_AVAILABLE = (
    "this pyStreamPU is not compiled with Julia. Build it from the sources with Julia "
    "(>= 1.10.9) installed:\n"
    "    pip install streampu --no-binary streampu -C cmake.define.SPU_LINK_JULIA=ON\n"
    "(from a clone of the repository: pip install . -C cmake.define.SPU_LINK_JULIA=ON)"
)


def available() -> bool:
    """Tell whether pyStreamPU is compiled with Julia.

    Returns:
        bool: True if the Julia modules can be used
    """
    return bool(getattr(_ext, "has_julia", False))


def _julia():
    if not available():
        raise ImportError(_NOT_AVAILABLE)
    from streampu._ext.jl import Julia

    return Julia


def init(n_proxies: int = 256) -> None:
    """Start the Julia runtime, if it is not started yet.

    Args:
        n_proxies (int): number of GC root slots per thread

    Raises:
        ImportError: if pyStreamPU is not compiled with Julia
    """
    _julia().init(n_proxies)


def is_init() -> bool:
    """Tell whether the Julia runtime is started.

    Returns:
        bool: False if it is not started, or if pyStreamPU is not compiled with Julia
    """
    return available() and _julia().is_init()


def eval(code: str) -> None:
    """Evaluate Julia code in the `Main` module (starts Julia if needed).

    Args:
        code (str): Julia code

    Raises:
        ImportError: if pyStreamPU is not compiled with Julia
        RuntimeError: if the evaluation raises a Julia exception
    """
    _julia().eval(code)


def eval_file(path: Union[str, os.PathLike]) -> None:
    """Evaluate a Julia file in the `Main` module (starts Julia if needed).

    Args:
        path (str | os.PathLike): path of the `.jl` file

    Raises:
        ImportError: if pyStreamPU is not compiled with Julia
        RuntimeError: if the file cannot be read, or if its evaluation raises a Julia
            exception
    """
    _julia().eval_file(path)
