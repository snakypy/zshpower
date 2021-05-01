from subprocess import run
from zshpower.prompt.sections.lib.utils import Version


class Zig(Version):
    def __init__(self):
        super(Zig, self).__init__()
        self.extensions = (".zig",)

    def get_version(self, config, version, key="zig", ext="zig-", space_elem=" "):
        return super().get(config, version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, key="zig", action=None):
        version = run("zig version 2>&1", capture_output=True, shell=True, text=True)

        if not version.returncode == 0:
            return False

        version = version.stdout.replace("\n", "")

        return super().set(version, key, action)
