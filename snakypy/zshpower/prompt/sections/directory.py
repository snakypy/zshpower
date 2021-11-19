from os import environ, geteuid
from pathlib import Path
from subprocess import run

from snakypy.zshpower.utils.catch import get_key
from snakypy.zshpower.utils.check import str_empty_in

from .utils import Color, element_spacing, symbol_ssh


def get_pwd() -> str:
    # import os
    # from os import getenv, system
    # from os import environ, getcwd, getcwdb, getenvb
    # from pathlib import Path
    # from os import getcwd

    # NOTES: https://stackoverflow.com/questions/123958/how-to-get-set-logical-directory-path-in-python
    # return os.popen('pwd').read().strip('\n')
    # return getenv('PWD')
    # return getcwd()
    return run("pwd", capture_output=True, shell=True, text=True).stdout.replace(
        "\n", ""
    )


def shorten_path(file_path, length) -> Path:
    return Path(*Path(file_path).parts[-length:])


class Directory:
    def __init__(self, config):
        self.username_enable = get_key(config, "username", "enable")
        self.hostname_enable = get_key(config, "hostname", "enable")
        self.truncate_value = get_key(config, "directory", "truncation_length")
        self.symbol = symbol_ssh(get_key(config, "directory", "symbol"), "")
        self.color = (
            get_key(config, "directory", "color")
            if get_key(config, "general", "color", "enable") is True
            else "negative"
        )
        self.prefix_color = get_key(config, "directory", "prefix", "color")
        self.prefix_text = element_spacing(
            get_key(config, "directory", "prefix", "text")
        )

    def __str__(self, prefix="", space_elem=" "):
        if str_empty_in(
            self.username_enable,
            self.hostname_enable,
            self.truncate_value,
            self.symbol,
            self.prefix_color,
            self.prefix_text,
        ):
            return ""

        if (
            self.username_enable is True
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
        dir_truncate = str(shorten_path(get_pwd(), self.truncate_value))

        if dir_truncate.split("/")[-1:] == str(Path.home()).split("/")[-1:]:
            dir_truncate = "~"
        return (
            f"{prefix}{Color(self.color)}{self.symbol}"
            f"{dir_truncate}{space_elem}{Color().NONE}"
        )
