from subprocess import run
from zshpower.prompt.sections.lib.utils import Version


class Deno(Version):
    # 🦕
    def __init__(self):
        super(Deno, self).__init__()
        self.files = ("mod.ts", "deps.ts", "mod.js", "deps.js")

    def get_version(self, config, version, key="deno", ext="deno-", space_elem=" "):
        return super().get(config, version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, key="deno", action=None):
        version = run("deno -V 2>&1", capture_output=True, shell=True, text=True)

        if version.returncode != 127 and version.returncode != 1:
            version = version.stdout.split()[1]
            return super().set(version, key, action)

        return False
