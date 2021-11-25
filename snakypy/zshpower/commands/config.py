from pydoc import pager

from snakypy.helpers.files import read_file

from snakypy.zshpower.config.base import Base
from snakypy.zshpower.utils.check import checking_init
from snakypy.zshpower.utils.process import open_file_with_editor


class ConfigCommand(Base):
    def __init__(self, home):
        Base.__init__(self, home)

    def run(self, arguments) -> bool:
        checking_init(self.HOME, self.logfile)

        if arguments["--open"]:
            open_file_with_editor(self.config_file)
        elif arguments["--view"]:
            read_config = read_file(self.config_file)
            pager(read_config)
            return True
        return False
