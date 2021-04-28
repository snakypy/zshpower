from subprocess import run
from zshpower.database.sql_inject import (
    SQLSelectVersionByName,
    SQLInsert,
    SQLUpdateVersionByName,
)
from zshpower.database.dao import DAO
from .lib.utils import symbol_ssh, element_spacing


class DotnetGetVersion:
    def __init__(self, config, version, space_elem=" "):

        self.config = config
        self.version = version
        self.space_elem = space_elem
        self.files = ("project.json", "global.json", "paket.dependencies")
        self.extensions = (".csproj", ".fsproj", ".xproj", ".sln")
        self.folders = ()
        self.symbol = symbol_ssh(config["dotnet"]["symbol"], ".net-")
        self.color = config["dotnet"]["color"]
        self.prefix_color = config["dotnet"]["prefix"]["color"]
        self.prefix_text = element_spacing(config["dotnet"]["prefix"]["text"])
        self.micro_version_enable = config["dotnet"]["version"]["micro"]["enable"]

    def __str__(self):
        from .lib.utils import Color, separator
        from zshpower.utils.catch import find_objects
        from os import getcwd

        dotnet_version = self.version

        if dotnet_version and find_objects(
            getcwd(), files=self.files, folders=self.folders, extension=self.extensions
        ):
            prefix = f"{Color(self.prefix_color)}{self.prefix_text}{Color().NONE}"

            return str(
                (
                    f"{separator(self.config)}{prefix}"
                    f"{Color(self.color)}{self.symbol}"
                    f"{dotnet_version}{self.space_elem}{Color().NONE}"
                )
            )
        return ""


class DotnetSetVersion(DAO):
    def __init__(self):
        DAO.__init__(self)

    def main(self, /, action=None):
        if action:
            dotnet_version = run(
                "dotnet --version 2>/dev/null",
                capture_output=True,
                shell=True,
                text=True,
            ).stdout

            if not dotnet_version.replace("\n", ""):
                return False

            dotnet_version = dotnet_version.replace("\n", "")

            if action == "insert":
                query = self.query(str(SQLSelectVersionByName("main", "dotnet")))

                if not query:
                    self.execute(
                        str(SQLInsert(
                            "main",
                            columns=("name", "version"),
                            values=("dotnet", dotnet_version),
                        ))
                    )
                    self.commit()

            elif action == "update":
                self.execute(str(SQLUpdateVersionByName("main", dotnet_version, "dotnet")))
                self.commit()

            self.connection.close()
            return True

        return False
