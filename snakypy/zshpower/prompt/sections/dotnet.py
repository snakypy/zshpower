from subprocess import run

from snakypy.zshpower.config.base import Base
from snakypy.zshpower.prompt.sections.utils import Version


class Dotnet(Version, Base):
    def __init__(self, *args):
        super(Dotnet, self).__init__()
        self.args: tuple = args
        self.key = "dotnet"
        self.app_executable = "dotnet"
        self.shorten = ".net-"
        self.files = ("project.json", "global.json", "paket.dependencies")
        self.extensions = (".csproj", ".fsproj", ".xproj", ".sln")

    def get_version(self, space_elem: str = " ") -> str:
        # args[0]: dict = config file (toml)
        # args[1]: dict = database registers
        return super().get(
            self.args[0], self.args[1], self.key, self.shorten, space_elem=space_elem
        )

    def set_version(self, action: str = "") -> bool:
        command = run("dotnet --version", capture_output=True, shell=True, text=True)
        version = command.stdout.replace("\n", "")
        return super().set(
            command, version, self.app_executable, self.key, action=action
        )

    def __str__(self):
        return self.get_version()
