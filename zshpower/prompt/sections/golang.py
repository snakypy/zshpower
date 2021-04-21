class Golang:
    def __init__(self, config):
        from .lib.utils import symbol_ssh, element_spacing

        self.config = config
        self.search_f = ("go.mod", "glide.yaml")
        self.go_symbol = config["golang"]["symbol"]
        self.go_symbol = symbol_ssh(config["golang"]["symbol"], "go-")
        self.go_color = config["golang"]["color"]
        self.go_prefix_color = config["golang"]["prefix"]["color"]
        self.go_prefix_text = element_spacing(config["golang"]["prefix"]["text"])
        self.go_version_enable = config["golang"]["version"]["enable"]
        self.gov_micro_enable = config["golang"]["version"]["micro"]["enable"]

    def get_version(self, space_elem=" "):
        from subprocess import check_output

        # Exemple print: ['go', 'version', 'go1.16.3', 'linux/amd64']
        go_version_full = (
            check_output(
                "go version",
                shell=True,
                universal_newlines=True,
            )
            .replace("\n", "")
            .split(" ")
        )

        go_version = go_version_full[2].replace("go", "").split(".")

        if not self.gov_micro_enable:
            version = "{0[0]}.{0[1]}".format(go_version)
            return f"{version}{space_elem}"
        else:
            version = "{0[0]}.{0[1]}.{0[2]}".format(go_version)
            return f"{version}{space_elem}"

    def __str__(self):
        from .lib.utils import Color, separator
        from zshpower.utils.catch import find_files
        from zshpower.utils.check import is_tool
        from os import getcwd as os_getcwd

        go_prefix1 = f"{Color(self.go_prefix_color)}{self.go_prefix_text}{Color().NONE}"

        if is_tool("go"):
            if self.go_version_enable and find_files(
                os_getcwd(), files=self.search_f, extension=".go"
            ):
                return str(
                    (
                        f"{separator(self.config)}{go_prefix1}"
                        f"{Color(self.go_color)}{self.go_symbol}"
                        f"{self.get_version()}{Color().NONE}"
                    )
                )
        return ""
