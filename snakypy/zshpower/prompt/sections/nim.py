from subprocess import run

from snakypy.zshpower.config.base import Base
from snakypy.zshpower.prompt.sections.utils import Version


class Nim(Version, Base):
    def __init__(self):
        super(Nim, self).__init__()
        self.extensions = (".nim", ".nims", ".nimble")
        self.files = ("nim.cfg",)

    def get_version(
        self, config, reg_version, key="nim", ext="nim-", space_elem=" "
    ) -> str:
        return super().get(config, reg_version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, exec_="nim", key="nim", action=None):
        command = run(
            "nim --version | awk '/Version/'",
            capture_output=True,
            shell=True,
            text=True,
        )
        version = command.stdout.split()[-3]
        return super().set(command, version, exec_, key, action)
