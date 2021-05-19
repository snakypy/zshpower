from snakypy.zshpower.prompt.sections.lib.utils import symbol_ssh
from snakypy.zshpower.prompt.sections.lib.utils import Color


class Took:
    def __init__(self, config, timer_took=""):
        self.enable = config["took"]["enable"]
        self.symbol = symbol_ssh(config["took"]["symbol"], "")
        self.text = config["took"]["text"]
        self.color = config["took"]["color"]
        self.involved = config["took"]["involved"]
        self.show_greater_than = config["took"]["show_greater_than"]
        self.timer_took = str(timer_took)

    def format_timer(self) -> str:
        if self.timer_took and len(self.timer_took) == 7:
            if self.timer_took[0] == "0" and self.timer_took[4] == "0":
                return f"{self.timer_took[1:3]} {self.timer_took[5:]}"
            elif self.timer_took[0] == "0":
                return f"{self.timer_took[1:3]} {self.timer_took[4:]}"
            elif self.timer_took[4] == "0":
                return f"{self.timer_took[0:3]} {self.timer_took[5:]}"
        else:
            if self.timer_took[0] == "0":
                return self.timer_took[1:3]
        return self.timer_took

    def __str__(self):
        if self.enable:

            verify_seconds = f"{self.format_timer()[:-1]}"

            if len(str(self.timer_took)) == 7:
                verify_seconds = f"{self.format_timer().split()[1].replace('s', '')}"

            if verify_seconds > str(self.show_greater_than):

                timer_took = f"{Color().NONE}{self.format_timer()}"

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
