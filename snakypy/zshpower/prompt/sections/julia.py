from subprocess import run

from snakypy.zshpower.config.base import Base
from snakypy.zshpower.prompt.sections.utils import Version


class Julia(Version, Base):
    def __init__(self):
        super(Julia, self).__init__()
        self.extensions = (".jl",)

    def get_version(
        self, config, reg_version, key="julia", ext="jl-", space_elem=" "
    ) -> str:
        return super().get(config, reg_version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, exec_="julia", key="julia", action=None):
        command = run("julia --version", capture_output=True, shell=True, text=True)
        version = command.stdout.replace("\n", "").split(" ")[2]
        return super().set(command, version, exec_, key, action)
