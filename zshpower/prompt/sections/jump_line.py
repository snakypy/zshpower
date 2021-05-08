class JumpLine:
    def __init__(self, config):
        self.enable = config["general"]["jump_line"]["enable"]

    def __str__(self):
        if not self.enable:
            return ""
        return "\n"
