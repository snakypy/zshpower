import sys
import snakypy
import tomlkit
from zshpower import HOME
from zshpower.sections.command import Command
from zshpower.sections.directory import Directory
from zshpower.sections.git import Git
from zshpower.sections.hostname import Hostname
from zshpower.sections.package import PyProject
from zshpower.sections.python import Python
from zshpower.sections.timer import Timer
from zshpower.sections.username import Username
from zshpower.sections.virtualenv import Virtualenv
from zshpower.zshpower import ZSHPower


class Prompt:
    """Class to perform the impression of the PROMPT style"""

    def __init__(self):
        self.zp = ZSHPower(HOME)

    @property
    def config(self):
        try:
            read_conf = snakypy.file.read(self.zp.config)
            parsed = tomlkit.parse(read_conf)
            return parsed
        except FileNotFoundError:
            self.zp.init_command()
            read_conf = snakypy.file.read(self.zp.config)
            parsed = tomlkit.parse(read_conf)
            snakypy.printer(
                f"[ZSHPower Warning] A new configuration file for that version "
                f'has been created in "{snakypy.FG.GREEN}{self.zp.config_root}{snakypy.ansi.NONE}".',
                foreground=snakypy.FG.YELLOW,
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
                    # sys.stdout.write(str(dinamic_section[item]))
                    ordered_section.append(dinamic_section[item])
        sections = "{}{}{}{}{}{}"
        return sections.format(static_section, *ordered_section, cmd)

    def right(self):
        timer = str(Timer(self.config))
        return timer


def main():
    if len(sys.argv) >= 1 and sys.argv[1] == "prompt":
        sys.stdout.write(Prompt().left())
    elif len(sys.argv) >= 1 and sys.argv[1] == "rprompt":
        sys.stdout.write(Prompt().right())
