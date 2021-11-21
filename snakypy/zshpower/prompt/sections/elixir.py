from subprocess import run

from snakypy.zshpower.config.base import Base
from snakypy.zshpower.prompt.sections.utils import Version


class Elixir(Version, Base):
    def __init__(self):
        super(Elixir, self).__init__()
        self.files = ("mix.exs",)
        self.extensions = (".ex",)

    def get_version(
        self, config, reg_version, key="elixir", ext="ex-", space_elem=" "
    ) -> str:
        return super().get(config, reg_version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, exec_="elixir", key="elixir", action=None) -> bool:
        command = run(
            "elixir -v 2>/dev/null | grep 'Elixir' | cut -d ' ' -f2",
            capture_output=True,
            shell=True,
            text=True,
        )
        version = command.stdout.replace("\n", "")
        return super().set(command, version, exec_, key, action)
