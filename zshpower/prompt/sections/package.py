from os import getcwd
from os.path import join


class Base:
    def __init__(self, config):
        from .lib.utils import symbol_ssh, element_spacing

        self.config = config
        self.files = ()
        self.folders = ()
        self.extensions = ()
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
            package_version
            and find_objects(
                os_getcwd(),
                files=self.files,
                folders=self.folders,
                extension=self.extensions,
            )
        ):
            prefix = f"{Color(self.prefix_color)}" f"{self.prefix_text}{Color().NONE}"
            return (
                f"{separator(self.config)}{prefix}"
                f"{Color(self.color)}"
                f"{self.symbol}{self.get_version()}{Color().NONE}"
            )
        return ""


class Python(Base):
    def __init__(self, config):
        Base.__init__(self, config)
        self.files = (
            "pyproject.toml",
            "manage.py",
            "requirements.txt",
            "setup.py",
            "__init__.py",
        )

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


class NodeJS(Base):
    def __init__(self, config):
        Base.__init__(self, config)
        self.files = ("package.json",)
        self.folders = ("node_modules",)

    def get_version(self, space_elem=" "):
        from snakypy.json import read as snakypy_json_read
        from contextlib import suppress
        from os.path import isfile

        if isfile(join(getcwd(), self.files[0])):
            with suppress(Exception):
                parsed = snakypy_json_read(join(getcwd(), self.files[0]))
                if "version" in parsed:
                    return f"{parsed['version']}{space_elem}"
        return ""

    def __str__(self):
        return Base.__str__(self)


class Rust(Base):
    def __init__(self, config):
        Base.__init__(self, config)
        self.files = ("Cargo.toml",)

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


def package(config):
    from os.path import exists

    if exists(join(getcwd(), Python(config).files[0])):
        return Python(config)
    elif exists(join(getcwd(), Rust(config).files[0])):
        return Rust(config)
    elif exists(join(getcwd(), NodeJS(config).files[0])):
        return NodeJS(config)
    return ""
