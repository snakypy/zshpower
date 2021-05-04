from contextlib import suppress
from snakypy import FG, printer
from tomlkit.exceptions import NonExistentKey, UnexpectedCharError
from sqlite3 import OperationalError
from snakypy.utils.decorators import only_for_linux
from zshpower.database.sql import sql

from zshpower.utils.decorators import silent_errors
from zshpower.config import package
from zshpower.database.dao import DAO
from zshpower.config.config import content as config_content
from zshpower.utils.shift import create_config
from snakypy.path import create as snakypy_path_create
from snakypy.file import read as snakypy_file_red
from tomlkit import parse as toml_parse
from zshpower.prompt.sections.directory import Directory
from zshpower.prompt.sections.git import Git
from zshpower.prompt.sections.hostname import Hostname
from zshpower.prompt.sections.command import Command
from zshpower.prompt.sections.username import Username
from zshpower.prompt.sections.package import package as pkg_version
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

# ## Test timer ## #
# from zshpower.utils.decorators import runtime


def corrupted_db():
    # printer("Wait...restoring database...", foreground=FG.WARNING)
    # DAO().create_table([item for item in sql().keys()][0])
    # Dart().set_version(action="insert")
    # Docker().set_version(action="insert")
    # Dotnet().set_version(action="insert")
    # Elixir().set_version(action="insert")
    # Golang().set_version(action="insert")
    # Java().set_version(action="insert")
    # Julia().set_version(action="insert")
    # NodeJs().set_version(action="insert")
    # Php().set_version(action="insert")
    # Ruby().set_version(action="insert")
    # Rust().set_version(action="insert")
    # Perl().set_version(action="insert")
    # Scala().set_version(action="insert")
    # CMake().set_version(action="insert")
    # Deno().set_version(action="insert")
    # Erlang().set_version(action="insert")
    # Helm().set_version(action="insert")
    # Kotlin().set_version(action="insert")
    # Crystal().set_version(action="insert")
    # Nim().set_version(action="insert")
    # Ocaml().set_version(action="insert")
    # Vagrant().set_version(action="insert")
    # Zig().set_version(action="insert")
    # printer("Restore completed.", foreground=FG.FINISH)
    printer(
        'Database corrupted. Run command: "zshpower init [--omz]" to restore.\n>> ',
        foreground=FG.ERROR,
    )


def db_fetchall():
    try:
        reg = DAO().select_columns(
            columns=("name", "version"), table=[item for item in sql().keys()][0]
        )
        # if not reg:
        #     corrupted_db()
        #     reg = DAO().select_columns(columns=("name", "version"), table=[item for item in sql().keys()][0])
        return reg
    except (KeyError, OperationalError):
        # corrupted_db()
        # reg = DAO().select_columns(columns=("name", "version"), table=[item for item in sql().keys()][0])
        # return reg
        return printer(
            f'{package.info["name"]} Error: Database corrupted. Run command: "zshpower init [--omz]" to restore.\n>> ',
            foreground=FG.ERROR,
        )


class Draw(DAO):
    def __init__(self):
        DAO.__init__(self)

    def config_load(self):
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

    # @runtime
    def prompt(self, jump_line="\n"):
        try:
            with suppress(KeyboardInterrupt):
                # Loading the settings to a local variable and thus improving performance
                config_loaded = self.config_load()

                db_reg = db_fetchall()

                if not config_loaded["general"]["jump_line"]["enable"]:
                    jump_line = ""

                username = (
                    Username(config_loaded)
                    if config_loaded["username"]["enable"]
                    else ""
                )

                hostname = (
                    Hostname(config_loaded)
                    if config_loaded["hostname"]["enable"]
                    else ""
                )

                directory = Directory(config_loaded)

                dinamic_section = {
                    "virtualenv": Virtualenv(config_loaded)
                    if config_loaded["virtualenv"]["enable"]
                    else "",
                    "python": Python(config_loaded)
                    if config_loaded["python"]["version"]["enable"]
                    else "",
                    "package": pkg_version(config_loaded)
                    if config_loaded["package"]["enable"]
                    else "",
                    "nodejs": NodeJs().get_version(config_loaded, db_reg["nodejs"])
                    if config_loaded["nodejs"]["version"]["enable"]
                    and "nodejs" in db_reg
                    else "",
                    "rust": Rust().get_version(config_loaded, db_reg["rust"])
                    if config_loaded["rust"]["version"]["enable"] and "rust" in db_reg
                    else "",
                    "golang": Golang().get_version(config_loaded, db_reg["golang"])
                    if config_loaded["golang"]["version"]["enable"]
                    and "golang" in db_reg
                    else "",
                    "ruby": Ruby().get_version(config_loaded, db_reg["ruby"])
                    if config_loaded["ruby"]["version"]["enable"] and "ruby" in db_reg
                    else "",
                    "dart": Dart().get_version(config_loaded, db_reg["dart"])
                    if config_loaded["dart"]["version"]["enable"] and "dart" in db_reg
                    else "",
                    "php": Php().get_version(config_loaded, db_reg["php"])
                    if config_loaded["php"]["version"]["enable"] and "php" in db_reg
                    else "",
                    "java": Java().get_version(config_loaded, db_reg["java"])
                    if config_loaded["java"]["version"]["enable"] and "java" in db_reg
                    else "",
                    "julia": Julia().get_version(config_loaded, db_reg["julia"])
                    if config_loaded["julia"]["version"]["enable"] and "julia" in db_reg
                    else "",
                    "dotnet": Dotnet().get_version(config_loaded, db_reg["dotnet"])
                    if config_loaded["dotnet"]["version"]["enable"]
                    and "dotnet" in db_reg
                    else "",
                    "elixir": Elixir().get_version(config_loaded, db_reg["elixir"])
                    if config_loaded["elixir"]["version"]["enable"]
                    and "elixir" in db_reg
                    else "",
                    "scala": Scala().get_version(config_loaded, db_reg["scala"])
                    if config_loaded["scala"]["version"]["enable"] and "scala" in db_reg
                    else "",
                    "perl": Perl().get_version(config_loaded, db_reg["perl"])
                    if config_loaded["perl"]["version"]["enable"] and "perl" in db_reg
                    else "",
                    "cmake": CMake().get_version(config_loaded, db_reg["cmake"])
                    if config_loaded["cmake"]["version"]["enable"] and "cmake" in db_reg
                    else "",
                    "crystal": Crystal().get_version(config_loaded, db_reg["crystal"])
                    if config_loaded["crystal"]["version"]["enable"]
                    and "crystal" in db_reg
                    else "",
                    "deno": Deno().get_version(config_loaded, db_reg["deno"])
                    if config_loaded["deno"]["version"]["enable"] and "deno" in db_reg
                    else "",
                    "erlang": Erlang().get_version(config_loaded, db_reg["erlang"])
                    if config_loaded["erlang"]["version"]["enable"]
                    and "erlang" in db_reg
                    else "",
                    "helm": Helm().get_version(config_loaded, db_reg["helm"])
                    if config_loaded["helm"]["version"]["enable"] and "helm" in db_reg
                    else "",
                    "kotlin": Kotlin().get_version(config_loaded, db_reg["kotlin"])
                    if config_loaded["kotlin"]["version"]["enable"]
                    and "kotlin" in db_reg
                    else "",
                    "nim": Nim().get_version(config_loaded, db_reg["nim"])
                    if config_loaded["nim"]["version"]["enable"] and "nim" in db_reg
                    else "",
                    "ocaml": Ocaml().get_version(config_loaded, db_reg["ocaml"])
                    if config_loaded["ocaml"]["version"]["enable"] and "ocaml" in db_reg
                    else "",
                    "vagrant": Vagrant().get_version(config_loaded, db_reg["vagrant"])
                    if config_loaded["vagrant"]["version"]["enable"]
                    and "vagrant" in db_reg
                    else "",
                    "zig": Zig().get_version(config_loaded, db_reg["zig"])
                    if config_loaded["zig"]["version"]["enable"] and "zig" in db_reg
                    else "",
                    # "gulp": Gulp().get_version(config_loaded)
                    # if config_loaded["gulp"]["version"]["enable"]
                    # else "",
                    "docker": Docker().get_version(config_loaded, db_reg["docker"])
                    if config_loaded["docker"]["version"]["enable"]
                    and "docker" in db_reg
                    else "",
                    "git": Git(config_loaded) if config_loaded["git"]["enable"] else "",
                }
                cmd = Command(config_loaded)
                static_section = f"{jump_line}{username}{hostname}{directory}"
                ordered_section = (
                    dinamic_section[item]
                    for element in config_loaded["general"]["position"]
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

            config_loaded = self.config_load()

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
