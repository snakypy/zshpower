import os
from .lib.utils import Color
from .lib.utils import symbol_ssh, git_status, element_spacing, separator


class Git(Color):
    def __init__(self, config, icon_space=" "):
        super().__init__()
        self.config = config
        self.git_enable = config["git"]["enable"]
        self.git_symbol = symbol_ssh(config["git"]["symbol"], "git:")
        self.git_color_symbol = config["git"]["color"]["symbol"]
        self.git_branch_color = config["git"]["branch"]["color"]
        self.git_prefix_color = config["git"]["prefix"]["color"]
        self.git_prefix_text = element_spacing(config["git"]["prefix"]["text"])
        self.git_symbol_enable = config["git"]["status"]["symbols"]["enable"]
        self.icons = {
            "A": [
                f"{Color('green')}"
                f"{symbol_ssh(config['git']['status']['symbol']['added'], '')}"
                f"{Color().NONE}",
                f"{Color('green')}+{icon_space}{Color().NONE}",
            ],
            "M": [
                f"{Color('blue')}"
                f"{symbol_ssh(config['git']['status']['symbol']['modified'], '')}"
                f"{Color().NONE}",
                f"{Color('blue')}#{icon_space}{Color().NONE}",
            ],
            "D": [
                f"{Color('red')}"
                f"{symbol_ssh(config['git']['status']['symbol']['deleted'], '')}"
                f"{Color().NONE}",
                f"{Color('red')}x{icon_space}{Color().NONE}",
            ],
            "??": [
                f"{Color('yellow')}"
                f"{symbol_ssh(config['git']['status']['symbol']['untracked'], '')}"
                f"{Color().NONE}",
                f"{Color('yellow')}?{icon_space}{Color().NONE}",
            ],
            "R": [
                f"{Color('magenta')}"
                f"{symbol_ssh(config['git']['status']['symbol']['renamed'], '')}"
                f"{Color().NONE}",
                f"{Color('magenta')}->{icon_space}{Color().NONE}",
            ],
            "UU": [
                f"{Color('red')}"
                f"{symbol_ssh(config['git']['status']['symbol']['conflicts'], '')}"
                f"{Color().NONE}",
                f"{Color('red')}!={icon_space}{Color().NONE}",
            ],
            "AH": [
                f"{Color('blue')}"
                f"{symbol_ssh(config['git']['status']['symbol']['ahead'], '')}"
                f"{Color().NONE}",
                f"{Color('blue')}^{icon_space}{Color().NONE}",
            ],
            "BH": [
                f"{Color('magenta')}"
                f"{symbol_ssh(config['git']['status']['symbol']['behind'], '')}"
                f"{Color().NONE}",
                f"{Color('magenta')}_{icon_space}{Color().NONE}",
            ],
            "DG": [
                f"{Color('yellow')}"
                f"{symbol_ssh(config['git']['status']['symbol']['diverged'], '')}"
                f"{Color().NONE}",
                f"{Color('yellow')}<->{icon_space}{Color().NONE}",
            ],
            "C": [
                f"{Color('yellow')}"
                f"{symbol_ssh(config['git']['status']['symbol']['copied'], '')}"
                f"{Color().NONE}",
                f"{Color('yellow')}**{icon_space}{Color().NONE}",
            ],
            "U": [
                f"{Color('magenta')}"
                f"{symbol_ssh(config['git']['status']['symbol']['unmerged'], '')}"
                f"{Color().NONE}",
                f"{Color('magenta')}={icon_space}{Color().NONE}",
            ],
            "CL": [
                f"{Color('green')}"
                f"{symbol_ssh(config['git']['status']['symbol']['clean'], '')}"
                f"{Color().NONE}",
                f"{Color('green')}~{icon_space}{Color().NONE}",
            ],
        }
        self.icons["AM"] = self.icons["M"]
        self.icons["UD"] = self.icons["UU"]

    def __str__(self):
        if os.path.isdir(os.path.join(os.getcwd(), ".git")):
            status_git = git_status(porcelain=True)
            status_git_text = git_status()
            branch_current = git_status(branch=True)
            branch_formated = (
                f"{Color(self.git_prefix_color)}"
                f"{self.git_prefix_text}{Color().NONE}"
                f"{Color(self.git_color_symbol)}"
                f"{self.git_symbol}{Color().NONE}"
                f"{Color(self.git_branch_color)}"
                f"{branch_current}"
                f"{Color().NONE}"
            )
            status_current = []
            status_icons = []
            if "??" in status_git:
                status_current.append("??")
            if "D" in status_git:
                status_current.append("D")
            if "R" in status_git:
                status_current.append("R")
            if "A" in status_git:
                status_current.append("A")
            if "AM" in status_git:
                status_current.append("AM")
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

            for item in status_current:
                if "SSH_CONNECTION" not in os.environ:
                    if self.git_symbol_enable:
                        status_icons.append(f"{self.icons[item][0]}")
                    else:
                        status_icons.append(f"{self.icons[item][1]}")
                else:
                    status_icons.append(f"{self.icons[item][1]}")

            # status = f'( {" ".join(sorted(status_icons)).strip()} )'
            # if len(status_current) == 1:
            status = "".join(sorted(status_icons))

            return f"{separator(self.config)}{branch_formated} {status}"
        return ""
