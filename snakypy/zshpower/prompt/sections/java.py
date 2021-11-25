from subprocess import run

from snakypy.zshpower.config.base import Base
from snakypy.zshpower.prompt.sections.utils import Version


class Java(Version, Base):
    def __init__(self):
        super(Java, self).__init__()
        self.extensions = (".java",)

    def get_version(
        self, config, reg_version, key="java", ext="java-", space_elem=" "
    ) -> str:
        return super().get(config, reg_version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, exec_="java", key="java", action=None) -> bool:
        command = run(
            """java -version 2>&1 | awk -F '"' '/version/ {print $2}'""",
            capture_output=True,
            shell=True,
            text=True,
        )
        version = command.stdout.replace("\n", "").split("_")[0]
        return super().set(command, version, exec_, key, action)
