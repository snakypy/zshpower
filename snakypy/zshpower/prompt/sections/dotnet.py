from subprocess import run

from snakypy.zshpower.prompt.sections.utils import Version


class Dotnet(Version):
    def __init__(self):
        super(Dotnet, self).__init__()
        self.files = ("project.json", "global.json", "paket.dependencies")
        self.extensions = (".csproj", ".fsproj", ".xproj", ".sln")

    def get_version(
        self, config, reg_version, key="dotnet", ext=".net-", space_elem=" "
    ) -> str:
        return super().get(config, reg_version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, key="dotnet", action=None) -> bool:

        version = run(
            "dotnet --version 2>/dev/null",
            capture_output=True,
            shell=True,
            text=True,
        ).stdout

        if not version.replace("\n", ""):
            return False
        version_format = version.replace("\n", "")
        return super().set(version_format, key, action)
