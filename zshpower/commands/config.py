from pydoc import pager as pydoc_pager
from shutil import which as shutil_which
from zshpower.config.base import Base
from os import environ
from subprocess import call as subprocess_call
from snakypy.file import read as snakypy_file_read
from zshpower.utils.check import checking_init


class ConfigCommand(Base):
    def __init__(self, home):
        Base.__init__(self, home)

    def main(self, arguments):

        checking_init(self.themes_folder)

        if arguments["--open"]:
            editors = ("vim", "nano", "emacs")
            for editor in editors:
                if shutil_which(editor):
                    get_editor = environ.get("EDITOR", editor)
                    with open(self.config) as f:
                        subprocess_call([get_editor, f.name])
                    return True
        elif arguments["--view"]:
            read_config = snakypy_file_read(self.config)
            pydoc_pager(read_config)
            return True
