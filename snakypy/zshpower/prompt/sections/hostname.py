from os import environ as os_environ
from socket import gethostname

from snakypy.zshpower.utils.catch import recursive_get

from .utils import Color, element_spacing, symbol_ssh


class Hostname:
    def __init__(self, config):

        self.config = config
        self.symbol = symbol_ssh(recursive_get(config, "hostname", "symbol"), "")
        self.hostname_enable = recursive_get(config, "hostname", "enable")
        self.hostname_color = recursive_get(config, "hostname", "color")
        self.hostname_prefix_color = recursive_get(
            config, "hostname", "prefix", "color"
        )
        self.hostname_prefix_text = element_spacing(
            recursive_get(config, "hostname", "prefix", "text")
        )

    def __str__(self, prefix="", space_elem=" "):
        if (
            recursive_get(self.config, "hostname", "enable")
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
