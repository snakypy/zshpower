from typing import Any

from snakypy.zshpower.prompt.sections.utils import Color, symbol_ssh
from snakypy.zshpower.utils.catch import get_key


class Took:
    def __init__(self, config: dict, took: Any = 0):
        self.enable = get_key(config, "took", "enable")
        self.symbol = symbol_ssh(get_key(config, "took", "symbol"), "")
        self.text = get_key(config, "took", "text")
        self.color = (
            get_key(config, "took", "color")
            if get_key(config, "general", "color", "enable") is True
            else "negative"
        )
        self.involved = get_key(config, "took", "involved")
        self.show_greater_than = get_key(config, "took", "show_greater_than")
        self.took = str(took)

    def format_took(self) -> str:
        if self.took and len(self.took) == 7:
            if self.took[0] == "0" and self.took[4] == "0":
                return f"{self.took[1:3]} {self.took[5:]}"
            elif self.took[0] == "0":
                return f"{self.took[1:3]} {self.took[4:]}"
            elif self.took[4] == "0":
                return f"{self.took[0:3]} {self.took[5:]}"
        else:
            if self.took[0] == "0":
                return self.took[1:3]
        return self.took

    def show(self):
        took_current = (
            f" {Color(self.color)}{self.symbol}{self.text} "
            f"{Color().NONE}{self.format_took()}"
        )
        if len(self.involved) == 2:
            took_current = (
                f" {self.involved[0]}{Color(self.color)}{self.symbol}{self.text} "
                f"{Color().NONE}{self.format_took()}{self.involved[1]}"
            )
        return took_current

    def __str__(self):
        if self.enable:
            if len(str(self.took)) == 7:
                return self.show()
            else:
                verify_seconds = f"{self.format_took()[:-1]}"
                if verify_seconds > str(self.show_greater_than):
                    return self.show()

        return ""
