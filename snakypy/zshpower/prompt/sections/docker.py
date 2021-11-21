from subprocess import run
from typing import Union

from snakypy.zshpower.config.base import Base
from snakypy.zshpower.prompt.sections.utils import Version


class Docker(Version, Base):
    def __init__(self):
        super(Docker, self).__init__()
        self.files = ("Dockerfile", "docker-compose.yml")

    def get_version(
        self, config, reg_version, key="docker", ext="dkr-", space_elem=" "
    ) -> Union[str, bool]:
        return super().get(config, reg_version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, exec_="docker", key="docker", action=None) -> bool:
        command = run("docker --version", capture_output=True, shell=True, text=True)
        version = command.stdout.split()[2].replace(",", "")
        return super().set(command, version, exec_, key, action)
