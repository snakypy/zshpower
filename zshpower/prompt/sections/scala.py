from subprocess import run
from zshpower.prompt.sections.lib.utils import Version


class Scala(Version):
    def __init__(self):
        super(Scala, self).__init__()
        self.extensions = (".scala", ".sc")
        self.files = ("build.sbt",)

    def get_version(self, config, version, key="scala", ext="sc-", space_elem=" "):
        return super().get(config, version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, key="scala", action=None):
        version = run(
            "scala -version 2>&1",
            capture_output=True,
            text=True,
            shell=True,
        )

        if version.returncode != 127 and version.returncode != 1:
            version = version.stdout.split("-")[0].split()[4]
            return super().set(version, key, action)

        return False
