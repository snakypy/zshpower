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
from zshpower.prompt.sections.nodejs import NodeJs, NodeJsSetVersion
from zshpower.prompt.sections.python import Python
from zshpower.prompt.sections.rust import Rust, RustSetVersion
from zshpower.prompt.sections.golang import GolangGetVersion, GolangSetVersion
from zshpower.prompt.sections.php import PhpGetVersion, PhpSetVersion
from zshpower.prompt.sections.elixir import ElixirGetVersion, ElixirSetVersion
from zshpower.prompt.sections.julia import Julia, JuliaSetVersion
from zshpower.prompt.sections.dotnet import DotnetGetVersion, DotnetSetVersion
from zshpower.prompt.sections.ruby import Ruby, RubySetVersion
from zshpower.prompt.sections.java import JavaGetVersion, JavaSetVersion
from zshpower.prompt.sections.dart import DartGetVersion, DartSetVersion
from zshpower.prompt.sections.virtualenv import Virtualenv
from zshpower.database.sql_inject import RetAllNameVersion, create_table

# Test timer
# from zshpower.utils.decorators import runtime


# def checking_items_db_config(config, reg):
#     """ Checking data DB in file configuration."""
#     config_keys = [i for i in config.keys()]
#     db_values = [j for i in reg.__dict__.values() for j in i]
#     for item in db_values:
#         if item not in config_keys:
#             return False
#     return True


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
        JuliaSetVersion().main(action="insert")
        NodeJsSetVersion().main(action="insert")
        PhpSetVersion().main(action="insert")
        RubySetVersion().main(action="insert")
        RustSetVersion().main(action="insert")

    def db_fetchall(self):
        try:
            reg = RetAllNameVersion(DAO(), columns=("name", "version"), table="main")

            if not reg:
                self.db_restore()
                reg = RetAllNameVersion(
                    DAO(), columns=("name", "version"), table="main"
                )
            return reg
        except (OperationalError, KeyError):
            self.db_restore()
            reg = RetAllNameVersion(DAO(), columns=("name", "version"), table="main")
            return reg

    # @runtime
    def prompt(self, jump_line="\n"):
        # Loading the settings to a local variable and thus improving performance
        config_loaded = self.config_load()

        db_reg = self.db_fetchall()

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
                "virtualenv": Virtualenv(config_loaded)
                if config_loaded["virtualenv"]["enable"]
                else "",
                "python": Python(config_loaded)
                if config_loaded["python"]["version"]["enable"]
                else "",
                "package": pkg_version(config_loaded)
                if config_loaded["package"]["enable"]
                else "",
                "nodejs": NodeJs(config_loaded, db_reg["nodejs"])
                if config_loaded["nodejs"]["version"]["enable"]
                else "",
                "rust": Rust(config_loaded, db_reg["rust"])
                if config_loaded["rust"]["version"]["enable"]
                else "",
                "golang": GolangGetVersion(config_loaded, db_reg["golang"])
                if config_loaded["golang"]["version"]["enable"]
                else "",
                "ruby": Ruby(config_loaded, db_reg["ruby"])
                if config_loaded["ruby"]["version"]["enable"]
                else "",
                "dart": DartGetVersion(config_loaded, db_reg["dart"])
                if config_loaded["dart"]["version"]["enable"]
                else "",
                "php": PhpGetVersion(config_loaded, db_reg["php"])
                if config_loaded["php"]["version"]["enable"]
                else "",
                "java": JavaGetVersion(config_loaded, db_reg["java"])
                if config_loaded["java"]["version"]["enable"]
                else "",
                "julia": Julia(config_loaded, db_reg["julia"])
                if config_loaded["julia"]["version"]["enable"]
                else "",
                "dotnet": DotnetGetVersion(config_loaded, db_reg["dotnet"])
                if config_loaded["dotnet"]["version"]["enable"]
                else "",
                "elixir": ElixirGetVersion(config_loaded, db_reg["elixir"])
                if config_loaded["elixir"]["version"]["enable"]
                else "",
                "docker": DockerGetVersion(config_loaded, db_reg["docker"])
                if config_loaded["docker"]["version"]["enable"]
                else "",
                "git": Git(config_loaded) if config_loaded["git"]["enable"] else "",
            }
            cmd = Command(config_loaded)

            static_section = f"{jump_line}{username}{hostname}{directory}"

            # TODO: No List Comprehension/Generator expressions (DEPRECATED)
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
