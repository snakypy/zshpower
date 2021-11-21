from snakypy.helpers import pick, printer
from snakypy.helpers.ansi import FG
from snakypy.helpers.files import backup_file, create_file
from snakypy.helpers.os import remove_objects

from snakypy.zshpower import __info__
from snakypy.zshpower.config.base import Base
from snakypy.zshpower.config.zshrc import zshrc_sample
from snakypy.zshpower.utils.catch import read_zshrc_omz
from snakypy.zshpower.utils.modifiers import (
    change_theme_in_zshrc,
    rm_source_zshrc,
    uninstall_by_pip,
)
from snakypy.zshpower.utils.process import reload_zsh


class UninstallCommand(Base):
    def __init__(self, home):
        Base.__init__(self, home)

    def using_omz(self):
        check = read_zshrc_omz(self.zsh_rc, self.logfile)
        if check:
            return True
        return False

    def zshpower_with_omz(self):
        title = "What did you want to uninstall?"
        options = [
            f"{__info__['name']}",
            f"{__info__['name']} and Oh My ZSH",
            "Cancel",
        ]
        reply = pick(title, options, colorful=True, index=True)
        # Cancel
        if reply is None or reply[0] == 2:
            printer("Whew! Thanks! :)", foreground=FG().GREEN)
            exit(0)
        # Remove structure ZSHPower
        # Note: Add folders first then files.
        remove_objects(
            objects=(
                self.database_root,
                self.cache_root,
                self.lib_root,
                self.theme_symlink,
            )
        )
        uninstall_by_pip(packages=(__info__["name"],))
        rm_source_zshrc(self.zsh_rc, self.source_code, self.logfile)
        change_theme_in_zshrc(self.zsh_rc, "robbyrussell", self.logfile)
        # ZSHPower and Oh My ZSH
        if reply[0] == 1:
            backup_file(self.zsh_rc, self.zsh_rc, date=True, extension=False)
            remove_objects(
                objects=(
                    self.omz_root,
                    self.zsh_rc,
                )
            )
            create_file(zshrc_sample, self.zsh_rc, force=True)
        printer("Uninstallation completed!", foreground=FG().FINISH)
        reload_zsh(reload_zsh(sleep_timer=2, message=True))
        return "ZSHPower removed!"

    def orphan_zshpower(self):
        title = f"Do you want to uninstall {__info__['name']}?"
        options = ["Yes", "No"]
        reply = pick(title, options, colorful=True, index=True)
        if reply is None or reply[0] == 1:
            printer("Whew! Thanks! :)", foreground=FG().GREEN)
            exit(0)
        remove_objects(
            objects=(
                self.database_root,
                self.cache_root,
                self.lib_root,
            )
        )
        uninstall_by_pip(packages=(__info__["name"],))
        rm_source_zshrc(self.zsh_rc, self.source_code, self.logfile)
        reload_zsh(reload_zsh(sleep_timer=2, message=True))
        return "ZSHPower removed!"

    def run(self) -> None:
        if self.using_omz():
            return self.zshpower_with_omz()
        return self.orphan_zshpower()
