from pydoc import pager

from snakypy.helpers import printer
from snakypy.helpers.ansi import FG
from snakypy.helpers.files import read_file
from snakypy.helpers.logging import Log

from snakypy.zshpower.config.base import Base
from snakypy.zshpower.utils.check import checking_init


class LogsCommand(Base):
    def __init__(self, home):
        Base.__init__(self, home)

    def run(self, arguments) -> None:
        checking_init(self.HOME, self.logfile)
        if arguments["--view"]:
            read_logs = read_file(self.logfile)
            pager(read_logs)
        elif arguments["--clean"]:
            Log(filename=self.logfile, force=True)
            printer("Logs have been cleaned up.", foreground=FG().FINISH)
