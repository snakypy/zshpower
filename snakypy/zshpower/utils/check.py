from os.path import exists, join

from snakypy.zshpower import __info__


def checking_init(home, logfile) -> bool:
    """Function that ends commands that depend on the created repository, but
    the repository was not created."""

    if not exists(join(home, f".{__info__['pkg_name']}")):
        from snakypy.zshpower.utils.shift import log_base

        log_base(logfile).record(
            f'Command "{__info__["pkg_name"]} init" has not been started.' "Aborted",
            colorize=True,
        )
        raise FileNotFoundError(
            f'Command "{__info__["pkg_name"]} init" has not been started.' "Aborted",
        )
    return True
