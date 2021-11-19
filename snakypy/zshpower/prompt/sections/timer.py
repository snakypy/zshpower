from time import strftime

from snakypy.zshpower.prompt.sections.utils import Color, symbol_ssh
from snakypy.zshpower.utils.catch import recursive_get


class Timer:
    def __init__(self, config):
        self.enable = recursive_get(config, "timer", "enable")
        self.symbol = symbol_ssh(recursive_get(config, "timer", "symbol"), "T:")
        self.color = (
            recursive_get(config, "timer", "color")
            if recursive_get(config, "general", "color", "enable") is True
            else "negative"
        )
        self.seconds_enable = recursive_get(config, "timer", "seconds", "enable")

    def __str__(self):
        if self.enable:
            get_timer = str(strftime("%H:%M"))
            if self.seconds_enable:
                get_timer = str(strftime("%H:%M:%S"))
            timer = f"{Color(self.color)}{self.symbol}" f"{get_timer}{Color().NONE}"
            return timer.strip()
        return ""
