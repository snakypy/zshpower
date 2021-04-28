from os import geteuid as os_geteuid


class Username:
    def __init__(self, config):
        from .lib.utils import symbol_ssh

        self.symbol = symbol_ssh(config["username"]["symbol"], "")
        self.username_enable = config["username"]["enable"]
        self.username_color = config["username"]["color"]
        if os_geteuid() == 0:
            self.username_color = "red"

    def __str__(self, space_elem=" "):
        from os import environ as os_environ
        from zshpower.utils.catch import current_user
        from .lib.utils import Color

        if self.username_enable or "SSH_CONNECTION" in os_environ or os_geteuid() == 0:
            user = current_user()
            username_export = f"{Color(self.username_color)}{self.symbol}{user}{space_elem}{Color().NONE}"
            return str(username_export)
        return ""
