from subprocess import run

from snakypy.zshpower.config.base import Base
from snakypy.zshpower.prompt.sections.utils import Version


class Dotnet(Version, Base):
    def __init__(self):
        super(Dotnet, self).__init__()
        self.files = ("project.json", "global.json", "paket.dependencies")
        self.extensions = (".csproj", ".fsproj", ".xproj", ".sln")

    def get_version(
        self, config, reg_version, key="dotnet", ext=".net-", space_elem=" "
    ) -> str:
        return super().get(config, reg_version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, exec_="dotnet", key="dotnet", action=None) -> bool:
        command = run("dotnet --version", capture_output=True, shell=True, text=True)
        version = command.stdout.replace("\n", "")
        return super().set(command, version, exec_, key, action)
