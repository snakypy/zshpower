class Php:
    def __init__(self, config):
        from .lib.utils import symbol_ssh, element_spacing

        self.config = config
        self.files = ("composer.json",)
        self.symbol = symbol_ssh(config["php"]["symbol"], "php-")
        self.color = config["php"]["color"]
        self.prefix_color = config["php"]["prefix"]["color"]
        self.prefix_text = element_spacing(config["php"]["prefix"]["text"])
        self.version_enable = config["php"]["version"]["enable"]
        self.micro_version_enable = config["php"]["version"]["micro"]["enable"]

    def get_version(self, space_elem=" "):
        from subprocess import run

        php_version = run(
            """php -v 2>&1 | grep "^PHP\\s*[0-9.]\\+" | awk '{print $2}'""",
            capture_output=True,
            shell=True,
            text=True,
        )
        php_version = php_version.stdout.replace("\n", "")

        if not php_version:
            return False

        if not self.micro_version_enable:
            return f"{'{0[0]}.{0[1]}'.format(php_version)}{space_elem}"
        return f"{'{0[0]}.{0[1]}.{0[2]}'.format(php_version)}{space_elem}"

    def __str__(self):
        from .lib.utils import Color, separator
        from zshpower.utils.catch import find_objects
        from os import getcwd as os_getcwd

        php_version = self.get_version()

        if (
            self.version_enable
            and php_version
            and find_objects(os_getcwd(), files=self.files, extension=(".php",))
        ):
            prefix = f"{Color(self.prefix_color)}{self.prefix_text}{Color().NONE}"

            return str(
                (
                    f"{separator(self.config)}{prefix}"
                    f"{Color(self.color)}{self.symbol}"
                    f"{self.get_version()}{Color().NONE}"
                )
            )
        return ""
