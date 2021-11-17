from subprocess import run
from typing import Union

from snakypy.zshpower.prompt.sections.utils import Version
from snakypy.zshpower.config.base import Base


class Docker(Version, Base):
    def __init__(self):
        super(Docker, self).__init__()
        self.files = ("Dockerfile", "docker-compose.yml")

    def get_version(
        self, config, reg_version, key="docker", ext="dkr-", space_elem=" "
    ) -> Union[str, bool]:
        return super().get(config, reg_version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, key="docker", action=None) -> bool:
        version = run(
            "docker --version",
            capture_output=True,
            text=True,
            shell=True,
        )

        version_format = version.stdout.split()[2].replace(",", "")

        if version.returncode != 0:
            self.log.record(version.stderr, colorize=True, level="error")
        elif version.returncode == 0:
            self.log.record(
                f"Docker {version_format} registered in the database!",
                colorize=True,
                level="info",
            )
            return super().set(version_format, key, action)
        return False
