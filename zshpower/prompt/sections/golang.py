from subprocess import run
from zshpower.database.sql_inject import (
    SQLSelectVersionByName,
    SQLInsert,
    SQLUpdateVersionByName,
)
from zshpower.database.dao import DAO
from .lib.utils import symbol_ssh, element_spacing


class GolangGetVersion:
    def __init__(self, config, version, space_elem=" "):

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
        from os import getcwd

        golang_version = self.version

        if golang_version and find_objects(
            getcwd(), files=self.files, folders=self.folders, extension=self.extensions
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

            golang_version = golang_version.replace("golang", "").split(" ")[2]

            if action == "insert":
                query = self.query(str(SQLSelectVersionByName("main", "golang")))

                if not query:
                    self.execute(
                        str(
                            SQLInsert(
                                "main",
                                columns=("name", "version"),
                                values=("golang", golang_version),
                            )
                        )
                    )
                    self.commit()

            elif action == "update":
                self.execute(str(SQLUpdateVersionByName("main", golang_version, "go")))
                self.commit()

            self.connection.close()
            return True

        return False
