from snakypy import printer
from snakypy.ansi import FG
from zshpower.config.base import Base
from zshpower.utils.process import reload_zsh
from zshpower.utils.shift import change_theme_in_zshrc
from zshpower.utils.catch import read_zshrc
from zshpower.utils.check import checking_init


class DeactivateCommand(Base):
    def __init__(self, home):
        Base.__init__(self, home)

    def main(self, arguments, *, theme_name="robbyrussell"):
        checking_init(self.themes_folder)

        if read_zshrc(self.zsh_rc):
            if not read_zshrc(self.zsh_rc)[0] == "zshpower":
                printer("Already disabled. Nothing to do.", foreground=FG.GREEN)
                exit(0)
            if not arguments["--theme"]:
                change_theme_in_zshrc(self.zsh_rc, theme_name)
            else:
                change_theme_in_zshrc(self.zsh_rc, arguments["--theme"])
            printer("Deactivation process finish.", foreground=FG.FINISH)
            reload_zsh()
