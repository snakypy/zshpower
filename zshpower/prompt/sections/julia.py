class Julia:
    def __init__(self, config):
        from .lib.utils import symbol_ssh, element_spacing

        self.config = config
        self.symbol = symbol_ssh(config["julia"]["symbol"], "jl-")
        self.color = config["julia"]["color"]
        self.prefix_color = config["julia"]["prefix"]["color"]
        self.prefix_text = element_spacing(config["julia"]["prefix"]["text"])
        self.version_enable = config["julia"]["version"]["enable"]
        self.micro_version_enable = config["julia"]["version"]["micro"]["enable"]

    def get_version(self, space_elem=" "):
        from subprocess import run

        output_version = run(
            "julia --version", capture_output=True, shell=True, text=True
        )

        if not output_version.stdout.replace("\n", ""):
            return False

        output_version = (
            output_version.stdout.replace("\n", "").split(" ")[2].split(".")
        )

        if not self.micro_version_enable:
            version_current = "{0[0]}.{0[1]}".format(output_version)
            return f"{version_current}{space_elem}"
        else:
            version_current = "{0[0]}.{0[1]}.{0[2]}".format(output_version)
            return f"{version_current}{space_elem}"

    def __str__(self):
        from .lib.utils import Color, separator
        from zshpower.utils.catch import find_objects
        from os import getcwd as os_getcwd

        prefix = f"{Color(self.prefix_color)}{self.prefix_text}{Color().NONE}"

        if (
            self.get_version()
            and self.version_enable
            and find_objects(os_getcwd(), extension=(".jl",))
        ):
            return str(
                (
                    f"{separator(self.config)}{prefix}"
                    f"{Color(self.color)}{self.symbol}"
                    f"{self.get_version()}{Color().NONE}"
                )
            )
        return ""
