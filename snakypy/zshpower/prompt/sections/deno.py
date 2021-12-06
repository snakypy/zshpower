from subprocess import run

from snakypy.zshpower.config.base import Base
from snakypy.zshpower.prompt.sections.utils import Version


class Deno(Version, Base):
    def __init__(self, *args):
        super(Deno, self).__init__()
        self.args: tuple = args
        self.key = "deno"
        self.app_executable = "deno"
        self.shorten = "deno-"
        self.finder = {
            "extensions": [".dart"],
            "folders": [],
            "files": ["mod.ts", "deps.ts", "mod.js", "deps.js"],
        }

    def get_version(self, space_elem: str = " ") -> str:
        return super().get(
            self.args[0], self.args[1], self.key, self.shorten, space_elem=space_elem
        )

    def set_version(self, action: str = "") -> bool:
        command = run("deno -V", capture_output=True, shell=True, text=True)
        version = command.stdout.split()[1]
        return super().set(
            command, version, self.app_executable, self.key, action=action
        )

    def __str__(self):
        return self.get_version()
