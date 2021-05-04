from snakypy import printer
from snakypy.ansi import FG
from snakypy.console import billboard, credence
from zshpower.config import package
from zshpower import __version__


class CreditsCommand:
    @staticmethod
    def run():
        print("\n")
        printer("Offered by:".center(50), foreground=FG.GREEN)
        billboard(
            package.info["organization_name"], justify="center", foreground=FG.YELLOW
        )
        printer("copyright (c) since 2020\n".center(100), foreground=FG.GREEN)
        credence(
            package.info["name"],
            __version__,
            package.info["home_page"],
            package.info,
            foreground=FG.CYAN,
        )
