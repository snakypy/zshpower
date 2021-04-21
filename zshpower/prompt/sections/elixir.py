class Elixir:
    def __init__(self, config):
        from .lib.utils import symbol_ssh, element_spacing

        self.config = config
        self.search_f = ("mix.exs",)
        self.eli_symbol = config["elixir"]["symbol"]
        self.eli_symbol = symbol_ssh(config["elixir"]["symbol"], "ex-")
        self.eli_color = config["elixir"]["color"]
        self.eli_prefix_color = config["elixir"]["prefix"]["color"]
        self.eli_prefix_text = element_spacing(config["elixir"]["prefix"]["text"])
        self.eli_version_enable = config["elixir"]["version"]["enable"]
        self.gov_micro_enable = config["elixir"]["version"]["micro"]["enable"]

    def get_version(self, space_elem=" "):
        from subprocess import check_output

        # Exemple print: ['1', '11', '3']
        eli_version = (
            check_output(
                """elixir -v 2>/dev/null | grep "Elixir" | cut -d ' ' -f2""",
                shell=True,
                universal_newlines=True,
            )
            .replace("\n", "")
            .split(".")
        )

        if not self.gov_micro_enable:
            version = "{0[0]}.{0[1]}".format(eli_version)
            return f"{version}{space_elem}"
        else:
            version = "{0[0]}.{0[1]}.{0[2]}".format(eli_version)
            return f"{version}{space_elem}"

    def __str__(self):
        from .lib.utils import Color, separator
        from zshpower.utils.catch import find_files
        from zshpower.utils.check import is_tool
        from os import getcwd as os_getcwd

        eli_prefix1 = f"{Color(self.eli_prefix_color)}{self.eli_prefix_text}{Color().NONE}"

        if is_tool("elixir"):
            if self.eli_version_enable and find_files(
                os_getcwd(), files=self.search_f, extension=".ex"
            ):
                return str(
                    (
                        f"{separator(self.config)}{eli_prefix1}"
                        f"{Color(self.eli_color)}{self.eli_symbol}"
                        f"{self.get_version()}{Color().NONE}"
                    )
                )
        return ""
