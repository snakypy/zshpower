from snakypy.helpers import printer
from snakypy.helpers.ansi import FG
from snakypy.helpers.catches.generic import whoami

from snakypy.zshpower.config.base import Base
from snakypy.zshpower.utils.catch import get_zsh_theme
from snakypy.zshpower.utils.check import checking_init
from snakypy.zshpower.utils.modifiers import change_theme
from snakypy.zshpower.utils.process import reload_zsh


class DeactivateCommand(Base):
    def __init__(self, home):
        Base.__init__(self, home)

    def run(self, arguments, *, theme_name="robbyrussell") -> bool:

        checking_init(self.HOME, self.logfile)

        if get_zsh_theme(self.zsh_rc, self.logfile):
            if not get_zsh_theme(self.zsh_rc, self.logfile)[0] == "zshpower":
                printer("Already disabled. Nothing to do.", foreground=FG().GREEN)
                exit(0)
            if not arguments["--theme"]:
                change_theme(self.zsh_rc, theme_name, self.logfile)
            else:
                change_theme(self.zsh_rc, arguments["--theme"], self.logfile)
            printer("Deactivation process finish.", foreground=FG().FINISH)
            self.log.record(
                f"User ({whoami()}) has disabled ZSHPower.", colorize=True, level="info"
            )
            reload_zsh()
            return True
        printer(
            "You are not using Oh My ZSH to run this command.",
            foreground=FG().WARNING,
        )
        return False
