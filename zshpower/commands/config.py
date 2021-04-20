from pydoc import pager as pydoc_pager
from shutil import which as shutil_which
from zshpower.config.base import Base
from snakypy.file import read as snakypy_file_red
from tomlkit import parse as toml_parse
from os import environ
from subprocess import call as subprocess_call
from snakypy.file import read as snakypy_file_read
from zshpower.utils.check import checking_init


def editor_run(editor, config):
    if shutil_which(editor):
        get_editor = environ.get("EDITOR", editor)
        with open(config) as f:
            subprocess_call([get_editor, f.name])
            exit(0)
    return


class ConfigCommand(Base):
    def __init__(self, home):
        Base.__init__(self, home)

    def main(self, arguments):

        checking_init(self.HOME)

        if arguments["--open"]:
            try:
                read_conf = snakypy_file_red(self.config_file)
                parsed = toml_parse(read_conf)
                editor_conf = parsed["general"]["config"]["editor"]
            except (FileNotFoundError, Exception):
                editor_conf = None

            if editor_conf:
                editor_run(editor_conf, self.config_file)
            else:
                editors = ("vim", "nano", "emacs", "micro")
                for edt in editors:
                    editor_run(edt, self.config_file)
        elif arguments["--view"]:
            read_config = snakypy_file_read(self.config_file)
            pydoc_pager(read_config)
            return True
