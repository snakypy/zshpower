from subprocess import run
from zshpower.database.sql_inject import (
    SQLSelectVersionByName,
    SQLInsert,
    SQLUpdateVersionByName,
)
from zshpower.database.dao import DAO
from .lib.utils import Color, separator
from zshpower.utils.catch import find_objects
from os import getcwd


class Ruby:
    def __init__(self, config, version, space_elem=" "):
        from .lib.utils import symbol_ssh, element_spacing

        self.config = config
        self.version = version
        self.space_elem = space_elem
        self.files = ("Gemfile", "Rakefile")
        self.extensions = (".rb",)
        self.folders = ()
        self.symbol = symbol_ssh(config["ruby"]["symbol"], "rb-")
        self.color = config["ruby"]["color"]
        self.prefix_color = config["ruby"]["prefix"]["color"]
        self.prefix_text = element_spacing(config["ruby"]["prefix"]["text"])
        self.micro_version_enable = config["ruby"]["version"]["micro"]["enable"]

    def __str__(self):

        ruby_version = self.version

        if ruby_version and find_objects(
            getcwd(), files=self.files, folders=self.folders, extension=self.extensions
        ):

            prefix = f"{Color(self.prefix_color)}{self.prefix_text}{Color().NONE}"

            return str(
                (
                    f"{separator(self.config)}{prefix}"
                    f"{Color(self.color)}{self.symbol}"
                    f"{ruby_version}{self.space_elem}{Color().NONE}"
                )
            )
        return ""


class RubySetVersion(DAO):
    def __init__(self):
        DAO.__init__(self)

    def main(self, /, action=None):
        if action:
            ruby_version = run(
                "ruby --version 2>/dev/null", capture_output=True, shell=True, text=True
            ).stdout

            ruby_version = ruby_version.replace("\n", " ").split(" ")[1].split("p")[0]

            if not ruby_version:
                return False

            if action == "insert":
                query = self.query(str(SQLSelectVersionByName("main", "ruby")))

                if not query:
                    self.execute(
                        str(
                            SQLInsert(
                                "main",
                                columns=("name", "version"),
                                values=("ruby", ruby_version),
                            )
                        )
                    )
                    self.commit()

            elif action == "update":
                self.execute(str(SQLUpdateVersionByName("main", ruby_version, "ruby")))
                self.commit()

            self.connection.close()
