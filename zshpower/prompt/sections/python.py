from sys import version_info as sys_version_info
from zshpower.prompt.sections.lib.utils import symbol_ssh, element_spacing
from zshpower.prompt.sections.lib.utils import Color, separator
from zshpower.utils.catch import find_objects
from zshpower.utils.check import is_tool
from os import environ as os_environ, getcwd


class Python:
    def __init__(self, config):

        self.config = config
        self.enable = config["python"]["version"]["enable"]
        self.files = (
            "__pycache__",
            "manage.py",
            "setup.py",
            "__init__.py",
            ".python-version",
            "requirements.txt",
            "pyproject.toml",
        )
        self.folders = ("__pycache__",)
        self.extensions = (".py",)
        self.symbol = symbol_ssh(config["python"]["symbol"], "py-")
        self.color = config["python"]["color"]
        self.prefix_color = config["python"]["prefix"]["color"]
        self.prefix_text = element_spacing(config["python"]["prefix"]["text"])
        self.micro_version_enable = config["python"]["version"]["micro"]["enable"]

    def get_version(self, space_elem=" "):

        if not self.micro_version_enable:
            return f"{'{0[0]}.{0[1]}'.format(sys_version_info)}{space_elem}"
        return f"{'{0[0]}.{0[1]}.{0[2]}'.format(sys_version_info)}{space_elem}"

    def __str__(self):

        if self.enable:
            if is_tool("python", f"python{'{0[0]}'.format(sys_version_info)}"):
                if (
                    find_objects(
                        getcwd(),
                        files=self.files,
                        folders=self.folders,
                        extension=self.extensions,
                    )
                    or "VIRTUAL_ENV" in os_environ
                ):
                    prefix = f"{Color(self.prefix_color)}{self.prefix_text}{Color().NONE}"

                    return str(
                        f"{separator(self.config)}{prefix}"
                        f"{Color(self.color)}{self.symbol}"
                        f"{self.get_version()}{Color().NONE}"
                    )
        return ""


# def _python(config):
#     import concurrent.futures
#
#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         future = executor.submit(Python, config)
#         return_value = future.result()
#         return return_value
