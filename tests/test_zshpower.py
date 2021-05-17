"""Tests for `zshpower` package."""

from tomlkit import parse as toml_parsed
from snakypy.helpers.files import read_file
from os.path import join, exists
from os import getcwd
from snakypy.zshpower import __version__


def test_version():
    pyproject = join(getcwd(), "pyproject.toml")
    if exists(pyproject):
        version_toml = toml_parsed(read_file(pyproject))["tool"]["poetry"]["version"]
        assert version_toml == __version__
