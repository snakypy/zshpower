from subprocess import run

from zshpower.database.dao import DAO


class GolangGetVersion:
    def __init__(self, config, version, space_elem=" "):
        from .lib.utils import symbol_ssh, element_spacing

        self.config = config
        self.version = version
        self.space_elem = space_elem
        self.extensions = (".go",)
        self.files = ("go.mod", "glide.yaml")
        self.folders = ("Godeps",)
        self.symbol = symbol_ssh(config["golang"]["symbol"], "go-")
        self.color = config["golang"]["color"]
        self.prefix_color = config["golang"]["prefix"]["color"]
        self.prefix_text = element_spacing(config["golang"]["prefix"]["text"])
        self.micro_version_enable = config["golang"]["version"]["micro"]["enable"]

    def __str__(self):
        from .lib.utils import Color, separator
        from zshpower.utils.catch import find_objects
        from os import getcwd as os_getcwd

        golang_version = self.version

        if (
            golang_version
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
                    f"{golang_version}{self.space_elem}{Color().NONE}"
                )
            )
        return ""


class GolangSetVersion(DAO):
    def __init__(self):
        DAO.__init__(self)

    def main(self, /, action=None):
        if action:
            golang_version = run(
                "go version", capture_output=True, shell=True, text=True
            ).stdout

            if not golang_version.replace("\n", ""):
                return False

            golang_version = golang_version.replace("go", "").split(" ")[2]

            if action == "insert":
                sql = f"""SELECT version FROM main WHERE name = 'golang';"""
                query = self.query(sql)

                if not query:
                    sql = f"""INSERT INTO main (name, version)
                    VALUES ('golang', '{golang_version}');"""
                    self.execute(sql)
                    self.commit()

            elif action == "update":
                sql = f"""UPDATE main SET version = '{golang_version}' WHERE name = 'golang';"""
                self.execute(sql)
                self.commit()

            self.connection.close()
            return True

        return False
