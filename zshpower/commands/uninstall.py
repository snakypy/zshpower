from datetime import datetime
from snakypy import printer, pick
from snakypy.ansi import FG
from snakypy.file import create as snakypy_file_create
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
from zshpower.utils.catch import read_zshrc_omz
from zshpower.utils.shift import change_theme_in_zshrc, rm_source_zshrc


def rm_init_file_package(init_file):
    with contextlib_suppress(Exception):
        os_remove(init_file)
    if shutil_which("pip") is not None:
        check_output(
            f'pip uninstall {package.info["name"]} -y',
            shell=True,
            universal_newlines=True,
        )


class UninstallCommand(Base):
    def __init__(self, home):
        Base.__init__(self, home)

    def main(self):
        checking_init(self.HOME)

        if not read_zshrc_omz(self.zsh_rc):
            title = f"Do you want to uninstall {package.info['name']}?"
            options = ["Yes", "No"]
            reply = pick(title, options, colorful=True, index=True)
            if reply is None or reply[0] == 1:
                printer("Whew! Thanks! :)", foreground=FG.GREEN)
                exit(0)
            rm_init_file_package(self.init_file)
            rm_source_zshrc(self.zsh_rc)
        else:
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

            rm_init_file_package(self.init_file)

            change_theme_in_zshrc(self.zsh_rc, "robbyrussell")

            if reply[0] == 1:
                shutil_rmtree(self.omz_root, ignore_errors=True)
                with contextlib_suppress(Exception):
                    shutil_copyfile(
                        self.zsh_rc, f"{self.zsh_rc}-D{datetime.today().isoformat()}"
                    )
                with contextlib_suppress(Exception):
                    os_remove(self.zsh_rc)

            snakypy_file_create("", f"{self.HOME}/.zshrc", force=True)

        reload_zsh()
        printer("Uninstall process finished.", foreground=FG.FINISH)
