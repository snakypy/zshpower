from subprocess import run

from snakypy.zshpower.config.base import Base
from snakypy.zshpower.prompt.sections.utils import Version


class Kotlin(Version, Base):
    def __init__(self):
        super(Kotlin, self).__init__()
        self.extensions = (".kt", ".kts")

    def get_version(
        self, config, reg_version, key="kotlin", ext="kt-", space_elem=" "
    ) -> str:
        return super().get(config, reg_version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, exec_="kotlin", key="kotlin", action=None):
        command = run("kotlin -version", capture_output=True, shell=True, text=True)
        version = command.stdout.split()[2].split("-")[0]
        return super().set(command, version, exec_, key, action)
