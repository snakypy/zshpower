from subprocess import run

from snakypy.helpers.catches.finders import is_tool

from snakypy.zshpower.prompt.sections.utils import Version
from snakypy.zshpower.config.base import Base


class CMake(Version, Base):
    def __init__(self):
        super(CMake, self).__init__()
        self.files = ("CMakeLists.txt", "CMakeCache.txt")

    def get_version(self, config, version, key="cmake", ext="cm-", space_elem=" "):
        return super().get(config, version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, exec="cmake", key="cmake", action=None):
        command = run("cmake --version", capture_output=True, shell=True, text=True)
        version = command.stdout.split()[2]
        return super().set(command, version, exec, key, action)

        # TODO: [DEPRECATED]
        # if is_tool(key):
        #     version = run("cmake --version", capture_output=True, shell=True, text=True)

        #     if version.returncode != 0:
        #         self.log.record(
        #             f"CMake version not registered: {version.stderr}",
        #             colorize=True,
        #             level="error",
        #         )
        #     elif version.returncode == 0:
        #         version_format = version.stdout.split()[2]
        #         self.log.record(
        #             f"CMake {version_format} registered in the database!",
        #             colorize=True,
        #             level="info",
        #         )
        #         return super().set(version_format, key, action)
