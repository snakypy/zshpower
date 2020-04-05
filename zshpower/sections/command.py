from .lib.utils import Color, symbol_ssh


class Command:
    def __init__(self, config):
        self.config = config
        self.cmd_symbol = symbol_ssh(config["command"]["symbol"], "> ")
        self.cmd_color = config["command"]["color"]
        self.cmd_new_line = config["command"]["new_line"]["enable"]

    def __str__(self, jump_line="\n"):
        if not self.cmd_new_line:
            jump_line = ""
        cmd_export = (
            f"{jump_line}{Color(self.cmd_color)}" f"{self.cmd_symbol}{Color().NONE}"
        )
        return str(cmd_export)
