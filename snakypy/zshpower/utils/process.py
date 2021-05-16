from snakypy.helpers.catches import shell
from snakypy.helpers import FG, printer
from snakypy.helpers.catches import whoami
from subprocess import call as subprocess_call


def reload_zsh() -> None:
    subprocess_call("exec zsh", shell=True)


def change_shell() -> bool:
    if shell() != "zsh":
        try:
            subprocess_call(f"chsh -s $(which zsh) {whoami()}", shell=True)
            return True
        except KeyboardInterrupt:
            printer("Canceled by user.", foreground=FG().WARNING)
    return False
