from subprocess import run

from snakypy.zshpower.config.base import Base
from snakypy.zshpower.prompt.sections.utils import Version


class Deno(Version, Base):
    # 🦕
    def __init__(self):
        super(Deno, self).__init__()
        self.files = ("mod.ts", "deps.ts", "mod.js", "deps.js")

    def get_version(
        self, config, reg_version, key="deno", ext="deno-", space_elem=" "
    ) -> str:
        return super().get(config, reg_version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, exec_="deno", key="deno", action=None) -> bool:
        command = run("deno -V", capture_output=True, shell=True, text=True)
        version = command.stdout.split()[1]
        return super().set(command, version, exec_, key, action)
