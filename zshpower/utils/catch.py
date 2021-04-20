from os import popen as os_popen, getuid as os_getuid
from snakypy import printer
from re import search as re_search
from zshpower.config import package
from zshpower import __version__
from re import M as re_m
from snakypy.ansi import FG, NONE
from docopt import docopt
from zshpower.config import menu

try:
    import pwd
except ImportError:
    pass


def read_zshrc(zshrc):
    try:
        with open(zshrc) as f:
            return f.read()
    except FileNotFoundError as fnf_err:
        printer(f"File not found {fnf_err}", foreground=FG.ERROR)


def arguments(argv=None):
    formatted_version = f"{package.info['name']} version: {FG.CYAN}{__version__}{NONE}"
    data = docopt(menu.options, argv=argv, version=formatted_version)
    return data


def read_zshrc_omz(zshrc):
    """ """
    current_zshrc = read_zshrc(zshrc)
    m = re_search(r"ZSH_THEME=\".*", current_zshrc)
    if m is not None:
        var_zsh_theme = m.group(0)
        lst = var_zsh_theme.split("=")
        theme_name = [s.strip('"') for s in lst][1]
        return theme_name, var_zsh_theme
    return


def current_shell():
    pw = pwd.getpwuid(os_getuid())
    path_shell = pw[-1]
    shell = str(path_shell).split("/")[-1]
    return shell, path_shell


def current_user():
    return str(os_popen("whoami").read()).replace("\n", "")


def plugins_current_zshrc(zshrc):
    current_zshrc = read_zshrc(zshrc)
    m = re_search(r"^plugins=\(.*", current_zshrc, flags=re_m)
    if m is not None:
        get = m.group(0)
        lst = get.split("=")
        current = [i.strip('"').replace("(", "").replace(")", "") for i in lst][1]
        return current.split()
    return


def get_line_source(zshrc):
    """ """
    current_zshrc = read_zshrc(zshrc)
    m = re_search(r"source \$HOME/.zshpower", current_zshrc)
    if m is not None:
        return m.group(0)
    return
