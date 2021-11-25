import os
from contextlib import suppress
from functools import reduce
from os.path import exists, isdir
from re import M
from re import search as re_search
from typing import Union

from docopt import docopt
from snakypy.helpers.ansi import FG, NONE
from snakypy.helpers.logging import Log

from snakypy.zshpower import __info__
from snakypy.zshpower.config import menu


def get_key(d, *keys) -> Union[str, bool]:
    """
    Function to get keys from a dictionary recursively without errors.
    If the key does not exist it returns an empty dictionary.

    Args:
        d ([dict]): Receive a dictionary

    Returns:
        [str, bool]: Returning a str or a boolean if the object is True or False.
    """
    data = reduce(lambda c, k: c.get(k, {}), keys, d)
    if data == {}:
        return ""
    return data


def read_file_log(file, logfile) -> str:
    """
    Read a file with log creation option if it does not exist
    """
    try:
        with open(file) as f:
            return f.read()
    except FileNotFoundError as err:
        Log(filename=logfile).record(
            f"The {file} file was not found.", colorize=True, level="error"
        )
        raise FileNotFoundError(f"The {file} file was not found.", err)


def arguments(argv=None) -> dict:
    formatted_version = (
        f"{__info__['name']} version: {FG().CYAN}{__info__['version']}{NONE}"
    )
    data = docopt(menu.options, argv=argv, version=formatted_version)
    return data


def get_zsh_theme(file, logfile) -> Union[tuple, bool]:
    """
    Get the current theme contained in the .zshrc file if using Oh My ZSH
    """
    current_file = read_file_log(file, logfile)
    m = re_search(r"ZSH_THEME=\".*", current_file)
    if m is not None:
        theme_var = m.group(0)
        lst = theme_var.split("=")
        theme_name = [s.strip('"') for s in lst][1]
        return theme_name, theme_var
    return False


def current_plugins(file, logfile) -> list:
    """
    Get current plugins from .zshrc file if using Oh My ZSH
    """
    current_file = read_file_log(file, logfile)
    m = re_search(r"^plugins=\(.*", current_file, flags=M)
    if m is not None:
        get = m.group(0)
        lst = get.split("=")
        current = [i.strip('"').replace("(", "").replace(")", "") for i in lst][1]
        return current.split()
    return []


def get_line(file, line, logfile) -> Union[str, bool]:
    """
    Get a given line from a given file
    """
    current_file = read_file_log(file, logfile)
    m = re_search(rf"{line}", current_file)
    if m is not None:
        return m.group(0)
    return False


def verify_objects(directory, /, files=(), folders=(), extension=()) -> bool:
    """
    Checks whether there are objects from a particular directory.
    These can be folders, files and file extensions.
    """
    with suppress(PermissionError):
        for file in os.listdir(directory):
            if folders:
                for i in folders:
                    if isdir(i):
                        return True
            if extension:
                for i in extension:
                    obj = os.path.join(directory, i)
                    if not isdir(obj) and file.endswith(i):
                        return True
        if files:
            for i in files:
                if exists(os.path.join(directory, i)):
                    return True
    return False
