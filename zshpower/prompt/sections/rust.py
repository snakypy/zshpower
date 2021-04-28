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


class Rust:
    def __init__(self, config, version, space_elem=" "):

        self.config = config
        self.version = version
        self.space_elem = space_elem
        self.files = ("Cargo.toml",)
        self.extensions = (".rs",)
        self.folders = ()
        self.symbol = symbol_ssh(config["rust"]["symbol"], "rs-")
        self.color = config["rust"]["color"]
        self.prefix_color = config["rust"]["prefix"]["color"]
        self.prefix_text = element_spacing(config["rust"]["prefix"]["text"])
        self.micro_version_enable = config["rust"]["version"]["micro"]["enable"]

    def __str__(self):

        rust_version = self.version

        if rust_version and find_objects(
            getcwd(), files=self.files, folders=self.folders, extension=self.extensions
        ):

            prefix = f"{Color(self.prefix_color)}{self.prefix_text}{Color().NONE}"

            return str(
                (
                    f"{separator(self.config)}{prefix}"
                    f"{Color(self.color)}{self.symbol}"
                    f"{rust_version}{self.space_elem}{Color().NONE}"
                )
            )
        return ""


class RustSetVersion(DAO):
    def __init__(self):
        DAO.__init__(self)

    def main(self, /, action=None):
        if action:
            rust_version = run(
                "rustc --version", capture_output=True, shell=True, text=True
            ).stdout

            rust_version = rust_version.split(" ")[1].replace("\n", "")

            if not rust_version:
                return False

            if action == "insert":
                query = self.query(str(SQLSelectVersionByName("main", "rust")))

                if not query:
                    self.execute(
                        str(SQLInsert(
                            "main",
                            columns=("name", "version"),
                            values=("rust", rust_version),
                        ))
                    )
                    self.commit()

            elif action == "update":
                self.execute(str(SQLUpdateVersionByName("main", rust_version, "rust")))
                self.commit()

            self.connection.close()
