from os.path import exists, getsize, isfile, join
from shutil import which
from sys import exit

from snakypy.helpers import FG, printer
from snakypy.helpers.decorators import only_linux
from snakypy.helpers.logging import Log

from snakypy.zshpower import __info__


def is_blank_file(filepath):
    """
    Checks if a file is blank, that is, it does not contain lines.
    """
    return isfile(filepath) and getsize(filepath) == 0


@only_linux
def tools_requirements(*args) -> bool:
    """
    Function that looks for the necessary tools, if it doesn't find them,
    it triggers a message and closes the program.
    """
    for tool in args:
        if which(tool) is None:
            printer(
                f'The tool "{tool}" is not installed on the operating system.',
                foreground=FG().ERROR,
            )
            exit()
    return True


def checking_init(home, logfile) -> bool:
    """
    Function that ends commands that depend on the created repository, but
    the repository was not created.
    """

    if not exists(join(home, f".{__info__['pkg_name']}")):
        Log(filename=logfile).record(
            f'Command "{__info__["pkg_name"]} init" has not been started.' "Aborted",
            colorize=True,
            level="error",
        )
        raise FileNotFoundError(
            f'Command "{__info__["pkg_name"]} init" has not been started.' "Aborted",
        )
    return True


def str_empty_in(*args):
    """
    Function that checks whether an object is an empty string.

    Returns:
        [bool]: Return bool
    """
    for _ in args:
        if "" in args:
            return True
    return False
