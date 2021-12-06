from subprocess import run

from snakypy.zshpower.config.base import Base
from snakypy.zshpower.prompt.sections.utils import Version


class Php(Version, Base):
    def __init__(self, *args):
        super(Php, self).__init__()
        self.args: tuple = args
        self.key = "php"
        self.app_executable = "php"
        self.shorten = "php-"
        self.finder = {
            "extensions": [".php"],
            "folders": [],
            "files": ["composer.json"],
        }

    def get_version(self, space_elem: str = " ") -> str:
        return super().get(
            self.args[0], self.args[1], self.key, self.shorten, space_elem=space_elem
        )

    def set_version(self, action: str = "") -> bool:
        command = run(
            f"""{self.app_executable} -v 2>&1 | grep "^PHP\\s*[0-9.]\\+" | awk '{{print $2}}'""",
            capture_output=True,
            shell=True,
            text=True,
        )
        version = command.stdout.replace("\n", "")
        return super().set(
            command, version, self.app_executable, self.key, action=action
        )

    def __str__(self):
        return self.get_version()
