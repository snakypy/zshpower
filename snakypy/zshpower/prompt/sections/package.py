from os import getcwd
from os.path import join
from .utils import symbol_ssh, element_spacing
from .utils import Color, separator
from snakypy.zshpower.utils.catch import verify_objects
from snakypy.helpers.files import read_json
from contextlib import suppress
from os.path import isfile, exists
from subprocess import run


class Base:
    def __init__(self, config):
        self.config = config
        self.files = ()
        self.folders = ()
        self.extensions = ()
        self.symbol = symbol_ssh(config["package"]["symbol"], "pkg-")
        self.enable = config["package"]["enable"]
        self.color = config["package"]["color"]
        self.prefix_color = config["package"]["prefix"]["color"]
        self.prefix_text = element_spacing(config["package"]["prefix"]["text"])

    def get_version(self):
        return ""

    def __str__(self):
        if self.enable:
            package_version = self.get_version()
            if package_version and verify_objects(
                getcwd(),
                files=self.files,
                folders=self.folders,
                extension=self.extensions,
            ):
                prefix = (
                    f"{Color(self.prefix_color)}" f"{self.prefix_text}{Color().NONE}"
                )
                return (
                    f"{separator(self.config)}{prefix}"
                    f"{Color(self.color)}"
                    f"{self.symbol}{package_version}{Color().NONE}"
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

    def get_version(self, space_elem=" ") -> str:
        if self.enable:
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
        if self.enable and isfile(join(getcwd(), self.files[0])):
            with suppress(Exception):
                parsed = read_json(join(getcwd(), self.files[0]))
                if "version" in parsed:
                    return f"{parsed['version']}{space_elem}"
        return ""

    def __str__(self):
        return Base.__str__(self)


class Rust(Base):
    def __init__(self, config):
        Base.__init__(self, config)
        self.files = ("Cargo.toml",)

    def get_version(self, space_elem=" ") -> str:
        if self.enable:
            python_package_version = run(
                f"""< {self.files[0]} grep "^version := *" | cut -d'"' -f2 | cut -d"'" -f2""",
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


# TODO: Future development
class CMake:
    # CMakeLists.txt
    pass


class Scala(Base):
    def __init__(self, config):
        Base.__init__(self, config)
        self.files = ("build.sbt",)

    def get_version(self, space_elem=" ") -> str:
        if self.enable:
            scala_package_version = run(
                f"""< {self.files[0]} grep "^version := *" | cut -d'"' -f2 | cut -d"'" -f2""",
                capture_output=True,
                shell=True,
                text=True,
            ).stdout

            try:
                scala_package_version = scala_package_version.replace("\n", "").split()[
                    -1
                ]
            except IndexError:
                scala_package_version = scala_package_version.replace("\n", "")

            if scala_package_version:
                return f"{scala_package_version}{space_elem}"
        return ""


class Crystal(Base):
    def __init__(self, config):
        Base.__init__(self, config)
        self.files = ("shard.yml",)

    def get_version(self, space_elem=" ") -> str:
        if self.enable:
            crystal_package_version = run(
                f"""< {self.files[0]} grep "^version: *" | cut -d'"' -f2 | cut -d"'" -f2""",
                capture_output=True,
                shell=True,
                text=True,
            ).stdout

            try:
                crystal_package_version = crystal_package_version.replace(
                    "\n", ""
                ).split()[1]
            except IndexError:
                crystal_package_version = crystal_package_version.replace("\n", "")

            if crystal_package_version:
                return f"{crystal_package_version}{space_elem}"
        return ""


class Helm(Base):
    def __init__(self, config):
        Base.__init__(self, config)
        self.files = ("Chart.yaml",)

    def get_version(self, space_elem=" ") -> str:
        if self.enable:
            helm_package_version = run(
                f"""< {self.files[0]} grep "^version: *" | cut -d'"' -f2 | cut -d"'" -f2""",
                capture_output=True,
                shell=True,
                text=True,
            ).stdout

            try:
                helm_package_version = helm_package_version.replace("\n", "").split()[1]
            except IndexError:
                helm_package_version = helm_package_version.replace("\n", "")

            if helm_package_version:
                return f"{helm_package_version}{space_elem}"
        return ""


class Package:
    def __init__(self, config):
        self.config = config

    def __str__(self):
        if exists(join(getcwd(), Python(self.config).files[0])):
            return str(Python(self.config))
        elif exists(join(getcwd(), Rust(self.config).files[0])):
            return str(Rust(self.config))
        elif exists(join(getcwd(), NodeJS(self.config).files[0])):
            return str(NodeJS(self.config))
        elif exists(join(getcwd(), Scala(self.config).files[0])):
            return str(Scala(self.config))
        elif exists(join(getcwd(), Crystal(self.config).files[0])):
            return str(Crystal(self.config))
        elif exists(join(getcwd(), Helm(self.config).files[0])):
            return str(Helm(self.config))
        return ""
