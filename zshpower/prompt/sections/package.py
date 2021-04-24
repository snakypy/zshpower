# from snakypy.file import read as snakypy_file_read
# from tomlkit import parse as toml_parse
# from tomlkit.exceptions import UnexpectedCharError, ParseError
from os import getcwd
from os.path import isfile, join


class Config:
    def __init__(self, config):
        from .lib.utils import symbol_ssh, element_spacing

        self.version_enable = config["package"]["enable"]
        self.symbol = symbol_ssh(config["package"]["symbol"], "pkg-")
        self.color = config["package"]["color"]
        self.prefix_color = config["package"]["prefix"]["color"]
        self.prefix_text = element_spacing(config["package"]["prefix"]["text"])


class PackagePython(Config):
    def __init__(self, config):
        Config.__init__(self, config)
        self.config = config
        self.files = ("pyproject.toml",)
        self.folders = ()
        self.extensions = ()

    def get_version(self, space_elem=" "):
        from subprocess import run

        python_package_version = run(
            f"""< {self.files[0]} grep "^version = *" | cut -d'"' -f2 | cut -d"'" -f2""",
            capture_output=True,
            shell=True,
            text=True,
        ).stdout

        python_package_version = python_package_version.replace("\n", "")

        if python_package_version:
            return f"{python_package_version}{space_elem}"
        return ""

    def __str__(self):
        from .lib.utils import Color, separator
        from zshpower.utils.catch import find_objects
        from os import getcwd as os_getcwd

        package_version = self.get_version()

        if (
            self.version_enable
            and package_version
            and find_objects(os_getcwd(), files=self.files, folders=self.folders, extension=self.extensions)
        ):
            prefix = (
                f"{Color(self.prefix_color)}"
                f"{self.prefix_text}{Color().NONE}"
            )
            return (
                f"{separator(self.config)}{prefix}"
                f"{Color(self.color)}"
                f"{self.symbol}{self.get_version()}{Color().NONE}"
            )
        return ""


class PackageNodeJS(PackagePython):
    def __init__(self, config):
        PackagePython.__init__(self, config)
        # self.package_file = join(getcwd(), "package.json")
        self.files = ("package.json",)
        self.folders = ()
        self.extensions = ()

    def get_version(self, space_elem=" "):
        from snakypy.json import read as snakypy_json_read
        from contextlib import suppress

        if isfile(join(getcwd(), self.package_file)):
            with suppress(Exception):
                parsed = snakypy_json_read(join(getcwd(), self.files[0]))
                if "version" in parsed:
                    return f"{parsed['version']}{space_elem}"
        return ""

    def __str__(self):
        return PackagePython.__str__(self)


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
            return str(PackagePython(config))
    return str(PackageNodeJS(config))
