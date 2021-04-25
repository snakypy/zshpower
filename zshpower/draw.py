try:
    from snakypy import FG
    from tomlkit.exceptions import NonExistentKey, UnexpectedCharError
except KeyboardInterrupt:
    pass
from snakypy.utils.decorators import only_for_linux
from zshpower.utils.decorators import silent_errors
from zshpower import HOME
from zshpower.config import package
from zshpower.config.base import Base

# Test timer
# from zshpower.utils.decorators import runtime


# TODO: Create a cache file containing the versions so that you
# don't run the command repeatedly.
class Draw(Base):
    """Class to perform the impression of the PROMPT style"""

    def __init__(self):
        Base.__init__(self, HOME)

    @property
    def config_load(self):
        try:
            from zshpower.config.config import content as config_content
            from zshpower.utils.shift import create_config
            from snakypy.path import create as snakypy_path_create
            from snakypy.file import read as snakypy_file_red
            from tomlkit import parse as toml_parse

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

    # @runtime
    def prompt(self, jump_line="\n"):
        try:
            from zshpower.prompt.sections.directory import Directory
            from zshpower.prompt.sections.git import Git
            from zshpower.prompt.sections.hostname import Hostname
            from zshpower.prompt.sections.package import package
            from zshpower.prompt.sections.docker import Docker
            from zshpower.prompt.sections.node import NodeJs
            from zshpower.prompt.sections.python import Python
            from zshpower.prompt.sections.rust import Rust
            from zshpower.prompt.sections.golang import Golang
            from zshpower.prompt.sections.php import Php
            from zshpower.prompt.sections.elixir import Elixir
            from zshpower.prompt.sections.julia import Julia
            from zshpower.prompt.sections.dotnet import Dotnet
            from zshpower.prompt.sections.ruby import Ruby
            from zshpower.prompt.sections.java import Java
            from zshpower.prompt.sections.dart import Dart
            from zshpower.prompt.sections.command import Command
            from zshpower.prompt.sections.username import Username
            from zshpower.prompt.sections.virtualenv import Virtualenv

            # Loading the settings to a local variable and thus improving performance
            config_loaded = self.config_load

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
                "package": package(config_loaded)
                if config_loaded["package"]["enable"]
                else "",
                "nodejs": NodeJs(config_loaded)
                if config_loaded["nodejs"]["version"]["enable"]
                else "",
                "rust": Rust(config_loaded)
                if config_loaded["rust"]["version"]["enable"]
                else "",
                "golang": Golang(config_loaded)
                if config_loaded["golang"]["version"]["enable"]
                else "",
                "ruby": Ruby(config_loaded)
                if config_loaded["ruby"]["version"]["enable"]
                else "",
                "dart": Dart(config_loaded)
                if config_loaded["dart"]["version"]["enable"]
                else "",
                "php": Php(config_loaded)
                if config_loaded["php"]["version"]["enable"]
                else "",
                "java": Java(config_loaded)
                if config_loaded["java"]["version"]["enable"]
                else "",
                "julia": Julia(config_loaded)
                if config_loaded["julia"]["version"]["enable"]
                else "",
                "dotnet": Dotnet(config_loaded)
                if config_loaded["dotnet"]["version"]["enable"]
                else "",
                "elixir": Elixir(config_loaded)
                if config_loaded["elixir"]["version"]["enable"]
                else "",
                "docker": Docker(config_loaded)
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
        except (NonExistentKey):
            return (
                f"{FG.ERROR}>>> {package.info['name']} Error: Key error in "
                f"the configuration file.\n > "
            )


"""
PERFORMANCE NOTE: AS ZSHPOWER NEEDS TO LOAD AN EXTERNAL CONFIGURATION TOML FILE AT ALL
TIMES WHEN A TERMINAL COMMAND IS LAUNCHED, PERFORMANCE IN LOADING THE ZSHPOWER VISUAL
MODEL SHOULD FALL A FEW MILLISECONDS.
"""


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
