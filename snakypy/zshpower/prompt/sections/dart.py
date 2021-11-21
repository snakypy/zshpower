from subprocess import run

from snakypy.zshpower.config.base import Base
from snakypy.zshpower.prompt.sections.utils import Version


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

    def set_version(self, exec_="dart", key="dart", action=None) -> bool:
        # The parameter 2>&1 is for the command to insert output to stdout, as some output to stderr.
        command = run("dart --version 2>&1", capture_output=True, shell=True, text=True)
        version = command.stdout.replace("\n", "").split(" ")[3]
        return super().set(command, version, exec_, key, action)
