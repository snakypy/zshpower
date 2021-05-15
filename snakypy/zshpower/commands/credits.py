from snakypy.helpers import printer
from snakypy.helpers.ansi import FG
from snakypy.helpers.console import billboard, credence
from snakypy.zshpower.config import package
from snakypy.zshpower import __version__


class CreditsCommand:
    @staticmethod
    def run() -> None:
        print("\n")
        printer("Offered by:".center(50), foreground=FG().GREEN)
        billboard(
            package.info["organization_name"],
            justify="center",
            foreground=FG().YELLOW,
        )
        printer("copyright (c) since 2020\n".center(100), foreground=FG().GREEN)
        credence(
            package.info["name"],
            __version__,
            package.info["home_page"],
            package.info,
            foreground=FG().CYAN,
        )
