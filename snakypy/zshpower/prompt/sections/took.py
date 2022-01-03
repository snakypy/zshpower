from datetime import timedelta

from snakypy.zshpower.prompt.sections.utils import Color, symbol_ssh
from snakypy.zshpower.utils.catch import get_key


class Took:
    def __init__(self, config: dict, elapsed: float = 0.0):
        self.enable = get_key(config, "took", "enable")
        self.symbol: str = symbol_ssh(get_key(config, "took", "symbol"), "")
        self.text: str = get_key(config, "took", "text")
        self.color: str = (
            get_key(config, "took", "color")
            if get_key(config, "general", "color", "enable") is True
            else "negative"
        )
        self.involved: str = get_key(config, "took", "involved")
        self.show_greater_than: str = get_key(config, "took", "show_greater_than")
        self.elapsed: float = elapsed

    def format_took(self) -> str:
        # split_timer out: ["00", "00", "00"] (H:M:S)
        split_timer = str(timedelta(seconds=self.elapsed)).split(":")
        if int(split_timer[0]) > 0:
            return f"{split_timer[0]}h {split_timer[1]}m {split_timer[2]}s"
        elif int(split_timer[1]) > 0:
            return f"{split_timer[1]}m {split_timer[2]}s"
        else:
            return f"{split_timer[2]}s"

    def show(self) -> str:
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
            split_timer = self.format_took().split(" ")
            seconds = int(self.format_took().split(" ")[-1].replace("s", ""))
            if len(split_timer) == 3 or len(split_timer) == 2:
                return self.show()
            else:
                if seconds > float(self.show_greater_than):
                    return self.show()
        return ""
