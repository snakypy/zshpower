from snakypy.zshpower.utils.catch import get_key

from .utils import Color, symbol_ssh


class Command:
    def __init__(self, config):
        self.config = config
        self.symbol = symbol_ssh(get_key(config, "command", "symbol"), "> ")
        self.error_symbol = symbol_ssh(
            get_key(config, "command", "error", "symbol"), "x "
        )
        self.error_color = get_key(config, "command", "error", "color")
        self.color = (
            get_key(config, "command", "color")
            if get_key(config, "general", "color", "enable") is True
            else "negative"
        )
        self.new_line = get_key(config, "command", "new_line", "enable")

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
