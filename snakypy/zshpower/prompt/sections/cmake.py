from subprocess import run
from snakypy.zshpower.prompt.sections.lib.utils import Version


class CMake(Version):
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
            return False

        version = version.stdout.split()[2]

        return super().set(version, key, action)
