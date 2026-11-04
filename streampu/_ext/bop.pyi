from __future__ import annotations

import typing

import streampu._ext.core

__all__: list[str] = [
    "Binaryop_add_float32_float32",
    "Binaryop_add_float32_float64",
    "Binaryop_add_float32_int16",
    "Binaryop_add_float32_int32",
    "Binaryop_add_float32_int64",
    "Binaryop_add_float32_int8",
    "Binaryop_add_float32_uint16",
    "Binaryop_add_float32_uint32",
    "Binaryop_add_float32_uint64",
    "Binaryop_add_float32_uint8",
    "Binaryop_add_float64_float32",
    "Binaryop_add_float64_float64",
    "Binaryop_add_float64_int16",
    "Binaryop_add_float64_int32",
    "Binaryop_add_float64_int64",
    "Binaryop_add_float64_int8",
    "Binaryop_add_float64_uint16",
    "Binaryop_add_float64_uint32",
    "Binaryop_add_float64_uint64",
    "Binaryop_add_float64_uint8",
    "Binaryop_add_int16_float32",
    "Binaryop_add_int16_float64",
    "Binaryop_add_int16_int16",
    "Binaryop_add_int16_int32",
    "Binaryop_add_int16_int64",
    "Binaryop_add_int16_int8",
    "Binaryop_add_int16_uint16",
    "Binaryop_add_int16_uint32",
    "Binaryop_add_int16_uint64",
    "Binaryop_add_int16_uint8",
    "Binaryop_add_int32_float32",
    "Binaryop_add_int32_float64",
    "Binaryop_add_int32_int16",
    "Binaryop_add_int32_int32",
    "Binaryop_add_int32_int64",
    "Binaryop_add_int32_int8",
    "Binaryop_add_int32_uint16",
    "Binaryop_add_int32_uint32",
    "Binaryop_add_int32_uint64",
    "Binaryop_add_int32_uint8",
    "Binaryop_add_int64_float32",
    "Binaryop_add_int64_float64",
    "Binaryop_add_int64_int16",
    "Binaryop_add_int64_int32",
    "Binaryop_add_int64_int64",
    "Binaryop_add_int64_int8",
    "Binaryop_add_int64_uint16",
    "Binaryop_add_int64_uint32",
    "Binaryop_add_int64_uint64",
    "Binaryop_add_int64_uint8",
    "Binaryop_add_int8_float32",
    "Binaryop_add_int8_float64",
    "Binaryop_add_int8_int16",
    "Binaryop_add_int8_int32",
    "Binaryop_add_int8_int64",
    "Binaryop_add_int8_int8",
    "Binaryop_add_int8_uint16",
    "Binaryop_add_int8_uint32",
    "Binaryop_add_int8_uint64",
    "Binaryop_add_int8_uint8",
    "Binaryop_add_uint16_float32",
    "Binaryop_add_uint16_float64",
    "Binaryop_add_uint16_int16",
    "Binaryop_add_uint16_int32",
    "Binaryop_add_uint16_int64",
    "Binaryop_add_uint16_int8",
    "Binaryop_add_uint16_uint16",
    "Binaryop_add_uint16_uint32",
    "Binaryop_add_uint16_uint64",
    "Binaryop_add_uint16_uint8",
    "Binaryop_add_uint32_float32",
    "Binaryop_add_uint32_float64",
    "Binaryop_add_uint32_int16",
    "Binaryop_add_uint32_int32",
    "Binaryop_add_uint32_int64",
    "Binaryop_add_uint32_int8",
    "Binaryop_add_uint32_uint16",
    "Binaryop_add_uint32_uint32",
    "Binaryop_add_uint32_uint64",
    "Binaryop_add_uint32_uint8",
    "Binaryop_add_uint64_float32",
    "Binaryop_add_uint64_float64",
    "Binaryop_add_uint64_int16",
    "Binaryop_add_uint64_int32",
    "Binaryop_add_uint64_int64",
    "Binaryop_add_uint64_int8",
    "Binaryop_add_uint64_uint16",
    "Binaryop_add_uint64_uint32",
    "Binaryop_add_uint64_uint64",
    "Binaryop_add_uint64_uint8",
    "Binaryop_add_uint8_float32",
    "Binaryop_add_uint8_float64",
    "Binaryop_add_uint8_int16",
    "Binaryop_add_uint8_int32",
    "Binaryop_add_uint8_int64",
    "Binaryop_add_uint8_int8",
    "Binaryop_add_uint8_uint16",
    "Binaryop_add_uint8_uint32",
    "Binaryop_add_uint8_uint64",
    "Binaryop_add_uint8_uint8",
    "Binaryop_and_int16_float32",
    "Binaryop_and_int16_float64",
    "Binaryop_and_int16_int16",
    "Binaryop_and_int16_int32",
    "Binaryop_and_int16_int64",
    "Binaryop_and_int16_int8",
    "Binaryop_and_int16_uint16",
    "Binaryop_and_int16_uint32",
    "Binaryop_and_int16_uint64",
    "Binaryop_and_int16_uint8",
    "Binaryop_and_int32_float32",
    "Binaryop_and_int32_float64",
    "Binaryop_and_int32_int16",
    "Binaryop_and_int32_int32",
    "Binaryop_and_int32_int64",
    "Binaryop_and_int32_int8",
    "Binaryop_and_int32_uint16",
    "Binaryop_and_int32_uint32",
    "Binaryop_and_int32_uint64",
    "Binaryop_and_int32_uint8",
    "Binaryop_and_int64_float32",
    "Binaryop_and_int64_float64",
    "Binaryop_and_int64_int16",
    "Binaryop_and_int64_int32",
    "Binaryop_and_int64_int64",
    "Binaryop_and_int64_int8",
    "Binaryop_and_int64_uint16",
    "Binaryop_and_int64_uint32",
    "Binaryop_and_int64_uint64",
    "Binaryop_and_int64_uint8",
    "Binaryop_and_int8_float32",
    "Binaryop_and_int8_float64",
    "Binaryop_and_int8_int16",
    "Binaryop_and_int8_int32",
    "Binaryop_and_int8_int64",
    "Binaryop_and_int8_int8",
    "Binaryop_and_int8_uint16",
    "Binaryop_and_int8_uint32",
    "Binaryop_and_int8_uint64",
    "Binaryop_and_int8_uint8",
    "Binaryop_and_uint16_float32",
    "Binaryop_and_uint16_float64",
    "Binaryop_and_uint16_int16",
    "Binaryop_and_uint16_int32",
    "Binaryop_and_uint16_int64",
    "Binaryop_and_uint16_int8",
    "Binaryop_and_uint16_uint16",
    "Binaryop_and_uint16_uint32",
    "Binaryop_and_uint16_uint64",
    "Binaryop_and_uint16_uint8",
    "Binaryop_and_uint32_float32",
    "Binaryop_and_uint32_float64",
    "Binaryop_and_uint32_int16",
    "Binaryop_and_uint32_int32",
    "Binaryop_and_uint32_int64",
    "Binaryop_and_uint32_int8",
    "Binaryop_and_uint32_uint16",
    "Binaryop_and_uint32_uint32",
    "Binaryop_and_uint32_uint64",
    "Binaryop_and_uint32_uint8",
    "Binaryop_and_uint64_float32",
    "Binaryop_and_uint64_float64",
    "Binaryop_and_uint64_int16",
    "Binaryop_and_uint64_int32",
    "Binaryop_and_uint64_int64",
    "Binaryop_and_uint64_int8",
    "Binaryop_and_uint64_uint16",
    "Binaryop_and_uint64_uint32",
    "Binaryop_and_uint64_uint64",
    "Binaryop_and_uint64_uint8",
    "Binaryop_and_uint8_float32",
    "Binaryop_and_uint8_float64",
    "Binaryop_and_uint8_int16",
    "Binaryop_and_uint8_int32",
    "Binaryop_and_uint8_int64",
    "Binaryop_and_uint8_int8",
    "Binaryop_and_uint8_uint16",
    "Binaryop_and_uint8_uint32",
    "Binaryop_and_uint8_uint64",
    "Binaryop_and_uint8_uint8",
    "Binaryop_div_float32_float32",
    "Binaryop_div_float32_float64",
    "Binaryop_div_float32_int16",
    "Binaryop_div_float32_int32",
    "Binaryop_div_float32_int64",
    "Binaryop_div_float32_int8",
    "Binaryop_div_float32_uint16",
    "Binaryop_div_float32_uint32",
    "Binaryop_div_float32_uint64",
    "Binaryop_div_float32_uint8",
    "Binaryop_div_float64_float32",
    "Binaryop_div_float64_float64",
    "Binaryop_div_float64_int16",
    "Binaryop_div_float64_int32",
    "Binaryop_div_float64_int64",
    "Binaryop_div_float64_int8",
    "Binaryop_div_float64_uint16",
    "Binaryop_div_float64_uint32",
    "Binaryop_div_float64_uint64",
    "Binaryop_div_float64_uint8",
    "Binaryop_div_int16_float32",
    "Binaryop_div_int16_float64",
    "Binaryop_div_int16_int16",
    "Binaryop_div_int16_int32",
    "Binaryop_div_int16_int64",
    "Binaryop_div_int16_int8",
    "Binaryop_div_int16_uint16",
    "Binaryop_div_int16_uint32",
    "Binaryop_div_int16_uint64",
    "Binaryop_div_int16_uint8",
    "Binaryop_div_int32_float32",
    "Binaryop_div_int32_float64",
    "Binaryop_div_int32_int16",
    "Binaryop_div_int32_int32",
    "Binaryop_div_int32_int64",
    "Binaryop_div_int32_int8",
    "Binaryop_div_int32_uint16",
    "Binaryop_div_int32_uint32",
    "Binaryop_div_int32_uint64",
    "Binaryop_div_int32_uint8",
    "Binaryop_div_int64_float32",
    "Binaryop_div_int64_float64",
    "Binaryop_div_int64_int16",
    "Binaryop_div_int64_int32",
    "Binaryop_div_int64_int64",
    "Binaryop_div_int64_int8",
    "Binaryop_div_int64_uint16",
    "Binaryop_div_int64_uint32",
    "Binaryop_div_int64_uint64",
    "Binaryop_div_int64_uint8",
    "Binaryop_div_int8_float32",
    "Binaryop_div_int8_float64",
    "Binaryop_div_int8_int16",
    "Binaryop_div_int8_int32",
    "Binaryop_div_int8_int64",
    "Binaryop_div_int8_int8",
    "Binaryop_div_int8_uint16",
    "Binaryop_div_int8_uint32",
    "Binaryop_div_int8_uint64",
    "Binaryop_div_int8_uint8",
    "Binaryop_div_uint16_float32",
    "Binaryop_div_uint16_float64",
    "Binaryop_div_uint16_int16",
    "Binaryop_div_uint16_int32",
    "Binaryop_div_uint16_int64",
    "Binaryop_div_uint16_int8",
    "Binaryop_div_uint16_uint16",
    "Binaryop_div_uint16_uint32",
    "Binaryop_div_uint16_uint64",
    "Binaryop_div_uint16_uint8",
    "Binaryop_div_uint32_float32",
    "Binaryop_div_uint32_float64",
    "Binaryop_div_uint32_int16",
    "Binaryop_div_uint32_int32",
    "Binaryop_div_uint32_int64",
    "Binaryop_div_uint32_int8",
    "Binaryop_div_uint32_uint16",
    "Binaryop_div_uint32_uint32",
    "Binaryop_div_uint32_uint64",
    "Binaryop_div_uint32_uint8",
    "Binaryop_div_uint64_float32",
    "Binaryop_div_uint64_float64",
    "Binaryop_div_uint64_int16",
    "Binaryop_div_uint64_int32",
    "Binaryop_div_uint64_int64",
    "Binaryop_div_uint64_int8",
    "Binaryop_div_uint64_uint16",
    "Binaryop_div_uint64_uint32",
    "Binaryop_div_uint64_uint64",
    "Binaryop_div_uint64_uint8",
    "Binaryop_div_uint8_float32",
    "Binaryop_div_uint8_float64",
    "Binaryop_div_uint8_int16",
    "Binaryop_div_uint8_int32",
    "Binaryop_div_uint8_int64",
    "Binaryop_div_uint8_int8",
    "Binaryop_div_uint8_uint16",
    "Binaryop_div_uint8_uint32",
    "Binaryop_div_uint8_uint64",
    "Binaryop_div_uint8_uint8",
    "Binaryop_eq_float32_float32",
    "Binaryop_eq_float32_float64",
    "Binaryop_eq_float32_int16",
    "Binaryop_eq_float32_int32",
    "Binaryop_eq_float32_int64",
    "Binaryop_eq_float32_int8",
    "Binaryop_eq_float32_uint16",
    "Binaryop_eq_float32_uint32",
    "Binaryop_eq_float32_uint64",
    "Binaryop_eq_float32_uint8",
    "Binaryop_eq_float64_float32",
    "Binaryop_eq_float64_float64",
    "Binaryop_eq_float64_int16",
    "Binaryop_eq_float64_int32",
    "Binaryop_eq_float64_int64",
    "Binaryop_eq_float64_int8",
    "Binaryop_eq_float64_uint16",
    "Binaryop_eq_float64_uint32",
    "Binaryop_eq_float64_uint64",
    "Binaryop_eq_float64_uint8",
    "Binaryop_eq_int16_float32",
    "Binaryop_eq_int16_float64",
    "Binaryop_eq_int16_int16",
    "Binaryop_eq_int16_int32",
    "Binaryop_eq_int16_int64",
    "Binaryop_eq_int16_int8",
    "Binaryop_eq_int16_uint16",
    "Binaryop_eq_int16_uint32",
    "Binaryop_eq_int16_uint64",
    "Binaryop_eq_int16_uint8",
    "Binaryop_eq_int32_float32",
    "Binaryop_eq_int32_float64",
    "Binaryop_eq_int32_int16",
    "Binaryop_eq_int32_int32",
    "Binaryop_eq_int32_int64",
    "Binaryop_eq_int32_int8",
    "Binaryop_eq_int32_uint16",
    "Binaryop_eq_int32_uint32",
    "Binaryop_eq_int32_uint64",
    "Binaryop_eq_int32_uint8",
    "Binaryop_eq_int64_float32",
    "Binaryop_eq_int64_float64",
    "Binaryop_eq_int64_int16",
    "Binaryop_eq_int64_int32",
    "Binaryop_eq_int64_int64",
    "Binaryop_eq_int64_int8",
    "Binaryop_eq_int64_uint16",
    "Binaryop_eq_int64_uint32",
    "Binaryop_eq_int64_uint64",
    "Binaryop_eq_int64_uint8",
    "Binaryop_eq_int8_float32",
    "Binaryop_eq_int8_float64",
    "Binaryop_eq_int8_int16",
    "Binaryop_eq_int8_int32",
    "Binaryop_eq_int8_int64",
    "Binaryop_eq_int8_int8",
    "Binaryop_eq_int8_uint16",
    "Binaryop_eq_int8_uint32",
    "Binaryop_eq_int8_uint64",
    "Binaryop_eq_int8_uint8",
    "Binaryop_eq_uint16_float32",
    "Binaryop_eq_uint16_float64",
    "Binaryop_eq_uint16_int16",
    "Binaryop_eq_uint16_int32",
    "Binaryop_eq_uint16_int64",
    "Binaryop_eq_uint16_int8",
    "Binaryop_eq_uint16_uint16",
    "Binaryop_eq_uint16_uint32",
    "Binaryop_eq_uint16_uint64",
    "Binaryop_eq_uint16_uint8",
    "Binaryop_eq_uint32_float32",
    "Binaryop_eq_uint32_float64",
    "Binaryop_eq_uint32_int16",
    "Binaryop_eq_uint32_int32",
    "Binaryop_eq_uint32_int64",
    "Binaryop_eq_uint32_int8",
    "Binaryop_eq_uint32_uint16",
    "Binaryop_eq_uint32_uint32",
    "Binaryop_eq_uint32_uint64",
    "Binaryop_eq_uint32_uint8",
    "Binaryop_eq_uint64_float32",
    "Binaryop_eq_uint64_float64",
    "Binaryop_eq_uint64_int16",
    "Binaryop_eq_uint64_int32",
    "Binaryop_eq_uint64_int64",
    "Binaryop_eq_uint64_int8",
    "Binaryop_eq_uint64_uint16",
    "Binaryop_eq_uint64_uint32",
    "Binaryop_eq_uint64_uint64",
    "Binaryop_eq_uint64_uint8",
    "Binaryop_eq_uint8_float32",
    "Binaryop_eq_uint8_float64",
    "Binaryop_eq_uint8_int16",
    "Binaryop_eq_uint8_int32",
    "Binaryop_eq_uint8_int64",
    "Binaryop_eq_uint8_int8",
    "Binaryop_eq_uint8_uint16",
    "Binaryop_eq_uint8_uint32",
    "Binaryop_eq_uint8_uint64",
    "Binaryop_eq_uint8_uint8",
    "Binaryop_ge_float32_float32",
    "Binaryop_ge_float32_float64",
    "Binaryop_ge_float32_int16",
    "Binaryop_ge_float32_int32",
    "Binaryop_ge_float32_int64",
    "Binaryop_ge_float32_int8",
    "Binaryop_ge_float32_uint16",
    "Binaryop_ge_float32_uint32",
    "Binaryop_ge_float32_uint64",
    "Binaryop_ge_float32_uint8",
    "Binaryop_ge_float64_float32",
    "Binaryop_ge_float64_float64",
    "Binaryop_ge_float64_int16",
    "Binaryop_ge_float64_int32",
    "Binaryop_ge_float64_int64",
    "Binaryop_ge_float64_int8",
    "Binaryop_ge_float64_uint16",
    "Binaryop_ge_float64_uint32",
    "Binaryop_ge_float64_uint64",
    "Binaryop_ge_float64_uint8",
    "Binaryop_ge_int16_float32",
    "Binaryop_ge_int16_float64",
    "Binaryop_ge_int16_int16",
    "Binaryop_ge_int16_int32",
    "Binaryop_ge_int16_int64",
    "Binaryop_ge_int16_int8",
    "Binaryop_ge_int16_uint16",
    "Binaryop_ge_int16_uint32",
    "Binaryop_ge_int16_uint64",
    "Binaryop_ge_int16_uint8",
    "Binaryop_ge_int32_float32",
    "Binaryop_ge_int32_float64",
    "Binaryop_ge_int32_int16",
    "Binaryop_ge_int32_int32",
    "Binaryop_ge_int32_int64",
    "Binaryop_ge_int32_int8",
    "Binaryop_ge_int32_uint16",
    "Binaryop_ge_int32_uint32",
    "Binaryop_ge_int32_uint64",
    "Binaryop_ge_int32_uint8",
    "Binaryop_ge_int64_float32",
    "Binaryop_ge_int64_float64",
    "Binaryop_ge_int64_int16",
    "Binaryop_ge_int64_int32",
    "Binaryop_ge_int64_int64",
    "Binaryop_ge_int64_int8",
    "Binaryop_ge_int64_uint16",
    "Binaryop_ge_int64_uint32",
    "Binaryop_ge_int64_uint64",
    "Binaryop_ge_int64_uint8",
    "Binaryop_ge_int8_float32",
    "Binaryop_ge_int8_float64",
    "Binaryop_ge_int8_int16",
    "Binaryop_ge_int8_int32",
    "Binaryop_ge_int8_int64",
    "Binaryop_ge_int8_int8",
    "Binaryop_ge_int8_uint16",
    "Binaryop_ge_int8_uint32",
    "Binaryop_ge_int8_uint64",
    "Binaryop_ge_int8_uint8",
    "Binaryop_ge_uint16_float32",
    "Binaryop_ge_uint16_float64",
    "Binaryop_ge_uint16_int16",
    "Binaryop_ge_uint16_int32",
    "Binaryop_ge_uint16_int64",
    "Binaryop_ge_uint16_int8",
    "Binaryop_ge_uint16_uint16",
    "Binaryop_ge_uint16_uint32",
    "Binaryop_ge_uint16_uint64",
    "Binaryop_ge_uint16_uint8",
    "Binaryop_ge_uint32_float32",
    "Binaryop_ge_uint32_float64",
    "Binaryop_ge_uint32_int16",
    "Binaryop_ge_uint32_int32",
    "Binaryop_ge_uint32_int64",
    "Binaryop_ge_uint32_int8",
    "Binaryop_ge_uint32_uint16",
    "Binaryop_ge_uint32_uint32",
    "Binaryop_ge_uint32_uint64",
    "Binaryop_ge_uint32_uint8",
    "Binaryop_ge_uint64_float32",
    "Binaryop_ge_uint64_float64",
    "Binaryop_ge_uint64_int16",
    "Binaryop_ge_uint64_int32",
    "Binaryop_ge_uint64_int64",
    "Binaryop_ge_uint64_int8",
    "Binaryop_ge_uint64_uint16",
    "Binaryop_ge_uint64_uint32",
    "Binaryop_ge_uint64_uint64",
    "Binaryop_ge_uint64_uint8",
    "Binaryop_ge_uint8_float32",
    "Binaryop_ge_uint8_float64",
    "Binaryop_ge_uint8_int16",
    "Binaryop_ge_uint8_int32",
    "Binaryop_ge_uint8_int64",
    "Binaryop_ge_uint8_int8",
    "Binaryop_ge_uint8_uint16",
    "Binaryop_ge_uint8_uint32",
    "Binaryop_ge_uint8_uint64",
    "Binaryop_ge_uint8_uint8",
    "Binaryop_gt_float32_float32",
    "Binaryop_gt_float32_float64",
    "Binaryop_gt_float32_int16",
    "Binaryop_gt_float32_int32",
    "Binaryop_gt_float32_int64",
    "Binaryop_gt_float32_int8",
    "Binaryop_gt_float32_uint16",
    "Binaryop_gt_float32_uint32",
    "Binaryop_gt_float32_uint64",
    "Binaryop_gt_float32_uint8",
    "Binaryop_gt_float64_float32",
    "Binaryop_gt_float64_float64",
    "Binaryop_gt_float64_int16",
    "Binaryop_gt_float64_int32",
    "Binaryop_gt_float64_int64",
    "Binaryop_gt_float64_int8",
    "Binaryop_gt_float64_uint16",
    "Binaryop_gt_float64_uint32",
    "Binaryop_gt_float64_uint64",
    "Binaryop_gt_float64_uint8",
    "Binaryop_gt_int16_float32",
    "Binaryop_gt_int16_float64",
    "Binaryop_gt_int16_int16",
    "Binaryop_gt_int16_int32",
    "Binaryop_gt_int16_int64",
    "Binaryop_gt_int16_int8",
    "Binaryop_gt_int16_uint16",
    "Binaryop_gt_int16_uint32",
    "Binaryop_gt_int16_uint64",
    "Binaryop_gt_int16_uint8",
    "Binaryop_gt_int32_float32",
    "Binaryop_gt_int32_float64",
    "Binaryop_gt_int32_int16",
    "Binaryop_gt_int32_int32",
    "Binaryop_gt_int32_int64",
    "Binaryop_gt_int32_int8",
    "Binaryop_gt_int32_uint16",
    "Binaryop_gt_int32_uint32",
    "Binaryop_gt_int32_uint64",
    "Binaryop_gt_int32_uint8",
    "Binaryop_gt_int64_float32",
    "Binaryop_gt_int64_float64",
    "Binaryop_gt_int64_int16",
    "Binaryop_gt_int64_int32",
    "Binaryop_gt_int64_int64",
    "Binaryop_gt_int64_int8",
    "Binaryop_gt_int64_uint16",
    "Binaryop_gt_int64_uint32",
    "Binaryop_gt_int64_uint64",
    "Binaryop_gt_int64_uint8",
    "Binaryop_gt_int8_float32",
    "Binaryop_gt_int8_float64",
    "Binaryop_gt_int8_int16",
    "Binaryop_gt_int8_int32",
    "Binaryop_gt_int8_int64",
    "Binaryop_gt_int8_int8",
    "Binaryop_gt_int8_uint16",
    "Binaryop_gt_int8_uint32",
    "Binaryop_gt_int8_uint64",
    "Binaryop_gt_int8_uint8",
    "Binaryop_gt_uint16_float32",
    "Binaryop_gt_uint16_float64",
    "Binaryop_gt_uint16_int16",
    "Binaryop_gt_uint16_int32",
    "Binaryop_gt_uint16_int64",
    "Binaryop_gt_uint16_int8",
    "Binaryop_gt_uint16_uint16",
    "Binaryop_gt_uint16_uint32",
    "Binaryop_gt_uint16_uint64",
    "Binaryop_gt_uint16_uint8",
    "Binaryop_gt_uint32_float32",
    "Binaryop_gt_uint32_float64",
    "Binaryop_gt_uint32_int16",
    "Binaryop_gt_uint32_int32",
    "Binaryop_gt_uint32_int64",
    "Binaryop_gt_uint32_int8",
    "Binaryop_gt_uint32_uint16",
    "Binaryop_gt_uint32_uint32",
    "Binaryop_gt_uint32_uint64",
    "Binaryop_gt_uint32_uint8",
    "Binaryop_gt_uint64_float32",
    "Binaryop_gt_uint64_float64",
    "Binaryop_gt_uint64_int16",
    "Binaryop_gt_uint64_int32",
    "Binaryop_gt_uint64_int64",
    "Binaryop_gt_uint64_int8",
    "Binaryop_gt_uint64_uint16",
    "Binaryop_gt_uint64_uint32",
    "Binaryop_gt_uint64_uint64",
    "Binaryop_gt_uint64_uint8",
    "Binaryop_gt_uint8_float32",
    "Binaryop_gt_uint8_float64",
    "Binaryop_gt_uint8_int16",
    "Binaryop_gt_uint8_int32",
    "Binaryop_gt_uint8_int64",
    "Binaryop_gt_uint8_int8",
    "Binaryop_gt_uint8_uint16",
    "Binaryop_gt_uint8_uint32",
    "Binaryop_gt_uint8_uint64",
    "Binaryop_gt_uint8_uint8",
    "Binaryop_le_float32_float32",
    "Binaryop_le_float32_float64",
    "Binaryop_le_float32_int16",
    "Binaryop_le_float32_int32",
    "Binaryop_le_float32_int64",
    "Binaryop_le_float32_int8",
    "Binaryop_le_float32_uint16",
    "Binaryop_le_float32_uint32",
    "Binaryop_le_float32_uint64",
    "Binaryop_le_float32_uint8",
    "Binaryop_le_float64_float32",
    "Binaryop_le_float64_float64",
    "Binaryop_le_float64_int16",
    "Binaryop_le_float64_int32",
    "Binaryop_le_float64_int64",
    "Binaryop_le_float64_int8",
    "Binaryop_le_float64_uint16",
    "Binaryop_le_float64_uint32",
    "Binaryop_le_float64_uint64",
    "Binaryop_le_float64_uint8",
    "Binaryop_le_int16_float32",
    "Binaryop_le_int16_float64",
    "Binaryop_le_int16_int16",
    "Binaryop_le_int16_int32",
    "Binaryop_le_int16_int64",
    "Binaryop_le_int16_int8",
    "Binaryop_le_int16_uint16",
    "Binaryop_le_int16_uint32",
    "Binaryop_le_int16_uint64",
    "Binaryop_le_int16_uint8",
    "Binaryop_le_int32_float32",
    "Binaryop_le_int32_float64",
    "Binaryop_le_int32_int16",
    "Binaryop_le_int32_int32",
    "Binaryop_le_int32_int64",
    "Binaryop_le_int32_int8",
    "Binaryop_le_int32_uint16",
    "Binaryop_le_int32_uint32",
    "Binaryop_le_int32_uint64",
    "Binaryop_le_int32_uint8",
    "Binaryop_le_int64_float32",
    "Binaryop_le_int64_float64",
    "Binaryop_le_int64_int16",
    "Binaryop_le_int64_int32",
    "Binaryop_le_int64_int64",
    "Binaryop_le_int64_int8",
    "Binaryop_le_int64_uint16",
    "Binaryop_le_int64_uint32",
    "Binaryop_le_int64_uint64",
    "Binaryop_le_int64_uint8",
    "Binaryop_le_int8_float32",
    "Binaryop_le_int8_float64",
    "Binaryop_le_int8_int16",
    "Binaryop_le_int8_int32",
    "Binaryop_le_int8_int64",
    "Binaryop_le_int8_int8",
    "Binaryop_le_int8_uint16",
    "Binaryop_le_int8_uint32",
    "Binaryop_le_int8_uint64",
    "Binaryop_le_int8_uint8",
    "Binaryop_le_uint16_float32",
    "Binaryop_le_uint16_float64",
    "Binaryop_le_uint16_int16",
    "Binaryop_le_uint16_int32",
    "Binaryop_le_uint16_int64",
    "Binaryop_le_uint16_int8",
    "Binaryop_le_uint16_uint16",
    "Binaryop_le_uint16_uint32",
    "Binaryop_le_uint16_uint64",
    "Binaryop_le_uint16_uint8",
    "Binaryop_le_uint32_float32",
    "Binaryop_le_uint32_float64",
    "Binaryop_le_uint32_int16",
    "Binaryop_le_uint32_int32",
    "Binaryop_le_uint32_int64",
    "Binaryop_le_uint32_int8",
    "Binaryop_le_uint32_uint16",
    "Binaryop_le_uint32_uint32",
    "Binaryop_le_uint32_uint64",
    "Binaryop_le_uint32_uint8",
    "Binaryop_le_uint64_float32",
    "Binaryop_le_uint64_float64",
    "Binaryop_le_uint64_int16",
    "Binaryop_le_uint64_int32",
    "Binaryop_le_uint64_int64",
    "Binaryop_le_uint64_int8",
    "Binaryop_le_uint64_uint16",
    "Binaryop_le_uint64_uint32",
    "Binaryop_le_uint64_uint64",
    "Binaryop_le_uint64_uint8",
    "Binaryop_le_uint8_float32",
    "Binaryop_le_uint8_float64",
    "Binaryop_le_uint8_int16",
    "Binaryop_le_uint8_int32",
    "Binaryop_le_uint8_int64",
    "Binaryop_le_uint8_int8",
    "Binaryop_le_uint8_uint16",
    "Binaryop_le_uint8_uint32",
    "Binaryop_le_uint8_uint64",
    "Binaryop_le_uint8_uint8",
    "Binaryop_lt_float32_float32",
    "Binaryop_lt_float32_float64",
    "Binaryop_lt_float32_int16",
    "Binaryop_lt_float32_int32",
    "Binaryop_lt_float32_int64",
    "Binaryop_lt_float32_int8",
    "Binaryop_lt_float32_uint16",
    "Binaryop_lt_float32_uint32",
    "Binaryop_lt_float32_uint64",
    "Binaryop_lt_float32_uint8",
    "Binaryop_lt_float64_float32",
    "Binaryop_lt_float64_float64",
    "Binaryop_lt_float64_int16",
    "Binaryop_lt_float64_int32",
    "Binaryop_lt_float64_int64",
    "Binaryop_lt_float64_int8",
    "Binaryop_lt_float64_uint16",
    "Binaryop_lt_float64_uint32",
    "Binaryop_lt_float64_uint64",
    "Binaryop_lt_float64_uint8",
    "Binaryop_lt_int16_float32",
    "Binaryop_lt_int16_float64",
    "Binaryop_lt_int16_int16",
    "Binaryop_lt_int16_int32",
    "Binaryop_lt_int16_int64",
    "Binaryop_lt_int16_int8",
    "Binaryop_lt_int16_uint16",
    "Binaryop_lt_int16_uint32",
    "Binaryop_lt_int16_uint64",
    "Binaryop_lt_int16_uint8",
    "Binaryop_lt_int32_float32",
    "Binaryop_lt_int32_float64",
    "Binaryop_lt_int32_int16",
    "Binaryop_lt_int32_int32",
    "Binaryop_lt_int32_int64",
    "Binaryop_lt_int32_int8",
    "Binaryop_lt_int32_uint16",
    "Binaryop_lt_int32_uint32",
    "Binaryop_lt_int32_uint64",
    "Binaryop_lt_int32_uint8",
    "Binaryop_lt_int64_float32",
    "Binaryop_lt_int64_float64",
    "Binaryop_lt_int64_int16",
    "Binaryop_lt_int64_int32",
    "Binaryop_lt_int64_int64",
    "Binaryop_lt_int64_int8",
    "Binaryop_lt_int64_uint16",
    "Binaryop_lt_int64_uint32",
    "Binaryop_lt_int64_uint64",
    "Binaryop_lt_int64_uint8",
    "Binaryop_lt_int8_float32",
    "Binaryop_lt_int8_float64",
    "Binaryop_lt_int8_int16",
    "Binaryop_lt_int8_int32",
    "Binaryop_lt_int8_int64",
    "Binaryop_lt_int8_int8",
    "Binaryop_lt_int8_uint16",
    "Binaryop_lt_int8_uint32",
    "Binaryop_lt_int8_uint64",
    "Binaryop_lt_int8_uint8",
    "Binaryop_lt_uint16_float32",
    "Binaryop_lt_uint16_float64",
    "Binaryop_lt_uint16_int16",
    "Binaryop_lt_uint16_int32",
    "Binaryop_lt_uint16_int64",
    "Binaryop_lt_uint16_int8",
    "Binaryop_lt_uint16_uint16",
    "Binaryop_lt_uint16_uint32",
    "Binaryop_lt_uint16_uint64",
    "Binaryop_lt_uint16_uint8",
    "Binaryop_lt_uint32_float32",
    "Binaryop_lt_uint32_float64",
    "Binaryop_lt_uint32_int16",
    "Binaryop_lt_uint32_int32",
    "Binaryop_lt_uint32_int64",
    "Binaryop_lt_uint32_int8",
    "Binaryop_lt_uint32_uint16",
    "Binaryop_lt_uint32_uint32",
    "Binaryop_lt_uint32_uint64",
    "Binaryop_lt_uint32_uint8",
    "Binaryop_lt_uint64_float32",
    "Binaryop_lt_uint64_float64",
    "Binaryop_lt_uint64_int16",
    "Binaryop_lt_uint64_int32",
    "Binaryop_lt_uint64_int64",
    "Binaryop_lt_uint64_int8",
    "Binaryop_lt_uint64_uint16",
    "Binaryop_lt_uint64_uint32",
    "Binaryop_lt_uint64_uint64",
    "Binaryop_lt_uint64_uint8",
    "Binaryop_lt_uint8_float32",
    "Binaryop_lt_uint8_float64",
    "Binaryop_lt_uint8_int16",
    "Binaryop_lt_uint8_int32",
    "Binaryop_lt_uint8_int64",
    "Binaryop_lt_uint8_int8",
    "Binaryop_lt_uint8_uint16",
    "Binaryop_lt_uint8_uint32",
    "Binaryop_lt_uint8_uint64",
    "Binaryop_lt_uint8_uint8",
    "Binaryop_max_float32_float32",
    "Binaryop_max_float32_float64",
    "Binaryop_max_float32_int16",
    "Binaryop_max_float32_int32",
    "Binaryop_max_float32_int64",
    "Binaryop_max_float32_int8",
    "Binaryop_max_float32_uint16",
    "Binaryop_max_float32_uint32",
    "Binaryop_max_float32_uint64",
    "Binaryop_max_float32_uint8",
    "Binaryop_max_float64_float32",
    "Binaryop_max_float64_float64",
    "Binaryop_max_float64_int16",
    "Binaryop_max_float64_int32",
    "Binaryop_max_float64_int64",
    "Binaryop_max_float64_int8",
    "Binaryop_max_float64_uint16",
    "Binaryop_max_float64_uint32",
    "Binaryop_max_float64_uint64",
    "Binaryop_max_float64_uint8",
    "Binaryop_max_int16_float32",
    "Binaryop_max_int16_float64",
    "Binaryop_max_int16_int16",
    "Binaryop_max_int16_int32",
    "Binaryop_max_int16_int64",
    "Binaryop_max_int16_int8",
    "Binaryop_max_int16_uint16",
    "Binaryop_max_int16_uint32",
    "Binaryop_max_int16_uint64",
    "Binaryop_max_int16_uint8",
    "Binaryop_max_int32_float32",
    "Binaryop_max_int32_float64",
    "Binaryop_max_int32_int16",
    "Binaryop_max_int32_int32",
    "Binaryop_max_int32_int64",
    "Binaryop_max_int32_int8",
    "Binaryop_max_int32_uint16",
    "Binaryop_max_int32_uint32",
    "Binaryop_max_int32_uint64",
    "Binaryop_max_int32_uint8",
    "Binaryop_max_int64_float32",
    "Binaryop_max_int64_float64",
    "Binaryop_max_int64_int16",
    "Binaryop_max_int64_int32",
    "Binaryop_max_int64_int64",
    "Binaryop_max_int64_int8",
    "Binaryop_max_int64_uint16",
    "Binaryop_max_int64_uint32",
    "Binaryop_max_int64_uint64",
    "Binaryop_max_int64_uint8",
    "Binaryop_max_int8_float32",
    "Binaryop_max_int8_float64",
    "Binaryop_max_int8_int16",
    "Binaryop_max_int8_int32",
    "Binaryop_max_int8_int64",
    "Binaryop_max_int8_int8",
    "Binaryop_max_int8_uint16",
    "Binaryop_max_int8_uint32",
    "Binaryop_max_int8_uint64",
    "Binaryop_max_int8_uint8",
    "Binaryop_max_uint16_float32",
    "Binaryop_max_uint16_float64",
    "Binaryop_max_uint16_int16",
    "Binaryop_max_uint16_int32",
    "Binaryop_max_uint16_int64",
    "Binaryop_max_uint16_int8",
    "Binaryop_max_uint16_uint16",
    "Binaryop_max_uint16_uint32",
    "Binaryop_max_uint16_uint64",
    "Binaryop_max_uint16_uint8",
    "Binaryop_max_uint32_float32",
    "Binaryop_max_uint32_float64",
    "Binaryop_max_uint32_int16",
    "Binaryop_max_uint32_int32",
    "Binaryop_max_uint32_int64",
    "Binaryop_max_uint32_int8",
    "Binaryop_max_uint32_uint16",
    "Binaryop_max_uint32_uint32",
    "Binaryop_max_uint32_uint64",
    "Binaryop_max_uint32_uint8",
    "Binaryop_max_uint64_float32",
    "Binaryop_max_uint64_float64",
    "Binaryop_max_uint64_int16",
    "Binaryop_max_uint64_int32",
    "Binaryop_max_uint64_int64",
    "Binaryop_max_uint64_int8",
    "Binaryop_max_uint64_uint16",
    "Binaryop_max_uint64_uint32",
    "Binaryop_max_uint64_uint64",
    "Binaryop_max_uint64_uint8",
    "Binaryop_max_uint8_float32",
    "Binaryop_max_uint8_float64",
    "Binaryop_max_uint8_int16",
    "Binaryop_max_uint8_int32",
    "Binaryop_max_uint8_int64",
    "Binaryop_max_uint8_int8",
    "Binaryop_max_uint8_uint16",
    "Binaryop_max_uint8_uint32",
    "Binaryop_max_uint8_uint64",
    "Binaryop_max_uint8_uint8",
    "Binaryop_min_float32_float32",
    "Binaryop_min_float32_float64",
    "Binaryop_min_float32_int16",
    "Binaryop_min_float32_int32",
    "Binaryop_min_float32_int64",
    "Binaryop_min_float32_int8",
    "Binaryop_min_float32_uint16",
    "Binaryop_min_float32_uint32",
    "Binaryop_min_float32_uint64",
    "Binaryop_min_float32_uint8",
    "Binaryop_min_float64_float32",
    "Binaryop_min_float64_float64",
    "Binaryop_min_float64_int16",
    "Binaryop_min_float64_int32",
    "Binaryop_min_float64_int64",
    "Binaryop_min_float64_int8",
    "Binaryop_min_float64_uint16",
    "Binaryop_min_float64_uint32",
    "Binaryop_min_float64_uint64",
    "Binaryop_min_float64_uint8",
    "Binaryop_min_int16_float32",
    "Binaryop_min_int16_float64",
    "Binaryop_min_int16_int16",
    "Binaryop_min_int16_int32",
    "Binaryop_min_int16_int64",
    "Binaryop_min_int16_int8",
    "Binaryop_min_int16_uint16",
    "Binaryop_min_int16_uint32",
    "Binaryop_min_int16_uint64",
    "Binaryop_min_int16_uint8",
    "Binaryop_min_int32_float32",
    "Binaryop_min_int32_float64",
    "Binaryop_min_int32_int16",
    "Binaryop_min_int32_int32",
    "Binaryop_min_int32_int64",
    "Binaryop_min_int32_int8",
    "Binaryop_min_int32_uint16",
    "Binaryop_min_int32_uint32",
    "Binaryop_min_int32_uint64",
    "Binaryop_min_int32_uint8",
    "Binaryop_min_int64_float32",
    "Binaryop_min_int64_float64",
    "Binaryop_min_int64_int16",
    "Binaryop_min_int64_int32",
    "Binaryop_min_int64_int64",
    "Binaryop_min_int64_int8",
    "Binaryop_min_int64_uint16",
    "Binaryop_min_int64_uint32",
    "Binaryop_min_int64_uint64",
    "Binaryop_min_int64_uint8",
    "Binaryop_min_int8_float32",
    "Binaryop_min_int8_float64",
    "Binaryop_min_int8_int16",
    "Binaryop_min_int8_int32",
    "Binaryop_min_int8_int64",
    "Binaryop_min_int8_int8",
    "Binaryop_min_int8_uint16",
    "Binaryop_min_int8_uint32",
    "Binaryop_min_int8_uint64",
    "Binaryop_min_int8_uint8",
    "Binaryop_min_uint16_float32",
    "Binaryop_min_uint16_float64",
    "Binaryop_min_uint16_int16",
    "Binaryop_min_uint16_int32",
    "Binaryop_min_uint16_int64",
    "Binaryop_min_uint16_int8",
    "Binaryop_min_uint16_uint16",
    "Binaryop_min_uint16_uint32",
    "Binaryop_min_uint16_uint64",
    "Binaryop_min_uint16_uint8",
    "Binaryop_min_uint32_float32",
    "Binaryop_min_uint32_float64",
    "Binaryop_min_uint32_int16",
    "Binaryop_min_uint32_int32",
    "Binaryop_min_uint32_int64",
    "Binaryop_min_uint32_int8",
    "Binaryop_min_uint32_uint16",
    "Binaryop_min_uint32_uint32",
    "Binaryop_min_uint32_uint64",
    "Binaryop_min_uint32_uint8",
    "Binaryop_min_uint64_float32",
    "Binaryop_min_uint64_float64",
    "Binaryop_min_uint64_int16",
    "Binaryop_min_uint64_int32",
    "Binaryop_min_uint64_int64",
    "Binaryop_min_uint64_int8",
    "Binaryop_min_uint64_uint16",
    "Binaryop_min_uint64_uint32",
    "Binaryop_min_uint64_uint64",
    "Binaryop_min_uint64_uint8",
    "Binaryop_min_uint8_float32",
    "Binaryop_min_uint8_float64",
    "Binaryop_min_uint8_int16",
    "Binaryop_min_uint8_int32",
    "Binaryop_min_uint8_int64",
    "Binaryop_min_uint8_int8",
    "Binaryop_min_uint8_uint16",
    "Binaryop_min_uint8_uint32",
    "Binaryop_min_uint8_uint64",
    "Binaryop_min_uint8_uint8",
    "Binaryop_mul_float32_float32",
    "Binaryop_mul_float32_float64",
    "Binaryop_mul_float32_int16",
    "Binaryop_mul_float32_int32",
    "Binaryop_mul_float32_int64",
    "Binaryop_mul_float32_int8",
    "Binaryop_mul_float32_uint16",
    "Binaryop_mul_float32_uint32",
    "Binaryop_mul_float32_uint64",
    "Binaryop_mul_float32_uint8",
    "Binaryop_mul_float64_float32",
    "Binaryop_mul_float64_float64",
    "Binaryop_mul_float64_int16",
    "Binaryop_mul_float64_int32",
    "Binaryop_mul_float64_int64",
    "Binaryop_mul_float64_int8",
    "Binaryop_mul_float64_uint16",
    "Binaryop_mul_float64_uint32",
    "Binaryop_mul_float64_uint64",
    "Binaryop_mul_float64_uint8",
    "Binaryop_mul_int16_float32",
    "Binaryop_mul_int16_float64",
    "Binaryop_mul_int16_int16",
    "Binaryop_mul_int16_int32",
    "Binaryop_mul_int16_int64",
    "Binaryop_mul_int16_int8",
    "Binaryop_mul_int16_uint16",
    "Binaryop_mul_int16_uint32",
    "Binaryop_mul_int16_uint64",
    "Binaryop_mul_int16_uint8",
    "Binaryop_mul_int32_float32",
    "Binaryop_mul_int32_float64",
    "Binaryop_mul_int32_int16",
    "Binaryop_mul_int32_int32",
    "Binaryop_mul_int32_int64",
    "Binaryop_mul_int32_int8",
    "Binaryop_mul_int32_uint16",
    "Binaryop_mul_int32_uint32",
    "Binaryop_mul_int32_uint64",
    "Binaryop_mul_int32_uint8",
    "Binaryop_mul_int64_float32",
    "Binaryop_mul_int64_float64",
    "Binaryop_mul_int64_int16",
    "Binaryop_mul_int64_int32",
    "Binaryop_mul_int64_int64",
    "Binaryop_mul_int64_int8",
    "Binaryop_mul_int64_uint16",
    "Binaryop_mul_int64_uint32",
    "Binaryop_mul_int64_uint64",
    "Binaryop_mul_int64_uint8",
    "Binaryop_mul_int8_float32",
    "Binaryop_mul_int8_float64",
    "Binaryop_mul_int8_int16",
    "Binaryop_mul_int8_int32",
    "Binaryop_mul_int8_int64",
    "Binaryop_mul_int8_int8",
    "Binaryop_mul_int8_uint16",
    "Binaryop_mul_int8_uint32",
    "Binaryop_mul_int8_uint64",
    "Binaryop_mul_int8_uint8",
    "Binaryop_mul_uint16_float32",
    "Binaryop_mul_uint16_float64",
    "Binaryop_mul_uint16_int16",
    "Binaryop_mul_uint16_int32",
    "Binaryop_mul_uint16_int64",
    "Binaryop_mul_uint16_int8",
    "Binaryop_mul_uint16_uint16",
    "Binaryop_mul_uint16_uint32",
    "Binaryop_mul_uint16_uint64",
    "Binaryop_mul_uint16_uint8",
    "Binaryop_mul_uint32_float32",
    "Binaryop_mul_uint32_float64",
    "Binaryop_mul_uint32_int16",
    "Binaryop_mul_uint32_int32",
    "Binaryop_mul_uint32_int64",
    "Binaryop_mul_uint32_int8",
    "Binaryop_mul_uint32_uint16",
    "Binaryop_mul_uint32_uint32",
    "Binaryop_mul_uint32_uint64",
    "Binaryop_mul_uint32_uint8",
    "Binaryop_mul_uint64_float32",
    "Binaryop_mul_uint64_float64",
    "Binaryop_mul_uint64_int16",
    "Binaryop_mul_uint64_int32",
    "Binaryop_mul_uint64_int64",
    "Binaryop_mul_uint64_int8",
    "Binaryop_mul_uint64_uint16",
    "Binaryop_mul_uint64_uint32",
    "Binaryop_mul_uint64_uint64",
    "Binaryop_mul_uint64_uint8",
    "Binaryop_mul_uint8_float32",
    "Binaryop_mul_uint8_float64",
    "Binaryop_mul_uint8_int16",
    "Binaryop_mul_uint8_int32",
    "Binaryop_mul_uint8_int64",
    "Binaryop_mul_uint8_int8",
    "Binaryop_mul_uint8_uint16",
    "Binaryop_mul_uint8_uint32",
    "Binaryop_mul_uint8_uint64",
    "Binaryop_mul_uint8_uint8",
    "Binaryop_ne_float32_float32",
    "Binaryop_ne_float32_float64",
    "Binaryop_ne_float32_int16",
    "Binaryop_ne_float32_int32",
    "Binaryop_ne_float32_int64",
    "Binaryop_ne_float32_int8",
    "Binaryop_ne_float32_uint16",
    "Binaryop_ne_float32_uint32",
    "Binaryop_ne_float32_uint64",
    "Binaryop_ne_float32_uint8",
    "Binaryop_ne_float64_float32",
    "Binaryop_ne_float64_float64",
    "Binaryop_ne_float64_int16",
    "Binaryop_ne_float64_int32",
    "Binaryop_ne_float64_int64",
    "Binaryop_ne_float64_int8",
    "Binaryop_ne_float64_uint16",
    "Binaryop_ne_float64_uint32",
    "Binaryop_ne_float64_uint64",
    "Binaryop_ne_float64_uint8",
    "Binaryop_ne_int16_float32",
    "Binaryop_ne_int16_float64",
    "Binaryop_ne_int16_int16",
    "Binaryop_ne_int16_int32",
    "Binaryop_ne_int16_int64",
    "Binaryop_ne_int16_int8",
    "Binaryop_ne_int16_uint16",
    "Binaryop_ne_int16_uint32",
    "Binaryop_ne_int16_uint64",
    "Binaryop_ne_int16_uint8",
    "Binaryop_ne_int32_float32",
    "Binaryop_ne_int32_float64",
    "Binaryop_ne_int32_int16",
    "Binaryop_ne_int32_int32",
    "Binaryop_ne_int32_int64",
    "Binaryop_ne_int32_int8",
    "Binaryop_ne_int32_uint16",
    "Binaryop_ne_int32_uint32",
    "Binaryop_ne_int32_uint64",
    "Binaryop_ne_int32_uint8",
    "Binaryop_ne_int64_float32",
    "Binaryop_ne_int64_float64",
    "Binaryop_ne_int64_int16",
    "Binaryop_ne_int64_int32",
    "Binaryop_ne_int64_int64",
    "Binaryop_ne_int64_int8",
    "Binaryop_ne_int64_uint16",
    "Binaryop_ne_int64_uint32",
    "Binaryop_ne_int64_uint64",
    "Binaryop_ne_int64_uint8",
    "Binaryop_ne_int8_float32",
    "Binaryop_ne_int8_float64",
    "Binaryop_ne_int8_int16",
    "Binaryop_ne_int8_int32",
    "Binaryop_ne_int8_int64",
    "Binaryop_ne_int8_int8",
    "Binaryop_ne_int8_uint16",
    "Binaryop_ne_int8_uint32",
    "Binaryop_ne_int8_uint64",
    "Binaryop_ne_int8_uint8",
    "Binaryop_ne_uint16_float32",
    "Binaryop_ne_uint16_float64",
    "Binaryop_ne_uint16_int16",
    "Binaryop_ne_uint16_int32",
    "Binaryop_ne_uint16_int64",
    "Binaryop_ne_uint16_int8",
    "Binaryop_ne_uint16_uint16",
    "Binaryop_ne_uint16_uint32",
    "Binaryop_ne_uint16_uint64",
    "Binaryop_ne_uint16_uint8",
    "Binaryop_ne_uint32_float32",
    "Binaryop_ne_uint32_float64",
    "Binaryop_ne_uint32_int16",
    "Binaryop_ne_uint32_int32",
    "Binaryop_ne_uint32_int64",
    "Binaryop_ne_uint32_int8",
    "Binaryop_ne_uint32_uint16",
    "Binaryop_ne_uint32_uint32",
    "Binaryop_ne_uint32_uint64",
    "Binaryop_ne_uint32_uint8",
    "Binaryop_ne_uint64_float32",
    "Binaryop_ne_uint64_float64",
    "Binaryop_ne_uint64_int16",
    "Binaryop_ne_uint64_int32",
    "Binaryop_ne_uint64_int64",
    "Binaryop_ne_uint64_int8",
    "Binaryop_ne_uint64_uint16",
    "Binaryop_ne_uint64_uint32",
    "Binaryop_ne_uint64_uint64",
    "Binaryop_ne_uint64_uint8",
    "Binaryop_ne_uint8_float32",
    "Binaryop_ne_uint8_float64",
    "Binaryop_ne_uint8_int16",
    "Binaryop_ne_uint8_int32",
    "Binaryop_ne_uint8_int64",
    "Binaryop_ne_uint8_int8",
    "Binaryop_ne_uint8_uint16",
    "Binaryop_ne_uint8_uint32",
    "Binaryop_ne_uint8_uint64",
    "Binaryop_ne_uint8_uint8",
    "Binaryop_or_int16_float32",
    "Binaryop_or_int16_float64",
    "Binaryop_or_int16_int16",
    "Binaryop_or_int16_int32",
    "Binaryop_or_int16_int64",
    "Binaryop_or_int16_int8",
    "Binaryop_or_int16_uint16",
    "Binaryop_or_int16_uint32",
    "Binaryop_or_int16_uint64",
    "Binaryop_or_int16_uint8",
    "Binaryop_or_int32_float32",
    "Binaryop_or_int32_float64",
    "Binaryop_or_int32_int16",
    "Binaryop_or_int32_int32",
    "Binaryop_or_int32_int64",
    "Binaryop_or_int32_int8",
    "Binaryop_or_int32_uint16",
    "Binaryop_or_int32_uint32",
    "Binaryop_or_int32_uint64",
    "Binaryop_or_int32_uint8",
    "Binaryop_or_int64_float32",
    "Binaryop_or_int64_float64",
    "Binaryop_or_int64_int16",
    "Binaryop_or_int64_int32",
    "Binaryop_or_int64_int64",
    "Binaryop_or_int64_int8",
    "Binaryop_or_int64_uint16",
    "Binaryop_or_int64_uint32",
    "Binaryop_or_int64_uint64",
    "Binaryop_or_int64_uint8",
    "Binaryop_or_int8_float32",
    "Binaryop_or_int8_float64",
    "Binaryop_or_int8_int16",
    "Binaryop_or_int8_int32",
    "Binaryop_or_int8_int64",
    "Binaryop_or_int8_int8",
    "Binaryop_or_int8_uint16",
    "Binaryop_or_int8_uint32",
    "Binaryop_or_int8_uint64",
    "Binaryop_or_int8_uint8",
    "Binaryop_or_uint16_float32",
    "Binaryop_or_uint16_float64",
    "Binaryop_or_uint16_int16",
    "Binaryop_or_uint16_int32",
    "Binaryop_or_uint16_int64",
    "Binaryop_or_uint16_int8",
    "Binaryop_or_uint16_uint16",
    "Binaryop_or_uint16_uint32",
    "Binaryop_or_uint16_uint64",
    "Binaryop_or_uint16_uint8",
    "Binaryop_or_uint32_float32",
    "Binaryop_or_uint32_float64",
    "Binaryop_or_uint32_int16",
    "Binaryop_or_uint32_int32",
    "Binaryop_or_uint32_int64",
    "Binaryop_or_uint32_int8",
    "Binaryop_or_uint32_uint16",
    "Binaryop_or_uint32_uint32",
    "Binaryop_or_uint32_uint64",
    "Binaryop_or_uint32_uint8",
    "Binaryop_or_uint64_float32",
    "Binaryop_or_uint64_float64",
    "Binaryop_or_uint64_int16",
    "Binaryop_or_uint64_int32",
    "Binaryop_or_uint64_int64",
    "Binaryop_or_uint64_int8",
    "Binaryop_or_uint64_uint16",
    "Binaryop_or_uint64_uint32",
    "Binaryop_or_uint64_uint64",
    "Binaryop_or_uint64_uint8",
    "Binaryop_or_uint8_float32",
    "Binaryop_or_uint8_float64",
    "Binaryop_or_uint8_int16",
    "Binaryop_or_uint8_int32",
    "Binaryop_or_uint8_int64",
    "Binaryop_or_uint8_int8",
    "Binaryop_or_uint8_uint16",
    "Binaryop_or_uint8_uint32",
    "Binaryop_or_uint8_uint64",
    "Binaryop_or_uint8_uint8",
    "Binaryop_sub_float32_float32",
    "Binaryop_sub_float32_float64",
    "Binaryop_sub_float32_int16",
    "Binaryop_sub_float32_int32",
    "Binaryop_sub_float32_int64",
    "Binaryop_sub_float32_int8",
    "Binaryop_sub_float32_uint16",
    "Binaryop_sub_float32_uint32",
    "Binaryop_sub_float32_uint64",
    "Binaryop_sub_float32_uint8",
    "Binaryop_sub_float64_float32",
    "Binaryop_sub_float64_float64",
    "Binaryop_sub_float64_int16",
    "Binaryop_sub_float64_int32",
    "Binaryop_sub_float64_int64",
    "Binaryop_sub_float64_int8",
    "Binaryop_sub_float64_uint16",
    "Binaryop_sub_float64_uint32",
    "Binaryop_sub_float64_uint64",
    "Binaryop_sub_float64_uint8",
    "Binaryop_sub_int16_float32",
    "Binaryop_sub_int16_float64",
    "Binaryop_sub_int16_int16",
    "Binaryop_sub_int16_int32",
    "Binaryop_sub_int16_int64",
    "Binaryop_sub_int16_int8",
    "Binaryop_sub_int16_uint16",
    "Binaryop_sub_int16_uint32",
    "Binaryop_sub_int16_uint64",
    "Binaryop_sub_int16_uint8",
    "Binaryop_sub_int32_float32",
    "Binaryop_sub_int32_float64",
    "Binaryop_sub_int32_int16",
    "Binaryop_sub_int32_int32",
    "Binaryop_sub_int32_int64",
    "Binaryop_sub_int32_int8",
    "Binaryop_sub_int32_uint16",
    "Binaryop_sub_int32_uint32",
    "Binaryop_sub_int32_uint64",
    "Binaryop_sub_int32_uint8",
    "Binaryop_sub_int64_float32",
    "Binaryop_sub_int64_float64",
    "Binaryop_sub_int64_int16",
    "Binaryop_sub_int64_int32",
    "Binaryop_sub_int64_int64",
    "Binaryop_sub_int64_int8",
    "Binaryop_sub_int64_uint16",
    "Binaryop_sub_int64_uint32",
    "Binaryop_sub_int64_uint64",
    "Binaryop_sub_int64_uint8",
    "Binaryop_sub_int8_float32",
    "Binaryop_sub_int8_float64",
    "Binaryop_sub_int8_int16",
    "Binaryop_sub_int8_int32",
    "Binaryop_sub_int8_int64",
    "Binaryop_sub_int8_int8",
    "Binaryop_sub_int8_uint16",
    "Binaryop_sub_int8_uint32",
    "Binaryop_sub_int8_uint64",
    "Binaryop_sub_int8_uint8",
    "Binaryop_sub_uint16_float32",
    "Binaryop_sub_uint16_float64",
    "Binaryop_sub_uint16_int16",
    "Binaryop_sub_uint16_int32",
    "Binaryop_sub_uint16_int64",
    "Binaryop_sub_uint16_int8",
    "Binaryop_sub_uint16_uint16",
    "Binaryop_sub_uint16_uint32",
    "Binaryop_sub_uint16_uint64",
    "Binaryop_sub_uint16_uint8",
    "Binaryop_sub_uint32_float32",
    "Binaryop_sub_uint32_float64",
    "Binaryop_sub_uint32_int16",
    "Binaryop_sub_uint32_int32",
    "Binaryop_sub_uint32_int64",
    "Binaryop_sub_uint32_int8",
    "Binaryop_sub_uint32_uint16",
    "Binaryop_sub_uint32_uint32",
    "Binaryop_sub_uint32_uint64",
    "Binaryop_sub_uint32_uint8",
    "Binaryop_sub_uint64_float32",
    "Binaryop_sub_uint64_float64",
    "Binaryop_sub_uint64_int16",
    "Binaryop_sub_uint64_int32",
    "Binaryop_sub_uint64_int64",
    "Binaryop_sub_uint64_int8",
    "Binaryop_sub_uint64_uint16",
    "Binaryop_sub_uint64_uint32",
    "Binaryop_sub_uint64_uint64",
    "Binaryop_sub_uint64_uint8",
    "Binaryop_sub_uint8_float32",
    "Binaryop_sub_uint8_float64",
    "Binaryop_sub_uint8_int16",
    "Binaryop_sub_uint8_int32",
    "Binaryop_sub_uint8_int64",
    "Binaryop_sub_uint8_int8",
    "Binaryop_sub_uint8_uint16",
    "Binaryop_sub_uint8_uint32",
    "Binaryop_sub_uint8_uint64",
    "Binaryop_sub_uint8_uint8",
    "Binaryop_xor_int16_float32",
    "Binaryop_xor_int16_float64",
    "Binaryop_xor_int16_int16",
    "Binaryop_xor_int16_int32",
    "Binaryop_xor_int16_int64",
    "Binaryop_xor_int16_int8",
    "Binaryop_xor_int16_uint16",
    "Binaryop_xor_int16_uint32",
    "Binaryop_xor_int16_uint64",
    "Binaryop_xor_int16_uint8",
    "Binaryop_xor_int32_float32",
    "Binaryop_xor_int32_float64",
    "Binaryop_xor_int32_int16",
    "Binaryop_xor_int32_int32",
    "Binaryop_xor_int32_int64",
    "Binaryop_xor_int32_int8",
    "Binaryop_xor_int32_uint16",
    "Binaryop_xor_int32_uint32",
    "Binaryop_xor_int32_uint64",
    "Binaryop_xor_int32_uint8",
    "Binaryop_xor_int64_float32",
    "Binaryop_xor_int64_float64",
    "Binaryop_xor_int64_int16",
    "Binaryop_xor_int64_int32",
    "Binaryop_xor_int64_int64",
    "Binaryop_xor_int64_int8",
    "Binaryop_xor_int64_uint16",
    "Binaryop_xor_int64_uint32",
    "Binaryop_xor_int64_uint64",
    "Binaryop_xor_int64_uint8",
    "Binaryop_xor_int8_float32",
    "Binaryop_xor_int8_float64",
    "Binaryop_xor_int8_int16",
    "Binaryop_xor_int8_int32",
    "Binaryop_xor_int8_int64",
    "Binaryop_xor_int8_int8",
    "Binaryop_xor_int8_uint16",
    "Binaryop_xor_int8_uint32",
    "Binaryop_xor_int8_uint64",
    "Binaryop_xor_int8_uint8",
    "Binaryop_xor_uint16_float32",
    "Binaryop_xor_uint16_float64",
    "Binaryop_xor_uint16_int16",
    "Binaryop_xor_uint16_int32",
    "Binaryop_xor_uint16_int64",
    "Binaryop_xor_uint16_int8",
    "Binaryop_xor_uint16_uint16",
    "Binaryop_xor_uint16_uint32",
    "Binaryop_xor_uint16_uint64",
    "Binaryop_xor_uint16_uint8",
    "Binaryop_xor_uint32_float32",
    "Binaryop_xor_uint32_float64",
    "Binaryop_xor_uint32_int16",
    "Binaryop_xor_uint32_int32",
    "Binaryop_xor_uint32_int64",
    "Binaryop_xor_uint32_int8",
    "Binaryop_xor_uint32_uint16",
    "Binaryop_xor_uint32_uint32",
    "Binaryop_xor_uint32_uint64",
    "Binaryop_xor_uint32_uint8",
    "Binaryop_xor_uint64_float32",
    "Binaryop_xor_uint64_float64",
    "Binaryop_xor_uint64_int16",
    "Binaryop_xor_uint64_int32",
    "Binaryop_xor_uint64_int64",
    "Binaryop_xor_uint64_int8",
    "Binaryop_xor_uint64_uint16",
    "Binaryop_xor_uint64_uint32",
    "Binaryop_xor_uint64_uint64",
    "Binaryop_xor_uint64_uint8",
    "Binaryop_xor_uint8_float32",
    "Binaryop_xor_uint8_float64",
    "Binaryop_xor_uint8_int16",
    "Binaryop_xor_uint8_int32",
    "Binaryop_xor_uint8_int64",
    "Binaryop_xor_uint8_int8",
    "Binaryop_xor_uint8_uint16",
    "Binaryop_xor_uint8_uint32",
    "Binaryop_xor_uint8_uint64",
    "Binaryop_xor_uint8_uint8",
]

class Binaryop_add_float32_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_float32_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_float32_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_float32_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_float32_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_float32_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_float32_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_float32_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_float32_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_float32_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_float64_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_float64_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_float64_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_float64_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_float64_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_float64_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_float64_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_float64_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_float64_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_float64_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_int16_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_int16_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_int16_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_int16_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_int16_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_int16_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_int16_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_int16_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_int16_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_int16_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_int32_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_int32_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_int32_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_int32_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_int32_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_int32_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_int32_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_int32_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_int32_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_int32_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_int64_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_int64_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_int64_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_int64_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_int64_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_int64_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_int64_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_int64_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_int64_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_int64_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_int8_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_int8_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_int8_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_int8_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_int8_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_int8_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_int8_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_int8_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_int8_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_int8_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_uint16_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_uint16_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_uint16_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_uint16_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_uint16_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_uint16_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_uint16_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_uint16_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_uint16_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_uint16_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_uint32_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_uint32_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_uint32_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_uint32_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_uint32_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_uint32_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_uint32_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_uint32_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_uint32_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_uint32_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_uint64_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_uint64_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_uint64_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_uint64_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_uint64_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_uint64_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_uint64_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_uint64_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_uint64_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_uint64_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_uint8_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_uint8_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_uint8_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_uint8_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_uint8_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_uint8_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_uint8_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_uint8_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_uint8_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_add_uint8_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_int16_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_int16_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_int16_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_int16_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_int16_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_int16_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_int16_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_int16_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_int16_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_int16_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_int32_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_int32_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_int32_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_int32_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_int32_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_int32_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_int32_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_int32_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_int32_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_int32_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_int64_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_int64_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_int64_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_int64_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_int64_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_int64_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_int64_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_int64_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_int64_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_int64_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_int8_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_int8_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_int8_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_int8_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_int8_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_int8_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_int8_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_int8_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_int8_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_int8_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_uint16_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_uint16_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_uint16_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_uint16_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_uint16_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_uint16_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_uint16_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_uint16_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_uint16_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_uint16_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_uint32_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_uint32_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_uint32_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_uint32_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_uint32_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_uint32_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_uint32_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_uint32_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_uint32_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_uint32_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_uint64_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_uint64_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_uint64_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_uint64_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_uint64_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_uint64_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_uint64_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_uint64_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_uint64_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_uint64_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_uint8_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_uint8_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_uint8_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_uint8_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_uint8_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_uint8_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_uint8_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_uint8_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_uint8_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_and_uint8_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_float32_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_float32_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_float32_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_float32_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_float32_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_float32_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_float32_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_float32_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_float32_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_float32_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_float64_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_float64_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_float64_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_float64_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_float64_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_float64_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_float64_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_float64_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_float64_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_float64_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_int16_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_int16_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_int16_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_int16_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_int16_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_int16_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_int16_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_int16_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_int16_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_int16_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_int32_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_int32_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_int32_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_int32_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_int32_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_int32_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_int32_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_int32_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_int32_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_int32_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_int64_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_int64_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_int64_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_int64_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_int64_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_int64_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_int64_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_int64_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_int64_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_int64_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_int8_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_int8_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_int8_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_int8_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_int8_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_int8_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_int8_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_int8_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_int8_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_int8_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_uint16_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_uint16_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_uint16_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_uint16_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_uint16_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_uint16_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_uint16_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_uint16_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_uint16_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_uint16_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_uint32_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_uint32_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_uint32_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_uint32_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_uint32_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_uint32_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_uint32_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_uint32_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_uint32_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_uint32_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_uint64_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_uint64_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_uint64_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_uint64_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_uint64_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_uint64_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_uint64_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_uint64_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_uint64_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_uint64_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_uint8_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_uint8_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_uint8_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_uint8_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_uint8_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_uint8_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_uint8_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_uint8_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_uint8_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_div_uint8_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_float32_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_float32_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_float32_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_float32_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_float32_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_float32_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_float32_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_float32_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_float32_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_float32_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_float64_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_float64_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_float64_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_float64_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_float64_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_float64_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_float64_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_float64_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_float64_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_float64_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_int16_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_int16_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_int16_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_int16_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_int16_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_int16_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_int16_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_int16_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_int16_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_int16_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_int32_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_int32_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_int32_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_int32_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_int32_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_int32_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_int32_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_int32_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_int32_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_int32_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_int64_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_int64_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_int64_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_int64_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_int64_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_int64_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_int64_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_int64_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_int64_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_int64_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_int8_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_int8_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_int8_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_int8_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_int8_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_int8_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_int8_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_int8_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_int8_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_int8_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_uint16_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_uint16_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_uint16_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_uint16_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_uint16_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_uint16_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_uint16_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_uint16_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_uint16_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_uint16_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_uint32_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_uint32_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_uint32_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_uint32_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_uint32_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_uint32_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_uint32_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_uint32_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_uint32_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_uint32_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_uint64_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_uint64_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_uint64_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_uint64_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_uint64_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_uint64_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_uint64_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_uint64_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_uint64_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_uint64_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_uint8_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_uint8_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_uint8_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_uint8_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_uint8_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_uint8_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_uint8_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_uint8_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_uint8_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_eq_uint8_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_float32_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_float32_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_float32_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_float32_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_float32_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_float32_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_float32_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_float32_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_float32_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_float32_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_float64_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_float64_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_float64_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_float64_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_float64_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_float64_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_float64_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_float64_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_float64_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_float64_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_int16_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_int16_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_int16_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_int16_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_int16_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_int16_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_int16_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_int16_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_int16_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_int16_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_int32_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_int32_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_int32_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_int32_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_int32_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_int32_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_int32_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_int32_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_int32_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_int32_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_int64_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_int64_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_int64_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_int64_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_int64_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_int64_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_int64_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_int64_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_int64_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_int64_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_int8_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_int8_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_int8_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_int8_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_int8_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_int8_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_int8_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_int8_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_int8_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_int8_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_uint16_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_uint16_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_uint16_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_uint16_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_uint16_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_uint16_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_uint16_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_uint16_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_uint16_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_uint16_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_uint32_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_uint32_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_uint32_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_uint32_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_uint32_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_uint32_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_uint32_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_uint32_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_uint32_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_uint32_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_uint64_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_uint64_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_uint64_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_uint64_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_uint64_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_uint64_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_uint64_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_uint64_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_uint64_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_uint64_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_uint8_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_uint8_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_uint8_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_uint8_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_uint8_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_uint8_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_uint8_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_uint8_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_uint8_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ge_uint8_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_float32_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_float32_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_float32_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_float32_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_float32_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_float32_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_float32_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_float32_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_float32_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_float32_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_float64_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_float64_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_float64_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_float64_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_float64_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_float64_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_float64_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_float64_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_float64_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_float64_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_int16_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_int16_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_int16_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_int16_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_int16_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_int16_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_int16_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_int16_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_int16_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_int16_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_int32_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_int32_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_int32_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_int32_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_int32_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_int32_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_int32_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_int32_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_int32_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_int32_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_int64_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_int64_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_int64_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_int64_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_int64_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_int64_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_int64_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_int64_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_int64_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_int64_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_int8_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_int8_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_int8_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_int8_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_int8_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_int8_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_int8_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_int8_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_int8_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_int8_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_uint16_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_uint16_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_uint16_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_uint16_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_uint16_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_uint16_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_uint16_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_uint16_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_uint16_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_uint16_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_uint32_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_uint32_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_uint32_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_uint32_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_uint32_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_uint32_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_uint32_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_uint32_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_uint32_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_uint32_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_uint64_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_uint64_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_uint64_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_uint64_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_uint64_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_uint64_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_uint64_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_uint64_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_uint64_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_uint64_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_uint8_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_uint8_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_uint8_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_uint8_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_uint8_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_uint8_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_uint8_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_uint8_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_uint8_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_gt_uint8_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_float32_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_float32_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_float32_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_float32_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_float32_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_float32_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_float32_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_float32_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_float32_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_float32_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_float64_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_float64_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_float64_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_float64_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_float64_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_float64_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_float64_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_float64_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_float64_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_float64_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_int16_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_int16_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_int16_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_int16_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_int16_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_int16_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_int16_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_int16_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_int16_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_int16_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_int32_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_int32_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_int32_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_int32_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_int32_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_int32_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_int32_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_int32_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_int32_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_int32_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_int64_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_int64_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_int64_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_int64_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_int64_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_int64_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_int64_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_int64_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_int64_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_int64_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_int8_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_int8_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_int8_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_int8_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_int8_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_int8_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_int8_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_int8_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_int8_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_int8_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_uint16_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_uint16_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_uint16_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_uint16_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_uint16_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_uint16_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_uint16_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_uint16_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_uint16_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_uint16_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_uint32_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_uint32_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_uint32_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_uint32_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_uint32_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_uint32_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_uint32_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_uint32_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_uint32_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_uint32_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_uint64_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_uint64_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_uint64_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_uint64_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_uint64_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_uint64_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_uint64_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_uint64_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_uint64_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_uint64_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_uint8_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_uint8_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_uint8_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_uint8_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_uint8_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_uint8_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_uint8_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_uint8_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_uint8_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_le_uint8_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_float32_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_float32_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_float32_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_float32_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_float32_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_float32_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_float32_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_float32_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_float32_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_float32_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_float64_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_float64_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_float64_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_float64_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_float64_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_float64_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_float64_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_float64_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_float64_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_float64_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_int16_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_int16_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_int16_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_int16_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_int16_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_int16_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_int16_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_int16_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_int16_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_int16_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_int32_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_int32_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_int32_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_int32_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_int32_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_int32_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_int32_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_int32_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_int32_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_int32_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_int64_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_int64_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_int64_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_int64_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_int64_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_int64_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_int64_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_int64_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_int64_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_int64_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_int8_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_int8_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_int8_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_int8_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_int8_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_int8_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_int8_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_int8_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_int8_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_int8_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_uint16_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_uint16_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_uint16_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_uint16_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_uint16_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_uint16_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_uint16_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_uint16_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_uint16_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_uint16_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_uint32_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_uint32_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_uint32_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_uint32_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_uint32_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_uint32_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_uint32_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_uint32_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_uint32_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_uint32_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_uint64_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_uint64_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_uint64_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_uint64_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_uint64_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_uint64_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_uint64_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_uint64_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_uint64_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_uint64_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_uint8_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_uint8_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_uint8_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_uint8_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_uint8_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_uint8_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_uint8_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_uint8_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_uint8_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_lt_uint8_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_float32_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_float32_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_float32_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_float32_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_float32_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_float32_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_float32_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_float32_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_float32_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_float32_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_float64_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_float64_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_float64_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_float64_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_float64_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_float64_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_float64_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_float64_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_float64_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_float64_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_int16_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_int16_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_int16_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_int16_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_int16_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_int16_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_int16_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_int16_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_int16_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_int16_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_int32_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_int32_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_int32_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_int32_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_int32_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_int32_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_int32_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_int32_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_int32_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_int32_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_int64_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_int64_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_int64_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_int64_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_int64_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_int64_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_int64_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_int64_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_int64_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_int64_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_int8_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_int8_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_int8_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_int8_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_int8_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_int8_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_int8_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_int8_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_int8_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_int8_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_uint16_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_uint16_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_uint16_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_uint16_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_uint16_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_uint16_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_uint16_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_uint16_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_uint16_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_uint16_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_uint32_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_uint32_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_uint32_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_uint32_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_uint32_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_uint32_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_uint32_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_uint32_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_uint32_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_uint32_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_uint64_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_uint64_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_uint64_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_uint64_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_uint64_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_uint64_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_uint64_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_uint64_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_uint64_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_uint64_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_uint8_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_uint8_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_uint8_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_uint8_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_uint8_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_uint8_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_uint8_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_uint8_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_uint8_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_max_uint8_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_float32_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_float32_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_float32_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_float32_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_float32_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_float32_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_float32_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_float32_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_float32_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_float32_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_float64_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_float64_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_float64_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_float64_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_float64_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_float64_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_float64_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_float64_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_float64_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_float64_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_int16_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_int16_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_int16_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_int16_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_int16_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_int16_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_int16_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_int16_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_int16_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_int16_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_int32_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_int32_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_int32_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_int32_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_int32_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_int32_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_int32_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_int32_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_int32_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_int32_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_int64_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_int64_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_int64_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_int64_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_int64_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_int64_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_int64_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_int64_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_int64_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_int64_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_int8_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_int8_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_int8_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_int8_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_int8_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_int8_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_int8_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_int8_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_int8_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_int8_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_uint16_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_uint16_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_uint16_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_uint16_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_uint16_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_uint16_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_uint16_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_uint16_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_uint16_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_uint16_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_uint32_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_uint32_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_uint32_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_uint32_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_uint32_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_uint32_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_uint32_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_uint32_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_uint32_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_uint32_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_uint64_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_uint64_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_uint64_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_uint64_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_uint64_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_uint64_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_uint64_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_uint64_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_uint64_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_uint64_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_uint8_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_uint8_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_uint8_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_uint8_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_uint8_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_uint8_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_uint8_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_uint8_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_uint8_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_min_uint8_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_float32_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_float32_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_float32_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_float32_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_float32_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_float32_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_float32_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_float32_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_float32_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_float32_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_float64_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_float64_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_float64_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_float64_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_float64_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_float64_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_float64_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_float64_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_float64_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_float64_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_int16_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_int16_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_int16_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_int16_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_int16_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_int16_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_int16_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_int16_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_int16_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_int16_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_int32_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_int32_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_int32_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_int32_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_int32_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_int32_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_int32_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_int32_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_int32_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_int32_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_int64_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_int64_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_int64_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_int64_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_int64_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_int64_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_int64_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_int64_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_int64_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_int64_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_int8_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_int8_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_int8_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_int8_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_int8_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_int8_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_int8_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_int8_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_int8_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_int8_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_uint16_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_uint16_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_uint16_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_uint16_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_uint16_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_uint16_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_uint16_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_uint16_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_uint16_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_uint16_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_uint32_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_uint32_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_uint32_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_uint32_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_uint32_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_uint32_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_uint32_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_uint32_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_uint32_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_uint32_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_uint64_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_uint64_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_uint64_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_uint64_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_uint64_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_uint64_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_uint64_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_uint64_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_uint64_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_uint64_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_uint8_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_uint8_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_uint8_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_uint8_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_uint8_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_uint8_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_uint8_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_uint8_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_uint8_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_mul_uint8_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_float32_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_float32_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_float32_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_float32_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_float32_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_float32_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_float32_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_float32_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_float32_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_float32_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_float64_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_float64_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_float64_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_float64_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_float64_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_float64_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_float64_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_float64_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_float64_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_float64_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_int16_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_int16_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_int16_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_int16_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_int16_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_int16_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_int16_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_int16_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_int16_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_int16_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_int32_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_int32_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_int32_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_int32_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_int32_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_int32_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_int32_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_int32_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_int32_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_int32_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_int64_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_int64_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_int64_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_int64_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_int64_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_int64_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_int64_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_int64_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_int64_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_int64_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_int8_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_int8_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_int8_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_int8_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_int8_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_int8_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_int8_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_int8_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_int8_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_int8_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_uint16_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_uint16_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_uint16_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_uint16_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_uint16_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_uint16_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_uint16_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_uint16_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_uint16_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_uint16_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_uint32_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_uint32_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_uint32_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_uint32_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_uint32_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_uint32_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_uint32_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_uint32_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_uint32_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_uint32_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_uint64_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_uint64_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_uint64_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_uint64_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_uint64_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_uint64_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_uint64_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_uint64_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_uint64_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_uint64_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_uint8_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_uint8_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_uint8_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_uint8_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_uint8_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_uint8_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_uint8_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_uint8_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_uint8_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_ne_uint8_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_int16_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_int16_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_int16_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_int16_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_int16_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_int16_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_int16_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_int16_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_int16_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_int16_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_int32_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_int32_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_int32_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_int32_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_int32_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_int32_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_int32_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_int32_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_int32_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_int32_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_int64_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_int64_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_int64_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_int64_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_int64_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_int64_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_int64_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_int64_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_int64_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_int64_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_int8_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_int8_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_int8_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_int8_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_int8_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_int8_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_int8_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_int8_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_int8_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_int8_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_uint16_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_uint16_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_uint16_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_uint16_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_uint16_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_uint16_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_uint16_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_uint16_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_uint16_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_uint16_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_uint32_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_uint32_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_uint32_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_uint32_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_uint32_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_uint32_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_uint32_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_uint32_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_uint32_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_uint32_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_uint64_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_uint64_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_uint64_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_uint64_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_uint64_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_uint64_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_uint64_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_uint64_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_uint64_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_uint64_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_uint8_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_uint8_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_uint8_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_uint8_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_uint8_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_uint8_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_uint8_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_uint8_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_uint8_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_or_uint8_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_float32_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_float32_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_float32_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_float32_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_float32_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_float32_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_float32_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_float32_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_float32_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_float32_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_float64_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_float64_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_float64_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_float64_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_float64_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_float64_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_float64_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_float64_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_float64_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_float64_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_int16_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_int16_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_int16_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_int16_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_int16_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_int16_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_int16_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_int16_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_int16_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_int16_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_int32_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_int32_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_int32_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_int32_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_int32_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_int32_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_int32_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_int32_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_int32_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_int32_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_int64_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_int64_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_int64_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_int64_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_int64_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_int64_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_int64_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_int64_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_int64_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_int64_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_int8_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_int8_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_int8_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_int8_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_int8_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_int8_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_int8_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_int8_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_int8_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_int8_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_uint16_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_uint16_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_uint16_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_uint16_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_uint16_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_uint16_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_uint16_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_uint16_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_uint16_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_uint16_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_uint32_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_uint32_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_uint32_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_uint32_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_uint32_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_uint32_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_uint32_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_uint32_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_uint32_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_uint32_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_uint64_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_uint64_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_uint64_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_uint64_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_uint64_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_uint64_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_uint64_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_uint64_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_uint64_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_uint64_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_uint8_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_uint8_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_uint8_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_uint8_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_uint8_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_uint8_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_uint8_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_uint8_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_uint8_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_sub_uint8_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_int16_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_int16_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_int16_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_int16_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_int16_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_int16_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_int16_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_int16_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_int16_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_int16_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_int32_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_int32_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_int32_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_int32_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_int32_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_int32_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_int32_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_int32_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_int32_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_int32_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_int64_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_int64_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_int64_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_int64_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_int64_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_int64_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_int64_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_int64_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_int64_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_int64_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_int8_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_int8_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_int8_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_int8_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_int8_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_int8_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_int8_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_int8_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_int8_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_int8_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_uint16_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_uint16_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_uint16_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_uint16_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_uint16_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_uint16_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_uint16_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_uint16_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_uint16_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_uint16_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_uint32_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_uint32_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_uint32_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_uint32_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_uint32_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_uint32_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_uint32_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_uint32_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_uint32_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_uint32_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_uint64_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_uint64_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_uint64_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_uint64_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_uint64_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_uint64_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_uint64_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_uint64_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_uint64_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_uint64_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_uint8_float32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_uint8_float64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_uint8_int16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_uint8_int32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_uint8_int64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_uint8_int8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_uint8_uint16(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_uint8_uint32(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_uint8_uint64(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Binaryop_xor_uint8_uint8(streampu._ext.core.Module):
    @typing.overload
    def __init__(
        self, n_in1: typing.SupportsInt | typing.SupportsIndex, n_in2: typing.SupportsInt | typing.SupportsIndex
    ) -> None: ...
    @typing.overload
    def __init__(self, n_elmts: typing.SupportsInt | typing.SupportsIndex) -> None: ...
