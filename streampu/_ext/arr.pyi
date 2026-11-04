from __future__ import annotations

import typing

import numpy
import numpy.typing

import streampu._ext.sfl

__all__: list[str] = [
    "Array_float32",
    "Array_float64",
    "Array_int16",
    "Array_int32",
    "Array_int64",
    "Array_int8",
    "Array_uint16",
    "Array_uint32",
    "Array_uint64",
    "Array_uint8",
]

class Array_float32(streampu._ext.sfl.Stateful):
    def __init__(self, data: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None: ...

class Array_float64(streampu._ext.sfl.Stateful):
    def __init__(self, data: typing.Annotated[numpy.typing.ArrayLike, numpy.float64]) -> None: ...

class Array_int16(streampu._ext.sfl.Stateful):
    def __init__(self, data: typing.Annotated[numpy.typing.ArrayLike, numpy.int16]) -> None: ...

class Array_int32(streampu._ext.sfl.Stateful):
    def __init__(self, data: typing.Annotated[numpy.typing.ArrayLike, numpy.int32]) -> None: ...

class Array_int64(streampu._ext.sfl.Stateful):
    def __init__(self, data: typing.Annotated[numpy.typing.ArrayLike, numpy.int64]) -> None: ...

class Array_int8(streampu._ext.sfl.Stateful):
    def __init__(self, data: typing.Annotated[numpy.typing.ArrayLike, numpy.int8]) -> None: ...

class Array_uint16(streampu._ext.sfl.Stateful):
    def __init__(self, data: typing.Annotated[numpy.typing.ArrayLike, numpy.uint16]) -> None: ...

class Array_uint32(streampu._ext.sfl.Stateful):
    def __init__(self, data: typing.Annotated[numpy.typing.ArrayLike, numpy.uint32]) -> None: ...

class Array_uint64(streampu._ext.sfl.Stateful):
    def __init__(self, data: typing.Annotated[numpy.typing.ArrayLike, numpy.uint64]) -> None: ...

class Array_uint8(streampu._ext.sfl.Stateful):
    def __init__(self, data: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None: ...
