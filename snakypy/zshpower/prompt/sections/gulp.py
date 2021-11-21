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
    def __init__(self):
        super(Gulp, self).__init__()
        self.files = ("gulpfile.js", "gulpfile.babel.js")
        self.folders = ("node_modules",)

    def get_version(
        self, config, reg_version, key="gulp", ext="gulp-", space_elem=" "
    ) -> str:
        version_local = "node_modules/gulp/package.json"
        enable = get_key(config, key, "version", "enable")
        symbol = symbol_ssh(get_key(config, key, "symbol"), ext)
        color = get_key(config, key, "color")
        prefix_color = get_key(config, key, "prefix", "color")
        prefix_text = element_spacing(get_key(config, key, "prefix", "text"))
        micro_version_enable = get_key(config, key, "version", "micro", "enable")

        if enable and verify_objects(
            getcwd(),
            files=self.files,
            folders=self.folders,
            extension=self.extensions,
        ):
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
                            f"{separator(config)}{prefix}"
                            f"{Color(color)}{symbol}"
                            f"Local {version_format}{Color().NONE}"
                        )
                    )
            else:
                return super().get(
                    config, reg_version, key=key, ext=ext, space_elem=space_elem
                )
        return ""

    def set_version(self, exec_="gulp", key="gulp", action=None) -> bool:
        command = run("gulp --version", capture_output=True, shell=True, text=True)
        version = command.stdout.split()[2]
        return super().set(command, version, exec_, key, action)
