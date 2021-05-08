from zshpower.utils.catch import current_user, current_shell
from snakypy.ansi import FG, NONE
from subprocess import call as subprocess_call


def reload_zsh() -> None:
    subprocess_call("exec zsh", shell=True)


def change_shell() -> bool:
    if current_shell()[0] != "zsh":
        try:
            subprocess_call(f"chsh -s $(which zsh) {current_user()}", shell=True)
            return True
        except KeyboardInterrupt as err:
            raise KeyboardInterrupt(f"{FG.WARNING}Canceled by user.{NONE}", err)
    return False


# # TODO: DEPRECATED
# def bash_command(cmd):
#     from subprocess import Popen as subprocess_popen
#
#     subprocess_popen(["su", "-c", cmd])
#
#
# def shell_command(cmd):
#     from subprocess import PIPE, Popen as subprocess_popen
#
#     p = subprocess_popen(
#         cmd, shell=True, stdout=PIPE, stderr=PIPE, universal_newlines=True
#     )
#     output, err = p.communicate()
#     return output.replace("\n", ""), err


# def systemctl_is_active(service):
#     from subprocess import PIPE, Popen as subprocess_popen

#     process = subprocess_popen(
#         ["systemctl", "is-active", service], stdout=PIPE, universal_newlines=True
#     )
#     output, err = process.communicate()
#     return output.replace("\n", ""), err
