import os
from .lib.utils import Color


class Command:
    def __init__(self, config):
        self.config = config
        self.cmd_symbol = config["command"]["symbol"]
        self.cmd_color = config["command"]["color"]
        self.cmd_new_line = config["command"]["new_line"]["enable"]

    def __str__(self, jump_line=" ", spacing=" "):
        if self.cmd_new_line:
            jump_line = "\n"
        input_export = (
            f"{jump_line}{Color(self.cmd_color)}"
            f"{self.cmd_symbol}{spacing}{Color().NONE}"
        )
        if "SSH_CONNECTION" in os.environ:
            input_export = f"{jump_line}{Color(self.cmd_color)}>{spacing}{Color().NONE}"
        return str(input_export)
