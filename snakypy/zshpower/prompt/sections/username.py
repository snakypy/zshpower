from os import geteuid
from os import environ as os_environ
from snakypy.helpers.catches import whoami
from .lib.utils import symbol_ssh
from .lib.utils import Color


class Username:
    def __init__(self, config):
        self.symbol = symbol_ssh(config["username"]["symbol"], "")
        self.enable = config["username"]["enable"]
        self.color = config["username"]["color"]
        if geteuid() == 0:
            self.color = "red"

    def __str__(self, space_elem=" "):
        if self.enable or "SSH_CONNECTION" in os_environ or geteuid() == 0:
            return (
                f"{Color(self.color)}{self.symbol}{whoami()}{space_elem}{Color().NONE}"
            )
        return ""
