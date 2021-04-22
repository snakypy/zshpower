class Golang:
    def __init__(self, config):
        from .lib.utils import symbol_ssh, element_spacing

        self.config = config
        self.files = ("go.mod", "glide.yaml")
        self.folders = ("Godeps",)
        self.symbol = symbol_ssh(config["golang"]["symbol"], "go-")
        self.color = config["golang"]["color"]
        self.prefix_color = config["golang"]["prefix"]["color"]
        self.prefix_text = element_spacing(config["golang"]["prefix"]["text"])
        self.version_enable = config["golang"]["version"]["enable"]
        self.micro_version_enable = config["golang"]["version"]["micro"]["enable"]

    def get_version(self, space_elem=" "):
        from subprocess import run

        output_version = run("go version", capture_output=True, shell=True, text=True)

        if not output_version.stdout.replace("\n", ""):
            return False

        output_version = output_version.stdout.replace("go", "").split(" ")
        output_version = output_version[2].split(".")

        if not self.micro_version_enable:
            version = "{0[0]}.{0[1]}".format(output_version)
            return f"{version}{space_elem}"
        else:
            version = "{0[0]}.{0[1]}.{0[2]}".format(output_version)
            return f"{version}{space_elem}"

    def __str__(self):
        from .lib.utils import Color, separator
        from zshpower.utils.catch import find_objects
        from zshpower.utils.check import is_tool
        from os import getcwd as os_getcwd

        prefix = f"{Color(self.prefix_color)}{self.prefix_text}{Color().NONE}"

        if (
            self.get_version()
            and self.version_enable
            and find_objects(
                os_getcwd(), files=self.files, folders=self.folders, extension=(".go",)
            )
        ):
            return str(
                (
                    f"{separator(self.config)}{prefix}"
                    f"{Color(self.color)}{self.symbol}"
                    f"{self.get_version()}{Color().NONE}"
                )
            )
        return ""
