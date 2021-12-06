from subprocess import run

from snakypy.zshpower.config.base import Base
from snakypy.zshpower.prompt.sections.utils import Version


class Erlang(Version, Base):
    def __init__(self, *args):
        super(Erlang, self).__init__()
        self.args: tuple = args
        self.key = "erlang"
        self.app_executable = "erl"
        self.shorten = "dkr-"
        self.finder = {
            "extensions": [".erl"],
            "folders": [],
            "files": ["rebar.config", "erlang.mk"],
        }

    def get_version(self, space_elem: str = " ") -> str:
        return super().get(
            self.args[0], self.args[1], self.key, self.shorten, space_elem=space_elem
        )

    def set_version(self, action: str = "") -> bool:
        command = run("erl -version 2>&1", capture_output=True, shell=True, text=True)
        version = command.stdout.split()[-1]
        return super().set(
            command, version, self.app_executable, self.key, action=action
        )

    def __str__(self):
        return self.get_version()
