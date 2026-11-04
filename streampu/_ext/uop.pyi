from __future__ import annotations

import typing

import streampu._ext.core

__all__: list[str] = [
    "Unaryop_abs_float32_float32",
    "Unaryop_abs_float32_float64",
    "Unaryop_abs_float32_int16",
    "Unaryop_abs_float32_int32",
    "Unaryop_abs_float32_int64",
    "Unaryop_abs_float32_int8",
    "Unaryop_abs_float64_float32",
    "Unaryop_abs_float64_float64",
    "Unaryop_abs_float64_int16",
    "Unaryop_abs_float64_int32",
    "Unaryop_abs_float64_int64",
    "Unaryop_abs_float64_int8",
    "Unaryop_abs_int16_float32",
    "Unaryop_abs_int16_float64",
    "Unaryop_abs_int16_int16",
    "Unaryop_abs_int16_int32",
    "Unaryop_abs_int16_int64",
    "Unaryop_abs_int16_int8",
    "Unaryop_abs_int32_float32",
    "Unaryop_abs_int32_float64",
    "Unaryop_abs_int32_int16",
    "Unaryop_abs_int32_int32",
    "Unaryop_abs_int32_int64",
    "Unaryop_abs_int32_int8",
    "Unaryop_abs_int64_float32",
    "Unaryop_abs_int64_float64",
    "Unaryop_abs_int64_int16",
    "Unaryop_abs_int64_int32",
    "Unaryop_abs_int64_int64",
    "Unaryop_abs_int64_int8",
    "Unaryop_abs_int8_float32",
    "Unaryop_abs_int8_float64",
    "Unaryop_abs_int8_int16",
    "Unaryop_abs_int8_int32",
    "Unaryop_abs_int8_int64",
    "Unaryop_abs_int8_int8",
    "Unaryop_cast_float32_float32",
    "Unaryop_cast_float32_float64",
    "Unaryop_cast_float32_int16",
    "Unaryop_cast_float32_int32",
    "Unaryop_cast_float32_int64",
    "Unaryop_cast_float32_int8",
    "Unaryop_cast_float32_uint16",
    "Unaryop_cast_float32_uint32",
    "Unaryop_cast_float32_uint64",
    "Unaryop_cast_float32_uint8",
    "Unaryop_cast_float64_float32",
    "Unaryop_cast_float64_float64",
    "Unaryop_cast_float64_int16",
    "Unaryop_cast_float64_int32",
    "Unaryop_cast_float64_int64",
    "Unaryop_cast_float64_int8",
    "Unaryop_cast_float64_uint16",
    "Unaryop_cast_float64_uint32",
    "Unaryop_cast_float64_uint64",
    "Unaryop_cast_float64_uint8",
    "Unaryop_cast_int16_float32",
    "Unaryop_cast_int16_float64",
    "Unaryop_cast_int16_int16",
    "Unaryop_cast_int16_int32",
    "Unaryop_cast_int16_int64",
    "Unaryop_cast_int16_int8",
    "Unaryop_cast_int16_uint16",
    "Unaryop_cast_int16_uint32",
    "Unaryop_cast_int16_uint64",
    "Unaryop_cast_int16_uint8",
    "Unaryop_cast_int32_float32",
    "Unaryop_cast_int32_float64",
    "Unaryop_cast_int32_int16",
    "Unaryop_cast_int32_int32",
    "Unaryop_cast_int32_int64",
    "Unaryop_cast_int32_int8",
    "Unaryop_cast_int32_uint16",
    "Unaryop_cast_int32_uint32",
    "Unaryop_cast_int32_uint64",
    "Unaryop_cast_int32_uint8",
    "Unaryop_cast_int64_float32",
    "Unaryop_cast_int64_float64",
    "Unaryop_cast_int64_int16",
    "Unaryop_cast_int64_int32",
    "Unaryop_cast_int64_int64",
    "Unaryop_cast_int64_int8",
    "Unaryop_cast_int64_uint16",
    "Unaryop_cast_int64_uint32",
    "Unaryop_cast_int64_uint64",
    "Unaryop_cast_int64_uint8",
    "Unaryop_cast_int8_float32",
    "Unaryop_cast_int8_float64",
    "Unaryop_cast_int8_int16",
    "Unaryop_cast_int8_int32",
    "Unaryop_cast_int8_int64",
    "Unaryop_cast_int8_int8",
    "Unaryop_cast_int8_uint16",
    "Unaryop_cast_int8_uint32",
    "Unaryop_cast_int8_uint64",
    "Unaryop_cast_int8_uint8",
    "Unaryop_cast_uint16_float32",
    "Unaryop_cast_uint16_float64",
    "Unaryop_cast_uint16_int16",
    "Unaryop_cast_uint16_int32",
    "Unaryop_cast_uint16_int64",
    "Unaryop_cast_uint16_int8",
    "Unaryop_cast_uint16_uint16",
    "Unaryop_cast_uint16_uint32",
    "Unaryop_cast_uint16_uint64",
    "Unaryop_cast_uint16_uint8",
    "Unaryop_cast_uint32_float32",
    "Unaryop_cast_uint32_float64",
    "Unaryop_cast_uint32_int16",
    "Unaryop_cast_uint32_int32",
    "Unaryop_cast_uint32_int64",
    "Unaryop_cast_uint32_int8",
    "Unaryop_cast_uint32_uint16",
    "Unaryop_cast_uint32_uint32",
    "Unaryop_cast_uint32_uint64",
    "Unaryop_cast_uint32_uint8",
    "Unaryop_cast_uint64_float32",
    "Unaryop_cast_uint64_float64",
    "Unaryop_cast_uint64_int16",
    "Unaryop_cast_uint64_int32",
    "Unaryop_cast_uint64_int64",
    "Unaryop_cast_uint64_int8",
    "Unaryop_cast_uint64_uint16",
    "Unaryop_cast_uint64_uint32",
    "Unaryop_cast_uint64_uint64",
    "Unaryop_cast_uint64_uint8",
    "Unaryop_cast_uint8_float32",
    "Unaryop_cast_uint8_float64",
    "Unaryop_cast_uint8_int16",
    "Unaryop_cast_uint8_int32",
    "Unaryop_cast_uint8_int64",
    "Unaryop_cast_uint8_int8",
    "Unaryop_cast_uint8_uint16",
    "Unaryop_cast_uint8_uint32",
    "Unaryop_cast_uint8_uint64",
    "Unaryop_cast_uint8_uint8",
    "Unaryop_neg_float32_float32",
    "Unaryop_neg_float32_float64",
    "Unaryop_neg_float32_int16",
    "Unaryop_neg_float32_int32",
    "Unaryop_neg_float32_int64",
    "Unaryop_neg_float32_int8",
    "Unaryop_neg_float64_float32",
    "Unaryop_neg_float64_float64",
    "Unaryop_neg_float64_int16",
    "Unaryop_neg_float64_int32",
    "Unaryop_neg_float64_int64",
    "Unaryop_neg_float64_int8",
    "Unaryop_neg_int16_float32",
    "Unaryop_neg_int16_float64",
    "Unaryop_neg_int16_int16",
    "Unaryop_neg_int16_int32",
    "Unaryop_neg_int16_int64",
    "Unaryop_neg_int16_int8",
    "Unaryop_neg_int32_float32",
    "Unaryop_neg_int32_float64",
    "Unaryop_neg_int32_int16",
    "Unaryop_neg_int32_int32",
    "Unaryop_neg_int32_int64",
    "Unaryop_neg_int32_int8",
    "Unaryop_neg_int64_float32",
    "Unaryop_neg_int64_float64",
    "Unaryop_neg_int64_int16",
    "Unaryop_neg_int64_int32",
    "Unaryop_neg_int64_int64",
    "Unaryop_neg_int64_int8",
    "Unaryop_neg_int8_float32",
    "Unaryop_neg_int8_float64",
    "Unaryop_neg_int8_int16",
    "Unaryop_neg_int8_int32",
    "Unaryop_neg_int8_int64",
    "Unaryop_neg_int8_int8",
    "Unaryop_not_int16_int16",
    "Unaryop_not_int16_int32",
    "Unaryop_not_int16_int64",
    "Unaryop_not_int16_int8",
    "Unaryop_not_int16_uint16",
    "Unaryop_not_int16_uint32",
    "Unaryop_not_int16_uint64",
    "Unaryop_not_int16_uint8",
    "Unaryop_not_int32_int16",
    "Unaryop_not_int32_int32",
    "Unaryop_not_int32_int64",
    "Unaryop_not_int32_int8",
    "Unaryop_not_int32_uint16",
    "Unaryop_not_int32_uint32",
    "Unaryop_not_int32_uint64",
    "Unaryop_not_int32_uint8",
    "Unaryop_not_int64_int16",
    "Unaryop_not_int64_int32",
    "Unaryop_not_int64_int64",
    "Unaryop_not_int64_int8",
    "Unaryop_not_int64_uint16",
    "Unaryop_not_int64_uint32",
    "Unaryop_not_int64_uint64",
    "Unaryop_not_int64_uint8",
    "Unaryop_not_int8_int16",
    "Unaryop_not_int8_int32",
    "Unaryop_not_int8_int64",
    "Unaryop_not_int8_int8",
    "Unaryop_not_int8_uint16",
    "Unaryop_not_int8_uint32",
    "Unaryop_not_int8_uint64",
    "Unaryop_not_int8_uint8",
    "Unaryop_not_uint16_int16",
    "Unaryop_not_uint16_int32",
    "Unaryop_not_uint16_int64",
    "Unaryop_not_uint16_int8",
    "Unaryop_not_uint16_uint16",
    "Unaryop_not_uint16_uint32",
    "Unaryop_not_uint16_uint64",
    "Unaryop_not_uint16_uint8",
    "Unaryop_not_uint32_int16",
    "Unaryop_not_uint32_int32",
    "Unaryop_not_uint32_int64",
    "Unaryop_not_uint32_int8",
    "Unaryop_not_uint32_uint16",
    "Unaryop_not_uint32_uint32",
    "Unaryop_not_uint32_uint64",
    "Unaryop_not_uint32_uint8",
    "Unaryop_not_uint64_int16",
    "Unaryop_not_uint64_int32",
    "Unaryop_not_uint64_int64",
    "Unaryop_not_uint64_int8",
    "Unaryop_not_uint64_uint16",
    "Unaryop_not_uint64_uint32",
    "Unaryop_not_uint64_uint64",
    "Unaryop_not_uint64_uint8",
    "Unaryop_not_uint8_int16",
    "Unaryop_not_uint8_int32",
    "Unaryop_not_uint8_int64",
    "Unaryop_not_uint8_int8",
    "Unaryop_not_uint8_uint16",
    "Unaryop_not_uint8_uint32",
    "Unaryop_not_uint8_uint64",
    "Unaryop_not_uint8_uint8",
    "Unaryop_sign_float32_float32",
    "Unaryop_sign_float32_float64",
    "Unaryop_sign_float32_int16",
    "Unaryop_sign_float32_int32",
    "Unaryop_sign_float32_int64",
    "Unaryop_sign_float32_int8",
    "Unaryop_sign_float64_float32",
    "Unaryop_sign_float64_float64",
    "Unaryop_sign_float64_int16",
    "Unaryop_sign_float64_int32",
    "Unaryop_sign_float64_int64",
    "Unaryop_sign_float64_int8",
    "Unaryop_sign_int16_float32",
    "Unaryop_sign_int16_float64",
    "Unaryop_sign_int16_int16",
    "Unaryop_sign_int16_int32",
    "Unaryop_sign_int16_int64",
    "Unaryop_sign_int16_int8",
    "Unaryop_sign_int32_float32",
    "Unaryop_sign_int32_float64",
    "Unaryop_sign_int32_int16",
    "Unaryop_sign_int32_int32",
    "Unaryop_sign_int32_int64",
    "Unaryop_sign_int32_int8",
    "Unaryop_sign_int64_float32",
    "Unaryop_sign_int64_float64",
    "Unaryop_sign_int64_int16",
    "Unaryop_sign_int64_int32",
    "Unaryop_sign_int64_int64",
    "Unaryop_sign_int64_int8",
    "Unaryop_sign_int8_float32",
    "Unaryop_sign_int8_float64",
    "Unaryop_sign_int8_int16",
    "Unaryop_sign_int8_int32",
    "Unaryop_sign_int8_int64",
    "Unaryop_sign_int8_int8",
]

class Unaryop_abs_float32_float32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_abs_float32_float64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_abs_float32_int16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_abs_float32_int32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_abs_float32_int64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_abs_float32_int8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_abs_float64_float32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_abs_float64_float64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_abs_float64_int16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_abs_float64_int32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_abs_float64_int64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_abs_float64_int8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_abs_int16_float32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_abs_int16_float64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_abs_int16_int16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_abs_int16_int32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_abs_int16_int64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_abs_int16_int8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_abs_int32_float32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_abs_int32_float64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_abs_int32_int16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_abs_int32_int32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_abs_int32_int64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_abs_int32_int8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_abs_int64_float32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_abs_int64_float64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_abs_int64_int16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_abs_int64_int32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_abs_int64_int64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_abs_int64_int8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_abs_int8_float32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_abs_int8_float64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_abs_int8_int16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_abs_int8_int32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_abs_int8_int64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_abs_int8_int8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_float32_float32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_float32_float64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_float32_int16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_float32_int32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_float32_int64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_float32_int8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_float32_uint16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_float32_uint32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_float32_uint64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_float32_uint8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_float64_float32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_float64_float64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_float64_int16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_float64_int32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_float64_int64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_float64_int8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_float64_uint16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_float64_uint32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_float64_uint64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_float64_uint8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_int16_float32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_int16_float64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_int16_int16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_int16_int32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_int16_int64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_int16_int8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_int16_uint16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_int16_uint32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_int16_uint64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_int16_uint8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_int32_float32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_int32_float64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_int32_int16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_int32_int32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_int32_int64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_int32_int8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_int32_uint16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_int32_uint32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_int32_uint64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_int32_uint8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_int64_float32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_int64_float64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_int64_int16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_int64_int32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_int64_int64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_int64_int8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_int64_uint16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_int64_uint32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_int64_uint64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_int64_uint8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_int8_float32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_int8_float64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_int8_int16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_int8_int32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_int8_int64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_int8_int8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_int8_uint16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_int8_uint32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_int8_uint64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_int8_uint8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_uint16_float32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_uint16_float64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_uint16_int16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_uint16_int32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_uint16_int64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_uint16_int8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_uint16_uint16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_uint16_uint32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_uint16_uint64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_uint16_uint8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_uint32_float32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_uint32_float64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_uint32_int16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_uint32_int32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_uint32_int64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_uint32_int8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_uint32_uint16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_uint32_uint32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_uint32_uint64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_uint32_uint8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_uint64_float32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_uint64_float64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_uint64_int16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_uint64_int32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_uint64_int64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_uint64_int8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_uint64_uint16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_uint64_uint32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_uint64_uint64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_uint64_uint8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_uint8_float32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_uint8_float64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_uint8_int16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_uint8_int32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_uint8_int64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_uint8_int8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_uint8_uint16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_uint8_uint32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_uint8_uint64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_cast_uint8_uint8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_neg_float32_float32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_neg_float32_float64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_neg_float32_int16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_neg_float32_int32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_neg_float32_int64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_neg_float32_int8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_neg_float64_float32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_neg_float64_float64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_neg_float64_int16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_neg_float64_int32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_neg_float64_int64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_neg_float64_int8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_neg_int16_float32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_neg_int16_float64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_neg_int16_int16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_neg_int16_int32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_neg_int16_int64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_neg_int16_int8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_neg_int32_float32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_neg_int32_float64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_neg_int32_int16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_neg_int32_int32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_neg_int32_int64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_neg_int32_int8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_neg_int64_float32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_neg_int64_float64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_neg_int64_int16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_neg_int64_int32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_neg_int64_int64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_neg_int64_int8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_neg_int8_float32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_neg_int8_float64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_neg_int8_int16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_neg_int8_int32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_neg_int8_int64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_neg_int8_int8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_int16_int16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_int16_int32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_int16_int64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_int16_int8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_int16_uint16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_int16_uint32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_int16_uint64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_int16_uint8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_int32_int16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_int32_int32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_int32_int64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_int32_int8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_int32_uint16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_int32_uint32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_int32_uint64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_int32_uint8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_int64_int16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_int64_int32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_int64_int64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_int64_int8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_int64_uint16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_int64_uint32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_int64_uint64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_int64_uint8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_int8_int16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_int8_int32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_int8_int64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_int8_int8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_int8_uint16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_int8_uint32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_int8_uint64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_int8_uint8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_uint16_int16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_uint16_int32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_uint16_int64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_uint16_int8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_uint16_uint16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_uint16_uint32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_uint16_uint64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_uint16_uint8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_uint32_int16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_uint32_int32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_uint32_int64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_uint32_int8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_uint32_uint16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_uint32_uint32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_uint32_uint64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_uint32_uint8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_uint64_int16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_uint64_int32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_uint64_int64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_uint64_int8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_uint64_uint16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_uint64_uint32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_uint64_uint64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_uint64_uint8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_uint8_int16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_uint8_int32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_uint8_int64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_uint8_int8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_uint8_uint16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_uint8_uint32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_uint8_uint64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_not_uint8_uint8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_sign_float32_float32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_sign_float32_float64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_sign_float32_int16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_sign_float32_int32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_sign_float32_int64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_sign_float32_int8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_sign_float64_float32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_sign_float64_float64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_sign_float64_int16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_sign_float64_int32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_sign_float64_int64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_sign_float64_int8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_sign_int16_float32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_sign_int16_float64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_sign_int16_int16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_sign_int16_int32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_sign_int16_int64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_sign_int16_int8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_sign_int32_float32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_sign_int32_float64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_sign_int32_int16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_sign_int32_int32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_sign_int32_int64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_sign_int32_int8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_sign_int64_float32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_sign_int64_float64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_sign_int64_int16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_sign_int64_int32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_sign_int64_int64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_sign_int64_int8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_sign_int8_float32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_sign_int8_float64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_sign_int8_int16(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_sign_int8_int32(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_sign_int8_int64(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Unaryop_sign_int8_int8(streampu._ext.core.Module):
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...
