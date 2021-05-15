from subprocess import run
from snakypy.zshpower.prompt.sections.lib.utils import Version


class Nim(Version):
    def __init__(self):
        super(Nim, self).__init__()
        self.extensions = (".nim", ".nims", ".nimble")
        self.files = ("nim.cfg",)

    def get_version(
        self, config, reg_version, key="nim", ext="nim-", space_elem=" "
    ) -> str:
        return super().get(config, reg_version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, key="nim", action=None) -> bool:
        version = run(
            "nim --version | awk '/Version/' 2>&1",
            capture_output=True,
            shell=True,
            text=True,
        )

        if version.returncode != 127 and version.returncode != 1:
            version_format = version.stdout.split()[-3]
            return super().set(version_format, key, action)

        return False
