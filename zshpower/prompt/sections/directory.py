from os import geteuid as os_geteuid
from os import environ
from pathlib import Path
from .lib.utils import Color, abspath_link
from .lib.utils import symbol_ssh, element_spacing
from tomlkit.exceptions import UnexpectedCharError


def shorten_path(file_path, length):
    return Path(*Path(file_path).parts[-length:])


class Directory:
    def __init__(self, config):
        self.username_enable = config["username"]["enable"]
        self.hostname_enable = config["hostname"]["enable"]
        self.directory_truncate_value = config["directory"]["truncation_length"]
        self.directory_symbol = symbol_ssh(config["directory"]["symbol"], "")
        self.directory_color = config["directory"]["color"]
        self.directory_prefix_color = config["directory"]["prefix"]["color"]
        self.directory_prefix_text = element_spacing(
            config["directory"]["prefix"]["text"]
        )

    def __str__(self, prefix="", space_elem=" "):
        if (
            self.username_enable
            or os_geteuid() == 0
            or self.hostname_enable
            or "SSH_CONNECTION" in environ
        ):
            prefix = (
                f"{Color(self.directory_prefix_color)}"
                f"{self.directory_prefix_text}{Color().NONE}"
            )

        if int(self.directory_truncate_value) < 0:
            self.directory_truncate_value = 0
        if int(self.directory_truncate_value) > 4:
            self.directory_truncate_value = 4

        dir_truncate = str(shorten_path(
            abspath_link(),
            self.directory_truncate_value
        ))

        if dir_truncate.split("/")[-1:] == str(Path.home()).split("/")[-1:]:
            dir_truncate = "~"
        directory_export = (
            f"{prefix}{Color(self.directory_color)}{self.directory_symbol}"
            f"{dir_truncate}{space_elem}{Color().NONE}"
        )

        return str(directory_export)
