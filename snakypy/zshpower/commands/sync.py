import sys
from sqlite3 import OperationalError

from snakypy.helpers import FG
from snakypy.helpers.catches.generic import whoami
from snakypy.helpers.console import printer

from snakypy.zshpower.commands.utils.handle import records
from snakypy.zshpower.config.base import Base
from snakypy.zshpower.utils.check import checking_init


class Sync(Base):
    def __init__(self, home):
        Base.__init__(self, home)

    def run(self) -> None:
        try:
            checking_init(self.HOME, self.logfile)
            records("update", "Synchronizing versions with database ...", FG().QUESTION)
            self.log.record(
                f"User ({whoami()}) updated the database.",
                colorize=True,
                level="info",
            )
            printer("Done!", foreground=FG().FINISH)
        except KeyboardInterrupt:
            printer(
                "This operation cannot be canceled. Wait for the operation.",
                foreground=FG().WARNING,
            )
        except OperationalError:
            self.log.record(
                "The database does not exist or is corrupted.",
                colorize=True,
                level="error",
            )
            printer(
                "The database does not exist or is corrupted.",
                foreground=FG().ERROR,
            )
            sys.exit(1)
