from os import environ, getcwd
from os.path import isdir, join

from snakypy.zshpower.prompt.sections.utils import (
    Color,
    element_spacing,
    git_status,
    separator,
    symbol_ssh,
)
from snakypy.zshpower.utils.catch import get_key


class Git:
    def __init__(self, config, icon_space=" "):

        self.config = config
        try:
            self.symbol = symbol_ssh(get_key(config, "git", "symbol"), "git:")
        except KeyError:
            self.symbol = symbol_ssh("\uf418", "git:")
        self.gcolor_enable = get_key(config, "general", "color", "enable")
        self.enable = get_key(config, "git", "enable")
        self.color_symbol = (
            get_key(config, "git", "color", "symbol")
            if self.gcolor_enable is True
            else "negative"
        )
        self.branch_color = (
            get_key(config, "git", "branch", "color")
            if self.gcolor_enable is True
            else "negative"
        )
        self.prefix_color = (
            get_key(config, "git", "prefix", "color")
            if self.gcolor_enable is True
            else "negative"
        )
        self.prefix_text = element_spacing(get_key(config, "git", "prefix", "text"))
        self.symbol_enable = get_key(config, "git", "status", "symbols", "enable")
        self.icons = {
            "A": [
                f"{Color('green') if self.gcolor_enable is True else Color('negative')}"
                f"{symbol_ssh(get_key(config, 'git', 'status', 'symbol', 'added'), '')}"
                f"{Color().NONE}",
                f"{Color('green') if self.gcolor_enable is True else Color('negative')}+"
                f"{icon_space}{Color().NONE}",
            ],
            # "AM": [
            #     f"{Color('white') if get_key(config, 'general', 'color', 'enable') is True else Color('negative')}"
            #     f"{symbol_ssh(get_key(config, 'git', 'status', 'symbol', 'changed'), '')}"
            #     f"{Color().NONE}",
            #     f"{Color('white') if self.gcolor_enable is True else Color('negative')}#
            #     {icon_space}{Color().NONE}",
            # ],
            "M": [
                f"{Color('blue') if self.gcolor_enable is True else Color('negative')}"
                f"{symbol_ssh(get_key(config, 'git', 'status', 'symbol', 'modified'), '')}"
                f"{Color().NONE}",
                f"{Color('blue') if self.gcolor_enable is True else Color('negative')}#"
                f"{icon_space}{Color().NONE}",
            ],
            "D": [
                f"{Color('red') if self.gcolor_enable is True else Color('negative')}"
                f"{symbol_ssh(get_key(config, 'git', 'status', 'symbol', 'deleted'), '')}"
                f"{Color().NONE}",
                f"{Color('red') if self.gcolor_enable is True else Color('negative')}x"
                f"{icon_space}{Color().NONE}",
            ],
            "??": [
                f"{Color('yellow') if self.gcolor_enable is True else Color('negative')}"
                f"{symbol_ssh(get_key(config, 'git', 'status', 'symbol', 'untracked'), '')}"
                f"{Color().NONE}",
                f"{Color('yellow') if self.gcolor_enable is True else Color('negative')}?"
                f"{icon_space}{Color().NONE}",
            ],
            "R": [
                f"{Color('magenta') if self.gcolor_enable is True else Color('negative')}"
                f"{symbol_ssh(get_key(config, 'git', 'status', 'symbol', 'renamed'), '')}"
                f"{Color().NONE}",
                f"{Color('magenta') if self.gcolor_enable is True else Color('negative')}->"
                f"{icon_space}{Color().NONE}",
            ],
            "UU": [
                f"{Color('red') if self.gcolor_enable is True else Color('negative')}"
                f"{symbol_ssh(get_key(config, 'git', 'status', 'symbol', 'conflicts'), '')}"
                f"{Color().NONE}",
                f"{Color('red') if self.gcolor_enable is True else Color('negative')}!="
                f"{icon_space}{Color().NONE}",
            ],
            "AH": [
                f"{Color('blue') if self.gcolor_enable is True else Color('negative')}"
                f"{symbol_ssh(get_key(config, 'git', 'status', 'symbol', 'ahead'), '')}"
                f"{Color().NONE}",
                f"{Color('blue') if self.gcolor_enable is True else Color('negative')}^"
                f"{icon_space}{Color().NONE}",
            ],
            "BH": [
                f"{Color('magenta') if self.gcolor_enable is True else Color('negative')}"
                f"{symbol_ssh(get_key(config, 'git', 'status', 'symbol', 'behind'), '')}"
                f"{Color().NONE}",
                f"{Color('magenta') if self.gcolor_enable is True else Color('negative')}_"
                f"{icon_space}{Color().NONE}",
            ],
            "DG": [
                f"{Color('yellow') if self.gcolor_enable is True else Color('negative')}"
                f"{symbol_ssh(get_key(config, 'git', 'status', 'symbol', 'diverged'), '')}"
                f"{Color().NONE}",
                f"{Color('yellow') if self.gcolor_enable is True else Color('negative')}<->"
                f"{icon_space}{Color().NONE}",
            ],
            "C": [
                f"{Color('yellow') if self.gcolor_enable is True else Color('negative')}"
                f"{symbol_ssh(get_key(config, 'git', 'status', 'symbol', 'copied'), '')}"
                f"{Color().NONE}",
                f"{Color('yellow') if self.gcolor_enable is True else Color('negative')}**"
                f"{icon_space}{Color().NONE}",
            ],
            "U": [
                f"{Color('magenta') if self.gcolor_enable is True else Color('negative')}"
                f"{symbol_ssh(get_key(config, 'git', 'status', 'symbol', 'unmerged'), '')}"
                f"{Color().NONE}",
                f"{Color('magenta') if self.gcolor_enable is True else Color('negative')}="
                f"{icon_space}{Color().NONE}",
            ],
            "CL": [
                f"{Color('green') if self.gcolor_enable is True else Color('negative')}"
                f"{symbol_ssh(get_key(config, 'git', 'status', 'symbol', 'clean'), '')}"
                f"{Color().NONE}",
                f"{Color('green') if self.gcolor_enable is True else Color('negative')}~"
                f"{icon_space}{Color().NONE}",
            ],
        }
        self.icons["UD"] = self.icons["UU"]

    def __str__(self):
        if isdir(join(getcwd(), ".git")) and self.enable:
            status_git = git_status(porcelain=True)
            status_git_text = git_status()
            branch_current = git_status(branch=True)
            branch_formated = (
                f"{Color(self.prefix_color)}"
                f"{self.prefix_text}{Color().NONE}"
                f"{Color(self.color_symbol)}"
                f"{self.symbol}{Color().NONE}"
                f"{Color(self.branch_color)}"
                f"{branch_current}"
                f"{Color().NONE}"
            )
            status_current = []
            if "??" in status_git:
                status_current.append("??")
            if "D" in status_git:
                status_current.append("D")
            if "R" in status_git:
                status_current.append("R")
            if "A" in status_git:
                status_current.append("A")
            # if "AM" in status_git:
            #     status_current.append("AM")
            if "M" in status_git:
                status_current.append("M")
            if "UU" in status_git:
                status_current.append("UU")
            if "U" in status_git:
                status_current.append("U")
            if "UD" in status_git:
                status_current.append("UD")
            if "C" in status_git:
                status_current.append("C")
            if "ahead" in status_git_text:
                status_current.append("AH")
            if "behind" in status_git_text:
                status_current.append("BH")
            if "diverged" in status_git_text:
                status_current.append("DG")
            if len(status_git) == 0:
                status_current.append("CL")

            status_icons = (
                self.icons[item][0]
                if self.symbol_enable
                else self.icons[item][1]
                if "SSH_CONNECTION" not in environ
                else self.icons[item][1]
                for item in status_current
            )

            # status = f'( {" ".join(sorted(status_icons)).strip()} )'
            # if len(status_current) == 1:
            status = "".join(sorted(status_icons))

            return f"{separator(self.config)}{branch_formated} {status}"
        return ""
