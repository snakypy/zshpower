from contextlib import suppress
from snakypy import FG, printer
from tomlkit.exceptions import NonExistentKey, UnexpectedCharError
from sqlite3 import OperationalError
from snakypy.utils.decorators import only_for_linux
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
from zshpower.prompt.sections.package import package as pkg_version
from zshpower.prompt.sections.docker import Docker
from zshpower.prompt.sections.nodejs import NodeJs, _nodejs
from zshpower.prompt.sections.python import Python, _python
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

# ## Test timer ## #
# from zshpower.utils.decorators import runtime


# def corrupted_db():
#     # printer("Wait...restoring database...", foreground=FG.WARNING)
#     # DAO().create_table([item for item in sql().keys()][0])
#     # Dart().set_version(action="insert")
#     # Docker().set_version(action="insert")
#     # Dotnet().set_version(action="insert")
#     # Elixir().set_version(action="insert")
#     # Golang().set_version(action="insert")
#     # Java().set_version(action="insert")
#     # Julia().set_version(action="insert")
#     # NodeJs().set_version(action="insert")
#     # Php().set_version(action="insert")
#     # Ruby().set_version(action="insert")
#     # Rust().set_version(action="insert")
#     # Perl().set_version(action="insert")
#     # Scala().set_version(action="insert")
#     # CMake().set_version(action="insert")
#     # Deno().set_version(action="insert")
#     # Erlang().set_version(action="insert")
#     # Helm().set_version(action="insert")
#     # Kotlin().set_version(action="insert")
#     # Crystal().set_version(action="insert")
#     # Nim().set_version(action="insert")
#     # Ocaml().set_version(action="insert")
#     # Vagrant().set_version(action="insert")
#     # Zig().set_version(action="insert")
#     # printer("Restore completed.", foreground=FG.FINISH)
#     printer(
#         'Database corrupted. Run command: "zshpower init [--omz]" to restore.\n>> ',
#         foreground=FG.ERROR,
#     )


# def get_register1():
#     try:
#         data = DAO().select_columns(
#             columns=("name", "version"), table=[item for item in sql().keys()][0]
#         )
#         return data
#     except (KeyError, OperationalError):
#         return printer(
#             f'{package.info["name"]} Error: Database corrupted. Run command:
#             "zshpower init [--omz]" to restore.\n>> ',
#             foreground=FG.ERROR,
#         )


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
                f'"zshpower init [--omz]" to restore.\n>> ',
                foreground=FG.ERROR,
            )

    # def version(self, instance, key):
    #     if key in self.register:
    #         return instance().get_version(self.config, self.register)
    #     return ""

    def version(self, instance, key):
        with ThreadPoolExecutor(max_workers=10) as executor:
            if key in self.register:
                future = executor.submit(instance().get_version, self.config, self.register)
                return_value = future.result()
                return return_value
            return ""

    # def ret_object(self, instance):
    #     with ThreadPoolExecutor(max_workers=10) as executor:
    #         future = executor.submit(instance().get_version, self.config, self.register)
    #         return_value = future.result()
    #         return return_value

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
                    "python": _python(self.config),
                    "package": pkg_version(self.config),
                    "nodejs": self.version(Ocaml, "nodejs"),
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
                    # # "gulp": Gulp().get_version(self.config),
                    "docker": self.version(Docker, "docker"),
                    "git": Git(self.config),
                }

                cmd = Command(self.config)
                static_section = f"{jump_line}{username}{hostname}{directory}"
                ordered_section = (
                    dinamic_section[item]
                    for element in self.config["general"]["position"]
                    for item in dinamic_section.keys()
                    if item in element
                )
                sections = "{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}"
                return sections.format(static_section, *ordered_section, cmd)

        except (NonExistentKey, UnexpectedCharError, ValueError):
            return (
                f"{FG.ERROR}{package.info['name']} Error: Key error in "
                f"the configuration file.\n> "
            )
        except KeyError:
            return (
                f"{FG.ERROR}{package.info['name']} Error: Database records are missing "
                f"or corrupted. Run the command to correct: \"{package.info['executable']} init [--omz]\".\n>> "
            )

    def rprompt(self):
        try:
            from zshpower.prompt.sections.timer import Timer

            config_loaded = self.get_config()

            timer = Timer(config_loaded) if config_loaded["timer"]["enable"] else ""
            return str(timer)
        except NonExistentKey:
            return (
                f"{FG.ERROR}>>> {package.info['name']} Error: Key error in "
                f"the configuration file.\n > "
            )


@silent_errors
@only_for_linux
def main():
    from sys import argv as sys_argv, stdout

    if len(sys_argv) < 2:
        raise TypeError("missing 1 required positional argument")
    if len(sys_argv) == 2 and sys_argv[1] == "prompt":
        stdout.write(Draw().prompt())
    elif len(sys_argv) == 2 and sys_argv[1] == "rprompt":
        stdout.write(Draw().rprompt())
