from snakypy.helpers import printer
from snakypy.helpers.ansi import FG

from snakypy.zshpower.config.base import Base
from snakypy.zshpower.utils.catch import read_zshrc_omz
from snakypy.zshpower.utils.check import checking_init
from snakypy.zshpower.utils.process import reload_zsh
from snakypy.zshpower.utils.shift import change_theme_in_zshrc


class DeactivateCommand(Base):
    def __init__(self, home):
        Base.__init__(self, home)

    def run(self, arguments, *, theme_name="robbyrussell") -> bool:

        checking_init(self.HOME, self.logfile)

        if read_zshrc_omz(self.zsh_rc, self.logfile):
            if not read_zshrc_omz(self.zsh_rc, self.logfile)[0] == "zshpower":
                printer("Already disabled. Nothing to do.", foreground=FG().GREEN)
                exit(0)
            if not arguments["--theme"]:
                change_theme_in_zshrc(self.zsh_rc, theme_name, self.logfile)
            else:
                change_theme_in_zshrc(self.zsh_rc, arguments["--theme"], self.logfile)
            printer("Deactivation process finish.", foreground=FG().FINISH)
            reload_zsh()
            return True
        printer(
            "You are not using Oh My ZSH to run this command.",
            foreground=FG().WARNING,
        )
        return False
