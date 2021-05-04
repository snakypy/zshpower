from pathlib import Path
from .lib.utils import symbol_ssh, element_spacing
from os import environ, getcwd
from os import geteuid
from .lib.utils import Color


def shorten_path(file_path, length):
    return Path(*Path(file_path).parts[-length:])


class Directory:
    def __init__(self, config):
        self.username_enable = config["username"]["enable"]
        self.hostname_enable = config["hostname"]["enable"]
        self.truncate_value = config["directory"]["truncation_length"]
        self.symbol = symbol_ssh(config["directory"]["symbol"], "")
        self.color = config["directory"]["color"]
        self.prefix_color = config["directory"]["prefix"]["color"]
        self.prefix_text = element_spacing(config["directory"]["prefix"]["text"])

    def __str__(self, prefix="", space_elem=" "):
        if (
            self.username_enable
            or geteuid() == 0
            or self.hostname_enable
            or "SSH_CONNECTION" in environ
        ):
            prefix = f"{Color(self.prefix_color)}" f"{self.prefix_text}{Color().NONE}"

        if int(self.truncate_value) < 0:
            self.truncate_value = 0
        if int(self.truncate_value) > 4:
            self.truncate_value = 4

        # Old "abspath_link()"
        dir_truncate = str(shorten_path(getcwd(), self.truncate_value))

        if dir_truncate.split("/")[-1:] == str(Path.home()).split("/")[-1:]:
            dir_truncate = "~"
        return (
            f"{prefix}{Color(self.color)}{self.symbol}"
            f"{dir_truncate}{space_elem}{Color().NONE}"
        )
