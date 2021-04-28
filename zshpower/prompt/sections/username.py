from os import geteuid
from .lib.utils import symbol_ssh
from os import environ as os_environ
from zshpower.utils.catch import current_user
from .lib.utils import Color


class Username:
    def __init__(self, config):
        self.symbol = symbol_ssh(config["username"]["symbol"], "")
        self.username_enable = config["username"]["enable"]
        self.username_color = config["username"]["color"]
        if geteuid() == 0:
            self.username_color = "red"

    def __str__(self, space_elem=" "):
        if self.username_enable or "SSH_CONNECTION" in os_environ or geteuid() == 0:
            return f"{Color(self.username_color)}{self.symbol}{current_user()}{space_elem}{Color().NONE}"
        return ""
