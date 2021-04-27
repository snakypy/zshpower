from subprocess import run
from zshpower.database.dao import DAO
from .lib.utils import symbol_ssh, element_spacing
from .lib.utils import Color, separator
from zshpower.utils.catch import find_objects
from os import getcwd as os_getcwd


class JavaGetVersion:
    def __init__(self, config, version, space_elem=" "):
        self.config = config
        self.version = version
        self.space_elem = space_elem
        self.extensions = (".java",)
        self.files = ()
        self.folders = ()
        self.symbol = symbol_ssh(config["java"]["symbol"], "java-")
        self.color = config["java"]["color"]
        self.prefix_color = config["java"]["prefix"]["color"]
        self.prefix_text = element_spacing(config["java"]["prefix"]["text"])
        self.version_enable = config["java"]["version"]["enable"]
        self.micro_version_enable = config["java"]["version"]["micro"]["enable"]

    def __str__(self):
        java_version = self.version

        if (
            self.version_enable
            and java_version
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
                    f"{java_version}{self.space_elem}{Color().NONE}"
                )
            )
        return ""


class JavaSetVersion(DAO):
    def __init__(self):
        DAO.__init__(self)

    def main(self, /, action=None):
        if action:
            java_version = run(
                """java -version 2>&1 | awk -F '"' '/version/ {print $2}'""",
                capture_output=True,
                shell=True,
                text=True,
            ).stdout

            if not java_version.replace("\n", ""):
                return False

            java_version = java_version.replace("\n", "").split("_")[0]

            if action == "insert":
                sql = f"""SELECT version FROM main WHERE name = 'java';"""
                query = self.query(sql)

                if not query:
                    sql = f"""INSERT INTO main (name, version)
                    VALUES ('java', '{java_version}');"""
                    self.execute(sql)
                    self.commit()

            elif action == "update":
                sql = f"""UPDATE main SET version = '{java_version}' WHERE name = 'java';"""
                self.execute(sql)
                self.commit()

            self.connection.close()
