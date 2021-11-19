from os import environ as os_environ
from os import geteuid

from snakypy.helpers.catches import whoami

from snakypy.zshpower.utils.catch import recursive_get

from .utils import Color, symbol_ssh


class Username:
    def __init__(self, config):
        self.symbol = symbol_ssh(recursive_get(config, "username", "symbol"), "")
        self.enable = recursive_get(config, "username", "enable")
        self.color = recursive_get(config, "username", "color")
        if geteuid() == 0:
            self.color = "red"

    def __str__(self, space_elem=" "):
        if self.enable or "SSH_CONNECTION" in os_environ or geteuid() == 0:
            return (
                f"{Color(self.color)}{self.symbol}{whoami()}{space_elem}{Color().NONE}"
            )
        return ""
