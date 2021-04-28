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
from .lib.utils import symbol_ssh, element_spacing


class PhpGetVersion:
    def __init__(self, config, version, space_elem=" "):

        self.config = config
        self.version = version
        self.space_elem = space_elem
        self.files = ("composer.json",)
        self.extensions = (".php",)
        self.folders = ()
        self.symbol = symbol_ssh(config["php"]["symbol"], "php-")
        self.color = config["php"]["color"]
        self.prefix_color = config["php"]["prefix"]["color"]
        self.prefix_text = element_spacing(config["php"]["prefix"]["text"])
        self.micro_version_enable = config["php"]["version"]["micro"]["enable"]

    def __str__(self):

        php_version = self.version

        if php_version and find_objects(
            getcwd(), files=self.files, folders=self.folders, extension=self.extensions
        ):
            prefix = f"{Color(self.prefix_color)}{self.prefix_text}{Color().NONE}"

            return str(
                (
                    f"{separator(self.config)}{prefix}"
                    f"{Color(self.color)}{self.symbol}"
                    f"{php_version}{self.space_elem}{Color().NONE}"
                )
            )
        return ""


class PhpSetVersion(DAO):
    def __init__(self):
        DAO.__init__(self)

    def main(self, /, action=None):
        if action:
            php_version = run(
                """php -v 2>&1 | grep "^PHP\\s*[0-9.]\\+" | awk '{print $2}'""",
                capture_output=True,
                shell=True,
                text=True,
            ).stdout

            php_version = php_version.replace("\n", "")

            if not php_version:
                return False

            if action == "insert":
                query = self.query(str(SQLSelectVersionByName("main", "php")))

                if not query:
                    self.execute(
                        str(SQLInsert(
                            "main",
                            columns=("name", "version"),
                            values=("php", php_version),
                        ))
                    )
                    self.commit()

            elif action == "update":
                self.execute(str(SQLUpdateVersionByName("main", php_version, "php")))
                self.commit()

            self.connection.close()
