from subprocess import run

from snakypy.zshpower.config.base import Base
from snakypy.zshpower.prompt.sections.utils import Version


class Cpp(Version, Base):
    def __init__(self, *args):
        super(Cpp, self).__init__()
        self.args: tuple = args
        self.key = "cpp"
        self.app_executable = "g++"
        self.shorten = "cpp-"
        self.finder = {"extensions": [".cpp"], "folders": [], "files": []}

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
        # https://stackoverflow.com/questions/36662063/how-can-i-know-the-version-of-c
        command = run(
            f"""{self.app_executable} -dM -E - < /dev/null | grep __STDC_VERSION__ | awk '{{ print $3 }}'""",
            capture_output=True,
            shell=True,
            text=True,
        )
        version = command.stdout.strip().replace("\n", "")
        return super().set(
            command, version, self.app_executable, self.key, action=action
        )

    def __str__(self):
        return self.get_version()
