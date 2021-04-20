from snakypy import printer
from snakypy.ansi import FG
from zshpower.config.base import Base
from zshpower.utils.process import reload_zsh
from zshpower.utils.shift import change_theme_in_zshrc
from zshpower.utils.catch import read_zshrc_omz
from zshpower.utils.check import checking_init


class ActivateCommand(Base):
    def __init__(self, home):
        Base.__init__(self, home)

    def main(self):
        checking_init(self.HOME)

        if read_zshrc_omz(self.zsh_rc):
            if read_zshrc_omz(self.zsh_rc)[0] == "zshpower":
                printer("Already activated. Nothing to do.", foreground=FG.GREEN)
                exit(0)
            change_theme_in_zshrc(self.zsh_rc, "zshpower")
            printer("Activation process finish.", foreground=FG.FINISH)
            reload_zsh()
            return True
        return printer(
            "You are not using Oh My ZSH to run this command.", foreground=FG.WARNING
        )
