class Python:
    def __init__(self, config):
        from .lib.utils import symbol_ssh, element_spacing

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
        from sys import version_info as sys_version_info

        if not self.pyv_micro_enable:
            version = "{0[0]}.{0[1]}".format(sys_version_info)
            return f"{version}{space_elem}"
        else:
            version = "{0[0]}.{0[1]}.{0[2]}".format(sys_version_info)
            return f"{version}{space_elem}"

    def __str__(self):
        from .lib.utils import Color, separator
        from zshpower.utils.catch import find_files
        from zshpower.utils.check import is_tool
        from os import environ as os_environ, getcwd as os_getcwd

        py_prefix1 = f"{Color(self.py_prefix_color)}{self.py_prefix_text}{Color().NONE}"
        if is_tool("python"):
            if (
                self.py_version_enable
                and find_files(os_getcwd(), self.search_f)
                or "VIRTUAL_ENV" in os_environ
            ):
                return str(
                    (
                        f"{separator(self.config)}{py_prefix1}"
                        f"{Color(self.py_color)}{self.py_symbol}"
                        f"{self.get_version()}{Color().NONE}"
                    )
                )
        return ""
