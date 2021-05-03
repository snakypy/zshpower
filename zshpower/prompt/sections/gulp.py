from os import getcwd
from subprocess import run
from zshpower.utils.catch import find_objects
from zshpower.prompt.sections.lib.utils import (
    Version,
    symbol_ssh,
    element_spacing,
    Color,
    separator,
)


class Gulp(Version):
    def __init__(self):
        super(Gulp, self).__init__()
        self.files = ("gulpfile.js",)

    def get_version(self, config, key="gulp", ext="gulp-", space_elem=" "):
        symbol = symbol_ssh(config[key]["symbol"], ext)
        color = config[key]["color"]
        prefix_color = config[key]["prefix"]["color"]
        prefix_text = element_spacing(config[key]["prefix"]["text"])
        micro_version_enable = config[key]["version"]["micro"]["enable"]

        version = run("gulp --version", capture_output=True, shell=True, text=True)

        if not version.returncode == 0:
            return False

        if version.stdout and find_objects(
            getcwd(),
            files=self.files,
            folders=self.folders,
            extension=self.extensions,
        ):
            prefix = f"{Color(prefix_color)}{prefix_text}{Color().NONE}"

            version = version.stdout.split()

            if not version[-1] == "Unknown":
                version = version[-1]
            else:
                version = version[2]

            if micro_version_enable:
                version_format = (
                    f"{'{0[0]}.{0[1]}.{0[2]}'.format(version.split('.'))}{space_elem}"
                )
            else:
                version_format = (
                    f"{'{0[0]}.{0[1]}'.format(version.split('.'))}{space_elem}"
                )

            return str(
                (
                    f"{separator(config)}{prefix}"
                    f"{Color(color)}{symbol}"
                    f"{version_format}{Color().NONE}"
                )
            )
        return ""
