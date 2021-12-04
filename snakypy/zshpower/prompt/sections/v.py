from subprocess import run

from snakypy.zshpower.config.base import Base
from snakypy.zshpower.prompt.sections.utils import Version


class V(Version, Base):
    def __init__(self, *args):
        super(V, self).__init__()
        self.args: tuple = args
        self.key = "v"
        self.app_executable = "v"
        self.shorten = "v-"
        self.extensions = (".v",)
        self.files = ("v.mod", "vpkg.json", ".vpkg-lock.json")

    def get_version(self, space_elem: str = " ") -> str:
        # args[0]: dict = config file (toml)
        # args[1]: dict = database registers
        return super().get(
            self.args[0], self.args[1], self.key, self.shorten, space_elem=space_elem
        )

    def set_version(self, action: str = "") -> bool:
        command = run(
            f"{self.app_executable} -v", capture_output=True, shell=True, text=True
        )
        version = command.stdout.split()[1]
        return super().set(
            command, version, self.app_executable, self.key, action=action
        )

    def __str__(self):
        return self.get_version()
