from os import environ
from pydoc import pager as pydoc_pager
from shutil import which as shutil_which
from subprocess import call as subprocess_call

from snakypy.helpers.files import read_file
from tomlkit import parse as toml_parse

from snakypy.zshpower.config.base import Base
from snakypy.zshpower.utils.check import checking_init


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
                read_conf = read_file(self.config_file)
                parsed = dict(toml_parse(read_conf))
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
            read_config = read_file(self.config_file)
            pydoc_pager(read_config)
            return True
        return False
