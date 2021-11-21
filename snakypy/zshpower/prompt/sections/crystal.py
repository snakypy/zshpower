from subprocess import run
from typing import Union

from snakypy.zshpower.config.base import Base
from snakypy.zshpower.prompt.sections.utils import Version


class Crystal(Version, Base):
    def __init__(self):
        super(Crystal, self).__init__()
        self.extensions = (".cr",)
        self.files = ("shard.yml",)

    def get_version(
        self, config, reg_version, key="crystal", ext="cr-", space_elem=" "
    ) -> Union[str, bool]:
        return super().get(config, reg_version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, exec_="crystal", key="crystal", action=None) -> bool:
        command = run("crystal version", capture_output=True, shell=True, text=True)
        version = command.stdout.split()[1]
        return super().set(command, version, exec_, key, action)
