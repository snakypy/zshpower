from shutil import which
from os.path import join, exists
from snakypy import printer, FG
from zshpower.config import package


def tools_requirements(*args):
    for tool in args:
        if which(tool) is None:
            raise Exception(
                f'The package \'{package.info["name"]}\' needs the "{tool}" tool.'
                " Tool not found. Aborted."
            )


def checking_init(root):
    """Function that ends commands that depend on the created repository, but
    the repository was not created."""
    if not exists(join(root, f"{package.info['pkg_name']}.zsh-theme")):
        printer(
            f'Command "{package.info["pkg_name"]} init" has not been started.'
            "Aborted",
            foreground=FG.WARNING,
        )
        exit(1)
    return True
