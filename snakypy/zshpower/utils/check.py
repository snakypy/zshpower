from os.path import join, exists
from snakypy.zshpower.config import package


def checking_init(home) -> bool:
    """Function that ends commands that depend on the created repository, but
    the repository was not created."""

    if not exists(join(home, f".{package.info['pkg_name']}")):
        raise FileNotFoundError(
            f'Command "{package.info["pkg_name"]} init" has not been started.'
            "Aborted",
        )
    return True
