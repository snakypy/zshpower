from zshpower.config.base import Base
from subprocess import call as subprocess_call
from os import environ
from shutil import which as shutil_which
from zshpower.utils.check import checking_init
from snakypy.file import read as snakypy_file_read
from tomlkit import parse as toml_parse
from snakypy.file import read as snakypy_file_red
from pydoc import pager as pydoc_pager


def editor_run(editor, config) -> bool:
    if shutil_which(editor):
        get_editor = environ.get("EDITOR", editor)
        with open(config) as f:
            subprocess_call([get_editor, f.name])
            return True
    return False


class ConfigCommand(Base):
    def __init__(self, home):
        Base.__init__(self, home)

    def run(self, arguments) -> bool:
        checking_init(self.HOME)

        if arguments["--open"]:
            try:
                read_conf = snakypy_file_red(self.config_file)
                parsed = toml_parse(read_conf)
                editor_conf = parsed["general"]["config"]["editor"]
                if editor_conf:
                    editor_run(editor_conf, self.config_file)
                else:
                    editors = ("vim", "nano", "emacs", "micro")
                    for edt in editors:
                        editor_run(edt, self.config_file)
            except FileNotFoundError:
                raise FileNotFoundError("File not found.")
        elif arguments["--view"]:
            read_config = snakypy_file_read(self.config_file)
            pydoc_pager(read_config)
            return True
        return False
