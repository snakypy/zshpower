from snakypy.helpers import printer
from snakypy.helpers.ansi import FG

from snakypy.zshpower.config.base import Base
from snakypy.zshpower.utils.catch import read_zshrc_omz
from snakypy.zshpower.utils.check import checking_init
from snakypy.zshpower.utils.modifiers import change_theme_in_zshrc
from snakypy.zshpower.utils.process import reload_zsh


class ActivateCommand(Base):
    def __init__(self, home):
        Base.__init__(self, home)

    def run(self) -> bool:

        checking_init(self.HOME, self.logfile)

        if read_zshrc_omz(self.zsh_rc, self.logfile):
            if read_zshrc_omz(self.zsh_rc, self.logfile)[0] == "zshpower":
                printer("Already activated. Nothing to do.", foreground=FG().GREEN)
                exit(0)
            change_theme_in_zshrc(self.zsh_rc, "zshpower", self.logfile)
            printer("Activation process finish.", foreground=FG().FINISH)
            reload_zsh()
            return True
        printer(
            "You are not using Oh My ZSH to run this command.",
            foreground=FG().WARNING,
        )
        return False
