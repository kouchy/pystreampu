from __future__ import annotations

import typing

import streampu._ext
import streampu._ext.interfaces
import streampu._ext.reporter
import streampu._ext.sfl

__all__: list[str] = [
    "AProbe",
    "Probe_float32",
    "Probe_float64",
    "Probe_int16",
    "Probe_int32",
    "Probe_int64",
    "Probe_int8",
    "Probe_latency",
    "Probe_occurrence",
    "Probe_throughput",
    "Probe_time",
    "Probe_timestamp",
    "Probe_uint16",
    "Probe_uint32",
    "Probe_uint64",
    "Probe_uint8",
    "Probe_value_float32",
    "Probe_value_float64",
    "Probe_value_int16",
    "Probe_value_int32",
    "Probe_value_int64",
    "Probe_value_int8",
    "Probe_value_uint16",
    "Probe_value_uint32",
    "Probe_value_uint64",
    "Probe_value_uint8",
]

class AProbe(streampu._ext.sfl.Stateful, streampu._ext.interfaces.Interface_reset):
    """
    Base class of the probes: modules that observe the graph and fill a column of a `Reporter_probe`.
    """

    @property
    def str_display(self) -> bool:
        """
        If True, display the probed values as a string of characters.
        """

    @str_display.setter
    def str_display(self, arg1: bool) -> None: ...

class Probe_float32(AProbe):
    def get_col_name(self) -> str:
        """
        Return the name of the column of the probe.
        """

    def register_reporter(self, reporter: streampu._ext.reporter.Reporter_probe) -> None:
        """
        Attach the probe to a reporter (if it was not given at creation).

        Args:
            reporter (Reporter_probe): the reporter
        """

    def set_col_buff_size(self, buffer_size: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Set the number of values kept by the probe between two reports.

        Args:
            buffer_size (int): number of values
        """

    def set_col_fmtflags(self, ff: streampu._ext.FormatFlags) -> None:
        """
        Set the format of the values of the column.

        Args:
            ff (FormatFlags): format flags, e.g. `FormatFlags.fixed | FormatFlags.showpoint`
        """

    def set_col_prec(self, precision: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Set the number of decimals of the values of the column.

        Args:
            precision (int): number of decimals
        """

    def set_col_size(self, col_size: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Set the width of the column.

        Args:
            col_size (int): width, in characters
        """

    def set_col_unit(self, unit: str) -> None:
        """
        Set the unit displayed under the name of the column.

        Args:
            unit (str): the unit, e.g. "(s)"
        """

class Probe_float64(AProbe):
    def get_col_name(self) -> str:
        """
        Return the name of the column of the probe.
        """

    def register_reporter(self, reporter: streampu._ext.reporter.Reporter_probe) -> None:
        """
        Attach the probe to a reporter (if it was not given at creation).

        Args:
            reporter (Reporter_probe): the reporter
        """

    def set_col_buff_size(self, buffer_size: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Set the number of values kept by the probe between two reports.

        Args:
            buffer_size (int): number of values
        """

    def set_col_fmtflags(self, ff: streampu._ext.FormatFlags) -> None:
        """
        Set the format of the values of the column.

        Args:
            ff (FormatFlags): format flags, e.g. `FormatFlags.fixed | FormatFlags.showpoint`
        """

    def set_col_prec(self, precision: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Set the number of decimals of the values of the column.

        Args:
            precision (int): number of decimals
        """

    def set_col_size(self, col_size: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Set the width of the column.

        Args:
            col_size (int): width, in characters
        """

    def set_col_unit(self, unit: str) -> None:
        """
        Set the unit displayed under the name of the column.

        Args:
            unit (str): the unit, e.g. "(s)"
        """

class Probe_int16(AProbe):
    def get_col_name(self) -> str:
        """
        Return the name of the column of the probe.
        """

    def register_reporter(self, reporter: streampu._ext.reporter.Reporter_probe) -> None:
        """
        Attach the probe to a reporter (if it was not given at creation).

        Args:
            reporter (Reporter_probe): the reporter
        """

    def set_col_buff_size(self, buffer_size: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Set the number of values kept by the probe between two reports.

        Args:
            buffer_size (int): number of values
        """

    def set_col_fmtflags(self, ff: streampu._ext.FormatFlags) -> None:
        """
        Set the format of the values of the column.

        Args:
            ff (FormatFlags): format flags, e.g. `FormatFlags.fixed | FormatFlags.showpoint`
        """

    def set_col_prec(self, precision: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Set the number of decimals of the values of the column.

        Args:
            precision (int): number of decimals
        """

    def set_col_size(self, col_size: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Set the width of the column.

        Args:
            col_size (int): width, in characters
        """

    def set_col_unit(self, unit: str) -> None:
        """
        Set the unit displayed under the name of the column.

        Args:
            unit (str): the unit, e.g. "(s)"
        """

class Probe_int32(AProbe):
    def get_col_name(self) -> str:
        """
        Return the name of the column of the probe.
        """

    def register_reporter(self, reporter: streampu._ext.reporter.Reporter_probe) -> None:
        """
        Attach the probe to a reporter (if it was not given at creation).

        Args:
            reporter (Reporter_probe): the reporter
        """

    def set_col_buff_size(self, buffer_size: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Set the number of values kept by the probe between two reports.

        Args:
            buffer_size (int): number of values
        """

    def set_col_fmtflags(self, ff: streampu._ext.FormatFlags) -> None:
        """
        Set the format of the values of the column.

        Args:
            ff (FormatFlags): format flags, e.g. `FormatFlags.fixed | FormatFlags.showpoint`
        """

    def set_col_prec(self, precision: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Set the number of decimals of the values of the column.

        Args:
            precision (int): number of decimals
        """

    def set_col_size(self, col_size: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Set the width of the column.

        Args:
            col_size (int): width, in characters
        """

    def set_col_unit(self, unit: str) -> None:
        """
        Set the unit displayed under the name of the column.

        Args:
            unit (str): the unit, e.g. "(s)"
        """

class Probe_int64(AProbe):
    def get_col_name(self) -> str:
        """
        Return the name of the column of the probe.
        """

    def register_reporter(self, reporter: streampu._ext.reporter.Reporter_probe) -> None:
        """
        Attach the probe to a reporter (if it was not given at creation).

        Args:
            reporter (Reporter_probe): the reporter
        """

    def set_col_buff_size(self, buffer_size: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Set the number of values kept by the probe between two reports.

        Args:
            buffer_size (int): number of values
        """

    def set_col_fmtflags(self, ff: streampu._ext.FormatFlags) -> None:
        """
        Set the format of the values of the column.

        Args:
            ff (FormatFlags): format flags, e.g. `FormatFlags.fixed | FormatFlags.showpoint`
        """

    def set_col_prec(self, precision: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Set the number of decimals of the values of the column.

        Args:
            precision (int): number of decimals
        """

    def set_col_size(self, col_size: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Set the width of the column.

        Args:
            col_size (int): width, in characters
        """

    def set_col_unit(self, unit: str) -> None:
        """
        Set the unit displayed under the name of the column.

        Args:
            unit (str): the unit, e.g. "(s)"
        """

class Probe_int8(AProbe):
    def get_col_name(self) -> str:
        """
        Return the name of the column of the probe.
        """

    def register_reporter(self, reporter: streampu._ext.reporter.Reporter_probe) -> None:
        """
        Attach the probe to a reporter (if it was not given at creation).

        Args:
            reporter (Reporter_probe): the reporter
        """

    def set_col_buff_size(self, buffer_size: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Set the number of values kept by the probe between two reports.

        Args:
            buffer_size (int): number of values
        """

    def set_col_fmtflags(self, ff: streampu._ext.FormatFlags) -> None:
        """
        Set the format of the values of the column.

        Args:
            ff (FormatFlags): format flags, e.g. `FormatFlags.fixed | FormatFlags.showpoint`
        """

    def set_col_prec(self, precision: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Set the number of decimals of the values of the column.

        Args:
            precision (int): number of decimals
        """

    def set_col_size(self, col_size: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Set the width of the column.

        Args:
            col_size (int): width, in characters
        """

    def set_col_unit(self, unit: str) -> None:
        """
        Set the unit displayed under the name of the column.

        Args:
            unit (str): the unit, e.g. "(s)"
        """

class Probe_latency(Probe_uint8):
    """
    Probe that reports the time elapsed since its previous execution, in microseconds.
    """

    def __init__(self, col_name: str, reporter: streampu._ext.reporter.Reporter_probe = None) -> None: ...

class Probe_occurrence(Probe_uint8):
    """
    Probe that reports the number of times it has been executed.
    """

    def __init__(self, col_name: str, reporter: streampu._ext.reporter.Reporter_probe = None) -> None: ...

class Probe_throughput(Probe_uint8):
    """
    Probe that reports a throughput: `data_size * n_frames / factor` per second (factor 2**20 by default, i.e. MB/s).
    """

    @typing.overload
    def __init__(
        self,
        data_size: typing.SupportsInt | typing.SupportsIndex,
        col_name: str,
        reporter: streampu._ext.reporter.Reporter_probe = None,
    ) -> None: ...
    @typing.overload
    def __init__(
        self,
        data_size: typing.SupportsInt | typing.SupportsIndex,
        col_name: str,
        factor: typing.SupportsFloat | typing.SupportsIndex,
        reporter: streampu._ext.reporter.Reporter_probe = None,
    ) -> None: ...

class Probe_time(Probe_uint8):
    """
    Probe that reports the time elapsed since its creation or its last reset, in seconds.
    """

    def __init__(self, col_name: str, reporter: streampu._ext.reporter.Reporter_probe = None) -> None: ...

class Probe_timestamp(Probe_uint8):
    """
    Probe that reports a timestamp in microseconds (modulo `mod` if `mod` is not 0).
    """

    @typing.overload
    def __init__(
        self,
        mod: typing.SupportsInt | typing.SupportsIndex,
        col_name: str,
        reporter: streampu._ext.reporter.Reporter_probe = None,
    ) -> None: ...
    @typing.overload
    def __init__(self, col_name: str, reporter: streampu._ext.reporter.Reporter_probe = None) -> None: ...

class Probe_uint16(AProbe):
    def get_col_name(self) -> str:
        """
        Return the name of the column of the probe.
        """

    def register_reporter(self, reporter: streampu._ext.reporter.Reporter_probe) -> None:
        """
        Attach the probe to a reporter (if it was not given at creation).

        Args:
            reporter (Reporter_probe): the reporter
        """

    def set_col_buff_size(self, buffer_size: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Set the number of values kept by the probe between two reports.

        Args:
            buffer_size (int): number of values
        """

    def set_col_fmtflags(self, ff: streampu._ext.FormatFlags) -> None:
        """
        Set the format of the values of the column.

        Args:
            ff (FormatFlags): format flags, e.g. `FormatFlags.fixed | FormatFlags.showpoint`
        """

    def set_col_prec(self, precision: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Set the number of decimals of the values of the column.

        Args:
            precision (int): number of decimals
        """

    def set_col_size(self, col_size: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Set the width of the column.

        Args:
            col_size (int): width, in characters
        """

    def set_col_unit(self, unit: str) -> None:
        """
        Set the unit displayed under the name of the column.

        Args:
            unit (str): the unit, e.g. "(s)"
        """

class Probe_uint32(AProbe):
    def get_col_name(self) -> str:
        """
        Return the name of the column of the probe.
        """

    def register_reporter(self, reporter: streampu._ext.reporter.Reporter_probe) -> None:
        """
        Attach the probe to a reporter (if it was not given at creation).

        Args:
            reporter (Reporter_probe): the reporter
        """

    def set_col_buff_size(self, buffer_size: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Set the number of values kept by the probe between two reports.

        Args:
            buffer_size (int): number of values
        """

    def set_col_fmtflags(self, ff: streampu._ext.FormatFlags) -> None:
        """
        Set the format of the values of the column.

        Args:
            ff (FormatFlags): format flags, e.g. `FormatFlags.fixed | FormatFlags.showpoint`
        """

    def set_col_prec(self, precision: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Set the number of decimals of the values of the column.

        Args:
            precision (int): number of decimals
        """

    def set_col_size(self, col_size: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Set the width of the column.

        Args:
            col_size (int): width, in characters
        """

    def set_col_unit(self, unit: str) -> None:
        """
        Set the unit displayed under the name of the column.

        Args:
            unit (str): the unit, e.g. "(s)"
        """

class Probe_uint64(AProbe):
    def get_col_name(self) -> str:
        """
        Return the name of the column of the probe.
        """

    def register_reporter(self, reporter: streampu._ext.reporter.Reporter_probe) -> None:
        """
        Attach the probe to a reporter (if it was not given at creation).

        Args:
            reporter (Reporter_probe): the reporter
        """

    def set_col_buff_size(self, buffer_size: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Set the number of values kept by the probe between two reports.

        Args:
            buffer_size (int): number of values
        """

    def set_col_fmtflags(self, ff: streampu._ext.FormatFlags) -> None:
        """
        Set the format of the values of the column.

        Args:
            ff (FormatFlags): format flags, e.g. `FormatFlags.fixed | FormatFlags.showpoint`
        """

    def set_col_prec(self, precision: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Set the number of decimals of the values of the column.

        Args:
            precision (int): number of decimals
        """

    def set_col_size(self, col_size: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Set the width of the column.

        Args:
            col_size (int): width, in characters
        """

    def set_col_unit(self, unit: str) -> None:
        """
        Set the unit displayed under the name of the column.

        Args:
            unit (str): the unit, e.g. "(s)"
        """

class Probe_uint8(AProbe):
    def get_col_name(self) -> str:
        """
        Return the name of the column of the probe.
        """

    def register_reporter(self, reporter: streampu._ext.reporter.Reporter_probe) -> None:
        """
        Attach the probe to a reporter (if it was not given at creation).

        Args:
            reporter (Reporter_probe): the reporter
        """

    def set_col_buff_size(self, buffer_size: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Set the number of values kept by the probe between two reports.

        Args:
            buffer_size (int): number of values
        """

    def set_col_fmtflags(self, ff: streampu._ext.FormatFlags) -> None:
        """
        Set the format of the values of the column.

        Args:
            ff (FormatFlags): format flags, e.g. `FormatFlags.fixed | FormatFlags.showpoint`
        """

    def set_col_prec(self, precision: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Set the number of decimals of the values of the column.

        Args:
            precision (int): number of decimals
        """

    def set_col_size(self, col_size: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Set the width of the column.

        Args:
            col_size (int): width, in characters
        """

    def set_col_unit(self, unit: str) -> None:
        """
        Set the unit displayed under the name of the column.

        Args:
            unit (str): the unit, e.g. "(s)"
        """

class Probe_value_float32(Probe_float32):
    def __init__(
        self,
        size: typing.SupportsInt | typing.SupportsIndex,
        col_name: str,
        reporter: streampu._ext.reporter.Reporter_probe,
    ) -> None:
        """
        Build a probe that reports the values of a socket (use `streampu.probe_value`).

        Args:
            size (int): number of elements of the probed socket
            col_name (str): name of the column
            reporter (Reporter_probe): reporter of the probe
        """

class Probe_value_float64(Probe_float64):
    def __init__(
        self,
        size: typing.SupportsInt | typing.SupportsIndex,
        col_name: str,
        reporter: streampu._ext.reporter.Reporter_probe,
    ) -> None:
        """
        Build a probe that reports the values of a socket (use `streampu.probe_value`).

        Args:
            size (int): number of elements of the probed socket
            col_name (str): name of the column
            reporter (Reporter_probe): reporter of the probe
        """

class Probe_value_int16(Probe_int16):
    def __init__(
        self,
        size: typing.SupportsInt | typing.SupportsIndex,
        col_name: str,
        reporter: streampu._ext.reporter.Reporter_probe,
    ) -> None:
        """
        Build a probe that reports the values of a socket (use `streampu.probe_value`).

        Args:
            size (int): number of elements of the probed socket
            col_name (str): name of the column
            reporter (Reporter_probe): reporter of the probe
        """

class Probe_value_int32(Probe_int32):
    def __init__(
        self,
        size: typing.SupportsInt | typing.SupportsIndex,
        col_name: str,
        reporter: streampu._ext.reporter.Reporter_probe,
    ) -> None:
        """
        Build a probe that reports the values of a socket (use `streampu.probe_value`).

        Args:
            size (int): number of elements of the probed socket
            col_name (str): name of the column
            reporter (Reporter_probe): reporter of the probe
        """

class Probe_value_int64(Probe_int64):
    def __init__(
        self,
        size: typing.SupportsInt | typing.SupportsIndex,
        col_name: str,
        reporter: streampu._ext.reporter.Reporter_probe,
    ) -> None:
        """
        Build a probe that reports the values of a socket (use `streampu.probe_value`).

        Args:
            size (int): number of elements of the probed socket
            col_name (str): name of the column
            reporter (Reporter_probe): reporter of the probe
        """

class Probe_value_int8(Probe_int8):
    def __init__(
        self,
        size: typing.SupportsInt | typing.SupportsIndex,
        col_name: str,
        reporter: streampu._ext.reporter.Reporter_probe,
    ) -> None:
        """
        Build a probe that reports the values of a socket (use `streampu.probe_value`).

        Args:
            size (int): number of elements of the probed socket
            col_name (str): name of the column
            reporter (Reporter_probe): reporter of the probe
        """

class Probe_value_uint16(Probe_uint16):
    def __init__(
        self,
        size: typing.SupportsInt | typing.SupportsIndex,
        col_name: str,
        reporter: streampu._ext.reporter.Reporter_probe,
    ) -> None:
        """
        Build a probe that reports the values of a socket (use `streampu.probe_value`).

        Args:
            size (int): number of elements of the probed socket
            col_name (str): name of the column
            reporter (Reporter_probe): reporter of the probe
        """

class Probe_value_uint32(Probe_uint32):
    def __init__(
        self,
        size: typing.SupportsInt | typing.SupportsIndex,
        col_name: str,
        reporter: streampu._ext.reporter.Reporter_probe,
    ) -> None:
        """
        Build a probe that reports the values of a socket (use `streampu.probe_value`).

        Args:
            size (int): number of elements of the probed socket
            col_name (str): name of the column
            reporter (Reporter_probe): reporter of the probe
        """

class Probe_value_uint64(Probe_uint64):
    def __init__(
        self,
        size: typing.SupportsInt | typing.SupportsIndex,
        col_name: str,
        reporter: streampu._ext.reporter.Reporter_probe,
    ) -> None:
        """
        Build a probe that reports the values of a socket (use `streampu.probe_value`).

        Args:
            size (int): number of elements of the probed socket
            col_name (str): name of the column
            reporter (Reporter_probe): reporter of the probe
        """

class Probe_value_uint8(Probe_uint8):
    def __init__(
        self,
        size: typing.SupportsInt | typing.SupportsIndex,
        col_name: str,
        reporter: streampu._ext.reporter.Reporter_probe,
    ) -> None:
        """
        Build a probe that reports the values of a socket (use `streampu.probe_value`).

        Args:
            size (int): number of elements of the probed socket
            col_name (str): name of the column
            reporter (Reporter_probe): reporter of the probe
        """
