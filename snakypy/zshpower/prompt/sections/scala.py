from subprocess import run

from snakypy.zshpower.config.base import Base
from snakypy.zshpower.prompt.sections.utils import Version


class Scala(Version, Base):
    def __init__(self):
        super(Scala, self).__init__()
        self.extensions = (".scala", ".sc")
        self.files = ("build.sbt",)

    def get_version(
        self, config, reg_version, key="scala", ext="sc-", space_elem=" "
    ) -> str:
        return super().get(config, reg_version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, exec_="scala", key="scala", action=None):
        # The parameter 2>&1 is for the command to insert output to stdout, as some output to stderr.
        command = run(
            "scala --version 2>&1", capture_output=True, shell=True, text=True
        )
        version = command.stdout.split("-")[0].split()[4]
        return super().set(command, version, exec_, key, action)
