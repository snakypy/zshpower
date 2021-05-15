from subprocess import run
from snakypy.zshpower.prompt.sections.lib.utils import Version


class Kotlin(Version):
    def __init__(self):
        super(Kotlin, self).__init__()
        self.extensions = (".kt", ".kts")

    def get_version(
        self, config, reg_version, key="kotlin", ext="kt-", space_elem=" "
    ) -> str:
        return super().get(config, reg_version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, key="kotlin", action=None) -> bool:
        version = run(
            "kotlin -version 2>&1", capture_output=True, shell=True, text=True
        )

        if version.returncode != 127 and version.returncode != 1:
            version_format = version.stdout.split()[2].split("-")[0]
            return super().set(version_format, key, action)

        return False
