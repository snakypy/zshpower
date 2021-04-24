class Java:
    def __init__(self, config):
        from .lib.utils import symbol_ssh, element_spacing

        self.config = config
        self.extensions = (".java",)
        # self.files = None
        # self.folders = None
        self.symbol = symbol_ssh(config["java"]["symbol"], "java-")
        self.color = config["java"]["color"]
        self.prefix_color = config["java"]["prefix"]["color"]
        self.prefix_text = element_spacing(config["java"]["prefix"]["text"])
        self.version_enable = config["java"]["version"]["enable"]
        self.micro_version_enable = config["java"]["version"]["micro"]["enable"]

    def get_version(self, space_elem=" "):
        from subprocess import run

        output_version = run(
            """java -version 2>&1 | awk -F '"' '/version/ {print $2}'""",
            capture_output=True,
            shell=True,
            text=True,
        )

        if not output_version.stdout.replace("\n", ""):
            return False

        output_version = (
            output_version.stdout.replace("\n", "").split("_")[0].split(".")
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
            self.version_enable
            and self.get_version()
            and find_objects(os_getcwd(), extension=self.extensions)
        ):
            return str(
                (
                    f"{separator(self.config)}{prefix}"
                    f"{Color(self.color)}{self.symbol}"
                    f"{self.get_version()}{Color().NONE}"
                )
            )
        return ""
