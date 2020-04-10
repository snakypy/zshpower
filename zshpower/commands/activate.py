from snakypy import printer
from snakypy.ansi import FG
from zshpower.config.base import Base
from zshpower.utils.process import reload_zsh
from zshpower.utils.shift import change_theme_in_zshrc
from zshpower.utils.catch import read_zshrc
from zshpower.utils.check import checking_init


class ActivateCommand(Base):
    def __init__(self, home):
        Base.__init__(self, home)

    def main(self):
        checking_init(self.themes_folder)

        if read_zshrc(self.zsh_rc):
            if read_zshrc(self.zsh_rc)[0] == "zshpower":
                printer("Already activated. Nothing to do.", foreground=FG.GREEN)
                exit(0)
            change_theme_in_zshrc(self.zsh_rc, "zshpower")
            printer("Activation process finish.", foreground=FG.FINISH)
            reload_zsh()
