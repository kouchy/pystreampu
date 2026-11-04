from __future__ import annotations

import typing

import streampu._ext.interfaces
import streampu._ext.sfl

__all__: list[str] = [
    "Sink_NO_float32",
    "Sink_NO_float64",
    "Sink_NO_int16",
    "Sink_NO_int32",
    "Sink_NO_int64",
    "Sink_NO_int8",
    "Sink_NO_uint16",
    "Sink_NO_uint32",
    "Sink_NO_uint64",
    "Sink_NO_uint8",
    "Sink_float32",
    "Sink_float64",
    "Sink_int16",
    "Sink_int32",
    "Sink_int64",
    "Sink_int8",
    "Sink_uint16",
    "Sink_uint32",
    "Sink_uint64",
    "Sink_uint8",
    "Sink_user_binary_float32",
    "Sink_user_binary_float64",
    "Sink_user_binary_int16",
    "Sink_user_binary_int32",
    "Sink_user_binary_int64",
    "Sink_user_binary_int8",
    "Sink_user_binary_uint16",
    "Sink_user_binary_uint32",
    "Sink_user_binary_uint64",
    "Sink_user_binary_uint8",
]

class Sink_NO_float32(Sink_float32):
    def __init__(self, max_data_size: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Sink_NO_float64(Sink_float64):
    def __init__(self, max_data_size: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Sink_NO_int16(Sink_int16):
    def __init__(self, max_data_size: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Sink_NO_int32(Sink_int32):
    def __init__(self, max_data_size: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Sink_NO_int64(Sink_int64):
    def __init__(self, max_data_size: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Sink_NO_int8(Sink_int8):
    def __init__(self, max_data_size: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Sink_NO_uint16(Sink_uint16):
    def __init__(self, max_data_size: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Sink_NO_uint32(Sink_uint32):
    def __init__(self, max_data_size: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Sink_NO_uint64(Sink_uint64):
    def __init__(self, max_data_size: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Sink_NO_uint8(Sink_uint8):
    def __init__(self, max_data_size: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Sink_float32(streampu._ext.sfl.Stateful, streampu._ext.interfaces.Interface_reset):
    def __init__(self, max_data_size: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Sink_float64(streampu._ext.sfl.Stateful, streampu._ext.interfaces.Interface_reset):
    def __init__(self, max_data_size: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Sink_int16(streampu._ext.sfl.Stateful, streampu._ext.interfaces.Interface_reset):
    def __init__(self, max_data_size: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Sink_int32(streampu._ext.sfl.Stateful, streampu._ext.interfaces.Interface_reset):
    def __init__(self, max_data_size: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Sink_int64(streampu._ext.sfl.Stateful, streampu._ext.interfaces.Interface_reset):
    def __init__(self, max_data_size: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Sink_int8(streampu._ext.sfl.Stateful, streampu._ext.interfaces.Interface_reset):
    def __init__(self, max_data_size: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Sink_uint16(streampu._ext.sfl.Stateful, streampu._ext.interfaces.Interface_reset):
    def __init__(self, max_data_size: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Sink_uint32(streampu._ext.sfl.Stateful, streampu._ext.interfaces.Interface_reset):
    def __init__(self, max_data_size: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Sink_uint64(streampu._ext.sfl.Stateful, streampu._ext.interfaces.Interface_reset):
    def __init__(self, max_data_size: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Sink_uint8(streampu._ext.sfl.Stateful, streampu._ext.interfaces.Interface_reset):
    def __init__(self, max_data_size: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Sink_user_binary_float32(Sink_float32):
    def __init__(self, max_data_size: typing.SupportsInt | typing.SupportsIndex, filename: str) -> None: ...

class Sink_user_binary_float64(Sink_float64):
    def __init__(self, max_data_size: typing.SupportsInt | typing.SupportsIndex, filename: str) -> None: ...

class Sink_user_binary_int16(Sink_int16):
    def __init__(self, max_data_size: typing.SupportsInt | typing.SupportsIndex, filename: str) -> None: ...

class Sink_user_binary_int32(Sink_int32):
    def __init__(self, max_data_size: typing.SupportsInt | typing.SupportsIndex, filename: str) -> None: ...

class Sink_user_binary_int64(Sink_int64):
    def __init__(self, max_data_size: typing.SupportsInt | typing.SupportsIndex, filename: str) -> None: ...

class Sink_user_binary_int8(Sink_int8):
    def __init__(self, max_data_size: typing.SupportsInt | typing.SupportsIndex, filename: str) -> None: ...

class Sink_user_binary_uint16(Sink_uint16):
    def __init__(self, max_data_size: typing.SupportsInt | typing.SupportsIndex, filename: str) -> None: ...

class Sink_user_binary_uint32(Sink_uint32):
    def __init__(self, max_data_size: typing.SupportsInt | typing.SupportsIndex, filename: str) -> None: ...

class Sink_user_binary_uint64(Sink_uint64):
    def __init__(self, max_data_size: typing.SupportsInt | typing.SupportsIndex, filename: str) -> None: ...

class Sink_user_binary_uint8(Sink_uint8):
    def __init__(self, max_data_size: typing.SupportsInt | typing.SupportsIndex, filename: str) -> None: ...
