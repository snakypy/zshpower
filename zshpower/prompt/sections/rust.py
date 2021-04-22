class Rust:
    def __init__(self, config):
        from .lib.utils import symbol_ssh, element_spacing

        self.config = config
        self.files = ("Cargo.toml",)
        self.symbol = symbol_ssh(config["rust"]["symbol"], "rs-")
        self.color = config["rust"]["color"]
        self.prefix_color = config["rust"]["prefix"]["color"]
        self.prefix_text = element_spacing(config["rust"]["prefix"]["text"])
        self.version_enable = config["rust"]["version"]["enable"]
        self.micro_version_enable = config["rust"]["version"]["micro"]["enable"]

    def get_version(self, space_elem=" "):
        from subprocess import run

        rust_version = run(
            "rustc --version", capture_output=True, shell=True, text=True
        )

        if not rust_version.stdout.replace("\n", ""):
            return False

        rust_version = rust_version.stdout.split(" ")[1].replace("\n", "").split(".")

        if not self.micro_version_enable:
            version = "{0[0]}.{0[1]}".format(rust_version)
            return f"{version}{space_elem}"
        else:
            version = "{0[0]}.{0[1]}.{0[2]}".format(rust_version)
            return f"{version}{space_elem}"

    def __str__(self):
        from .lib.utils import Color, separator
        from zshpower.utils.catch import find_objects
        from os import getcwd as os_getcwd

        prefix = f"{Color(self.prefix_color)}{self.prefix_text}{Color().NONE}"

        if (
            self.get_version()
            and self.version_enable
            and find_objects(os_getcwd(), files=self.files, extension=(".rs",))
        ):
            return str(
                (
                    f"{separator(self.config)}{prefix}"
                    f"{Color(self.color)}{self.symbol}"
                    f"{self.get_version()}{Color().NONE}"
                )
            )
        return ""
