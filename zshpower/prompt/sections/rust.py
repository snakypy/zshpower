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
            return f"{'{0[0]}.{0[1]}'.format(rust_version)}{space_elem}"
        return f"{'{0[0]}.{0[1]}.{0[2]}'.format(rust_version)}{space_elem}"

    def __str__(self):
        from .lib.utils import Color, separator
        from zshpower.utils.catch import find_objects
        from os import getcwd as os_getcwd

        rust_version = self.get_version()

        if (
            self.version_enable
            and rust_version
            and find_objects(os_getcwd(), files=self.files, extension=(".rs",))
        ):
            prefix = f"{Color(self.prefix_color)}{self.prefix_text}{Color().NONE}"

            return str(
                (
                    f"{separator(self.config)}{prefix}"
                    f"{Color(self.color)}{self.symbol}"
                    f"{rust_version}{Color().NONE}"
                )
            )
        return ""
