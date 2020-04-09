from subprocess import call as subprocess_call
from subprocess import Popen as subprocess_popen
from zshpower.cli.utils.catch import current_user, current_shell
from snakypy import printer
from snakypy.ansi import FG


def reload_zsh():
    subprocess_call("exec zsh", shell=True)


def bash_command(cmd):
    subprocess_popen(["/bin/bash", "-c", cmd])


def change_shell():
    if current_shell()[0] != "zsh":
        try:
            subprocess_call(f"chsh -s $(which zsh) {current_user()}", shell=True)
        except KeyboardInterrupt:
            printer("Canceled by user", foreground=FG.WARNING)
