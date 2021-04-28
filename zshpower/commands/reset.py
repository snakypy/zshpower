from zshpower.config.base import Base
from snakypy import printer
from snakypy.ansi import FG
from zshpower.utils.process import reload_zsh
from zshpower.utils.check import checking_init
from zshpower.utils.shift import create_config
from zshpower.config.config import content as config_content


class ResetCommand(Base):
    def __init__(self, home):
        Base.__init__(self, home)

    def main(self):
        checking_init(self.HOME)
        create_config(config_content, self.config_file, force=True)
        printer("Reset process finished.", foreground=FG.FINISH)
        reload_zsh()
