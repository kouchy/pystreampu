from __future__ import annotations

import streampu._ext.sfl

__all__: list[str] = ["Set"]

class Set(streampu._ext.sfl.Stateful):
    """
    Module that wraps a sequence, so that the whole sequence can be used as a single task (`exec`).
    """

    def __init__(self: set, sequence: ...) -> None:
        """
        Build a set from a sequence.

        Args:
            sequence (Sequence): the sequence to wrap
        """

    @property
    def sequence(self) -> ...:
        """
        Sequence wrapped by the set.
        """
