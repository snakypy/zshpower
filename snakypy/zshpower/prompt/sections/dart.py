from subprocess import run

from snakypy.zshpower.prompt.sections.utils import Version
from snakypy.zshpower.config.base import Base


class Dart(Version, Base):
    def __init__(self):
        super(Dart, self).__init__()
        self.extensions = (".dart",)
        self.files = (
            "pubspec.yaml",
            "config.src.yaml",
            "analysis_options.yaml",
        )

    def get_version(
        self, config, reg_version, key="dart", ext="dt-", space_elem=" "
    ) -> str:
        return super().get(config, reg_version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, key="dart", action=None) -> bool:
        version = run("dart --version 2>&1", capture_output=True, shell=True, text=True)

        if not version.returncode == 0:
            self.log.record(version.stderr, colorize=True, level="error")
            return False

        version_format = version.stdout.replace("\n", "").split(" ")[3]

        self.log.record(
            f"Dart {version_format} registered in the database!",
            colorize=True,
            level="info",
        )

        return super().set(version_format, key, action)
