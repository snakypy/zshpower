from zshpower.prompt.sections.lib.utils import symbol_ssh
from zshpower.prompt.sections.lib.utils import Color
from time import strftime


class Timer:
    def __init__(self, config):
        self.enable = config["timer"]["enable"]
        self.symbol = symbol_ssh(config["timer"]["symbol"], "T:")
        self.color = config["timer"]["color"]
        self.seconds_enable = config["timer"]["seconds"]["enable"]

    def __str__(self):
        if self.enable:
            get_timer = str(strftime("%H:%M"))
            if self.seconds_enable:
                get_timer = str(strftime("%H:%M:%S"))
            timer = f"{Color(self.color)}{self.symbol}" f"{get_timer}{Color().NONE}"
            return timer.strip()
        return ""
