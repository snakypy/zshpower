from contextlib import suppress
from snakypy import FG, printer
from tomlkit.exceptions import NonExistentKey, UnexpectedCharError
from sqlite3 import OperationalError
from snakypy.utils.decorators import only_for_linux
from zshpower.prompt.sections.gulp import Gulp
from zshpower.database.sql import sql
from zshpower.prompt.sections.jump_line import JumpLine
from zshpower.utils.decorators import silent_errors
from zshpower.config import package
from zshpower.database.dao import DAO
from zshpower.config.config import content as config_content
from zshpower.utils.shift import create_config
from snakypy.path import create as snakypy_path_create
from snakypy.file import read as snakypy_file_red
from tomlkit import parse as toml_parse
from concurrent.futures import ThreadPoolExecutor
from zshpower.prompt.sections.directory import Directory
from zshpower.prompt.sections.git import Git
from zshpower.prompt.sections.hostname import Hostname
from zshpower.prompt.sections.command import Command
from zshpower.prompt.sections.username import Username
from zshpower.prompt.sections.package import Package
from zshpower.prompt.sections.docker import Docker
from zshpower.prompt.sections.nodejs import NodeJs
from zshpower.prompt.sections.python import Python
from zshpower.prompt.sections.rust import Rust
from zshpower.prompt.sections.golang import Golang
from zshpower.prompt.sections.php import Php
from zshpower.prompt.sections.elixir import Elixir
from zshpower.prompt.sections.julia import Julia
from zshpower.prompt.sections.scala import Scala
from zshpower.prompt.sections.ruby import Ruby
from zshpower.prompt.sections.dotnet import Dotnet
from zshpower.prompt.sections.java import Java
from zshpower.prompt.sections.dart import Dart
from zshpower.prompt.sections.virtualenv import Virtualenv
from zshpower.prompt.sections.zig import Zig
from zshpower.prompt.sections.vagrant import Vagrant
from zshpower.prompt.sections.ocaml import Ocaml
from zshpower.prompt.sections.nim import Nim
from zshpower.prompt.sections.kotlin import Kotlin
from zshpower.prompt.sections.helm import Helm
from zshpower.prompt.sections.erlang import Erlang
from zshpower.prompt.sections.deno import Deno
from zshpower.prompt.sections.crystal import Crystal
from zshpower.prompt.sections.cmake import CMake
from zshpower.prompt.sections.perl import Perl
from zshpower.prompt.sections.timer import Timer
from sys import argv as sys_argv, stdout

# ## Test timer ## #
# from zshpower.utils.decorators import runtime


class Draw(DAO):
    def __init__(self):
        DAO.__init__(self)
        self.config = self.get_config()
        self.register = self.get_register()

    def get_config(self):
        try:
            read_conf = snakypy_file_red(self.config_file)
            parsed = toml_parse(read_conf)
            return parsed

        except (FileNotFoundError, NonExistentKey):
            snakypy_path_create(self.zshpower_home)
            create_config(config_content, self.config_file)
            read_conf = snakypy_file_red(self.config_file)
            parsed = toml_parse(read_conf)
            return parsed

    def get_register(self):
        try:
            data = self.select_columns(
                columns=("name", "version"), table=[item for item in sql().keys()][0]
            )
            return data
        except (KeyError, OperationalError):
            return printer(
                f'{package.info["name"]} Error: Database corrupted. Run command: '
                f'"zshpower reset --db" to restore.\n>> ',
                foreground=FG.ERROR,
            )

    def version(self, instance, key):
        with ThreadPoolExecutor(max_workers=2) as executor:
            if key in self.register:
                future = executor.submit(
                    instance().get_version, self.config, self.register
                )
                return_value = future.result()
                return return_value
            return ""

    @staticmethod
    def get_keys(dic, item):
        return dic[item]

    # @runtime
    def prompt(self):
        try:
            with suppress(KeyboardInterrupt):
                jump_line = JumpLine(self.config)
                username = Username(self.config)
                hostname = Hostname(self.config)
                directory = Directory(self.config)
                dinamic_section = {
                    "virtualenv": Virtualenv(self.config),
                    "python": Python(self.config),
                    "package": Package(self.config),
                    "nodejs": self.version(NodeJs, "nodejs"),
                    "rust": self.version(Rust, "rust"),
                    "golang": self.version(Golang, "golang"),
                    "ruby": self.version(Ruby, "ruby"),
                    "dart": self.version(Dart, "dart"),
                    "php": self.version(Php, "php"),
                    "java": self.version(Java, "java"),
                    "julia": self.version(Julia, "julia"),
                    "dotnet": self.version(Dotnet, "dotnet"),
                    "elixir": self.version(Elixir, "elixir"),
                    "scala": self.version(Scala, "scala"),
                    "perl": self.version(Perl, "perl"),
                    "cmake": self.version(CMake, "cmake"),
                    "crystal": self.version(Crystal, "crystal"),
                    "deno": self.version(Deno, "deno"),
                    "erlang": self.version(Erlang, "erlang"),
                    "helm": self.version(Helm, "helm"),
                    "kotlin": self.version(Kotlin, "kotlin"),
                    "nim": self.version(Nim, "nim"),
                    "ocaml": self.version(Ocaml, "ocaml"),
                    "vagrant": self.version(Vagrant, "vagrant"),
                    "zig": self.version(Zig, "zig"),
                    "gulp": self.version(Gulp, "gulp"),
                    "docker": self.version(Docker, "docker"),
                    "git": Git(self.config),
                }

                cmd = Command(self.config)
                static_section = f"{jump_line}{username}{hostname}{directory}"

                # Using ThreadPoolExecutor, not Generators
                with ThreadPoolExecutor(max_workers=2) as executor:
                    ordered_section = []
                    for elem in self.config["general"]["position"]:
                        for item in dinamic_section.keys():
                            if item == elem:
                                future = executor.submit(
                                    self.get_keys, dinamic_section, item
                                )
                                ordered_section.append(future.result())

                # Using Generators, not ThreadPoolExecutor
                # ordered_section = (
                #     dinamic_section[item]
                #     for element in self.config["general"]["position"]
                #     for item in dinamic_section.keys()
                #     if item == element
                # )

                sections = "{}{}" + "{}" * len(dinamic_section)
                return sections.format(static_section, *ordered_section, cmd)

        except (NonExistentKey, UnexpectedCharError, ValueError):
            return (
                f"{FG.ERROR}{package.info['name']} Error: Key error in "
                f"the configuration file.\n> "
            )
        except KeyError:
            return (
                f"{FG.ERROR}{package.info['name']} Error: Database records are missing "
                f"or corrupted. Run the command to correct: \"{package.info['executable']} reset --db\".\n>> "
            )

    def rprompt(self):
        try:
            timer = Timer(self.config)
            return str(timer)
        except NonExistentKey:
            return (
                f"{FG.ERROR}>>> {package.info['name']} Error: Key error in "
                f"the configuration file.\n > "
            )


@silent_errors
@only_for_linux
def main():
    if len(sys_argv) < 2:
        raise TypeError("missing 1 required positional argument")
    if len(sys_argv) == 2 and sys_argv[1] == "prompt":
        stdout.write(Draw().prompt())
    elif len(sys_argv) == 2 and sys_argv[1] == "rprompt":
        stdout.write(Draw().rprompt())
