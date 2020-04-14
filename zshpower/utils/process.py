from subprocess import call as subprocess_call
from subprocess import PIPE, Popen as subprocess_popen
from zshpower.utils.catch import current_user, current_shell
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


def systemctl_is_active(service):
    process = subprocess_popen(
        ["systemctl", "is-active", service], stdout=PIPE, universal_newlines=True
    )
    output, err = process.communicate()
    return output.replace("\n", ""), err
