from sys import version_info
from snakypy.zshpower.utils.catch import verify_objects
from snakypy.helpers.catches import is_tool
from snakypy.helpers.files import read_file
from os import environ, getcwd
from os.path import isfile, join, exists, isdir
from snakypy.zshpower import HOME
from snakypy.zshpower.prompt.sections.lib.utils import symbol_ssh, element_spacing
from snakypy.zshpower.prompt.sections.lib.utils import Color, separator


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

    def get_version(self, space_elem=" ") -> str:

        # Checking if you use Python through pyenv or the system.
        if isdir(join(HOME, ".pyenv")):
            if exists(join(getcwd(), self.files[4])):
                if read_file(join(getcwd(), self.files[4])).strip() == "system":
                    python_version = (
                        f"{'{0[0]}.{0[1]}.{0[2]}'.format(version_info)}".split(".")
                    )
                else:
                    python_version = (
                        read_file(join(getcwd(), self.files[4])).strip().split(".")
                    )
            else:
                if read_file(join(HOME, ".pyenv/version")).strip() == "system":
                    python_version = (
                        f"{'{0[0]}.{0[1]}.{0[2]}'.format(version_info)}".split(".")
                    )
                else:
                    python_version = (
                        read_file(join(HOME, ".pyenv/version")).strip().split(".")
                    )
        else:
            python_version = f"{'{0[0]}.{0[1]}.{0[2]}'.format(version_info)}".split(".")

        if not self.micro_version_enable:
            return f"{'{0[0]}.{0[1]}'.format(python_version)}{space_elem}"
        return f"{'{0[0]}.{0[1]}.{0[2]}'.format(python_version)}{space_elem}"

    def __str__(self):
        if self.enable:
            if is_tool("python"):
                if (
                    verify_objects(
                        getcwd(),
                        files=self.files,
                        folders=self.folders,
                        extension=self.extensions,
                    )
                    or "VIRTUAL_ENV" in environ
                ):
                    prefix = (
                        f"{Color(self.prefix_color)}{self.prefix_text}{Color().NONE}"
                    )

                    return str(
                        f"{separator(self.config)}{prefix}"
                        f"{Color(self.color)}{self.symbol}"
                        f"{self.get_version()}{Color().NONE}"
                    )
        return ""


class Virtualenv:
    def __init__(self, config):
        self.config = config
        self.enable = config["python"]["virtualenv"]["enable"]
        self.hash_enable = config["python"]["virtualenv"]["poetry"]["hash"]["enable"]
        self.py_enable = config["python"]["virtualenv"]["poetry"]["py"]["enable"]
        self.symbol = symbol_ssh(config["python"]["virtualenv"]["symbol"], "")
        self.involved = config["python"]["virtualenv"]["involved"]
        self.color = config["python"]["virtualenv"]["color"]
        self.prefix_color = config["python"]["virtualenv"]["prefix"]["color"]
        self.prefix_text = element_spacing(
            config["python"]["virtualenv"]["prefix"]["text"]
        )
        self.name_enable = config["python"]["virtualenv"]["name"]["normal"]["enable"]
        self.name_text = config["python"]["virtualenv"]["name"]["text"]

    def get_virtualenv(self) -> str:
        if "VIRTUAL_ENV" in environ:
            venv_path = environ["VIRTUAL_ENV"]
            # The "venv_hash" option is only for virtual machines created with
            # poetry, where it generates a hash in the name of the virtual machine.
            if not self.hash_enable and isfile(join(getcwd(), "pyproject.toml")):
                venv_path = environ["VIRTUAL_ENV"].split("/")[-1]
                if "-" in venv_path:
                    return "-".join(venv_path.split("-")[:-2])
            # The "pg_version" option is only for virtual machines created with
            # poetry, where it generates the current version of Python in the name
            # of the virtual machine.
            if not self.py_enable and isfile(join(getcwd(), "pyproject.toml")):
                if "-" in venv_path:
                    return "-".join(venv_path.split("/")[-1].split("-")[:-1])

            return venv_path.split("/")[-1]
        return ""

    def __str__(self, space_elem=" "):
        involved_prefix = ""
        involved_suffix = ""

        if self.enable:
            if "VIRTUAL_ENV" in environ:
                prefix = (
                    f"{Color(self.prefix_color)}" f"{self.prefix_text}{Color().NONE}"
                )
                if len(self.involved) == 2:
                    involved_prefix = self.involved[0]
                    involved_suffix = self.involved[1]

                if self.name_enable:
                    ret = (
                        f"{separator(self.config)}{prefix}{Color(self.color)}"
                        f"{self.symbol}"
                        f"{involved_prefix}{self.get_virtualenv()}{involved_suffix}"
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
