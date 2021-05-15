from snakypy.helpers.catches import shell
from snakypy.helpers.ansi import FG, NONE
from snakypy.helpers.catches import whoami
from subprocess import call as subprocess_call


def reload_zsh() -> None:
    subprocess_call("exec zsh", shell=True)


def change_shell() -> bool:
    if shell()[0] != "zsh":
        try:
            subprocess_call(f"chsh -s $(which zsh) {whoami()}", shell=True)
            return True
        except KeyboardInterrupt as err:
            raise KeyboardInterrupt(f"{FG().WARNING}Canceled by user.{NONE}", err)
    return False
