from __future__ import annotations

import typing

import streampu._ext
import streampu._ext.sfl

__all__: list[str] = ["Switcher"]

class Switcher(streampu._ext.sfl.Stateful):
    """

    Module that implements a conditional path in a sequence.

    Its task `commute` sends its data to one of `n_data_sockets` paths, chosen by the
    output of a controller; its task `select` takes the data of the path that was
    executed and forwards it.

    """

    @typing.overload
    def __init__(
        self,
        n_data_sockets: typing.SupportsInt | typing.SupportsIndex,
        n_elmts_commute: typing.SupportsInt | typing.SupportsIndex,
        datatype_commute: streampu._ext.dtype,
        n_elmts_select: typing.SupportsInt | typing.SupportsIndex,
        datatype_select: streampu._ext.dtype,
    ) -> None:
        """
        Build a switcher whose commuted and selected data have different types.

        Args:
            n_data_sockets (int): number of paths
            n_elmts_commute (int): number of elements of the commuted data
            datatype_commute (dtype): data type of the commuted data
            n_elmts_select (int): number of elements of the selected data
            datatype_select (dtype): data type of the selected data
        """

    @typing.overload
    def __init__(
        self,
        n_data_sockets: typing.SupportsInt | typing.SupportsIndex,
        n_elmts: typing.SupportsInt | typing.SupportsIndex,
        datatype: streampu._ext.dtype,
    ) -> None:
        """
        Build a switcher.

        Args:
            n_data_sockets (int): number of paths
            n_elmts (int): number of elements of the data
            datatype (dtype): data type of the data
        """
