# -*- coding: utf-8 -*-
import streampu._ext
from streampu._ext import int32


def finalizer(n_elmts: int, dtype: streampu._ext.dtype = int32):
    """Build a finalizer.

    Args:
        n_elmts (int): socket size
        dtype (streampu._ext.dtype): data type

    Returns:
        out (Module): a new finalizer

    Raises:
        TypeError: if dtype is not a valid dtype
    """
    streampu._ext.dtype.throw_if_invalid(dtype)

    class_name = f"Finalizer_{str(dtype)}"
    class_type = getattr(streampu._ext.fin, class_name)
    return class_type(n_elmts)


__all__ = ["finalizer"]
