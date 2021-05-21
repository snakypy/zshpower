from subprocess import run
from snakypy.zshpower.prompt.sections.utils import Version


class Zig(Version):
    def __init__(self):
        super(Zig, self).__init__()
        self.extensions = (".zig",)

    def get_version(
        self, config, reg_version, key="zig", ext="zig-", space_elem=" "
    ) -> str:
        return super().get(config, reg_version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, key="zig", action=None) -> bool:
        version = run("zig version 2>&1", capture_output=True, shell=True, text=True)

        if version.returncode != 127 and version.returncode != 1:
            version_format = version.stdout.replace("\n", "")

            return super().set(version_format, key, action)

        return False
