from subprocess import run

from snakypy.zshpower.config.base import Base
from snakypy.zshpower.prompt.sections.utils import Version


class CMake(Version, Base):
    def __init__(self):
        super(CMake, self).__init__()
        self.files = ("CMakeLists.txt", "CMakeCache.txt")

    def get_version(self, config, version, key="cmake", ext="cm-", space_elem=" "):
        return super().get(config, version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, exec_="cmake", key="cmake", action=None):
        command = run("cmake --version", capture_output=True, shell=True, text=True)
        version = command.stdout.split()[2]
        return super().set(command, version, exec_, key, action)
