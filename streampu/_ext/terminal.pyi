from __future__ import annotations

import collections.abc
import datetime

import streampu._ext.reporter

__all__: list[str] = ["Terminal", "Terminal_dump", "Terminal_std"]

class Terminal:
    """
    Base class of the terminals, which display the reports of reporters.
    """

    def __init__(self) -> None: ...
    def final_report(self, stream: ... = ...) -> None:
        """
        Print the final report.

        Args:
            stream (file): stream where the report is written
        """

    def legend(self, stream: ... = ...) -> None:
        """
        Print the legend: titles, names and units of the columns.

        Args:
            stream (file): stream where the legend is written
        """

    def report(self, stream: ... = ..., final: bool = False) -> None:
        """
        Print a report line with the current values of the reporters.

        Args:
            stream (file): stream where the report is written
            final (bool): True for the final report
        """

    def start_temp_report(self, freq: datetime.timedelta = ...) -> None:
        """
        Print temporary reports periodically, from a background thread.

        Args:
            freq (datetime.timedelta): period of the reports
        """

    def stop_temp_report(self) -> None:
        """
        Stop the periodic reports started by `start_temp_report`.
        """

    def temp_report(self, stream: ... = ...) -> None:
        """
        Print a temporary report (the line is overwritten by the next report).

        Args:
            stream (file): stream where the report is written
        """

class Terminal_dump(Terminal_std):
    """
    Terminal that prints one line per report (no overwritten temporary line), e.g. to a file.
    """

    def __init__(self, reporters: collections.abc.Sequence[streampu._ext.reporter.Reporter]) -> None:
        """
        Build a terminal.

        The terminal keeps the reporters alive (the list given here).

        Args:
            reporters (list[Reporter]): reporters to display
        """

class Terminal_std(Terminal):
    """
    Terminal that prints the reports as aligned columns.
    """

    def __init__(self, reporters: collections.abc.Sequence[streampu._ext.reporter.Reporter]) -> None:
        """
        Build a terminal.

        The terminal keeps the reporters alive (the list given here).

        Args:
            reporters (list[Reporter]): reporters to display
        """

    @property
    def reporters(self) -> list[streampu._ext.reporter.Reporter]:
        """
        Reporters displayed by the terminal.
        """
