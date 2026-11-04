from __future__ import annotations

import typing

import streampu._ext.sfl

__all__: list[str] = ["Sleeper"]

class Sleeper(streampu._ext.sfl.Stateful):
    """
    Module whose task only sleeps, e.g. to emulate some work.
    """

    def __init__(self, ns: typing.SupportsInt | typing.SupportsIndex = 0) -> None:
        """
        Build a sleeper.

        Args:
            ns (int): sleep duration per execution, in nanoseconds
        """

    @property
    def ns(self) -> int:
        """
        Sleep duration per execution, in nanoseconds.
        """

    @ns.setter
    def ns(self, arg1: typing.SupportsInt | typing.SupportsIndex) -> None: ...
