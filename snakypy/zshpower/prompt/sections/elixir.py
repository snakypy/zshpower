from subprocess import run

from snakypy.zshpower.config.base import Base
from snakypy.zshpower.prompt.sections.utils import Version


class Elixir(Version, Base):
    def __init__(self, *args):
        super(Elixir, self).__init__()
        self.args: tuple = args
        self.key = "elixir"
        self.app_executable = "elixir"
        self.shorten = "ex-"
        self.finder = {"extensions": [".ex"], "folders": [], "files": ["mix.exs"]}

    def get_version(self, space_elem: str = " ") -> str:
        # args[0]: dict = config file (toml)
        # args[1]: dict = database registers
        return super().get(
            self.args[0], self.args[1], self.key, self.shorten, space_elem=space_elem
        )

    def set_version(self, action: str = "") -> bool:
        command = run(
            "elixir -v 2>/dev/null | grep 'Elixir' | cut -d ' ' -f2",
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
