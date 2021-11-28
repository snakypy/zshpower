from pydoc import pager

from snakypy.helpers import printer
from snakypy.helpers.ansi import FG
from snakypy.helpers.files import create_file, read_file
from snakypy.helpers.os.removals import remove_objects

from snakypy.zshpower.config.base import Base
from snakypy.zshpower.utils.check import checking_init, is_blank_file


class LogsCommand(Base):
    def __init__(self, home):
        Base.__init__(self, home)

    def run(self, arguments) -> None:
        checking_init(self.HOME, self.logfile)
        if arguments["--view"]:
            try:
                read_logs = read_file(self.logfile)
                pager(read_logs)
            except FileNotFoundError:
                printer("Log files not found:", foreground=FG().WARNING)
        elif arguments["--clean"]:
            if is_blank_file(self.logfile):
                printer(
                    "The logs have already been cleared. Nothing to do.",
                    foreground=FG().WARNING,
                )
            else:
                remove_objects(objects=(self.logfile,))
                create_file("", self.logfile, force=True)
                printer("Logs have been cleaned up.", foreground=FG().FINISH)
