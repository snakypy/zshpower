from subprocess import run
from zshpower.database.sql_inject import (
    SQLSelectVersionByName,
    SQLInsert,
    SQLUpdateVersionByName,
)
from zshpower.database.dao import DAO
from .lib.utils import separator
from zshpower.utils.catch import find_objects
from os import getcwd
from .lib.utils import Color


class NodeJs:
    def __init__(self, config, version, space_elem=" "):
        from .lib.utils import symbol_ssh, element_spacing

        self.config = config
        self.version = version
        self.space_elem = space_elem
        self.files = ("package.json",)
        self.folders = ("node_modules",)
        self.symbol = symbol_ssh(self.config["nodejs"]["symbol"], "node-")
        self.color = self.config["nodejs"]["color"]
        self.prefix_color = self.config["nodejs"]["prefix"]["color"]
        self.prefix_text = element_spacing(self.config["nodejs"]["prefix"]["text"])
        self.micro_version_enable = self.config["nodejs"]["version"]["micro"]["enable"]

    def __str__(self):

        nodejs_version = self.version

        if nodejs_version and find_objects(
            getcwd(), files=self.files, folders=self.folders
        ):

            prefix = f"{Color(self.prefix_color)}" f"{self.prefix_text}{Color().NONE}"

            return str(
                f"{separator(self.config)}{prefix}"
                f"{Color(self.color)}"
                f"{self.symbol}{nodejs_version}{self.space_elem}{Color().NONE}"
            )
        return ""


class NodeJsSetVersion(DAO):
    def __init__(self):
        DAO.__init__(self)

    def main(self, /, action=None):
        if action:
            nodejs_version = run(
                "node -v 2>/dev/null", capture_output=True, shell=True, text=True
            ).stdout

            if not nodejs_version.replace("\n", ""):
                return False

            nodejs_version = nodejs_version.replace("\n", "").split("v")[1]

            if action == "insert":
                query = self.query(str(SQLSelectVersionByName("main", "nodejs")))

                if not query:
                    self.execute(
                        str(
                            SQLInsert(
                                "main",
                                columns=("name", "version"),
                                values=("nodejs", nodejs_version),
                            )
                        )
                    )
                    self.commit()

            elif action == "update":
                self.execute(
                    str(SQLUpdateVersionByName("main", nodejs_version, "nodejs"))
                )
                self.commit()

            self.connection.close()
