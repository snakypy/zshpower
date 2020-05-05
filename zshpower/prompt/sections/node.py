from .lib.utils import Color
from os.path import isfile, isdir, join
from os import getcwd
from .lib.utils import Color, symbol_ssh, separator, element_spacing
from zshpower.utils.process import shell_command


class NodeJs(Color):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.package_json = join(getcwd(), "package.json")
        self.node_modules = join(getcwd(), "node_modules")
        self.node_version_enable = config["nodejs"]["version"]["enable"]
        self.node_version_micro_enable = config["nodejs"]["version"]["micro"]["enable"]
        self.node_symbol = symbol_ssh(config["nodejs"]["symbol"], "node-")
        self.node_color = config["nodejs"]["color"]
        self.node_prefix_color = config["nodejs"]["prefix"]["color"]
        self.node_prefix_text = element_spacing(config["nodejs"]["prefix"]["text"])

    def get_version(self, space_elem=" "):
        tool = {
            "node": shell_command("node", "node -v 2>/dev/null"),
            "nodejs": shell_command("nodejs", "nodejs -v 2>/dev/null"),
            "nodenv": shell_command("nodenv", "nodenv version-name"),
        }
        lst_version = ""
        if tool["nodenv"]:
            if tool["nodenv"][0] == "system" or tool["nodenv"][0] == "node":
                lst_version = tool["node"][0].split(".")
            else:
                lst_version = tool["nodenv"][0].split(".")
        elif tool["node"]:
            lst_version = tool["node"][0].split(".")
        elif tool["nodejs"]:
            lst_version = tool["nodejs"][0].split(".")

        if not self.node_version_micro_enable:
            return f"{'.'.join(lst_version[:-1])}{space_elem}".replace("v", "")
        return f"{'.'.join(lst_version)}{space_elem}".replace("v", "")

    def __str__(self):
        if self.node_version_enable:
            if isfile(self.package_json) or isdir(self.node_modules):
                node_prefix = (
                    f"{Color(self.node_prefix_color)}"
                    f"{self.node_prefix_text}{Color().NONE}"
                )
                node_export = (
                    f"{separator(self.config)}{node_prefix}"
                    f"{Color(self.node_color)}"
                    f"{self.node_symbol}{self.get_version()}{Color().NONE}"
                )
                return str(node_export)
        return ""
