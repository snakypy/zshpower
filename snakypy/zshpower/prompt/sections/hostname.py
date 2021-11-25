from os import environ as os_environ
from socket import gethostname

from snakypy.zshpower.utils.catch import get_key

from .utils import Color, element_spacing, symbol_ssh


class Hostname:
    def __init__(self, config):

        self.config = config
        self.symbol = symbol_ssh(get_key(config, "hostname", "symbol"), "")
        self.hostname_enable = get_key(config, "hostname", "enable")
        self.hostname_color = get_key(config, "hostname", "color")
        self.hostname_prefix_color = get_key(config, "hostname", "prefix", "color")
        self.hostname_prefix_text = element_spacing(
            get_key(config, "hostname", "prefix", "text")
        )

    def __str__(self, prefix="", space_elem=" "):
        if (
            get_key(self.config, "hostname", "enable") is True
            or "SSH_CONNECTION" in os_environ
        ):
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
