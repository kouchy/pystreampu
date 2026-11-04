# -*- coding: utf-8 -*-
"""Add some python magic for handling dtypes."""

from __future__ import annotations

from typing import Union

import numpy as np

from . import _ext
from ._array import array

dtype = _ext.dtype
uint8 = _ext.uint8
uint16 = _ext.uint16
uint32 = _ext.uint32
uint64 = _ext.uint64
int8 = _ext.int8
int16 = _ext.int16
int32 = _ext.int32
int64 = _ext.int64
float32 = _ext.float32
float64 = _ext.float64
Socket = _ext.core.Socket


def _dtype_call(self: dtype, data: Union[Socket, np.array]) -> Socket:
    """Create socket representing `data` with the dtype of `self`.

    Args:
        self (dtype): A dtype object
        data (Socket): A socket or a numpy array to be casted.

    Returns:
        out (Socket): a socket representing data with the `dtype` of `self`
    """
    if isinstance(data, Socket):
        return data.astype(self)

    return array(data, dtype=self)


dtype.__call__ = _dtype_call


def _throw_if_invalid(obj):
    """Check if the input is a valid dtype.

    Args:
        obj (Any): An object to be checked

    Raises:
        TypeError: If the input is not a valid dtype.
    """
    if not issubclass(type(obj), dtype):
        msg = f"type '{type(obj)}' does not name a StreamPU datatype."
        raise TypeError(msg)


dtype.throw_if_invalid = staticmethod(_throw_if_invalid)


__all__ = [
    "dtype",
    "uint8",
    "uint16",
    "uint32",
    "uint64",
    "int8",
    "int16",
    "int32",
    "int64",
    "float32",
    "float64",
]
