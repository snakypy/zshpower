from snakypy.zshpower.prompt.sections.lib.utils import symbol_ssh
from snakypy.zshpower.prompt.sections.lib.utils import Color



class Took:
    def __init__(self, config, took=0):
        self.enable = config["took"]["enable"]
        self.symbol = symbol_ssh(config["took"]["symbol"], "")
        self.text = config["took"]["text"]
        self.color = config["took"]["color"]
        self.involved = config["took"]["involved"]
        self.show_greater_than = config["took"]["show_greater_than"]
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
        timer_took_format = (
            f" {Color(self.color)}{self.symbol}{self.text} "
            f"{Color().NONE}{self.format_took()}"
        )

        if len(self.involved) == 2:
            timer_took_format = (
                f" {self.involved[0]}{Color(self.color)}{self.symbol}{self.text} "
                f"{Color().NONE}{self.format_took()}{self.involved[1]}"
            )

        return timer_took_format


    def __str__(self):
        if self.enable:
            if len(str(self.took)) == 7:
                return self.show()
            else:
                verify_seconds = f"{self.format_took()[:-1]}"
                if verify_seconds > str(self.show_greater_than):
                    return self.show()

        return ""
