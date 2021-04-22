# from snakypy.file import read as snakypy_file_read
# from tomlkit import parse as toml_parse
# from tomlkit.exceptions import UnexpectedCharError, ParseError
from os import getcwd
from os.path import isfile, join


class Configs:
    def __init__(self, config):
        from .lib.utils import symbol_ssh, element_spacing

        self.package_enable = config["package"]["enable"]
        self.package_symbol = symbol_ssh(config["package"]["symbol"], "pkg-")
        self.package_color = config["package"]["color"]
        self.package_prefix_color = config["package"]["prefix"]["color"]
        self.package_prefix_text = element_spacing(config["package"]["prefix"]["text"])


class Package(Configs):
    def __init__(self, config):
        Configs.__init__(self, config)
        self.config = config
        self.package_file = join(getcwd(), "pyproject.toml")

    def get_version(self, space_elem=" "):
        from zshpower.utils.process import shell_command

        if isfile(self.package_file):
            cmd = f"""< {self.package_file} grep "^version = *" | cut -d'"' -f2 | cut -d"'" -f2"""
            return f"{shell_command(cmd)[0]}{space_elem}"
        return ""

    def __str__(self):
        from .lib.utils import Color, separator

        if self.package_enable and self.get_version() != "":
            package_prefix = (
                f"{Color(self.package_prefix_color)}"
                f"{self.package_prefix_text}{Color().NONE}"
            )
            return (
                f"{separator(self.config)}{package_prefix}"
                f"{Color(self.package_color)}"
                f"{self.package_symbol}{self.get_version()}{Color().NONE}"
            )
        return ""


class NodePackage(Package):
    def __init__(self, config):
        Package.__init__(self, config)
        self.package_file = join(getcwd(), "package.json")

    def get_version(self, space_elem=" "):
        from snakypy.json import read as snakypy_json_read
        from contextlib import suppress

        if isfile(join(getcwd(), self.package_file)):
            with suppress(Exception):
                parsed = snakypy_json_read(join(getcwd(), self.package_file))
                if "version" in parsed:
                    return f"{parsed['version']}{space_elem}"
        return ""

    def __str__(self):
        return Package.__str__(self)


def get_package(config):
    from os.path import exists

    files_project_py = (
        "manage.py",
        "setup.py",
        "__init__.py",
        "requirements.txt",
        "pyproject.toml",
    )
    for i in files_project_py:
        if exists(join(getcwd(), i)):
            return str(Package(config))
    return str(NodePackage(config))
