class Php:
    def __init__(self, config):
        from .lib.utils import symbol_ssh, element_spacing

        self.config = config
        self.search_f = ("composer.json",)
        self.php_symbol = config["php"]["symbol"]
        self.php_symbol = symbol_ssh(config["php"]["symbol"], "php-")
        self.php_color = config["php"]["color"]
        self.php_prefix_color = config["php"]["prefix"]["color"]
        self.php_prefix_text = element_spacing(config["php"]["prefix"]["text"])
        self.php_version_enable = config["php"]["version"]["enable"]
        self.phpv__micro_enable = config["php"]["version"]["micro"]["enable"]

    def get_version(self, space_elem=" "):
        from subprocess import check_output

        # Exemple print: ['8', '0', '3']
        php_version = (
            check_output(
                """php -v 2>&1 | grep "^PHP\\s*[0-9.]\\+" | awk '{print $2}'""",
                shell=True,
                universal_newlines=True,
            )
            .replace("\n", "")
            .split(".")
        )

        if not self.phpv__micro_enable:
            version = "{0[0]}.{0[1]}".format(php_version)
            return f"{version}{space_elem}"
        else:
            version = "{0[0]}.{0[1]}.{0[2]}".format(php_version)
            return f"{version}{space_elem}"

    def __str__(self):
        from .lib.utils import Color, separator
        from zshpower.utils.catch import find_files
        from zshpower.utils.check import is_tool
        from os import getcwd as os_getcwd

        php_prefix1 = f"{Color(self.php_prefix_color)}{self.php_prefix_text}{Color().NONE}"

        if is_tool("php"):
            if self.php_version_enable and find_files(
                os_getcwd(), files=self.search_f, extension=".php"
            ):
                return str(
                    (
                        f"{separator(self.config)}{php_prefix1}"
                        f"{Color(self.php_color)}{self.php_symbol}"
                        f"{self.get_version()}{Color().NONE}"
                    )
                )
        return ""
