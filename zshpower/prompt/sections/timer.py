class Timer:
    def __init__(self, config):
        from .lib.utils import symbol_ssh

        self.symbol = symbol_ssh(config["timer"]["symbol"], "T:")
        self.color = config["timer"]["color"]
        self.seconds_enable = config["timer"]["seconds"]["enable"]

    def __str__(self):
        from .lib.utils import Color
        from time import strftime

        c = Color()
        get_timer = str(strftime("%H:%M"))
        if self.seconds_enable:
            get_timer = str(strftime("%H:%M:%S"))
        timer = f"{Color(self.color)}{self.symbol}" f"{get_timer}{c.NONE}"
        return timer.strip()
