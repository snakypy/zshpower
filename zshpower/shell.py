from sys import argv as sys_argv, stdout
from tomlkit import parse as toml_parse
from snakypy.file import read as snakypy_file_red
from snakypy.path import create as snakypy_path_create
from zshpower import HOME
from zshpower.utils.shift import create_config
from zshpower.config.config import content as config_content
from zshpower.prompt.sections.command import Command
from zshpower.prompt.sections.directory import Directory
from zshpower.prompt.sections.git import Git
from zshpower.prompt.sections.hostname import Hostname
from zshpower.prompt.sections.package import PyProject
from zshpower.prompt.sections.python import Python
from zshpower.prompt.sections.timer import Timer
from zshpower.prompt.sections.username import Username
from zshpower.prompt.sections.virtualenv import Virtualenv
from zshpower.config.base import Base


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
        except FileNotFoundError:
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
        if not self.config_load["general"]["jump_line"]["enable"]:
            jump_line = ""
        username = Username(self.config_load)
        hostname = Hostname(self.config_load)
        directory = Directory(self.config_load)
        dinamic_section = {
            "package": PyProject(self.config_load),
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
        sections = "{}{}{}{}{}{}"
        return sections.format(static_section, *ordered_section, cmd)

    def right(self):
        timer = str(Timer(self.config_load))
        return timer


def main():
    if len(sys_argv) >= 1 and sys_argv[1] == "prompt":
        stdout.write(Prompt().left())
    elif len(sys_argv) >= 1 and sys_argv[1] == "rprompt":
        stdout.write(Prompt().right())
