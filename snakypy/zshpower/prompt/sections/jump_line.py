from snakypy.zshpower.utils.catch import get_key


class JumpLine:
    def __init__(self, config: dict):
        self.enable: str = get_key(config, "general", "jump_line", "enable")

    def __str__(self):
        if self.enable:
            return "\n"
        return ""
