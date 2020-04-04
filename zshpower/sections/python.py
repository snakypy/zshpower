import os
import sys
from os.path import exists, join
from .lib.utils import Color, symbol_ssh, separator, element_spacing


class Python(Color):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.search_f = (
            "__pycache__",
            "manage.py",
            "setup.py",
            "__init__.py",
            ".python-version",
            "requirements.txt",
            "pyproject.toml",
        )
        self.py_symbol = config["python"]["symbol"]
        self.py_symbol = symbol_ssh(config["python"]["symbol"], "py-")
        self.py_color = config["python"]["color"]
        self.py_prefix_color = config["python"]["prefix"]["color"]
        self.py_prefix_text = element_spacing(config["python"]["prefix"]["text"])
        self.py_version_enable = config["python"]["version"]["enable"]
        self.pyv_micro_enable = config["python"]["version"]["micro"]["enable"]

    def get_version(self, space_elem=" "):
        if not self.pyv_micro_enable:
            version = "{0[0]}.{0[1]}".format(sys.version_info)
            return f"{version}{space_elem}"
        else:
            version = "{0[0]}.{0[1]}.{0[2]}".format(sys.version_info)
            return f"{version}{space_elem}"

    def __str__(self):
        py_prefix1 = f"{Color(self.py_prefix_color)}{self.py_prefix_text}{Color().NONE}"
        if self.py_version_enable:
            for item in self.search_f:
                if exists(join(os.getcwd(), item)) or "VIRTUAL_ENV" in os.environ:
                    return str(
                        (
                            f"{separator(self.config)}{py_prefix1}"
                            f"{Color(self.py_color)}{self.py_symbol}"
                            f"{self.get_version()}{Color().NONE}"
                        )
                    )
        return ""
