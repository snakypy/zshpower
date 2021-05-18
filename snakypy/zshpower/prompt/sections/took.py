from snakypy.zshpower.prompt.sections.lib.utils import symbol_ssh
from snakypy.zshpower.prompt.sections.lib.utils import Color


class Took:
    def __init__(self, config, timer_took=0):
        self.enable = config["took"]["enable"]
        self.symbol = symbol_ssh(config["took"]["symbol"], "")
        self.text = config["took"]["text"]
        self.color = config["took"]["color"]
        self.involved = config["took"]["involved"]
        self.show_greater_than = config["took"]["show_greater_than"]
        self.timer_took = timer_took

    def __str__(self):
        if self.enable:

            if int(self.timer_took) > int(self.show_greater_than):

                timer_took = f"{Color().NONE}{self.timer_took}s"
                timer_took_format = (
                    f" {Color(self.color)}{self.symbol}{self.text} "
                    f"{timer_took}{Color().NONE}"
                )

                if len(self.involved) == 2:
                    timer_took_format = (
                        f" {self.involved[0]}{Color(self.color)}{self.symbol}{self.text} "
                        f"{timer_took}{Color().NONE}{self.involved[1]}"
                    )

                return timer_took_format

        return ""
