from subprocess import run
from snakypy.zshpower.prompt.sections.lib.utils import Version


class Julia(Version):
    def __init__(self):
        super(Julia, self).__init__()
        self.extensions = (".jl",)

    def get_version(
        self, config, reg_version, key="julia", ext="jl-", space_elem=" "
    ) -> str:
        return super().get(config, reg_version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, key="julia", action=None) -> bool:
        version = run("julia --version", capture_output=True, shell=True, text=True)

        if version.returncode != 127 and version.returncode != 1:
            version_format = version.stdout.replace("\n", "").split(" ")[2]
            return super().set(version_format, key, action)

        return False
