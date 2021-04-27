from subprocess import run

from zshpower.database.dao import DAO


class DotnetGetVersion:
    def __init__(self, config, version, space_elem=" "):
        from .lib.utils import symbol_ssh, element_spacing

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
        from os import getcwd as os_getcwd

        dotnet_version = self.version

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
                "dotnet --version 2>/dev/null", capture_output=True, shell=True, text=True
            ).stdout

            if not dotnet_version.replace("\n", ""):
                return False

            dotnet_version = dotnet_version.replace("\n", "")

            if action == "insert":
                sql = f"""SELECT version FROM main WHERE name = 'dotnet';"""
                query = self.query(sql)

                if not query:
                    sql = f"""INSERT INTO main (name, version)
                    VALUES ('dotnet', '{dotnet_version}');"""
                    self.execute(sql)
                    self.commit()

            elif action == "update":
                sql = f"""UPDATE main SET version = '{dotnet_version}' WHERE name = 'dotnet';"""
                self.execute(sql)
                self.commit()

            self.connection.close()
            return True

        return False
