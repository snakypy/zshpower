class Dotnet:
    def __init__(self, config):
        from .lib.utils import symbol_ssh, element_spacing

        self.config = config
        self.files = ("project.json", "global.json", "paket.dependencies")
        self.extensions = (".csproj", ".fsproj", ".xproj", ".sln")
        self.folders = ()
        self.symbol = symbol_ssh(config["dotnet"]["symbol"], ".net-")
        self.color = config["dotnet"]["color"]
        self.prefix_color = config["dotnet"]["prefix"]["color"]
        self.prefix_text = element_spacing(config["dotnet"]["prefix"]["text"])
        self.micro_version_enable = config["dotnet"]["version"]["micro"]["enable"]

    def get_version(self, space_elem=" "):
        from subprocess import run

        dotnet_version = run(
            "dotnet --version 2>/dev/null", capture_output=True, shell=True, text=True
        ).stdout

        if not dotnet_version.replace("\n", ""):
            return False

        dotnet_version = dotnet_version.replace("\n", "").split(".")

        if not self.micro_version_enable:
            return f"{'{0[0]}.{0[1]}'.format(dotnet_version)}{space_elem}"
        return f"{'{0[0]}.{0[1]}.{0[2]}'.format(dotnet_version)}{space_elem}"

    def __str__(self):
        from .lib.utils import Color, separator
        from zshpower.utils.catch import find_objects
        from os import getcwd as os_getcwd

        dotnet_version = self.get_version()

        if (
            dotnet_version
            and find_objects(
                os_getcwd(),
                files=self.files,
                folders=self.folders,
                extension=self.extensions,
            )
        ):
            prefix = f"{Color(self.prefix_color)}{self.prefix_text}{Color().NONE}"

            return str(
                (
                    f"{separator(self.config)}{prefix}"
                    f"{Color(self.color)}{self.symbol}"
                    f"{dotnet_version}{Color().NONE}"
                )
            )
        return ""
