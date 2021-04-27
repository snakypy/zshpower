from subprocess import run

from zshpower.database.dao import DAO


class ElixirGetVersion:
    def __init__(self, config, version, space_elem=" "):
        from .lib.utils import symbol_ssh, element_spacing

        self.config = config
        self.version = version
        self.space_elem = space_elem
        self.files = ("mix.exs",)
        self.extensions = (".ex",)
        self.folders = ()
        self.symbol = symbol_ssh(config["elixir"]["symbol"], "ex-")
        self.color = config["elixir"]["color"]
        self.prefix_color = config["elixir"]["prefix"]["color"]
        self.prefix_text = element_spacing(config["elixir"]["prefix"]["text"])
        self.micro_version_enable = config["elixir"]["version"]["micro"]["enable"]

    def __str__(self):
        from .lib.utils import Color, separator
        from zshpower.utils.catch import find_objects
        from os import getcwd as os_getcwd

        elixir_version = self.version

        if (
            elixir_version
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
                    f"{elixir_version}{self.space_elem}{Color().NONE}"
                )
            )
        return ""


class ElixirSetVersion(DAO):
    def __init__(self):
        DAO.__init__(self)

    def main(self, /, action=None):
        if action:
            elixir_version = run(
                "elixir -v 2>/dev/null | grep 'Elixir' | cut -d ' ' -f2",
                capture_output=True,
                shell=True,
                text=True,
            ).stdout

            if not elixir_version.replace("\n", ""):
                return False

            elixir_version = elixir_version.replace("\n", "")

            if action == "insert":
                sql = f"""SELECT version FROM main WHERE name = 'elixir';"""
                query = self.query(sql)

                if not query:
                    sql = f"""INSERT INTO main (name, version)
                    VALUES ('elixir', '{elixir_version}');"""
                    self.execute(sql)
                    self.commit()

            elif action == "update":
                sql = f"""UPDATE main SET version = '{elixir_version}' WHERE name = 'elixir';"""
                self.execute(sql)
                self.commit()

            self.connection.close()
            return True

        return False
