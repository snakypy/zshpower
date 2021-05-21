from snakypy.helpers import printer
from snakypy.helpers.ansi import FG
from snakypy.helpers.console import billboard, credence
from snakypy.zshpower import __info__


def billboard_manual() -> str:
    # This sign was generated by the "figlet" program (http://www.figlet.org/).
    # It also has a package called pyfiglet (https://pypi.org/project/pyfiglet/).
    text = """
                    ____              _
                   / ___| _ __   __ _| | ___   _ _ __  _   _
                   \___ \| '_ \ / _` | |/ / | | | '_ \| | | |
                    ___) | | | | (_| |   <| |_| | |_) | |_| |
                   |____/|_| |_|\__,_|_|\_\\\__, | .__/ \__, |
                                           |___/|_|    |___/
    """
    return text


class CreditsCommand:
    @staticmethod
    def run() -> None:
        print("\n")
        printer("Offered by:".center(50), foreground=FG().GREEN)
        printer(
            billboard_manual(),
            foreground=FG().YELLOW,
        )
        billboard(
            __info__["organization_name"],
            justify="center",
            foreground=FG().YELLOW,
        )
        printer("copyright (c) since 2020\n".center(100), foreground=FG().GREEN)
        credence(
            __info__["name"],
            __info__["version"],
            __info__["home_page"],
            __info__,
            foreground=FG().CYAN,
        )
