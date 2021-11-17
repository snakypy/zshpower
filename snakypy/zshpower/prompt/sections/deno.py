from subprocess import run

from snakypy.zshpower.prompt.sections.utils import Version
from snakypy.zshpower.config.base import Base


class Deno(Version, Base):
    # 🦕
    def __init__(self):
        super(Deno, self).__init__()
        self.files = ("mod.ts", "deps.ts", "mod.js", "deps.js")

    def get_version(
        self, config, reg_version, key="deno", ext="deno-", space_elem=" "
    ) -> str:
        return super().get(config, reg_version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, key="deno", action=None) -> bool:
        version = run("deno -V 2>&1", capture_output=True, shell=True, text=True)

        if version.returncode != 0:
            self.log.record(version.stderr, colorize=True, level="error")
        elif version.returncode == 0:
            version_format = version.stdout.split()[1]
            self.log.record(
                f"Deno {version_format} registered in the database!",
                colorize=True,
                level="info",
            )
            return super().set(version_format, key, action)

        return False
