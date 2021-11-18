from os.path import exists, join

from snakypy.helpers.logging import Log

from snakypy.zshpower import __info__


def checking_init(home, logfile) -> bool:
    """Function that ends commands that depend on the created repository, but
    the repository was not created."""

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
