from time import strftime

from snakypy.zshpower.prompt.sections.utils import Color, symbol_ssh
from snakypy.zshpower.utils.catch import get_key


class Timer:
    def __init__(self, config):
        self.enable = get_key(config, "timer", "enable")
        self.symbol = symbol_ssh(get_key(config, "timer", "symbol"), "T:")
        self.color = (
            get_key(config, "timer", "color")
            if get_key(config, "general", "color", "enable") is True
            else "negative"
        )
        self.seconds_enable = get_key(config, "timer", "seconds", "enable")

    def __str__(self):
        if self.enable:
            get_timer = str(strftime("%H:%M"))
            if self.seconds_enable:
                get_timer = str(strftime("%H:%M:%S"))
            timer = f"{Color(self.color)}{self.symbol}" f"{get_timer}{Color().NONE}"
            return timer.strip()
        return ""
