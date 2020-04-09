from datetime import datetime
from snakypy import printer, pick
from snakypy.ansi import FG
from os import remove as os_remove
from zshpower.config import package
from zshpower.config.base import Base
from subprocess import check_output
from contextlib import suppress as contextlib_suppress
from zshpower.utils.check import checking_init
from shutil import which as shutil_which
from shutil import copyfile as shutil_copyfile
from shutil import rmtree as shutil_rmtree
from zshpower.utils.process import reload_zsh
from zshpower.utils.shift import change_theme_in_zshrc


class UninstallCommand(Base):
    def __init__(self, home):
        Base.__init__(self, home)

    def main(self):
        checking_init(self.themes_folder)

        title = f"What did you want to uninstall?"
        options = [
            f"{package.info['name']}",
            f"{package.info['name']} and Oh My ZSH",
            "Cancel",
        ]
        reply = pick(title, options, colorful=True, index=True)

        if reply is None or reply[0] == 2:
            printer("Whew! Thanks! :)", foreground=FG.GREEN)
            exit(0)

        with contextlib_suppress(Exception):
            os_remove(self.theme_file)

        pip_check = shutil_which("pip")
        if pip_check is not None:
            check_output(
                f'pip uninstall {package.info["name"]} -y',
                shell=True,
                universal_newlines=True,
            )
        change_theme_in_zshrc(self.zsh_rc, "robbyrussell")

        if reply[0] == 1:
            shutil_rmtree(self.omz_root, ignore_errors=True)
            with contextlib_suppress(Exception):
                shutil_copyfile(
                    self.zsh_rc, f"{self.zsh_rc}-D{datetime.today().isoformat()}"
                )
            with contextlib_suppress(Exception):
                os_remove(self.zsh_rc)

        reload_zsh()

        printer("Uninstall process finished.", foreground=FG.FINISH)
