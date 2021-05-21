from os import environ as os_environ
from socket import gethostname

from .utils import Color, element_spacing, symbol_ssh


class Hostname:
    def __init__(self, config):

        self.config = config
        self.symbol = symbol_ssh(config["hostname"]["symbol"], "")
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
            return (
                f"{prefix}{Color(self.hostname_color)}{self.symbol}"
                f"{gethostname()}{space_elem}{Color().NONE}"
            )
        return ""
