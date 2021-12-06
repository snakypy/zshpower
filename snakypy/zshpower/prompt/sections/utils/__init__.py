from os import environ, getcwd
from subprocess import CompletedProcess, check_output
from typing import List, Union

from snakypy.helpers.catches.finders import is_tool

from snakypy.zshpower.database.dao import DAO
from snakypy.zshpower.utils.catch import get_key, verify_objects


def symbol_ssh(symbol1: str, symbol2: str, spacing: str = " ") -> str:
    if symbol1 != {}:
        if symbol1 != "":
            symbol1 += spacing
        if "SSH_CONNECTION" in environ:
            symbol1 = symbol2
        return symbol1
    return ""


def git_status(
    *, porcelain: bool = False, branch: bool = False
) -> Union[str, List[str]]:
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


def separator(config: dict, spacing: str = " ") -> str:

    sep = get_key(config, "general", "separator", "element")
    if sep is not dict:
        sep += spacing if sep != "" else sep
        sep_color = get_key(config, "general", "separator", "color")
        if sep_color is not dict:
            separator_style = f"{Color(sep_color)}{sep}{Color().NONE}"
            return separator_style
    return ""


def element_spacing(element: str, spacing: str = " "):
    if element != {}:
        if element != "":
            element += spacing
        return element
    return ""


class Color:
    """Color application compatible only ZSH."""

    NONE = "%f"

    def __init__(self, set_color: str = ""):
        self.color = f"%F{{{set_color}}}"
        if set_color == "negative":
            self.color = ""

    def __str__(self):
        return self.color


class Version(DAO):
    def __init__(self):
        DAO.__init__(self)
        self.finder_path = getcwd()
        self.finder = {"extensions": [], "folders": [], "files": []}

    def get(
        self,
        config: dict,
        database: dict,
        key: str = "",
        shorten: str = "",
        space_elem: str = "",
        not_split: bool = False,
    ) -> str:
        enable = get_key(config, key, "version", "enable")
        symbol = symbol_ssh(get_key(config, key, "symbol"), shorten)
        color = (
            get_key(config, key, "color")
            if get_key(config, "general", "color", "enable") is True
            else "negative"
        )
        prefix_color = get_key(config, key, "prefix", "color")
        prefix_text = element_spacing(get_key(config, key, "prefix", "text"))
        micro_version_enable = get_key(config, key, "version", "micro", "enable")

        if (
            enable is True
            and verify_objects(self.finder_path, data=self.finder) is True
        ):
            if get_key(database, key):
                prefix = f"{Color(prefix_color)}{prefix_text}{Color().NONE}"

                if not_split:
                    return str(
                        (
                            f"{separator(config)}{prefix}"
                            f"{Color(color)}{symbol}"
                            f"{get_key(database, key)}{space_elem}{Color().NONE}"
                        )
                    )

                if micro_version_enable is True:
                    version = f"{'{0[0]}.{0[1]}.{0[2]}'.format(get_key(database, key).split('.'))}{space_elem}"
                else:
                    version = f"{'{0[0]}.{0[1]}'.format(get_key(database, key).split('.'))}{space_elem}"

                return str(
                    (
                        f"{separator(config)}{prefix}"
                        f"{Color(color)}{symbol}"
                        f"{version}{Color().NONE}"
                    )
                )
        return ""

    def set(
        self,
        command: Union[CompletedProcess, CompletedProcess[str]],
        version: str,
        app_executable: str,
        key: str,
        action: str = "",
    ) -> bool:
        if is_tool(app_executable) and action:
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
