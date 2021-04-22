class Dotnet:
    def __init__(self, config):
        from .lib.utils import symbol_ssh, element_spacing

        self.config = config
        self.files = ("project.json", "global.json", "paket.dependencies")
        self.extensions = (".csproj", ".fsproj", ".xproj", ".sln")
        self.symbol = symbol_ssh(config["dotnet"]["symbol"], "dn-")
        self.color = config["dotnet"]["color"]
        self.prefix_color = config["dotnet"]["prefix"]["color"]
        self.prefix_text = element_spacing(config["dotnet"]["prefix"]["text"])
        self.version_enable = config["dotnet"]["version"]["enable"]
        self.micro_version_enable = config["dotnet"]["version"]["micro"]["enable"]

    def get_version(self, space_elem=" "):
        from subprocess import run

        dotnet_version = run(
            "dotnet --version 2>/dev/null", capture_output=True, shell=True, text=True
        )

        if not dotnet_version.stdout.replace("\n", ""):
            return False

        dotnet_version = dotnet_version.stdout.replace("\n", "").split(".")

        if not self.micro_version_enable:
            version_current = "{0[0]}.{0[1]}".format(dotnet_version)
            return f"{version_current}{space_elem}"
        else:
            version_current = "{0[0]}.{0[1]}.{0[2]}".format(dotnet_version)
            return f"{version_current}{space_elem}"

    def __str__(self):
        from .lib.utils import Color, separator
        from zshpower.utils.catch import find_objects
        from os import getcwd as os_getcwd

        prefix = f"{Color(self.prefix_color)}{self.prefix_text}{Color().NONE}"

        if (
            self.version_enable
            and self.get_version()
            and find_objects(
                os_getcwd(),
                files=self.files,
                extension=self.extensions,
            )
        ):
            return str(
                (
                    f"{separator(self.config)}{prefix}"
                    f"{Color(self.color)}{self.symbol}"
                    f"{self.get_version()}{Color().NONE}"
                )
            )
        return ""
