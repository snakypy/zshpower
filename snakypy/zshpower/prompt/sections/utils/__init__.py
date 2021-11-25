from os import environ, getcwd
from subprocess import check_output
from typing import List, Union

from snakypy.helpers.catches.finders import is_tool

from snakypy.zshpower.database.dao import DAO
from snakypy.zshpower.utils.catch import get_key, verify_objects


def symbol_ssh(symbol1, symbol2, spacing=" ") -> str:
    if symbol1 != {}:
        if symbol1 != "":
            symbol1 += spacing
        if "SSH_CONNECTION" in environ:
            symbol1 = symbol2
        return symbol1
    return ""


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

    sep = get_key(config, "general", "separator", "element")
    if sep is not dict:
        sep += spacing if sep != "" else sep
        sep_color = get_key(config, "general", "separator", "color")
        if sep_color is not dict:
            separator_style = f"{Color(sep_color)}{sep}{Color().NONE}"
            return separator_style
    return ""


def element_spacing(element, spacing=" "):
    if element != {}:
        if element != "":
            element += spacing
        return element
    return ""


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
        self.verify_objects_dir = getcwd()

    def get(
        self,
        config,
        reg_version: dict,
        key="",
        ext="",
        space_elem="",
    ) -> str:
        enable = get_key(config, key, "version", "enable")
        symbol = symbol_ssh(get_key(config, key, "symbol"), ext)
        color = (
            get_key(config, key, "color")
            if get_key(config, "general", "color", "enable") is True
            else "negative"
        )
        prefix_color = get_key(config, key, "prefix", "color")
        prefix_text = element_spacing(get_key(config, key, "prefix", "text"))
        micro_version_enable = get_key(config, key, "version", "micro", "enable")

        if enable is True:
            if reg_version[key] and verify_objects(
                self.verify_objects_dir,
                files=self.files,
                folders=self.folders,
                extension=self.extensions,
            ):
                prefix = f"{Color(prefix_color)}{prefix_text}{Color().NONE}"

                if micro_version_enable is True:
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

    def set(self, command, version, exec_="", key="", action=None) -> bool:
        if is_tool(exec_) and action:
            # Conditions to save in database
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

            # Register logs
            if command.returncode != 0:
                self.log.record(
                    f"{key.title()} version not registered: {command.stderr}",
                    colorize=True,
                    level="error",
                )
            elif command.returncode == 0:
                self.log.record(
                    f"{key.title()} {version} registered in the database!",
                    colorize=True,
                    level="info",
                )

            return True
        return False
