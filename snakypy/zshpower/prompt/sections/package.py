import re
from contextlib import suppress
from os import getcwd, listdir
from os.path import exists, isfile, join
from shutil import which
from subprocess import run

from snakypy.helpers.files import read_json
from snakypy.helpers.files.generic import read_file

from snakypy.zshpower.utils.catch import get_key, verify_objects

from .utils import Color, element_spacing, separator, symbol_ssh


class Base:
    def __init__(self, config: dict):
        self.config: dict = config
        self.finder: dict = {"extensions": [], "folders": [], "files": []}
        self.symbol = symbol_ssh(get_key(config, "package", "symbol"), "pkg-")
        self.enable = get_key(config, "package", "enable")
        self.color = (
            get_key(config, "package", "color")
            if get_key(config, "general", "color", "enable") is True
            else "negative"
        )
        self.prefix_color = get_key(config, "package", "prefix", "color")
        self.prefix_text = element_spacing(get_key(config, "package", "prefix", "text"))

    def finder_version(self, file, regex):
        try:
            if self.enable:
                file_content = read_file(file)
                re_search = re.search(regex, file_content)
                version = re_search.group(0)
                return version
            return ""
        except (IndexError, FileNotFoundError):
            return ""

    def get_version_yaml(self, space_elem=""):
        try:
            regex = r"version:.*"
            get_line = self.finder_version(self.finder["files"][0], regex)
            version = get_line.split('"')[1]
            return f"{version}{space_elem}"
        except (IndexError, FileNotFoundError):
            return ""

    def get_version_toml(self, space_elem=""):
        try:
            regex = r"version = \".*"
            get_line = self.finder_version(self.finder["files"][0], regex)
            version = get_line.split("=")[1].replace('"', "").strip()
            return f"{version}{space_elem}"
        except (IndexError, FileNotFoundError):
            return ""

    def get_version_json(self, filename, space_elem=""):
        if self.enable and isfile(join(getcwd(), filename)):
            with suppress(Exception):
                parsed = read_json(join(getcwd(), filename))
                if "version" in parsed:
                    return f"{parsed['version']}{space_elem}"
        return ""

    def __str__(self, get_version=""):
        if self.enable:
            package_version = get_version
            if package_version and verify_objects(getcwd(), data=self.finder) is True:
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
        self.finder = {
            "extensions": [],
            "folders": [],
            "files": [
                "pyproject.toml",
                "manage.py",
                "requirements.txt",
                "setup.py",
                "__init__.py",
            ],
        }

    def get_version(self, space_elem=" "):
        return super().get_version_toml(space_elem=space_elem)

    def __str__(self, get_version=""):
        return super().__str__(get_version=self.get_version())


class NodeJS(Base):
    def __init__(self, config):
        Base.__init__(self, config)
        self.finder = {
            "extensions": [],
            "folders": ["node_modules"],
            "files": ["package.json"],
        }

    def get_version(self, space_elem=" "):
        return super().get_version_json(self.finder["files"][0], space_elem=space_elem)

    def __str__(self, get_version=""):
        return super().__str__(get_version=self.get_version())


class Rust(Base):
    def __init__(self, config):
        Base.__init__(self, config)
        self.finder = {"extensions": [], "folders": [], "files": ["Cargo.toml"]}

    def get_version(self, space_elem=" "):
        return super().get_version_toml(space_elem=space_elem)

    def __str__(self, get_version=""):
        return super().__str__(get_version=self.get_version())


class Scala(Base):
    def __init__(self, config):
        Base.__init__(self, config)
        self.finder = {"extensions": [], "folders": [], "files": ["build.sbt"]}

    def get_version(self, space_elem=" "):
        try:
            regex = r"version := .*"
            get_line = super().finder_version(self.finder["files"][0], regex)
            version = get_line.split('"')[1]
            return f"{version}{space_elem}"
        except (IndexError, FileNotFoundError):
            return ""

    def __str__(self, get_version=""):
        return super().__str__(get_version=self.get_version())


class Crystal(Base):
    def __init__(self, config):
        Base.__init__(self, config)
        self.finder = {"extensions": [], "folders": [], "files": ["shard.yml"]}

    def get_version(self, space_elem=" "):
        return super().get_version_yaml(space_elem=space_elem)

    def __str__(self, get_version=""):
        return super().__str__(get_version=self.get_version())


class Helm(Base):
    def __init__(self, config):
        Base.__init__(self, config)
        self.finder = {"extensions": [], "folders": [], "files": ["Chart.yaml"]}

    def get_version(self, space_elem=" "):
        return super().get_version_yaml(space_elem=space_elem)

    def __str__(self, get_version=""):
        return super().__str__(get_version=self.get_version())


class Ruby(Base):
    def __init__(self, config):
        Base.__init__(self, config)
        self.finder = {"extensions": [".gemspec"], "folders": [], "files": []}

    def search_gemspec(self, directory):
        for file in listdir(directory):
            if file.endswith(self.finder["extensions"][0]):
                return file
        return False

    def get_version(self, space_elem=" "):
        file = self.search_gemspec(getcwd())
        if file is not False and which("ruby"):
            command = run(
                f"""ruby -e 'puts Gem::Specification::load("{file}").version'""",
                shell=True,
                text=True,
                capture_output=True,
            )
            if command.returncode == 0:
                version = command.stdout.strip().replace("\n", "")
                return f"{version}{space_elem}"
        return ""

    def __str__(self, get_version=""):
        return super().__str__(get_version=self.get_version())


class V(Base):
    def __init__(self, config):
        Base.__init__(self, config)
        self.finder = {"extensions": [], "folders": [], "files": ["vpkg.json"]}

    def get_version(self, space_elem=" "):
        return super().get_version_yaml(space_elem=space_elem)

    def __str__(self, get_version=""):
        return super().__str__(get_version=self.get_version())


class Package:
    def __init__(self, config: dict, *args):
        self.config: dict = config
        self.args = args

    def __str__(self):
        listing = get_key(self.config, "package", "display")

        if listing:

            pyproject_toml = join(getcwd(), Python(self.config).finder["files"][0])
            gemspec = Ruby(self.config).search_gemspec(getcwd())
            package_json = join(getcwd(), NodeJS(self.config).finder["files"][0])
            cargo_toml = join(getcwd(), Rust(self.config).finder["files"][0])
            build_sbt = join(getcwd(), Scala(self.config).finder["files"][0])
            shard_yaml = join(getcwd(), Crystal(self.config).finder["files"][0])
            chart_yaml = join(getcwd(), Helm(self.config).finder["files"][0])
            vpkg_json = join(getcwd(), V(self.config).finder["files"][0])

            if exists(pyproject_toml) and "python" in listing:
                return str(Python(self.config))
            elif exists(package_json) and ("node" in listing or "nodejs" in listing):
                return str(NodeJS(self.config))
            elif exists(gemspec) and "ruby" in listing:
                return str(Ruby(self.config))
            elif exists(cargo_toml) and "rust" in listing:
                return str(Rust(self.config))
            elif exists(build_sbt) and "scala" in listing:
                return str(Scala(self.config))
            elif exists(chart_yaml) and "helm" in listing:
                return str(Helm(self.config))
            elif exists(vpkg_json) and "v" in listing:
                return str(V(self.config))
            elif exists(shard_yaml) and "crystal" in listing:
                return str(Crystal(self.config))
            elif exists(chart_yaml) and "helm" in listing:
                return str(Helm(self.config))
        return ""
