from tomlkit import parse as toml_parse
from tomlkit.exceptions import UnexpectedCharError, ParseError
from snakypy.file import read as snakypy_file_read
from snakypy.json import read as snakypy_json_read
from os import getcwd
from os.path import isfile, join, exists
from .lib.utils import Color, symbol_ssh, separator, element_spacing


class Configs:
    def __init__(self, config):
        self.package_enable = config["package"]["enable"]
        self.package_symbol = symbol_ssh(config["package"]["symbol"], "pkg-")
        self.package_color = config["package"]["color"]
        self.package_prefix_color = config["package"]["prefix"]["color"]
        self.package_prefix_text = element_spacing(
            config["package"]["prefix"]["text"]
        )


class Package(Configs):
    def __init__(self, config):
        Configs.__init__(self, config)
        self.config = config
        self.package_file = join(getcwd(), "pyproject.toml")

    def get_version(self, space_elem=" "):
        try:
            if isfile(self.package_file):
                read_f = snakypy_file_read(self.package_file)
                parsed = dict(toml_parse(read_f))
                for item in parsed.values():
                    for data in item.values():
                        if "version" in data:
                            return f"{data['version']}{space_elem}"
            return ""
        except (UnexpectedCharError, ParseError):
            return f"Error{space_elem}"

    def __str__(self):
        if (
            self.package_enable
            and self.get_version() != ""
        ):
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
        if isfile(join(getcwd(), self.package_file)):
            parsed = snakypy_json_read(join(getcwd(), self.package_file))
            return f"{parsed['version']}{space_elem}"
        return ""

    def __str__(self):
        return Package.__str__(self)


def get_package(config):
    status = set()
    files_project_py = (
        "manage.py",
        "setup.py",
        "__init__.py",
        "requirements.txt",
        "pyproject.toml",
    )
    for i in files_project_py:
        if exists(join(getcwd(), i)):
            status.add(True)
    if True not in status:
        return str(NodePackage(config))
    return str(Package(config))
