from subprocess import run
from zshpower.prompt.sections.lib.utils import Version


class Nim(Version):
    def __init__(self):
        super(Nim, self).__init__()
        self.extensions = (".nim", ".nims", ".nimble")
        self.files = ("nim.cfg",)

    def get_version(self, config, version, key="nim", ext="nim-", space_elem=" "):
        return super().get(config, version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, key="nim", action=None):
        version = run("nim --version | awk '/Version/' 2>&1", capture_output=True, shell=True, text=True)

        if not version.returncode == 0:
            return False

        version = version.stdout.split()[-3]

        return super().set(version, key, action)
