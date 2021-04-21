class Rust:
    def __init__(self, config):
        from .lib.utils import symbol_ssh, element_spacing

        self.config = config
        self.search_f = ("Cargo.toml", "cargo.toml")
        self.rs_symbol = config["rust"]["symbol"]
        self.rs_symbol = symbol_ssh(config["rust"]["symbol"], "rs-")
        self.rs_color = config["rust"]["color"]
        self.rs_prefix_color = config["rust"]["prefix"]["color"]
        self.rs_prefix_text = element_spacing(config["rust"]["prefix"]["text"])
        self.rs_version_enable = config["rust"]["version"]["enable"]
        self.rsv_micro_enable = config["rust"]["version"]["micro"]["enable"]

    def get_version(self, space_elem=" "):
        from subprocess import check_output

        rust_version_full = (
            check_output(
                "rustc --version",
                shell=True,
                universal_newlines=True,
            )
            .replace("\n", "")
            .split(".")
        )
        rust_version = [v.replace("rustc ", "") for v in rust_version_full]

        if not self.rsv_micro_enable:
            version = "{0[0]}.{0[1]}".format(rust_version)
            return f"{version}{space_elem}"
        else:
            version = "{0[0]}.{0[1]}.{0[2]}".format(rust_version)
            return f"{version}{space_elem}"

    def __str__(self):
        from .lib.utils import Color, separator
        from zshpower.utils.catch import find_files
        from zshpower.utils.check import is_tool
        from os import getcwd as os_getcwd

        rs_prefix1 = f"{Color(self.rs_prefix_color)}{self.rs_prefix_text}{Color().NONE}"

        if is_tool("rustc"):
            if self.rs_version_enable and find_files(
                os_getcwd(), files=self.search_f, extension=".rs"
            ):
                return str(
                    (
                        f"{separator(self.config)}{rs_prefix1}"
                        f"{Color(self.rs_color)}{self.rs_symbol}"
                        f"{self.get_version()}{Color().NONE}"
                    )
                )
        return ""
