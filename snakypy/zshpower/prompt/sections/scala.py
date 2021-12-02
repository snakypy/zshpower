from subprocess import run

from snakypy.zshpower.config.base import Base
from snakypy.zshpower.prompt.sections.utils import Version


class Scala(Version, Base):
    def __init__(self, *args):
        super(Scala, self).__init__()
        self.args: tuple = args
        self.key = "scala"
        self.app_executable = "scala"
        self.shorten = "sc-"
        self.extensions = (".scala", ".sc")
        self.files = ("build.sbt",)

    def get_version(self, space_elem: str = " ") -> str:
        return super().get(
            self.args[0], self.args[1], self.key, self.shorten, space_elem=space_elem
        )

    def set_version(self, action: str = "") -> bool:
        command = run(
            f"{self.app_executable} --version 2>&1",
            capture_output=True,
            shell=True,
            text=True,
        )
        version = command.stdout.split("-")[0].split()[4]
        return super().set(
            command, version, self.app_executable, self.key, action=action
        )

    def __str__(self):
        return self.get_version()
