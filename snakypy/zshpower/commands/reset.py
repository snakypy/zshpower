import curses

from snakypy.helpers import printer
from snakypy.helpers.ansi import FG
from snakypy.helpers.console import loading

from snakypy.zshpower.commands.utils.handle import records
from snakypy.zshpower.config.base import Base
from snakypy.zshpower.config.config import content as config_content
from snakypy.zshpower.database.dao import DAO
from snakypy.zshpower.utils.check import checking_init
from snakypy.zshpower.utils.process import reload_zsh
from snakypy.zshpower.utils.shift import create_config


class ResetCommand(Base):
    def __init__(self, home):
        Base.__init__(self, home)

    def run(self, arguments) -> None:
        checking_init(self.HOME)
        if arguments["--config"]:
            create_config(config_content, self.config_file, force=True)
            printer("Reset process finished.", foreground=FG().FINISH)
            reload_zsh()
        elif arguments["--db"]:
            DAO().create_table(self.tbl_main)
            printer(
                "Entering the process of resetting the DB. Wait ...",
                foreground=FG().QUESTION,
            )
            records("insert")
            curses.initscr()
            curses.curs_set(0)
            loading(
                set_time=0.050,
                bar=False,
                header="ZSHPower Restoring the database ...",
                foreground=FG().QUESTION,
            )
            curses.curs_set(1)
            curses.endwin()
            printer("Done!", foreground=FG().FINISH)
