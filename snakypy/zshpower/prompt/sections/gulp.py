from os import getcwd
from os.path import isfile, join
from subprocess import run

from snakypy.helpers.files import read_json

from snakypy.zshpower.config.base import Base
from snakypy.zshpower.prompt.sections.utils import (
    Color,
    Version,
    element_spacing,
    separator,
    symbol_ssh,
)
from snakypy.zshpower.utils.catch import get_key, verify_objects


class Gulp(Version, Base):
    def __init__(self, *args):
        super(Gulp, self).__init__()
        self.args: tuple = args
        self.finder = {
            "extensions": [],
            "folders": [],
            "files": ["gulpfile.js", "gulpfile.babel.js"],
        }
        self.key = "gulp"
        self.app_executable = "gulp"
        self.shorten = "gulp-"

    def get_version(self, space_elem: str = " ") -> str:
        # args[0]: dict = config file (toml)
        # args[1]: dict = database registers
        version_local = "node_modules/gulp/package.json"
        enable = get_key(self.args[0], self.key, "version", "enable")
        symbol = symbol_ssh(get_key(self.args[0], self.key, "symbol"), self.shorten)
        color = get_key(self.args[0], self.key, "color")
        prefix_color = get_key(self.args[0], self.key, "prefix", "color")
        prefix_text = element_spacing(get_key(self.args[0], self.key, "prefix", "text"))
        micro_version_enable = get_key(
            self.args[0], self.key, "version", "micro", "enable"
        )

        if enable and verify_objects(getcwd(), data=self.finder) is True:
            prefix = f"{Color(prefix_color)}{prefix_text}{Color().NONE}"
            if isfile(join(getcwd(), version_local)):
                parsed = read_json(join(getcwd(), version_local))
                if "version" in parsed:
                    version_ = parsed["version"]

                    if micro_version_enable:
                        version_format = f"{'{0[0]}.{0[1]}.{0[2]}'.format(version_.split('.'))}{space_elem}"
                    else:
                        version_format = (
                            f"{'{0[0]}.{0[1]}'.format(version_.split('.'))}{space_elem}"
                        )

                    return str(
                        (
                            f"{separator(self.args[0])}{prefix}"
                            f"{Color(color)}{symbol}"
                            f"Local {version_format}{Color().NONE}"
                        )
                    )
            else:
                return super().get(
                    self.args[0],
                    self.args[1],
                    self.key,
                    self.shorten,
                    space_elem=space_elem,
                )
        return ""

    def set_version(self, action: str = "") -> bool:
        command = run("gulp --version", capture_output=True, shell=True, text=True)
        version = command.stdout.split()[2]
        return super().set(command, version, self.app_executable, self.key, action)

    def __str__(self):
        return self.get_version()
