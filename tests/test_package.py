"""Test some package level functionality."""

import os

import streampu as spu


def test_get_cmake_dirs():
    dirs = spu.get_cmake_dirs()
    assert dirs is not None

    # split the directories by colon and check that we get a list of directories
    dir_list = dirs.split(":")
    assert isinstance(dir_list, list)
    assert len(dir_list) > 0
    # check that each directory exists
    for dir in dir_list:
        assert os.path.isdir(dir)


def test_version():
    version = spu.__version__
    assert version is not None
    assert isinstance(version, str)
    assert len(version) > 0


if __name__ == "__main__":
    test_get_cmake_dirs()
    test_version()
