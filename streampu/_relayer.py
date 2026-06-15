# -*- coding: utf-8 -*-
import streampu._ext
from streampu._ext import int32


def relayer(n_elmts: int, ns: int = 0, dtype: streampu._ext.dtype = int32):
    """Build a delayer.

    Args:
        n_elmts (int): number of elements
        ns (int): sleep time in nanoseconds
        dtype (streampu._ext.dtype): Data type

    Returns:
        out (Module): a new delayer

    Raises:
        TypeError: if dtype is not a valid dtype
    """
    streampu._ext.dtype.throw_if_invalid(dtype)

    class_name = f"Relayer_{str(dtype)}"
    class_type = getattr(streampu._ext.rel, class_name)
    return class_type(n_elmts, ns)


__all__ = ["relayer"]
