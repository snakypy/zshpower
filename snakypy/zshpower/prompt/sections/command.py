from snakypy.zshpower.utils.catch import recursive_get

from .utils import Color, symbol_ssh


class Command:
    def __init__(self, config):
        self.config = config
        self.symbol = symbol_ssh(recursive_get(config, "command", "symbol"), "> ")
        self.error_symbol = symbol_ssh(
            recursive_get(config, "command", "error", "symbol"), "x "
        )
        self.error_color = recursive_get(config, "command", "error", "color")
        self.color = (
            recursive_get(config, "command", "color")
            if recursive_get(config, "general", "color", "enable") is True
            else "negative"
        )
        self.new_line = recursive_get(config, "command", "new_line", "enable")

    def __str__(self, jump_line="\n"):
        if not self.new_line:
            jump_line = ""
        return (
            f"{jump_line}{Color(self.color)}"
            f"%(?.{self.symbol}."
            f"{Color(self.error_color)}"
            f"{self.error_symbol})"
            f"{Color().NONE}"
        )
