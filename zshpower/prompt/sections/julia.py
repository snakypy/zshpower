from subprocess import run
from zshpower.database.sql_inject import (
    SQLSelectVersionByName,
    SQLInsert,
    SQLUpdateVersionByName,
)
from zshpower.database.dao import DAO
from .lib.utils import symbol_ssh, element_spacing
from .lib.utils import Color, separator
from zshpower.utils.catch import find_objects
from os import getcwd


class Julia:
    def __init__(self, config, version, space_elem=" "):

        self.config = config
        self.version = version
        self.space_elem = space_elem
        self.extensions = (".jl",)
        self.files = ()
        self.folders = ()
        self.symbol = symbol_ssh(config["julia"]["symbol"], "jl-")
        self.color = config["julia"]["color"]
        self.prefix_color = config["julia"]["prefix"]["color"]
        self.prefix_text = element_spacing(config["julia"]["prefix"]["text"])
        self.micro_version_enable = config["julia"]["version"]["micro"]["enable"]

    def __str__(self):

        julia_version = self.version

        if julia_version and find_objects(
            getcwd(), files=self.files, folders=self.folders, extension=self.extensions
        ):
            prefix = f"{Color(self.prefix_color)}{self.prefix_text}{Color().NONE}"

            return str(
                (
                    f"{separator(self.config)}{prefix}"
                    f"{Color(self.color)}{self.symbol}"
                    f"{julia_version}{self.space_elem}{Color().NONE}"
                )
            )
        return ""


class JuliaSetVersion(DAO):
    def __init__(self):
        DAO.__init__(self)

    def main(self, /, action=None):
        if action:
            julia_version = run(
                "julia --version", capture_output=True, shell=True, text=True
            ).stdout

            if not julia_version.replace("\n", ""):
                return False

            julia_version = julia_version.replace("\n", "").split(" ")[2]

            if action == "insert":
                query = self.query(str(SQLSelectVersionByName("main", "julia")))

                if not query:
                    self.execute(
                        str(SQLInsert(
                            "main",
                            columns=("name", "version"),
                            values=("julia", julia_version),
                        ))
                    )
                    self.commit()

            elif action == "update":
                self.execute(str(SQLUpdateVersionByName("main", julia_version, "julia")))
                self.commit()

            self.connection.close()
