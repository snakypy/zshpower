from os import getcwd
from os.path import join, isfile
from subprocess import run
from snakypy.helpers.files import read_json
from snakypy.zshpower.prompt.sections.utils import (
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
        self.folders = ("node_modules",)

    def get_version(
        self, config, reg_version, key="gulp", ext="gulp-", space_elem=" "
    ) -> str:
        version_local = "node_modules/gulp/package.json"
        enable = config[key]["version"]["enable"]
        symbol = symbol_ssh(config[key]["symbol"], ext)
        color = config[key]["color"]
        prefix_color = config[key]["prefix"]["color"]
        prefix_text = element_spacing(config[key]["prefix"]["text"])
        micro_version_enable = config[key]["version"]["micro"]["enable"]

        if enable and isfile(join(getcwd(), self.files[0])):
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

    def set_version(self, key="gulp", action=None) -> bool:
        version = run("gulp --version", capture_output=True, shell=True, text=True)

        if version.returncode != 127 and version.returncode != 1:
            version_format = version.stdout.split()[2]
            return super().set(f"CLI {version_format}", key, action)

        return False
