from __future__ import annotations

import typing

__all__: list[str] = [
    "Interface_clone",
    "Interface_get_set_n_frames",
    "Interface_is_done",
    "Interface_reset",
    "Interface_set_seed",
    "Interface_waiting",
]

class Interface_clone:
    """
    Interface of the objects that can be duplicated (e.g. on several threads).
    """

    def clone(self) -> Interface_clone:
        """
        Return a copy of the object.

        Returns:
            out (Interface_clone): the copy
        """

class Interface_get_set_n_frames:
    """
    Interface of the objects that process several frames per execution.
    """

    @property
    def n_frames(self) -> int:
        """
        Number of frames processed at each execution (rows of the socket data).
        """

    @n_frames.setter
    def n_frames(self, arg1: typing.SupportsInt | typing.SupportsIndex) -> None: ...

class Interface_is_done:
    """
    Interface of the objects that can tell when they have nothing more to produce.
    """

    def is_done(self) -> bool:
        """
        Tell whether the object has nothing more to produce (e.g. a source at the end of its file).

        Returns:
            out (bool): True if done
        """

class Interface_reset:
    """
    Interface of the objects that can be reset to their initial state.
    """

    def reset(self) -> None:
        """
        Reset the object to its initial state.
        """

class Interface_set_seed:
    """
    Interface of the objects that use a random generator.
    """

    def set_seed(self, seed: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Set the seed of the random generator.

        Args:
            seed (int): the new seed
        """

class Interface_waiting(Interface_reset):
    """
    Interface of the objects that can block while waiting for data (e.g. pipeline adaptors).
    """

    def cancel_waiting(self) -> None:
        """
        Send the cancel signal and wake up the waiting tasks.
        """

    def send_cancel_signal(self) -> None:
        """
        Ask the waiting tasks to stop waiting.
        """

    def wake_up(self) -> None:
        """
        Wake up the waiting tasks.
        """
