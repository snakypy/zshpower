from subprocess import run

from snakypy.zshpower.prompt.sections.utils import Version
from snakypy.zshpower.config.base import Base


class CMake(Version, Base):
    def __init__(self):
        super(CMake, self).__init__()
        self.files = ("CMakeLists.txt", "CMakeCache.txt")

    def get_version(self, config, version, key="cmake", ext="cm-", space_elem=" "):
        return super().get(config, version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, key="cmake", action=None):
        version = run(
            "cmake --version 2>&1", capture_output=True, shell=True, text=True
        )
        if not version.returncode == 0:
            self.log.record(version.stderr, colorize=True, level="error")
            return False

        version = version.stdout.split()[2]
        self.log.record(
            f"CMake {version} registered in the database!", colorize=True, level="info"
        )

        return super().set(version, key, action)
