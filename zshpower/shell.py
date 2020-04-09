from sys import argv as sys_argv, stdout
from tomlkit import parse as toml_parse
from snakypy.file import read as snakypy_file_red
from snakypy import printer, FG
from snakypy.ansi import NONE
from zshpower import HOME
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
from zshpower.commands import init


class Prompt:
    """Class to perform the impression of the PROMPT style"""

    def __init__(self):
        self.zp = Base(HOME)

    @property
    def config(self):
        try:
            read_conf = snakypy_file_red(self.zp.config)
            parsed = toml_parse(read_conf)
            return parsed
        except FileNotFoundError:
            init.InitCommand(HOME).main()
            read_conf = snakypy_file_red(self.zp.config)
            parsed = toml_parse(read_conf)
            printer(
                f"[ZSHPower Warning] A new configuration file for that version "
                f'has been created in "{FG.GREEN}{self.zp.config_root}{NONE}".',
                foreground=FG.YELLOW,
            )
            return parsed

    def left(self, jump_line="\n"):
        if not self.config["general"]["jump_line"]["enable"]:
            jump_line = ""
        username = Username(self.config)
        hostname = Hostname(self.config)
        directory = Directory(self.config)
        dinamic_section = {
            "package": PyProject(self.config),
            "python": Python(self.config),
            "virtualenv": Virtualenv(self.config),
            "git": Git(self.config),
        }
        cmd = Command(self.config)

        static_section = f"{jump_line}{username}{hostname}{directory}"

        ordered_section = []
        for element in self.config["general"]["position"]:
            for item in dinamic_section.keys():
                if item == element:
                    # stdout.write(str(dinamic_section[item]))
                    ordered_section.append(dinamic_section[item])
        sections = "{}{}{}{}{}{}"
        return sections.format(static_section, *ordered_section, cmd)

    def right(self):
        timer = str(Timer(self.config))
        return timer


def main():
    if len(sys_argv) >= 1 and sys_argv[1] == "prompt":
        stdout.write(Prompt().left())
    elif len(sys_argv) >= 1 and sys_argv[1] == "rprompt":
        stdout.write(Prompt().right())
