from snakypy.zshpower.utils.catch import recursive_get


class JumpLine:
    def __init__(self, config):
        self.enable = recursive_get(config, "general", "jump_line", "enable")

    def __str__(self):
        if not self.enable:
            return ""
        return "\n"
