from os import geteuid as os_geteuid


class Username:
    def __init__(self, config):
        self.color = config["username"]["color"]
        if os_geteuid() == 0:
            self.color = "red"

    def __str__(self, space_elem=" "):
        from os import environ as os_environ
        from zshpower.utils.catch import current_user
        from .lib.utils import Color

        if "SSH_CONNECTION" in os_environ or os_geteuid() == 0:
            user = current_user()
            username = (
                f"{Color(self.color)}{user}{space_elem}{Color().NONE}"
            )
            return str(username)
        return ""
