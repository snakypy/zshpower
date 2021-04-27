from zshpower.database.sql import select_all
try:
    from snakypy import FG
    from tomlkit.exceptions import NonExistentKey, UnexpectedCharError
except KeyboardInterrupt:
    pass
from sqlite3 import OperationalError
from snakypy.utils.decorators import only_for_linux
from zshpower.utils.decorators import silent_errors
from zshpower import HOME
from zshpower.config import package
from zshpower.database.dao import DAO
from os.path import join
from zshpower.database.generators import create_table
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
from zshpower.prompt.sections.docker import DockerGetVersion, DockerSetVersion
from zshpower.prompt.sections.nodejs import NodeJs
from zshpower.prompt.sections.python import Python
from zshpower.prompt.sections.rust import Rust
from zshpower.prompt.sections.golang import GolangGetVersion, GolangSetVersion
from zshpower.prompt.sections.php import Php
from zshpower.prompt.sections.elixir import ElixirGetVersion, ElixirSetVersion
from zshpower.prompt.sections.julia import Julia
from zshpower.prompt.sections.dotnet import DotnetGetVersion, DotnetSetVersion
from zshpower.prompt.sections.ruby import Ruby
from zshpower.prompt.sections.java import JavaGetVersion, JavaSetVersion
from zshpower.prompt.sections.dart import DartGetVersion, DartSetVersion
from zshpower.prompt.sections.virtualenv import virtualenv
# Test timer
# from zshpower.utils.decorators import runtime


# TODO: Create a cache file containing the versions so that you
# don't run the command repeatedly.
class Draw(DAO):
    def __init__(self):
        DAO.__init__(self)

    def config_load(self):
        try:
            read_conf = snakypy_file_red(self.config_file)
            parsed = toml_parse(read_conf)
            return parsed

        except (FileNotFoundError, NonExistentKey):
            snakypy_path_create(self.config_root)
            create_config(config_content, self.config_file)
            read_conf = snakypy_file_red(self.config_file)
            parsed = toml_parse(read_conf)
            # printer(
            #     f"[ZSHPower Warning] A new configuration file for that version "
            #     f'has been created in "{self.config_root}".',
            #     foreground=FG.YELLOW,
            # )
            return parsed

    def db_restore(self):
        create_table(DAO(), join(HOME, self.data_root, self.database_name))
        DartSetVersion().main(action="insert")
        DockerSetVersion().main(action="insert")
        DotnetSetVersion().main(action="insert")
        ElixirSetVersion().main(action="insert")
        GolangSetVersion().main(action="insert")
        JavaSetVersion().main(action="insert")
        # Manager(DAO()).julia(self.table_name, option="insert")
        # Manager(DAO()).nodejs(self.table_name, option="insert")
        # Manager(DAO()).php(self.table_name, option="insert")
        # Manager(DAO()).ruby(self.table_name, option="insert")
        # Manager(DAO()).rust(self.table_name, option="insert")

    def db_fetchall(self):
        try:
            reg = select_all(DAO(), columns=("name", "version"), table="main")
            # TODO: se faltar uma registro apenas tratar.
            # TODO: Apagar dados para depois salvar
            if not reg:
                self.db_restore()
                reg = select_all(DAO(), columns=("name", "version"), table="main")
            return reg
        except (OperationalError, KeyError):
            self.db_restore()
            reg = select_all(DAO(), columns=("name", "version"), table="main")
            return reg

    # @runtime
    def prompt(self, jump_line="\n"):
        # self.reg = select_database_all(DAO(HOME), self.table_name)

        # Loading the settings to a local variable and thus improving performance
        config_loaded = self.config_load()

        reg = self.db_fetchall()

        try:

            if not config_loaded["general"]["jump_line"]["enable"]:
                jump_line = ""

            username = (
                Username(config_loaded) if config_loaded["username"]["enable"] else ""
            )

            hostname = (
                Hostname(config_loaded) if config_loaded["hostname"]["enable"] else ""
            )

            directory = Directory(config_loaded)

            dinamic_section = {
                "virtualenv": virtualenv(config_loaded)
                if config_loaded["virtualenv"]["enable"]
                else "",
                "python": Python(config_loaded)
                if config_loaded["python"]["version"]["enable"]
                else "",
                "package": pkg_version(config_loaded)
                if config_loaded["package"]["enable"]
                else "",
                "nodejs": NodeJs(config_loaded, reg["nodejs"])
                if config_loaded["nodejs"]["version"]["enable"]
                else "",
                "rust": Rust(config_loaded, reg["rust"])
                if config_loaded["rust"]["version"]["enable"]
                else "",
                "golang": GolangGetVersion(config_loaded, reg["golang"])
                if config_loaded["golang"]["version"]["enable"]
                else "",
                "ruby": Ruby(config_loaded, reg["ruby"])
                if config_loaded["ruby"]["version"]["enable"]
                else "",
                "dart": DartGetVersion(config_loaded, reg["dart"])
                if config_loaded["dart"]["version"]["enable"]
                else "",
                "php": Php(config_loaded, reg["php"])
                if config_loaded["php"]["version"]["enable"]
                else "",
                "java": JavaGetVersion(config_loaded, reg["java"])
                if config_loaded["java"]["version"]["enable"]
                else "",
                "julia": Julia(config_loaded, reg["julia"])
                if config_loaded["julia"]["version"]["enable"]
                else "",
                "dotnet": DotnetGetVersion(config_loaded, reg["dotnet"])
                if config_loaded["dotnet"]["version"]["enable"]
                else "",
                "elixir": ElixirGetVersion(config_loaded, reg["elixir"])
                if config_loaded["elixir"]["version"]["enable"]
                else "",
                "docker": DockerGetVersion(config_loaded, reg["docker"])
                if config_loaded["docker"]["version"]["enable"]
                else "",
                "git": Git(config_loaded) if config_loaded["git"]["enable"] else "",
            }
            cmd = Command(config_loaded)

            static_section = f"{jump_line}{username}{hostname}{directory}"

            # # No List Comprehension/Generator expressions
            # ordered_section = []
            # for element in config_loaded["general"]["position"]:
            #     for item in dinamic_section.keys():
            #         if item == element:
            #             # stdout.write(str(dinamic_section[item]))
            #             ordered_section.append(dinamic_section[item])

            ordered_section = (
                dinamic_section[item]
                for element in config_loaded["general"]["position"]
                for item in dinamic_section.keys()
                if item in element
            )

            sections = "{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}"
            return sections.format(static_section, *ordered_section, cmd)

        except (NonExistentKey, UnexpectedCharError, ValueError):
            return (
                f"{FG.ERROR}>>> {package.info['name']} Error: Key error in "
                f"the configuration file.\n> "
            )

    def rprompt(self):
        try:
            from zshpower.prompt.sections.timer import Timer

            config_loaded = self.config_load

            timer = str(Timer(config_loaded) if config_loaded["timer"]["enable"] else "")
            return timer
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
