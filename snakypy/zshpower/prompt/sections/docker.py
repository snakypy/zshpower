from subprocess import run
from typing import Union

from snakypy.zshpower.prompt.sections.utils import Version


class Docker(Version):
    def __init__(self):
        super(Docker, self).__init__()
        self.files = ("Dockerfile", "docker-compose.yml")

    def get_version(
        self, config, reg_version, key="docker", ext="dkr-", space_elem=" "
    ) -> Union[str, bool]:
        return super().get(config, reg_version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, key="docker", action=None) -> bool:
        version = run(
            "docker version",
            capture_output=True,
            text=True,
            shell=True,
        )

        if version.returncode != 127 and version.returncode != 1:
            version_format = (
                version.stdout.split("Version")[1]
                .strip()
                .split("\n")[0]
                .replace(":", "")
                .strip()
            )
            return super().set(version_format, key, action)

        return False
