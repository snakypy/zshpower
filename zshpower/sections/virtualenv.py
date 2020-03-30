import os
from .lib.utils import Color, separator, choice_symbol


def get_virtualenv_name():
    if "VIRTUAL_ENV" in os.environ:
        venv_name = os.environ["VIRTUAL_ENV"].split("/")[-1]
        # Treatment for virtual machines created with Poetry
        venv_name = "-".join(venv_name.split("-")[:-2])
        return venv_name
    return ""


class Virtualenv(Color):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.venv_enable = config["virtualenv"]["enable"]
        self.venv_symbol = choice_symbol(config["virtualenv"]["symbol"], "")
        self.venv_color = config["virtualenv"]["color"]
        self.venv_prefix_color = config["virtualenv"]["prefix"]["color"]
        self.venv_prefix_text = config["virtualenv"]["prefix"]["text"]
        self.venv_name_enable = config["virtualenv"]["name"]["normal"]["enable"]
        self.venv_name_text = config["virtualenv"]["name"]["text"]

    def __str__(self, space_elem=" "):
        if "VIRTUAL_ENV" in os.environ and self.venv_enable:
            env_prefix = (
                f"{Color(self.venv_prefix_color)}"
                f"{self.venv_prefix_text}{Color().NONE}"
            )
            if self.venv_name_enable:
                virtualenv = (
                    f"{separator(self.config)}{env_prefix}{Color(self.venv_color)}"
                    f"{self.venv_symbol}{get_virtualenv_name()}{space_elem}"
                    f"{Color().NONE}"
                )
            else:
                virtualenv = (
                    f"{separator(self.config)}{env_prefix}{Color(self.venv_color)}"
                    f"{self.venv_symbol}{self.venv_name_text}{space_elem}"
                    f"{Color().NONE}"
                )
            return str(virtualenv)
        return ""
