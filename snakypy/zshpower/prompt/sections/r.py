from subprocess import run

from snakypy.zshpower.config.base import Base
from snakypy.zshpower.prompt.sections.utils import Version


class R(Version, Base):
    def __init__(self, *args):
        super(R, self).__init__()
        self.args: tuple = args
        self.key = "r"
        self.app_executable = "Rscript"
        self.shorten = "r-"
        self.finder = {"extensions": [".r", ".R"], "folders": [], "files": []}

    def get_version(self, space_elem: str = " ") -> str:
        # args[0]: dict = config file (toml)
        # args[1]: dict = database registers
        return super().get(
            self.args[0],
            self.args[1],
            self.key,
            self.shorten,
            space_elem=space_elem,
            not_split=True,
        )

    def set_version(self, action: str = "") -> bool:
        command = run(
            f"{self.app_executable} --version 2>&1",
            capture_output=True,
            shell=True,
            text=True,
        )
        version = command.stdout.strip().replace("\n", "").split(" ")[-2]
        return super().set(
            command, version, self.app_executable, self.key, action=action
        )

    def __str__(self):
        return self.get_version()
