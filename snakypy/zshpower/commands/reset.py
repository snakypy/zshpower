from concurrent.futures import ThreadPoolExecutor

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
        checking_init(self.HOME, self.logfile)
        if arguments["--config"]:
            create_config(config_content, self.config_file, force=True)
            printer("Reset process finished.", foreground=FG().FINISH)
            self.log.record("Config files reset", colorize=True, level="info")
            reload_zsh()
        elif arguments["--db"]:
            DAO().create_table(self.tbl_main)
            with ThreadPoolExecutor(max_workers=2) as executor:
                executor.submit(
                    loading,
                    set_time=0.140,
                    bar=False,
                    header="ZSHPower Restoring the database ...",
                    foreground=FG().QUESTION,
                )
                executor.submit(records, action="insert")
            printer("Done!", foreground=FG().FINISH)
            self.log.record("Database reset", colorize=True, level="info")
