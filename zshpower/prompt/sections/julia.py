class Julia:
    def __init__(self, config):
        from .lib.utils import symbol_ssh, element_spacing

        self.config = config
        self.jl_symbol = config["julia"]["symbol"]
        self.jl_symbol = symbol_ssh(config["julia"]["symbol"], "ex-")
        self.jl_color = config["julia"]["color"]
        self.jl_prefix_color = config["julia"]["prefix"]["color"]
        self.jl_prefix_text = element_spacing(config["julia"]["prefix"]["text"])
        self.jl_version_enable = config["julia"]["version"]["enable"]
        self.jlv_micro_enable = config["julia"]["version"]["micro"]["enable"]

    def get_version(self, space_elem=" "):
        from subprocess import check_output

        # Exemple print: ['1', '6', '0']
        jl_version = (
            check_output(
                """julia --version""",
                shell=True,
                universal_newlines=True,
            )
            .replace("\n", "")
            .split(" ")[2]
            .split(".")
        )

        if not self.jlv_micro_enable:
            version = "{0[0]}.{0[1]}".format(jl_version)
            return f"{version}{space_elem}"
        else:
            version = "{0[0]}.{0[1]}.{0[2]}".format(jl_version)
            return f"{version}{space_elem}"

    def __str__(self):
        from .lib.utils import Color, separator
        from zshpower.utils.catch import find_files
        from zshpower.utils.check import is_tool
        from os import getcwd as os_getcwd

        jl_prefix1 = f"{Color(self.jl_prefix_color)}{self.jl_prefix_text}{Color().NONE}"

        if is_tool("julia"):
            if self.jl_version_enable and find_files(os_getcwd(), extension=(".jl",)):
                return str(
                    (
                        f"{separator(self.config)}{jl_prefix1}"
                        f"{Color(self.jl_color)}{self.jl_symbol}"
                        f"{self.get_version()}{Color().NONE}"
                    )
                )
        return ""
