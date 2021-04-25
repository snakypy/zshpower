from os import environ as os_environ


def get_virtualenv_name():
    if "VIRTUAL_ENV" in os_environ:
        venv_name = os_environ["VIRTUAL_ENV"].split("/")[-1]
        # Treatment for virtual machines created with Poetry
        if "-" in venv_name:
            venv_name = "-".join(venv_name.split("-")[:-2])
        return venv_name
    return ""


class Virtualenv:
    def __init__(self, config):
        from .lib.utils import symbol_ssh, element_spacing

        self.config = config
        self.venv_symbol = symbol_ssh(config["virtualenv"]["symbol"], "")
        self.venv_involved = config["virtualenv"]["involved"]
        self.venv_color = config["virtualenv"]["color"]
        self.venv_prefix_color = config["virtualenv"]["prefix"]["color"]
        self.venv_prefix_text = element_spacing(config["virtualenv"]["prefix"]["text"])
        self.venv_name_enable = config["virtualenv"]["name"]["normal"]["enable"]
        self.venv_name_text = config["virtualenv"]["name"]["text"]

    def __str__(self, space_elem=" "):
        from .lib.utils import Color, separator

        involved_prefix = ""
        involved_suffix = ""

        if "VIRTUAL_ENV" in os_environ:
            env_prefix = (
                f"{Color(self.venv_prefix_color)}"
                f"{self.venv_prefix_text}{Color().NONE}"
            )
            if len(self.venv_involved) == 2:
                involved_prefix = self.venv_involved[0]
                involved_suffix = self.venv_involved[1]
            if self.venv_name_enable:
                virtualenv = (
                    f"{separator(self.config)}{env_prefix}{Color(self.venv_color)}"
                    f"{self.venv_symbol}"
                    f"{involved_prefix}{get_virtualenv_name()}{involved_suffix}"
                    f"{space_elem}{Color().NONE}"
                )
            else:
                virtualenv = (
                    f"{separator(self.config)}{env_prefix}{Color(self.venv_color)}"
                    f"{self.venv_symbol}"
                    f"{involved_prefix}{self.venv_name_text}{involved_suffix}"
                    f"{space_elem}{Color().NONE}"
                )
            return str(virtualenv)
        return ""
