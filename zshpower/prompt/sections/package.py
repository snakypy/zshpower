import os
from os.path import isfile

import snakypy
import tomlkit

from .lib.utils import Color, symbol_ssh, separator, element_spacing


class PyProject(Color):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.pyproject_f = os.path.join(os.getcwd(), "pyproject.toml")
        self.pyproject_enable = config["pyproject"]["enable"]
        self.pyproject_symbol = symbol_ssh(config["pyproject"]["symbol"], "pkg-")
        self.pyproject_color = config["pyproject"]["color"]
        self.pyproject_prefix_color = config["pyproject"]["prefix"]["color"]
        self.pyproject_prefix_text = element_spacing(
            config["pyproject"]["prefix"]["text"]
        )

    def get_version(self, space_elem=" "):
        if isfile(self.pyproject_f):
            read_f = snakypy.file.read(self.pyproject_f)
            parsed = dict(tomlkit.parse(read_f))
            for item in parsed.values():
                for data in item.values():
                    return f"{data['version']}{space_elem}"
        return ""

    def __str__(self):
        if self.pyproject_enable and isfile(self.pyproject_f):
            pyproject_prefix = (
                f"{Color(self.pyproject_prefix_color)}"
                f"{self.pyproject_prefix_text}{Color().NONE}"
            )
            pyproject_export = (
                f"{separator(self.config)}{pyproject_prefix}"
                f"{Color(self.pyproject_color)}"
                f"{self.pyproject_symbol}{self.get_version()}{Color().NONE}"
            )
            return str(pyproject_export)
        return ""
