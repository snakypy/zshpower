class Hostname:
    def __init__(self, config):
        from .lib.utils import element_spacing

        self.config = config
        self.hostname_color = self.config["hostname"]["color"]
        self.hostname_prefix_color = self.config["hostname"]["prefix"]["color"]
        self.hostname_prefix_text = element_spacing(
            self.config["hostname"]["prefix"]["text"]
        )

    def __str__(self, prefix="", space_elem=" "):
        from .lib.utils import Color
        from os import environ as os_environ
        from socket import gethostname as socket_gethostname

        if self.config["username"]["enable"] or "SSH_CONNECTION" in os_environ:
            prefix = (
                f"{Color(self.hostname_prefix_color)}"
                f"{self.hostname_prefix_text}"
                f"{Color().NONE}"
            )

        if "SSH_CONNECTION" in os_environ:
            hostname_export = (
                f"{prefix}{Color(self.hostname_color)}"
                f"{socket_gethostname()}{space_elem}{Color().NONE}"
            )
            return str(hostname_export)

        return ""
