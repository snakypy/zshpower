class Ruby:
    def __init__(self, config):
        from .lib.utils import symbol_ssh, element_spacing

        self.config = config
        self.search_f = ("Gemfile", "Rakefile")
        self.rb_symbol = config["ruby"]["symbol"]
        self.rb_symbol = symbol_ssh(config["ruby"]["symbol"], "ex-")
        self.rb_color = config["ruby"]["color"]
        self.rb_prefix_color = config["ruby"]["prefix"]["color"]
        self.rb_prefix_text = element_spacing(config["ruby"]["prefix"]["text"])
        self.rb_version_enable = config["ruby"]["version"]["enable"]
        self.rbv_micro_enable = config["ruby"]["version"]["micro"]["enable"]

    def get_version(self, space_elem=" "):
        from subprocess import check_output

        # Example print: ['3', '0', '1p64']
        rb_version = (
            check_output(
                """ruby --version 2>/dev/null""",
                shell=True,
                universal_newlines=True,
            )
            .replace("\n", "")
            .split(" ")[1].split(".")
        )

        if not self.rbv_micro_enable:
            version = "{0[0]}.{0[1]}".format(rb_version)
            return f"{version}{space_elem}"
        else:
            version = "{0[0]}.{0[1]}.{0[2]}".format(rb_version)
            return f"{version}{space_elem}"

    def __str__(self):
        from .lib.utils import Color, separator
        from zshpower.utils.catch import find_files
        from zshpower.utils.check import is_tool
        from os import getcwd as os_getcwd

        rb_prefix1 = f"{Color(self.rb_prefix_color)}{self.rb_prefix_text}{Color().NONE}"

        if is_tool("ruby"):
            if self.rb_version_enable and find_files(
                os_getcwd(),
                files=self.search_f,
                extension=(".rb",),
            ):
                return str(
                    (
                        f"{separator(self.config)}{rb_prefix1}"
                        f"{Color(self.rb_color)}{self.rb_symbol}"
                        f"{self.get_version()}{Color().NONE}"
                    )
                )
        return ""
