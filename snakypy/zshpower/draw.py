from concurrent.futures import ThreadPoolExecutor
from contextlib import suppress
from sqlite3 import OperationalError
from sys import argv as sys_argv
from sys import stdout
from typing import Any

from snakypy.helpers import FG, printer
from snakypy.helpers.decorators import only_linux
from snakypy.helpers.files import read_file
from snakypy.helpers.path import create as create_path
from tomlkit import parse as toml_parse

from snakypy.zshpower import __info__
from snakypy.zshpower.config.config import config_content
from snakypy.zshpower.database.dao import DAO
from snakypy.zshpower.prompt.sections.c import C
from snakypy.zshpower.prompt.sections.cmake import CMake
from snakypy.zshpower.prompt.sections.command import Command
from snakypy.zshpower.prompt.sections.cpp import Cpp
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
from snakypy.zshpower.prompt.sections.lua import Lua
from snakypy.zshpower.prompt.sections.nim import Nim
from snakypy.zshpower.prompt.sections.nodejs import NodeJs
from snakypy.zshpower.prompt.sections.ocaml import OCaml
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
from snakypy.zshpower.prompt.sections.v import V
from snakypy.zshpower.prompt.sections.zig import Zig
from snakypy.zshpower.utils.catch import get_key
from snakypy.zshpower.utils.check import str_empty_in
from snakypy.zshpower.utils.modifiers import create_toml

# ## Test timer ## #
# from snakypy.helpers.decorators import runtime


class Draw(DAO):
    def __init__(self):
        DAO.__init__(self)
        self.config: dict = self.get_config()
        self.database = self.get_database()

    def get_config(self) -> dict:
        """
        Takes data from the TOML configuration file and serializes it to a dictionary.
        """
        try:
            config = dict(toml_parse(read_file(self.config_file)))
            return config

        except FileNotFoundError:
            create_path(self.zshpower_home)
            create_toml(config_content, self.config_file)
            config = dict(toml_parse(read_file(self.config_file)))
            self.log.record(
                "Configuration files does not exist, however it was created.",
                colorize=True,
                level="critical",
            )
            return config

    def get_database(self) -> dict:
        """
        Takes data from the database and serializes it to a dictionary.
        """
        try:
            data: dict = self.select_columns(
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
                f'"{__info__["executable"]} reset --db" to restore.\n>> ',
                foreground=FG().ERROR,
            )
            exit(1)

    def dynamic_sections(self) -> list:
        sections = {
            "virtualenv": Virtualenv,
            "python": Python,
            "package": Package,
            "nodejs": NodeJs,
            "c": C,
            "cpp": Cpp,
            "rust": Rust,
            "golang": Golang,
            "ruby": Ruby,
            "dart": Dart,
            "php": Php,
            "java": Java,
            "julia": Julia,
            "dotnet": Dotnet,
            "elixir": Elixir,
            "scala": Scala,
            "perl": Perl,
            "cmake": CMake,
            "crystal": Crystal,
            "deno": Deno,
            "erlang": Erlang,
            "helm": Helm,
            "kotlin": Kotlin,
            "lua": Lua,
            "nim": Nim,
            "ocaml": OCaml,
            "vagrant": Vagrant,
            "zig": Zig,
            "gulp": Gulp,
            "docker": Docker,
            "v": V,
            "git": Git,
        }
        with ThreadPoolExecutor() as executor:
            sections_ = []
            if not str_empty_in(get_key(self.config, "general", "position")):
                for pos_key in get_key(self.config, "general", "position"):
                    for key in sections.keys():
                        if key == pos_key:
                            future = executor.submit(
                                sections[key], self.config, self.database
                            )
                            if future.result() and future.result() is not None:
                                sections_.append(future.result())
        return sections_

    # @runtime
    def prompt(self, took: Any = 0) -> str:
        with suppress(KeyboardInterrupt):
            dynamic_sections = self.dynamic_sections()
            if not dynamic_sections:
                return ">>> "
            static_section = (
                f"{JumpLine(self.config)}"
                f"{Username(self.config)}"
                f"{Hostname(self.config)}"
                f"{Directory(self.config)}"
            )
            cmd = Command(self.config)
            took_ = Took(self.config, took)
            structure = "{}{}{}" + "{}" * len(dynamic_sections)
            return structure.format(static_section, *dynamic_sections, took_, cmd)
        return ">>> "

    def rprompt(self) -> str:
        timer = Timer(self.config)
        return f"{timer}"


# @silent_errors
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
