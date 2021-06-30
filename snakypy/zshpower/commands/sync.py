import sys
from concurrent.futures import ThreadPoolExecutor
from sqlite3 import OperationalError

from snakypy.helpers import FG
from snakypy.helpers.console import loading, printer

from snakypy.zshpower.commands.utils.handle import records
from snakypy.zshpower.config.base import Base
from snakypy.zshpower.utils.check import checking_init


class Sync(Base):
    def __init__(self, home):
        Base.__init__(self, home)

    def run(self) -> None:
        try:
            checking_init(self.HOME)
            with ThreadPoolExecutor(max_workers=2) as executor:
                executor.submit(
                    loading,
                    set_time=0.100,
                    bar=False,
                    header="Synchronizing versions with database ...",
                    foreground=FG().QUESTION,
                )
                executor.submit(records, action="update")
            self.log.record("Database update.", colorize=True, level="info")
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
