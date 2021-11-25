from snakypy.zshpower.utils.catch import get_key


class JumpLine:
    def __init__(self, config):
        self.enable = get_key(config, "general", "jump_line", "enable")

    def __str__(self):
        if not self.enable:
            return ""
        return "\n"
