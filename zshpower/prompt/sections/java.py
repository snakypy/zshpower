from subprocess import run
from zshpower.prompt.sections.lib.utils import Version


class Java(Version):
    def __init__(self):
        super(Java, self).__init__()
        self.extensions = (".java",)

    def get_version(
        self, config, reg_version, key="java", ext="java-", space_elem=" "
    ) -> str:
        return super().get(config, reg_version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, key="java", action=None) -> bool:
        version = run(
            """java -version 2>&1 | awk -F '"' '/version/ {print $2}'""",
            capture_output=True,
            shell=True,
            text=True,
        )

        if version.stdout.replace("\n", ""):
            version_format = version.stdout.replace("\n", "").split("_")[0]
            return super().set(version_format, key, action)

        return False
