from subprocess import run
from typing import Union

from snakypy.zshpower.prompt.sections.utils import Version
from snakypy.zshpower.config.base import Base


class Crystal(Version, Base):
    def __init__(self):
        super(Crystal, self).__init__()
        self.extensions = (".cr",)
        self.files = ("shard.yml",)

    def get_version(
        self, config, reg_version, key="crystal", ext="cr-", space_elem=" "
    ) -> Union[str, bool]:
        return super().get(config, reg_version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, key="crystal", action=None) -> bool:
        version = run(
            "crystal version 2>&1", capture_output=True, shell=True, text=True
        )

        if version.returncode != 0:
            self.log.record(version.stderr, colorize=True, level="error")
        elif version.returncode == 0:
            version_format = version.stdout.split()[1]
            self.log.record(
                f"Crystal {version_format} registered in the database!",
                colorize=True,
                level="info",
            )
            return super().set(version_format, key, action)

        return False
