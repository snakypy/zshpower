from sys import argv as sys_argv, stdout
from tomlkit import parse as toml_parse
from snakypy.file import read as snakypy_file_red
from snakypy.utils.decorators import only_for_linux
from snakypy import FG
from snakypy.path import create as snakypy_path_create
from zshpower import HOME
from zshpower.config import package
from zshpower.utils.shift import create_config
from zshpower.config.config import content as config_content
from zshpower.prompt.sections.command import Command
from zshpower.prompt.sections.directory import Directory
from zshpower.prompt.sections.git import Git
from zshpower.prompt.sections.hostname import Hostname
from zshpower.prompt.sections.package import get_package
from zshpower.prompt.sections.docker import Docker
from zshpower.prompt.sections.node import NodeJs
from zshpower.prompt.sections.python import Python
from zshpower.prompt.sections.timer import Timer
from zshpower.prompt.sections.username import Username
from zshpower.prompt.sections.virtualenv import Virtualenv
from zshpower.config.base import Base
from tomlkit.exceptions import NonExistentKey, UnexpectedCharError


# TODO: Create a cache file containing the versions so that you
# don't run the command repeatedly.
class Prompt(Base):
    """Class to perform the impression of the PROMPT style"""

    def __init__(self):
        Base.__init__(self, HOME)

    @property
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

    def left(self, jump_line="\n"):
        try:
            if not self.config_load["general"]["jump_line"]["enable"]:
                jump_line = ""
            username = Username(self.config_load)
            hostname = Hostname(self.config_load)
            directory = Directory(self.config_load)
            dinamic_section = {
                "docker": Docker(self.config_load),
                "nodejs": NodeJs(self.config_load),
                "package": get_package(self.config_load),
                "python": Python(self.config_load),
                "virtualenv": Virtualenv(self.config_load),
                "git": Git(self.config_load),
            }
            cmd = Command(self.config_load)

            static_section = f"{jump_line}{username}{hostname}{directory}"

            ordered_section = []
            for element in self.config_load["general"]["position"]:
                for item in dinamic_section.keys():
                    if item == element:
                        # stdout.write(str(dinamic_section[item]))
                        ordered_section.append(dinamic_section[item])
            sections = "{}{}{}{}{}{}{}{}"
            return sections.format(static_section, *ordered_section, cmd)
        except (NonExistentKey, UnexpectedCharError, ValueError):
            return (
                f"{FG.ERROR}>>> {package.info['name']} Error: Key error in "
                f"the configuration file. "
            )

    def right(self):
        try:
            timer = str(Timer(self.config_load))
            return timer
        except (NonExistentKey):
            return (
                f"{FG.ERROR}>>> {package.info['name']} Error: Key error in "
                f"the configuration file. "
            )


@only_for_linux
def main():
    if len(sys_argv) < 2:
        raise TypeError("missing 1 required positional argument")
    if len(sys_argv) == 2 and sys_argv[1] == "prompt":
        stdout.write(Prompt().left())
    elif len(sys_argv) == 2 and sys_argv[1] == "rprompt":
        stdout.write(Prompt().right())
