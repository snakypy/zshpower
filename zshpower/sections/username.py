import os
from zshpower import utils
from .lib.utils import Color


class Username(Color):
    def __init__(self, config):
        super().__init__()
        self.username_enable = config["username"]["enable"]
        self.username_color = config["username"]["color"]
        if os.geteuid() == 0:
            self.username_color = "red"

    def __str__(self, space_elem=" "):
        if "SSH_CONNECTION" in os.environ or self.username_enable or os.geteuid() == 0:
            user = utils.current_user()
            username_export = (
                f"{Color(self.username_color)}{user}{space_elem}{Color().NONE}"
            )
            return str(username_export)
        return ""
