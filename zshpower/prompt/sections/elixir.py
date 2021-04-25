class Elixir:
    def __init__(self, config):
        from .lib.utils import symbol_ssh, element_spacing

        self.config = config
        self.files = ("mix.exs",)
        self.extensions = (".ex",)
        self.folders = ()
        self.symbol = symbol_ssh(config["elixir"]["symbol"], "ex-")
        self.color = config["elixir"]["color"]
        self.prefix_color = config["elixir"]["prefix"]["color"]
        self.prefix_text = element_spacing(config["elixir"]["prefix"]["text"])
        self.micro_version_enable = config["elixir"]["version"]["micro"]["enable"]

    def get_version(self, space_elem=" "):
        from subprocess import run

        elixir_version = run(
            "elixir -v 2>/dev/null | grep 'Elixir' | cut -d ' ' -f2",
            capture_output=True,
            shell=True,
            text=True,
        ).stdout

        if not elixir_version.replace("\n", ""):
            return False

        elixir_version = elixir_version.replace("\n", "").split(".")

        if not self.micro_version_enable:
            return f"{'{0[0]}.{0[1]}'.format(elixir_version)}{space_elem}"
        return f"{'{0[0]}.{0[1]}.{0[2]}'.format(elixir_version)}{space_elem}"

    def __str__(self):
        from .lib.utils import Color, separator
        from zshpower.utils.catch import find_objects
        from os import getcwd as os_getcwd

        elixir_version = self.get_version()

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
                    f"{elixir_version}{Color().NONE}"
                )
            )
        return ""
