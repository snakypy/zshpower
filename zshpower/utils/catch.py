from os import popen as os_popen, getuid as os_getuid
from os.path import exists
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


def arguments(argv=None):
    formatted_version = f"{package.info['name']} version: {FG.CYAN}{__version__}{NONE}"
    data = docopt(menu.options, argv=argv, version=formatted_version)
    return data


def read_zshrc(zsh_rc):
    """ """
    if exists(zsh_rc):
        with open(zsh_rc) as r:
            content_ = r.read()
        m = re_search(r"ZSH_THEME=\".*", content_)
        if m is not None:
            zsh_theme = m.group(0)
            lst = zsh_theme.split("=")
            theme_name = [s.strip('"') for s in lst][1]
            return theme_name, content_, zsh_theme
    return False


def current_shell():
    pw = pwd.getpwuid(os_getuid())
    path_shell = pw[-1]
    shell = str(path_shell).split("/")[-1]
    return shell, path_shell


def current_user():
    return str(os_popen("whoami").read()).replace("\n", "")


def plugins_current_zshrc(zsh_rc):
    content_ = read_zshrc(zsh_rc)[1]
    m = re_search(r"^plugins=\(.*", content_, flags=re_m)
    if m is not None:
        get = m.group(0)
        lst = get.split("=")
        current = [i.strip('"').replace("(", "").replace(")", "") for i in lst][1]
        return current.split()
