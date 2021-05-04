from subprocess import run
from zshpower.prompt.sections.lib.utils import Version


class Kotlin(Version):
    def __init__(self):
        super(Kotlin, self).__init__()
        self.extensions = (".kt", ".kts")

    def get_version(self, config, version, key="kotlin", ext="kt-", space_elem=" "):
        return super().get(config, version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, key="kotlin", action=None):
        version = run(
            "kotlin -version 2>&1", capture_output=True, shell=True, text=True
        )

        if version.returncode != 127 and version.returncode != 1:
            version = version.stdout.split()[2].split("-")[0]
            return super().set(version, key, action)

        return False
