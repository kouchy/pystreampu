from __future__ import annotations

import typing

import streampu._ext.interfaces
import streampu._ext.sfl

__all__: list[str] = ["Controller", "Controller_cyclic", "Controller_limit", "Controller_static"]

class Controller(streampu._ext.sfl.Stateful, streampu._ext.interfaces.Interface_reset):
    """
    Base class of the controllers: modules that output the index of the path to take in a `Switcher`.
    """

    @property
    def path(self) -> int:
        """
        Index of the current path.
        """

    @path.setter
    def path(self, arg1: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Controller_cyclic(Controller):
    """
    Controller that cycles through the paths: 0, 1, ..., n_paths - 1, 0, ...
    """

    def __init__(
        self,
        n_paths: typing.SupportsInt | typing.SupportsIndex,
        init_path: typing.SupportsInt | typing.SupportsIndex = 0,
    ) -> None:
        """
        Build a cyclic controller.

        Args:
            n_paths (int): number of paths
            init_path (int): first path
        """

    def set_n_paths(self, n_paths: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Change the number of paths.

        Args:
            n_paths (int): number of paths
        """

    @property
    def path(self) -> int:
        """
        Index of the current path.
        """

    @path.setter
    def path(self, arg1: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Controller_limit(Controller):
    """
    Controller that outputs `init_path` for the first `limit` executions, then the other path.
    """

    def __init__(
        self, limit: typing.SupportsInt | typing.SupportsIndex, init_path: typing.SupportsInt | typing.SupportsIndex = 0
    ) -> None:
        """
        Build a controller with a limit.

        Args:
            limit (int): number of executions before switching path
            init_path (int): first path (0 or 1)
        """

class Controller_static(Controller):
    """
    Controller that always outputs the same path (it can be changed with `path`).
    """

    def __init__(self, init_path: typing.SupportsInt | typing.SupportsIndex = 0) -> None:
        """
        Build a static controller.

        Args:
            init_path (int): path to output
        """
