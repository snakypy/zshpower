import curses
from zshpower.database.dao import DAO
from zshpower.utils.process import reload_zsh
from zshpower.utils.check import checking_init
from zshpower.utils.shift import create_config
from zshpower.config.config import content as config_content
from snakypy.console import loading
from zshpower.config.base import Base
from snakypy.ansi import FG
from snakypy import printer
from zshpower.commands.lib.handle import records


class ResetCommand(Base):
    def __init__(self, home):
        Base.__init__(self, home)

    def run(self, arguments) -> None:
        checking_init(self.HOME)
        if arguments["--config"]:
            create_config(config_content, self.config_file, force=True)
            printer("Reset process finished.", foreground=FG.FINISH)
            reload_zsh()
        elif arguments["--db"]:
            DAO().create_table(self.tbl_main)
            records("insert")
            curses.initscr()
            curses.curs_set(0)
            loading(
                set_time=0.050,
                bar=False,
                header="ZSHPower Restoring the database ...",
                foreground=FG.QUESTION,
            )
            curses.curs_set(1)
            curses.endwin()
            printer("Done!", foreground=FG.FINISH)
