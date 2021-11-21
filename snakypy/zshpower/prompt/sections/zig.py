from subprocess import run

from snakypy.zshpower.config.base import Base
from snakypy.zshpower.prompt.sections.utils import Version


class Zig(Version, Base):
    def __init__(self):
        super(Zig, self).__init__()
        self.extensions = (".zig",)

    def get_version(
        self, config, reg_version, key="zig", ext="zig-", space_elem=" "
    ) -> str:
        return super().get(config, reg_version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, exec_="zig", key="zig", action=None):
        command = run("zig version", capture_output=True, shell=True, text=True)
        version = command.stdout.replace("\n", "")
        return super().set(command, version, exec_, key, action)
