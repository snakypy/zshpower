from subprocess import call as subprocess_call
from time import sleep

from snakypy.helpers import FG, printer
from snakypy.helpers.catches import shell, whoami
from snakypy.helpers.logging import Log


def reload_zsh(sleep_timer=None, message=False) -> None:
    if message:
        printer("Restarting terminal, wait...", foreground=FG().WARNING)
    if sleep_timer:
        sleep(sleep_timer)
    subprocess_call("exec zsh", shell=True)


def change_shell(logfile) -> bool:
    if shell() != "zsh":
        try:
            subprocess_call(f"chsh -s $(which zsh) {whoami()}", shell=True)
            return True
        except KeyboardInterrupt:
            Log(filename=logfile).record(
                f"Shell change canceled by user ({whoami()})",
                colorize=True,
                level="warning",
            )
            printer("Canceled by user.", foreground=FG().WARNING)
    return False
