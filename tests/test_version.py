"""Test that a version string can be retrieved from the library."""

import streampu as spu


def test_version():
    version = spu.__version__
    assert isinstance(version, str)
    assert len(version) > 0
