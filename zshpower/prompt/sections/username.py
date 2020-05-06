from os import geteuid as os_geteuid
from os import environ as os_environ
from zshpower.utils.catch import current_user
from .lib.utils import Color


class Username:
    def __init__(self, config):
        self.username_enable = config["username"]["enable"]
        self.username_color = config["username"]["color"]
        if os_geteuid() == 0:
            self.username_color = "red"

    def __str__(self, space_elem=" "):
        if "SSH_CONNECTION" in os_environ or self.username_enable or os_geteuid() == 0:
            user = current_user()
            username_export = (
                f"{Color(self.username_color)}{user}{space_elem}{Color().NONE}"
            )
            return str(username_export)
        return ""
