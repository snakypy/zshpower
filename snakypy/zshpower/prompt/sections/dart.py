from subprocess import run

from snakypy.zshpower.config.base import Base
from snakypy.zshpower.prompt.sections.utils import Version


class Dart(Version, Base):
    def __init__(self, *args):
        super(Dart, self).__init__()
        self.args: tuple = args
        self.key = "dart"
        self.app_executable = "dart"
        self.shorten = "dt-"
        self.finder = {
            "extensions": [".dart"],
            "folders": [],
            "files": ["pubspec.yaml", "config.src.yaml", "analysis_options.yaml"],
        }

    def get_version(self, space_elem: str = " ") -> str:
        return super().get(
            self.args[0], self.args[1], self.key, self.shorten, space_elem=space_elem
        )

    def set_version(self, action: str = "") -> bool:
        command = run("dart --version 2>&1", capture_output=True, shell=True, text=True)
        version = command.stdout.replace("\n", "").split(" ")[3]
        return super().set(
            command, version, self.app_executable, self.key, action=action
        )

    def __str__(self):
        return self.get_version()
