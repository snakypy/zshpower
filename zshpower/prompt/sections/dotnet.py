class Dotnet:
    def __init__(self, config):
        from .lib.utils import symbol_ssh, element_spacing

        self.config = config
        self.search_f = ("project.json", "global.json", "paket.dependencies")
        self.dn_symbol = config["dotnet"]["symbol"]
        self.dn_symbol = symbol_ssh(config["dotnet"]["symbol"], "ex-")
        self.dn_color = config["dotnet"]["color"]
        self.dn_prefix_color = config["dotnet"]["prefix"]["color"]
        self.dn_prefix_text = element_spacing(config["dotnet"]["prefix"]["text"])
        self.dn_version_enable = config["dotnet"]["version"]["enable"]
        self.dnv_micro_enable = config["dotnet"]["version"]["micro"]["enable"]

    def get_version(self, space_elem=" "):
        from subprocess import check_output

        # Exemple print: ['5', '0', '202']
        dn_version = (
            check_output(
                """dotnet --version 2>/dev/null""",
                shell=True,
                universal_newlines=True,
            )
            .replace("\n", "")
            .split(".")
        )

        if not self.dnv_micro_enable:
            version = "{0[0]}.{0[1]}".format(dn_version)
            return f"{version}{space_elem}"
        else:
            version = "{0[0]}.{0[1]}.{0[2]}".format(dn_version)
            return f"{version}{space_elem}"

    def __str__(self):
        from .lib.utils import Color, separator
        from zshpower.utils.catch import find_files
        from zshpower.utils.check import is_tool
        from os import getcwd as os_getcwd

        dn_prefix1 = f"{Color(self.dn_prefix_color)}{self.dn_prefix_text}{Color().NONE}"

        if is_tool("dotnet"):
            if self.dn_version_enable and find_files(
                os_getcwd(),
                files=self.search_f,
                extension=(".csproj", ".fsproj", ".xproj", ".sln"),
            ):
                return str(
                    (
                        f"{separator(self.config)}{dn_prefix1}"
                        f"{Color(self.dn_color)}{self.dn_symbol}"
                        f"{self.get_version()}{Color().NONE}"
                    )
                )
        return ""
