from zshpower.database.dao import DAO
from .lib.utils import symbol_ssh, element_spacing
from subprocess import run
from zshpower.database.sql import SQLSelectVersionByName, SQLInsert, SQLUpdateVersionByName


class DartGetVersion:
    def __init__(self, config, version, space_elem=" "):
        self.config = config
        self.version = version
        self.space_elem = space_elem
        self.extensions = (".dart",)
        self.files = (
            "pubspec.yaml",
            "config.src.yaml",
            "analysis_options.yaml",
        )
        self.folders = ()
        self.symbol = symbol_ssh(self.config["dart"]["symbol"], "dart-")
        self.color = self.config["dart"]["color"]
        self.prefix_color = self.config["dart"]["prefix"]["color"]
        self.prefix_text = element_spacing(self.config["dart"]["prefix"]["text"])
        self.micro_version_enable = self.config["dart"]["version"]["micro"]["enable"]

    def __str__(self):
        from .lib.utils import Color, separator
        from zshpower.utils.catch import find_objects
        from os import getcwd

        dart_version = self.version

        if (
            dart_version
            and find_objects(
                getcwd(),
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
                    f"{dart_version}{self.space_elem}{Color().NONE}"
                )
            )
        return ""


class DartSetVersion(DAO):
    def __init__(self):
        DAO.__init__(self)

    def main(self, /, action=None):
        if action:
            dart_version = run(
                "dart --version 2>&1", capture_output=True, shell=True, text=True
            )
            if not dart_version.returncode == 0:
                return False

            dart_version = dart_version.stdout.replace("\n", "").split(" ")[3]

            if action == "insert":
                query = self.query(SQLSelectVersionByName("main", "dart"))

                if not query:
                    self.execute(SQLInsert("main", columns=("name", "version"), values=("dart", dart_version)))
                    self.commit()

            elif action == "update":
                self.execute(SQLUpdateVersionByName("main", dart_version, "dart"))
                self.commit()

            self.connection.close()
            return True

        return False

# def dart(config):
#     import concurrent.futures
#
#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         future = executor.submit(DartGetVersion, config)
#         return_value = future.result()
#         return return_value
