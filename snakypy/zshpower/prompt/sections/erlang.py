from subprocess import run

from snakypy.zshpower.config.base import Base
from snakypy.zshpower.prompt.sections.utils import Version


class Erlang(Version, Base):
    def __init__(self):
        super(Erlang, self).__init__()
        self.files = ("rebar.config", "erlang.mk")

    def get_version(
        self, config, reg_version, key="erlang", ext="erl-", space_elem=" "
    ) -> str:
        return super().get(config, reg_version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, exec_="erl", key="erlang", action=None) -> bool:
        # The parameter 2>&1 is for the command to insert output to stdout, as some output to stderr.
        command = run("erl -version 2>&1", capture_output=True, shell=True, text=True)
        version = command.stdout.split()[-1]
        return super().set(command, version, exec_, key, action)
