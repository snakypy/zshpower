from contextlib import suppress
from os import getcwd
from os.path import join

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


class Ember(Version, Base):
    def __init__(self, *args):
        super(Ember, self).__init__()
        self.args: tuple = args
        self.key = "ember"
        self.shorten = "ember-"
        self.finder = {
            "extensions": [],
            "folders": ("node_modules",),
            "files": [
                join("node_modules", "ember-cli", "package.json"),
                "ember-cli-build.js",
            ],
        }

    def get_version(self, space_elem: str = " "):
        enable = get_key(self.args[0], self.key, "version", "enable")
        symbol = symbol_ssh(get_key(self.args[0], self.key, "symbol"), self.shorten)
        color = (
            get_key(self.args[0], self.key, "color")
            if get_key(self.args[0], "general", "color", "enable") is True
            else "negative"
        )
        prefix_color = get_key(self.args[0], self.key, "prefix", "color")
        prefix_text = element_spacing(get_key(self.args[0], self.key, "prefix", "text"))
        micro_version_enable = get_key(
            self.args[0], self.key, "version", "micro", "enable"
        )

        if enable is True and verify_objects(getcwd(), data=self.finder) is True:
            with suppress(FileNotFoundError):
                parsed = read_json(self.finder["files"][0])
                if "version" not in parsed:
                    return ""
                version = f"{parsed['version']}{space_elem}"

                # # Using subprocess
                # command = run(
                #     f"""grep '"version":' {self.files[1]} | cut -d\\" -f4""",
                #     capture_output=True,
                #     shell=True,
                #     text=True,
                # )
                # version = command.stdout.replace("\n", "").strip()

                version = version.replace("\n", "").strip()

                prefix = f"{Color(prefix_color)}{prefix_text}{Color().NONE}"

                if micro_version_enable is True:
                    version = f"{'{0[0]}.{0[1]}.{0[2]}'.format(version.split('.'))}"
                else:
                    version = f"{'{0[0]}.{0[1]}'.format(version.split('.'))}"

                return str(
                    (
                        f"{separator(self.args[0])}{prefix}"
                        f"{Color(color)}{symbol}"
                        f"{version}{space_elem}{Color().NONE}"
                    )
                )
        return ""

    def __str__(self):
        return self.get_version()
