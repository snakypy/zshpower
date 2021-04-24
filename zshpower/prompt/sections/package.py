# from snakypy.file import read as snakypy_file_read
# from tomlkit import parse as toml_parse
# from tomlkit.exceptions import UnexpectedCharError, ParseError
from os import getcwd
from os.path import isfile, join


class Base():
    def __init__(self, config):
        from .lib.utils import symbol_ssh, element_spacing

        self.config = config
        self.files = ()
        self.folders = ()
        self.extensions = ()
        self.version_enable = config["package"]["enable"]
        self.symbol = symbol_ssh(config["package"]["symbol"], "pkg-")
        self.color = config["package"]["color"]
        self.prefix_color = config["package"]["prefix"]["color"]
        self.prefix_text = element_spacing(config["package"]["prefix"]["text"])

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


# class Config:
#     def __init__(self, config):
#         from .lib.utils import symbol_ssh, element_spacing

#         self.version_enable = config["package"]["enable"]
#         self.symbol = symbol_ssh(config["package"]["symbol"], "pkg-")
#         self.color = config["package"]["color"]
#         self.prefix_color = config["package"]["prefix"]["color"]
#         self.prefix_text = element_spacing(config["package"]["prefix"]["text"])


class PackagePython(Base):
    def __init__(self, config):
        Base.__init__(self, config)
        self.files = ("pyproject.toml",)

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
        return super().__str__()


class PackageNodeJS(Base):
    def __init__(self, config):
        Base.__init__(self, config)
        self.files = ("package.json",)

    def get_version(self, space_elem=" "):
        from snakypy.json import read as snakypy_json_read
        from contextlib import suppress

        if isfile(join(getcwd(), self.files[0])):
            with suppress(Exception):
                parsed = snakypy_json_read(join(getcwd(), self.files[0]))
                if "version" in parsed:
                    return f"{parsed['version']}{space_elem}"
        return ""

    def __str__(self):
        return Base.__str__(self)


class Package():
    def __init__(self, config):
        PackagePython.__init__(self, config)
        PackageNodeJS.__init__(self, config)

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

    # def __str__(self):
    #     return self.__init__()


def get_package(config):
    from os.path import exists

    # files_project_py = (
    #     "manage.py",
    #     "setup.py",
    #     "__init__.py",
    #     "requirements.txt",
    #     "pyproject.toml",
    # )
    # for i in files_project_py:
    #     if exists(join(getcwd(), i)):
    #         return str(PackagePython(config))
    # return str(PackageNodeJS(config))

    if exists(join(getcwd(), "pyproject.toml")) and exists(join(getcwd(), "package.json")):
        return f"{PackagePython(config)}{PackageNodeJS(config)}"
    return ""
