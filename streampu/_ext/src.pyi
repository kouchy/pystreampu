from __future__ import annotations

import typing

import streampu._ext.interfaces
import streampu._ext.sfl

__all__: list[str] = [
    "Source_float32",
    "Source_float64",
    "Source_int16",
    "Source_int32",
    "Source_int64",
    "Source_int8",
    "Source_random_float32",
    "Source_random_float64",
    "Source_random_int16",
    "Source_random_int32",
    "Source_random_int64",
    "Source_random_int8",
    "Source_random_uint16",
    "Source_random_uint32",
    "Source_random_uint64",
    "Source_random_uint8",
    "Source_uint16",
    "Source_uint32",
    "Source_uint64",
    "Source_uint8",
    "Source_user_binary_float32",
    "Source_user_binary_float64",
    "Source_user_binary_int16",
    "Source_user_binary_int32",
    "Source_user_binary_int64",
    "Source_user_binary_int8",
    "Source_user_binary_uint16",
    "Source_user_binary_uint32",
    "Source_user_binary_uint64",
    "Source_user_binary_uint8",
    "Source_user_float32",
    "Source_user_float64",
    "Source_user_int16",
    "Source_user_int32",
    "Source_user_int64",
    "Source_user_int8",
    "Source_user_uint16",
    "Source_user_uint32",
    "Source_user_uint64",
    "Source_user_uint8",
]

class Source_float32(
    streampu._ext.sfl.Stateful,
    streampu._ext.interfaces.Interface_set_seed,
    streampu._ext.interfaces.Interface_is_done,
    streampu._ext.interfaces.Interface_reset,
):
    def __init__(self, max_data_size: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Source_float64(
    streampu._ext.sfl.Stateful,
    streampu._ext.interfaces.Interface_set_seed,
    streampu._ext.interfaces.Interface_is_done,
    streampu._ext.interfaces.Interface_reset,
):
    def __init__(self, max_data_size: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Source_int16(
    streampu._ext.sfl.Stateful,
    streampu._ext.interfaces.Interface_set_seed,
    streampu._ext.interfaces.Interface_is_done,
    streampu._ext.interfaces.Interface_reset,
):
    def __init__(self, max_data_size: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Source_int32(
    streampu._ext.sfl.Stateful,
    streampu._ext.interfaces.Interface_set_seed,
    streampu._ext.interfaces.Interface_is_done,
    streampu._ext.interfaces.Interface_reset,
):
    def __init__(self, max_data_size: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Source_int64(
    streampu._ext.sfl.Stateful,
    streampu._ext.interfaces.Interface_set_seed,
    streampu._ext.interfaces.Interface_is_done,
    streampu._ext.interfaces.Interface_reset,
):
    def __init__(self, max_data_size: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Source_int8(
    streampu._ext.sfl.Stateful,
    streampu._ext.interfaces.Interface_set_seed,
    streampu._ext.interfaces.Interface_is_done,
    streampu._ext.interfaces.Interface_reset,
):
    def __init__(self, max_data_size: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Source_random_float32(Source_float32):
    def __init__(
        self,
        max_data_size: typing.SupportsInt | typing.SupportsIndex,
        seed: typing.SupportsInt | typing.SupportsIndex = 0,
    ) -> None: ...

class Source_random_float64(Source_float64):
    def __init__(
        self,
        max_data_size: typing.SupportsInt | typing.SupportsIndex,
        seed: typing.SupportsInt | typing.SupportsIndex = 0,
    ) -> None: ...

class Source_random_int16(Source_int16):
    def __init__(
        self,
        max_data_size: typing.SupportsInt | typing.SupportsIndex,
        seed: typing.SupportsInt | typing.SupportsIndex = 0,
    ) -> None: ...

class Source_random_int32(Source_int32):
    def __init__(
        self,
        max_data_size: typing.SupportsInt | typing.SupportsIndex,
        seed: typing.SupportsInt | typing.SupportsIndex = 0,
    ) -> None: ...

class Source_random_int64(Source_int64):
    def __init__(
        self,
        max_data_size: typing.SupportsInt | typing.SupportsIndex,
        seed: typing.SupportsInt | typing.SupportsIndex = 0,
    ) -> None: ...

class Source_random_int8(Source_int8):
    def __init__(
        self,
        max_data_size: typing.SupportsInt | typing.SupportsIndex,
        seed: typing.SupportsInt | typing.SupportsIndex = 0,
    ) -> None: ...

class Source_random_uint16(Source_uint16):
    def __init__(
        self,
        max_data_size: typing.SupportsInt | typing.SupportsIndex,
        seed: typing.SupportsInt | typing.SupportsIndex = 0,
    ) -> None: ...

class Source_random_uint32(Source_uint32):
    def __init__(
        self,
        max_data_size: typing.SupportsInt | typing.SupportsIndex,
        seed: typing.SupportsInt | typing.SupportsIndex = 0,
    ) -> None: ...

class Source_random_uint64(Source_uint64):
    def __init__(
        self,
        max_data_size: typing.SupportsInt | typing.SupportsIndex,
        seed: typing.SupportsInt | typing.SupportsIndex = 0,
    ) -> None: ...

class Source_random_uint8(Source_uint8):
    def __init__(
        self,
        max_data_size: typing.SupportsInt | typing.SupportsIndex,
        seed: typing.SupportsInt | typing.SupportsIndex = 0,
    ) -> None: ...

class Source_uint16(
    streampu._ext.sfl.Stateful,
    streampu._ext.interfaces.Interface_set_seed,
    streampu._ext.interfaces.Interface_is_done,
    streampu._ext.interfaces.Interface_reset,
):
    def __init__(self, max_data_size: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Source_uint32(
    streampu._ext.sfl.Stateful,
    streampu._ext.interfaces.Interface_set_seed,
    streampu._ext.interfaces.Interface_is_done,
    streampu._ext.interfaces.Interface_reset,
):
    def __init__(self, max_data_size: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Source_uint64(
    streampu._ext.sfl.Stateful,
    streampu._ext.interfaces.Interface_set_seed,
    streampu._ext.interfaces.Interface_is_done,
    streampu._ext.interfaces.Interface_reset,
):
    def __init__(self, max_data_size: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Source_uint8(
    streampu._ext.sfl.Stateful,
    streampu._ext.interfaces.Interface_set_seed,
    streampu._ext.interfaces.Interface_is_done,
    streampu._ext.interfaces.Interface_reset,
):
    def __init__(self, max_data_size: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Source_user_binary_float32(Source_float32):
    def __init__(
        self,
        max_data_size: typing.SupportsInt | typing.SupportsIndex,
        filename: str,
        auto_reset: bool = True,
        fifo_mode: bool = False,
    ) -> None: ...

class Source_user_binary_float64(Source_float64):
    def __init__(
        self,
        max_data_size: typing.SupportsInt | typing.SupportsIndex,
        filename: str,
        auto_reset: bool = True,
        fifo_mode: bool = False,
    ) -> None: ...

class Source_user_binary_int16(Source_int16):
    def __init__(
        self,
        max_data_size: typing.SupportsInt | typing.SupportsIndex,
        filename: str,
        auto_reset: bool = True,
        fifo_mode: bool = False,
    ) -> None: ...

class Source_user_binary_int32(Source_int32):
    def __init__(
        self,
        max_data_size: typing.SupportsInt | typing.SupportsIndex,
        filename: str,
        auto_reset: bool = True,
        fifo_mode: bool = False,
    ) -> None: ...

class Source_user_binary_int64(Source_int64):
    def __init__(
        self,
        max_data_size: typing.SupportsInt | typing.SupportsIndex,
        filename: str,
        auto_reset: bool = True,
        fifo_mode: bool = False,
    ) -> None: ...

class Source_user_binary_int8(Source_int8):
    def __init__(
        self,
        max_data_size: typing.SupportsInt | typing.SupportsIndex,
        filename: str,
        auto_reset: bool = True,
        fifo_mode: bool = False,
    ) -> None: ...

class Source_user_binary_uint16(Source_uint16):
    def __init__(
        self,
        max_data_size: typing.SupportsInt | typing.SupportsIndex,
        filename: str,
        auto_reset: bool = True,
        fifo_mode: bool = False,
    ) -> None: ...

class Source_user_binary_uint32(Source_uint32):
    def __init__(
        self,
        max_data_size: typing.SupportsInt | typing.SupportsIndex,
        filename: str,
        auto_reset: bool = True,
        fifo_mode: bool = False,
    ) -> None: ...

class Source_user_binary_uint64(Source_uint64):
    def __init__(
        self,
        max_data_size: typing.SupportsInt | typing.SupportsIndex,
        filename: str,
        auto_reset: bool = True,
        fifo_mode: bool = False,
    ) -> None: ...

class Source_user_binary_uint8(Source_uint8):
    def __init__(
        self,
        max_data_size: typing.SupportsInt | typing.SupportsIndex,
        filename: str,
        auto_reset: bool = True,
        fifo_mode: bool = False,
    ) -> None: ...

class Source_user_float32(Source_float32):
    def __init__(
        self,
        max_data_size: typing.SupportsInt | typing.SupportsIndex,
        filename: str,
        auto_reset: bool = True,
        start_idx: typing.SupportsInt | typing.SupportsIndex = 0,
    ) -> None: ...

class Source_user_float64(Source_float64):
    def __init__(
        self,
        max_data_size: typing.SupportsInt | typing.SupportsIndex,
        filename: str,
        auto_reset: bool = True,
        start_idx: typing.SupportsInt | typing.SupportsIndex = 0,
    ) -> None: ...

class Source_user_int16(Source_int16):
    def __init__(
        self,
        max_data_size: typing.SupportsInt | typing.SupportsIndex,
        filename: str,
        auto_reset: bool = True,
        start_idx: typing.SupportsInt | typing.SupportsIndex = 0,
    ) -> None: ...

class Source_user_int32(Source_int32):
    def __init__(
        self,
        max_data_size: typing.SupportsInt | typing.SupportsIndex,
        filename: str,
        auto_reset: bool = True,
        start_idx: typing.SupportsInt | typing.SupportsIndex = 0,
    ) -> None: ...

class Source_user_int64(Source_int64):
    def __init__(
        self,
        max_data_size: typing.SupportsInt | typing.SupportsIndex,
        filename: str,
        auto_reset: bool = True,
        start_idx: typing.SupportsInt | typing.SupportsIndex = 0,
    ) -> None: ...

class Source_user_int8(Source_int8):
    def __init__(
        self,
        max_data_size: typing.SupportsInt | typing.SupportsIndex,
        filename: str,
        auto_reset: bool = True,
        start_idx: typing.SupportsInt | typing.SupportsIndex = 0,
    ) -> None: ...

class Source_user_uint16(Source_uint16):
    def __init__(
        self,
        max_data_size: typing.SupportsInt | typing.SupportsIndex,
        filename: str,
        auto_reset: bool = True,
        start_idx: typing.SupportsInt | typing.SupportsIndex = 0,
    ) -> None: ...

class Source_user_uint32(Source_uint32):
    def __init__(
        self,
        max_data_size: typing.SupportsInt | typing.SupportsIndex,
        filename: str,
        auto_reset: bool = True,
        start_idx: typing.SupportsInt | typing.SupportsIndex = 0,
    ) -> None: ...

class Source_user_uint64(Source_uint64):
    def __init__(
        self,
        max_data_size: typing.SupportsInt | typing.SupportsIndex,
        filename: str,
        auto_reset: bool = True,
        start_idx: typing.SupportsInt | typing.SupportsIndex = 0,
    ) -> None: ...

class Source_user_uint8(Source_uint8):
    def __init__(
        self,
        max_data_size: typing.SupportsInt | typing.SupportsIndex,
        filename: str,
        auto_reset: bool = True,
        start_idx: typing.SupportsInt | typing.SupportsIndex = 0,
    ) -> None: ...
