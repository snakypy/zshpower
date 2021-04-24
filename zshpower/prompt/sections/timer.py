class Timer:
    def __init__(self, config):
        from .lib.utils import symbol_ssh

        self.timer_enable = config["timer"]["enable"]
        self.timer_symbol = symbol_ssh(config["timer"]["symbol"], "T:")
        self.timer_color = config["timer"]["color"]
        self.timer_seconds_enable = config["timer"]["seconds"]["enable"]

    def __str__(self):
        from .lib.utils import Color
        from time import strftime

        if self.timer_enable:
            c = Color()
            get_timer = str(strftime("%H:%M"))
            if self.timer_seconds_enable:
                get_timer = str(strftime("%H:%M:%S"))
            timer = (
                f"{Color(self.timer_color)}{self.timer_symbol}" f"{get_timer}{c.NONE}"
            )
            return timer.strip()
        return ""
