from os import environ as os_environ
from .lib.utils import symbol_ssh, element_spacing
from .lib.utils import Color, separator


def get_virtualenv_name():
    if "VIRTUAL_ENV" in os_environ:
        venv_name = os_environ["VIRTUAL_ENV"].split("/")[-1]
        # Treatment for virtual machines created with Poetry
        if "-" in venv_name:
            return "-".join(venv_name.split("-")[:-2])
    return ""


class Virtualenv:
    def __init__(self, config):
        self.config = config
        self.symbol = symbol_ssh(config["virtualenv"]["symbol"], "")
        self.involved = config["virtualenv"]["involved"]
        self.color = config["virtualenv"]["color"]
        self.prefix_color = config["virtualenv"]["prefix"]["color"]
        self.prefix_text = element_spacing(config["virtualenv"]["prefix"]["text"])
        self.name_enable = config["virtualenv"]["name"]["normal"]["enable"]
        self.name_text = config["virtualenv"]["name"]["text"]

    def __str__(self, space_elem=" "):
        involved_prefix = ""
        involved_suffix = ""

        if "VIRTUAL_ENV" in os_environ:
            prefix = (
                f"{Color(self.prefix_color)}"
                f"{self.prefix_text}{Color().NONE}"
            )

            if len(self.involved) == 2:
                involved_prefix = self.involved[0]
                involved_suffix = self.involved[1]

            if self.name_enable:
                ret = (
                    f"{separator(self.config)}{prefix}{Color(self.color)}"
                    f"{self.symbol}"
                    f"{involved_prefix}{get_virtualenv_name()}{involved_suffix}"
                    f"{space_elem}{Color().NONE}"
                )
            else:
                ret = (
                    f"{separator(self.config)}{prefix}{Color(self.color)}"
                    f"{self.symbol}"
                    f"{involved_prefix}{self.name_text}{involved_suffix}"
                    f"{space_elem}{Color().NONE}"
                )
            return str(ret)
        return ""
