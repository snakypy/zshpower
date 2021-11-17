from os import getcwd, environ
from subprocess import check_output
from typing import List, Union

from snakypy.zshpower.database.dao import DAO
from snakypy.zshpower.utils.catch import verify_objects


def symbol_ssh(symbol1, symbol2, spacing=" ") -> list:
    if symbol1 != "":
        symbol1 += spacing
    if "SSH_CONNECTION" in environ:
        symbol1 = symbol2
    return symbol1


def git_status(*, porcelain=False, branch=False) -> Union[str, List[str]]:
    porcelain_set = "--porcelain" if porcelain else ""
    branch_set = "--branch" if branch else ""

    if porcelain and not branch:
        status: Union[str, List[str]] = check_output(
            f"git status {porcelain_set}", shell=True, universal_newlines=True
        ).split()
    elif branch and not porcelain:
        data = check_output(
            f"git status {branch_set}", shell=True, universal_newlines=True
        ).split()
        if data[0] == "HEAD":
            status = f"{Color('red')}HEAD{Color().NONE}"
        else:
            status = data[2]
    else:
        status = check_output(
            f"git status {porcelain_set} {branch_set}",
            shell=True,
            universal_newlines=True,
        ).split()
    return status


def separator(config, spacing=" ") -> str:
    sep = config["general"]["separator"]["element"]
    sep += spacing if sep != "" else sep
    sep_color = config["general"]["separator"]["color"]
    separator_style = f"{Color(sep_color)}{sep}{Color().NONE}"
    return separator_style


def element_spacing(element, spacing=" "):
    if element != "":
        element += spacing
    return element


class Color:
    """Color application compatible only ZSH."""

    NONE = "%f"

    def __init__(self, set_color=""):
        self.color = f"%F{{{set_color}}}"
        if set_color == "negative":
            self.color = ""

    def __str__(self):
        return self.color


class Version(DAO):
    def __init__(self):
        DAO.__init__(self)
        self.extensions = ()
        self.files = ()
        self.folders = ()

    def get(self, config, reg_version: dict, key="", ext="", space_elem="") -> str:
        enable = config[key]["version"]["enable"]
        symbol = symbol_ssh(config[key]["symbol"], ext)
        color = (
            config[key]["color"]
            if config["general"]["color"]["enable"] is True
            else "negative"
        )
        prefix_color = config[key]["prefix"]["color"]
        prefix_text = element_spacing(config[key]["prefix"]["text"])
        micro_version_enable = config[key]["version"]["micro"]["enable"]

        if enable:
            if reg_version[key] and verify_objects(
                getcwd(),
                files=self.files,
                folders=self.folders,
                extension=self.extensions,
            ):
                prefix = f"{Color(prefix_color)}{prefix_text}{Color().NONE}"

                if micro_version_enable:
                    version_format = f"{'{0[0]}.{0[1]}.{0[2]}'.format(reg_version[key].split('.'))}{space_elem}"
                else:
                    version_format = f"{'{0[0]}.{0[1]}'.format(reg_version[key].split('.'))}{space_elem}"

                return str(
                    (
                        f"{separator(config)}{prefix}"
                        f"{Color(color)}{symbol}"
                        f"{version_format}{Color().NONE}"
                    )
                )
        return ""

    def set(self, version, key="", action=None) -> bool:
        if action:
            # Conditions
            if action == "insert":
                query = DAO().select_where(
                    self.tbl_main, key, "name", select=("version",)
                )
                if not query:
                    DAO().insert(
                        self.tbl_main,
                        columns=("name", "version"),
                        values=(key, version),
                    )

            elif action == "update":
                DAO().update(self.tbl_main, "version", version, "name", key)
            return True
        return False
