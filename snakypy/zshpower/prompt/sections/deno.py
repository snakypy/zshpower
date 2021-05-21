from subprocess import run
from snakypy.zshpower.prompt.sections.utils import Version


class Deno(Version):
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

        if version.returncode != 127 and version.returncode != 1:
            version_format = version.stdout.split()[1]
            return super().set(version_format, key, action)

        return False
