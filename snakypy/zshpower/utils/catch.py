import os
from contextlib import suppress
from os.path import exists, isdir
from re import M as re_m
from re import search as re_search

from docopt import docopt
from snakypy.helpers.ansi import FG, NONE

from snakypy.zshpower import __info__
from snakypy.zshpower.config import menu


def read_zshrc(zshrc) -> str:
    try:
        with open(zshrc) as f:
            return f.read()
    except FileNotFoundError as err:
        raise FileNotFoundError("File not found.", err)


def arguments(argv=None) -> dict:
    formatted_version = (
        f"{__info__['name']} version: {FG().CYAN}{__info__['version']}{NONE}"
    )
    data = docopt(menu.options, argv=argv, version=formatted_version)
    return data


def read_zshrc_omz(zshrc) -> tuple:
    """ """
    current_zshrc = read_zshrc(zshrc)
    m = re_search(r"ZSH_THEME=\".*", current_zshrc)
    if m is not None:
        var_zsh_theme = m.group(0)
        lst = var_zsh_theme.split("=")
        theme_name = [s.strip('"') for s in lst][1]
        return theme_name, var_zsh_theme
    return ()


def plugins_current_zshrc(zshrc) -> list:
    current_zshrc = read_zshrc(zshrc)
    m = re_search(r"^plugins=\(.*", current_zshrc, flags=re_m)
    if m is not None:
        get = m.group(0)
        lst = get.split("=")
        current = [i.strip('"').replace("(", "").replace(")", "") for i in lst][1]
        return current.split()
    return []


def get_line_source(zshrc) -> str:
    current_zshrc = read_zshrc(zshrc)
    m = re_search(r"source \$HOME/.zshpower", current_zshrc)
    if m is not None:
        return m.group(0)
    return ""


def verify_objects(directory, /, files=(), folders=(), extension=()) -> bool:
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
