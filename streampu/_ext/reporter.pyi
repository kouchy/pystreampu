from __future__ import annotations

import collections.abc

import streampu._ext.interfaces

__all__: list[str] = ["Reporter", "Reporter_probe"]

class Reporter(streampu._ext.interfaces.Interface_reset):
    """
    Base class of the reporters, which provide the values displayed by a terminal.
    """

    def init(self) -> None:
        """
        Initialize the reporter before the first report.
        """

    @property
    def groups(self) -> list[tuple[tuple[str, str, int], list[tuple[str, str, int]]]]:
        """
        Groups of columns of the reporter: titles and column names.
        """

class Reporter_probe(Reporter, streampu._ext.interfaces.Interface_get_set_n_frames):
    """

    Reporter that gathers the values of probes, one column per probe.

    Probes are attached to it when they are created (their `reporter` argument).

    """

    def __init__(self, group_name: str, group_description: str) -> None:
        """
        Build a reporter.

        Args:
            group_name (str): title of the group of columns
            group_description (str): subtitle of the group of columns
        """

    def register_probes(self, probes: collections.abc.Sequence[...]) -> None:
        """
        Attach probes to the reporter.

        Args:
            probes (list[AProbe]): probes to attach
        """
