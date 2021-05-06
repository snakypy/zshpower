from subprocess import run
from zshpower.prompt.sections.lib.utils import Version


class Erlang(Version):
    def __init__(self):
        super(Erlang, self).__init__()
        self.files = ("rebar.config", "erlang.mk")

    def get_version(
        self, config, reg_version, key="erlang", ext="erl-", space_elem=" "
    ):
        return super().get(config, reg_version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, key="erlang", action=None):
        version = run("erl -version 2>&1", capture_output=True, shell=True, text=True)

        if version.returncode != 127 and version.returncode != 1:
            version = version.stdout.split()[-1]
            return super().set(version, key, action)

        return False
