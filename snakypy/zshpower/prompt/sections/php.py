from subprocess import run

from snakypy.zshpower.config.base import Base
from snakypy.zshpower.prompt.sections.utils import Version


class Php(Version, Base):
    def __init__(self):
        super(Php, self).__init__()
        self.files = ("composer.json",)
        self.extensions = (".php",)

    def get_version(
        self, config, reg_version, key="php", ext="php-", space_elem=" "
    ) -> str:
        return super().get(config, reg_version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, exec_="php", key="php", action=None):
        command = run(
            """php -v 2>&1 | grep "^PHP\\s*[0-9.]\\+" | awk '{print $2}'""",
            capture_output=True,
            shell=True,
            text=True,
        )
        version = command.stdout.replace("\n", "")
        return super().set(command, version, exec_, key, action)
