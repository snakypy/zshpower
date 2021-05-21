from os.path import exists, join

from snakypy.zshpower import __info__


def checking_init(home) -> bool:
    """Function that ends commands that depend on the created repository, but
    the repository was not created."""

    if not exists(join(home, f".{__info__['pkg_name']}")):
        raise FileNotFoundError(
            f'Command "{__info__["pkg_name"]} init" has not been started.' "Aborted",
        )
    return True
