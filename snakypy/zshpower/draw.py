from concurrent.futures import ThreadPoolExecutor
from contextlib import suppress
from sqlite3 import OperationalError
from sys import argv as sys_argv
from sys import stdout
from typing import Any

from snakypy.helpers import FG, printer
from snakypy.helpers.decorators import only_linux, silent_errors
from snakypy.helpers.files import read_file
from snakypy.helpers.path import create as create_path
from tomlkit import parse as toml_parse

from snakypy.zshpower import __info__
from snakypy.zshpower.config.config import config_content
from snakypy.zshpower.database.dao import DAO
from snakypy.zshpower.prompt.sections.cmake import CMake
from snakypy.zshpower.prompt.sections.command import Command
from snakypy.zshpower.prompt.sections.crystal import Crystal
from snakypy.zshpower.prompt.sections.dart import Dart
from snakypy.zshpower.prompt.sections.deno import Deno
from snakypy.zshpower.prompt.sections.directory import Directory
from snakypy.zshpower.prompt.sections.docker import Docker
from snakypy.zshpower.prompt.sections.dotnet import Dotnet
from snakypy.zshpower.prompt.sections.elixir import Elixir
from snakypy.zshpower.prompt.sections.erlang import Erlang
from snakypy.zshpower.prompt.sections.git import Git
from snakypy.zshpower.prompt.sections.golang import Golang
from snakypy.zshpower.prompt.sections.gulp import Gulp
from snakypy.zshpower.prompt.sections.helm import Helm
from snakypy.zshpower.prompt.sections.hostname import Hostname
from snakypy.zshpower.prompt.sections.java import Java
from snakypy.zshpower.prompt.sections.julia import Julia
from snakypy.zshpower.prompt.sections.jump_line import JumpLine
from snakypy.zshpower.prompt.sections.kotlin import Kotlin
from snakypy.zshpower.prompt.sections.nim import Nim
from snakypy.zshpower.prompt.sections.nodejs import NodeJs
from snakypy.zshpower.prompt.sections.ocaml import Ocaml
from snakypy.zshpower.prompt.sections.package import Package
from snakypy.zshpower.prompt.sections.perl import Perl
from snakypy.zshpower.prompt.sections.php import Php
from snakypy.zshpower.prompt.sections.python import Python, Virtualenv
from snakypy.zshpower.prompt.sections.ruby import Ruby
from snakypy.zshpower.prompt.sections.rust import Rust
from snakypy.zshpower.prompt.sections.scala import Scala
from snakypy.zshpower.prompt.sections.timer import Timer
from snakypy.zshpower.prompt.sections.took import Took
from snakypy.zshpower.prompt.sections.username import Username
from snakypy.zshpower.prompt.sections.vagrant import Vagrant
from snakypy.zshpower.prompt.sections.zig import Zig
from snakypy.zshpower.utils.catch import get_key
from snakypy.zshpower.utils.check import str_empty_in
from snakypy.zshpower.utils.modifiers import create_toml

# ## Test timer ## #
# from snakypy.helpers.decorators import runtime


class Draw(DAO):
    def __init__(self):
        DAO.__init__(self)
        self.config = self.get_config()
        self.register = self.get_register()

    def get_config(self) -> dict:
        try:
            parsed = dict(toml_parse(read_file(self.config_file)))
            return parsed

        except FileNotFoundError:
            create_path(self.zshpower_home)
            create_toml(config_content, self.config_file)
            parsed = dict(toml_parse(read_file(self.config_file)))
            self.log.record(
                "Configuration files does not exist, however it was created.",
                colorize=True,
                level="critical",
            )
            return parsed

    def get_register(self):
        try:
            data = self.select_columns(
                columns=("name", "version"),
                table=self.tbl_main,
            )
            return data
        except (KeyError, OperationalError):
            self.log.record(
                "Corrupted database. Firing guidance message.",
                colorize=True,
                level="error",
            )
            printer(
                f'{__info__["name"]} Error: Database corrupted. Run command: '
                f'"zshpower reset --db" to restore.\n>> ',
                foreground=FG().ERROR,
            )

    def version(self, instance, key) -> str:
        with ThreadPoolExecutor() as executor:
            if key in self.register:
                future = executor.submit(
                    instance().get_version, self.config, self.register
                )
                return_value = future.result()
                return return_value
            return ""

    @staticmethod
    def get_keys(dict_: dict, key: Any) -> str:
        return dict_[key]

    # @runtime
    def prompt(self, took: Any = 0) -> str:
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
            took_ = Took(self.config, took)
            static_section = f"{jump_line}{username}{hostname}{directory}"

            # Using ThreadPoolExecutor, not Generators
            with ThreadPoolExecutor() as executor:
                ordered_section = []
                if not str_empty_in(get_key(self.config, "general", "position")):
                    for elem in get_key(self.config, "general", "position"):
                        for item in dinamic_section.keys():
                            if item == elem:
                                future = executor.submit(
                                    self.get_keys, dinamic_section, item
                                )
                                ordered_section.append(future.result())

                    sections = "{}{}{}" + "{}" * len(dinamic_section)
                    return sections.format(static_section, *ordered_section, took_, cmd)
        return ">>> "

    def rprompt(self) -> str:
        timer = Timer(self.config)
        return f"{timer}"


@silent_errors
@only_linux
def main() -> None:
    if len(sys_argv) < 2:
        raise TypeError("missing 1 required positional argument")
    if len(sys_argv) == 3 and sys_argv[1] == "prompt" and sys_argv[2]:
        stdout.write(Draw().prompt(took=sys_argv[2]))
    elif len(sys_argv) == 2 and sys_argv[1] == "prompt":
        stdout.write(Draw().prompt())
    elif len(sys_argv) == 2 and sys_argv[1] == "rprompt":
        stdout.write(Draw().rprompt())
