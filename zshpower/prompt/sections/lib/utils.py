import os
from subprocess import check_output
# from snakypy import FG
# from snakypy.ansi import NONE as s_none


# class Color:
#     """Colors bash"""
#
#     NONE = s_none
#
#     def __init__(self, set_color="none"):
#         self.set_color = set_color
#         self.color = {"green": FG.GREEN,
#                       "red": FG.RED,
#                       "blue": FG.BLUE,
#                       "yellow": FG.YELLOW,
#                       "cyan": FG.CYAN,
#                       "magenta": FG.MAGENTA,
#                       "white": FG.WHITE,
#                       "black": FG.BLACK,
#                       "none": ""}
#
#     def __str__(self):
#         return self.color.get(self.set_color, "")


# class Color:
#     """Color application compatible only with Oh My ZSH."""
#     NONE = "%{$reset_color%}"
#
#     def __init__(self, set_color=None):
#         self.color = f"%{{$fg[{set_color}]%}}"
#
#     def __str__(self):
#         return self.color

class Color:
    """Color application compatible only ZSH."""
    NONE = "%f"

    def __init__(self, set_color=""):
        self.color = f"%F{{{set_color}}}"
        if set_color == "white":
            self.color = ""

    def __str__(self):
        return self.color


def symbol_ssh(symbol1, symbol2, spacing=" "):
    # TODO: Add icon in SSH by options true/false - Next version
    if symbol1 != "":
        symbol1 += spacing
    if "SSH_CONNECTION" in os.environ:
        symbol1 = symbol2
    return symbol1


def abspath_link():
    cwd = check_output("pwd -L", shell=True, universal_newlines=True).strip()
    return cwd


def git_status(*, porcelain=False, branch=False):
    porcelain_set = "--porcelain" if porcelain else ""
    branch_set = "--branch" if branch else ""
    if porcelain and not branch:
        status = check_output(f"git status {porcelain_set}",
                              shell=True, universal_newlines=True).split()
    elif branch and not porcelain:
        data = check_output(f"git status {branch_set}",
                            shell=True, universal_newlines=True).split()
        if data[0] == "HEAD":
            status = f"{Color('red')}HEAD{Color().NONE}"
        else:
            status = data[2]
    else:
        status = check_output(f"git status {porcelain_set} {branch_set}",
                              shell=True, universal_newlines=True).split()
    return status


def separator(config, spacing=" "):
    sep = config["general"]["separator"]["element"]
    sep += spacing if sep != "" else sep
    sep_color = config["general"]["separator"]["color"]
    separator_style = f"{Color(sep_color)}{sep}{Color().NONE}"
    return separator_style


def element_spacing(element, spacing=" "):
    if element != "":
        element += spacing
    return element
