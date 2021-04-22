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
            version_current = "{0[0]}.{0[1]}".format(php_version.split("."))
            return f"{version_current}{space_elem}"
        else:
            version_current = "{0[0]}.{0[1]}.{0[2]}".format(php_version.split("."))
            return f"{version_current}{space_elem}"

    def __str__(self):
        from .lib.utils import Color, separator
        from zshpower.utils.catch import find_objects
        from zshpower.utils.check import is_tool
        from os import getcwd as os_getcwd

        prefix = f"{Color(self.prefix_color)}{self.prefix_text}{Color().NONE}"

        if (
            self.get_version()
            and self.version_enable
            and find_objects(os_getcwd(), files=self.files, extension=(".php",))
        ):
            return str(
                (
                    f"{separator(self.config)}{prefix}"
                    f"{Color(self.color)}{self.symbol}"
                    f"{self.get_version()}{Color().NONE}"
                )
            )
        return ""
