from subprocess import run
from zshpower.prompt.sections.lib.utils import Version


class Julia(Version):
    def __init__(self):
        super(Julia, self).__init__()
        self.extensions = (".jl",)

    def get_version(self, config, version, key="julia", ext="jl-", space_elem=" "):
        return super().get(config, version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, key="julia", action=None):
        version = run(
            "julia --version", capture_output=True, shell=True, text=True
        ).stdout

        if not version.replace("\n", ""):
            return False

        version = version.replace("\n", "").split(" ")[2]

        return super().set(version, key, action)
