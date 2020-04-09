from socket import gethostname as socket_gethostname
from os import environ as os_environ
from .lib.utils import Color, element_spacing


class Hostname(Color):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.hostname_enable = self.config["hostname"]["enable"]
        self.hostname_color = self.config["hostname"]["color"]
        self.hostname_prefix_color = self.config["hostname"]["prefix"]["color"]
        self.hostname_prefix_text = element_spacing(
            self.config["hostname"]["prefix"]["text"]
        )

    def __str__(self, prefix="", space_elem=" "):
        if self.config["username"]["enable"] or "SSH_CONNECTION" in os_environ:
            prefix = (
                f"{Color(self.hostname_prefix_color)}"
                f"{self.hostname_prefix_text}"
                f"{Color().NONE}"
            )

        if "SSH_CONNECTION" in os_environ or self.hostname_enable:
            hostname_export = (
                f"{prefix}{Color(self.hostname_color)}"
                f"{socket_gethostname()}{space_elem}{Color().NONE}"
            )
            return str(hostname_export)

        return ""
