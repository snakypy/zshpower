from subprocess import run
from zshpower.prompt.sections.lib.utils import Version


class Elixir(Version):
    def __init__(self):
        super(Elixir, self).__init__()
        self.files = ("mix.exs",)
        self.extensions = (".ex",)

    def get_version(self, config, version, key="elixir", ext="ex-", space_elem=" "):
        return super().get(config, version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, key="elixir", action=None):

        version = run(
            "elixir -v 2>/dev/null | grep 'Elixir' | cut -d ' ' -f2",
            capture_output=True,
            shell=True,
            text=True,
        ).stdout

        if not version.replace("\n", ""):
            return False

        version = version.replace("\n", "")

        return super().set(version, key, action)
