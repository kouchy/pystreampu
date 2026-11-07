"""Tests of the terminals and of the public base classes."""

import gc
import weakref

import pytest

import streampu as spu


@pytest.mark.parametrize("terminal_class", [spu.Terminal_std, spu.Terminal_dump])
def test_terminal_keeps_its_reporters_alive(terminal_class):
    """The terminal only stores pointers to the reporters: it keeps their Python objects alive."""
    reporter = spu.Reporter_probe("Experiment title", "Subtitle")
    ref = weakref.ref(reporter)
    terminal = terminal_class([reporter])
    del reporter
    gc.collect()
    assert ref() is not None  # kept alive by the terminal
    assert terminal.reporters[0] is ref()
    del terminal
    gc.collect()
    assert ref() is None  # released with the terminal


def test_terminal_reporters_property_does_not_own_them():
    reporter = spu.Reporter_probe("Title", "Subtitle")
    terminal = spu.Terminal_std([reporter])
    reporters = terminal.reporters
    del terminal, reporters
    gc.collect()
    reporter.init()  # still valid


def test_stateful_is_public():
    assert spu.Stateful is spu._ext.sfl.Stateful
    assert issubclass(spu.Stateful_core, spu.Stateful)
    assert isinstance(spu.Iterator(1), spu.Stateful)
