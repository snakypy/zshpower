"""Tests for `zshpower` package."""

from os import getcwd
from os.path import exists, join

from snakypy.helpers.files import read_file
from tomlkit import parse as toml_parsed

from snakypy.zshpower import __info__


def test_version():
    pyproject = join(getcwd(), "pyproject.toml")
    if exists(pyproject):
        version_toml = toml_parsed(read_file(pyproject))["tool"]["poetry"]["version"]
        assert version_toml == __info__["version"]
