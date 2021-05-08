from os.path import join, exists
from shutil import which
from zshpower.config import package


def is_tool(*args) -> bool:
    for tool in args:
        if which(tool) is not None:
            return True
    return False


def tools_requirements(*args) -> bool:
    for tool in args:
        if which(tool) is None:
            raise Exception(
                f'The package \'{package.info["name"]}\' needs the "{tool}" tool.'
                " Tool not found. Aborted."
            )
    return True


def checking_init(home) -> bool:
    """Function that ends commands that depend on the created repository, but
    the repository was not created."""

    if not exists(join(home, f".{package.info['pkg_name']}")):
        raise FileNotFoundError(
            f'Command "{package.info["pkg_name"]} init" has not been started.'
            "Aborted",
        )
    return True
