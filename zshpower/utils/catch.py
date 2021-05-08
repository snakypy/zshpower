import pwd
import os
from re import search as re_search
from snakypy.ansi import FG, NONE
from zshpower.config import menu
from docopt import docopt
from zshpower import __version__
from zshpower.config import package
from os import getuid
from os import popen
from re import M as re_m
from os.path import exists, isdir
from contextlib import suppress


def read_zshrc(zshrc) -> str:
    try:
        with open(zshrc) as f:
            return f.read()
    except FileNotFoundError as err:
        raise FileNotFoundError("File not found.", err)


def arguments(argv=None) -> dict:
    formatted_version = f"{package.info['name']} version: {FG.CYAN}{__version__}{NONE}"
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


def current_shell() -> tuple:
    pw = pwd.getpwuid(getuid())
    path_shell = pw[-1]
    shell = str(path_shell).split("/")[-1]
    return shell, path_shell


def current_user() -> str:
    return str(popen("whoami").read()).replace("\n", "")


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


def find_objects(directory, /, files=(), folders=(), extension=()) -> bool:
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
