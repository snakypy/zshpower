from subprocess import run
from zshpower.prompt.sections.lib.utils import Version


class Erlang(Version):
    def __init__(self):
        super(Erlang, self).__init__()
        self.files = ("rebar.config", "erlang.mk")

    def get_version(
        self, config, reg_version, key="erlang", ext="erl-", space_elem=" "
    ) -> str:
        return super().get(config, reg_version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, key="erlang", action=None) -> bool:
        version = run("erl -version 2>&1", capture_output=True, shell=True, text=True)

        if version.returncode != 127 and version.returncode != 1:
            version_format = version.stdout.split()[-1]
            return super().set(version_format, key, action)

        return False