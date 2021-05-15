from getpass import getpass
from os.path import exists
from subprocess import Popen, PIPE
from snakypy.zshpower.config.zshrc import zshrc_sample
from snakypy.zshpower.config import package
from snakypy.zshpower.config.base import Base
from snakypy.helpers.files import backup_file
from snakypy.zshpower.utils.shift import (
    change_theme_in_zshrc,
    rm_source_zshrc,
    uninstall_by_pip,
)
from snakypy.helpers.os import remove_objects
from snakypy.zshpower.utils.check import checking_init
from snakypy.zshpower.utils.process import reload_zsh
from snakypy.zshpower.utils.catch import read_zshrc_omz
from snakypy.helpers.files import create_file
from snakypy.helpers.ansi import FG
from snakypy.helpers import printer, pick
from snakypy.zshpower import HOME


def finished() -> None:
    try:
        if exists(Base(HOME).sync_path) or exists(Base(HOME).cron_path):
            pass_ok = False

            message = """
                     You need to provide the superuser password to remove the process on ZSHPower on Cron.
                     If you do not want this step to be done, you can cancel with Ctrl + C.
                     """

            printer(message, foreground=FG().WARNING)

            while not pass_ok:
                sudo_password = getpass()

                command = f"""su -c 'rm -f {Base(HOME).sync_path}; rm -f {Base(HOME).cron_path}'"""
                p = Popen(
                    command,
                    stdin=PIPE,
                    stderr=PIPE,
                    stdout=PIPE,
                    universal_newlines=True,
                    shell=True,
                )
                communicate = p.communicate(sudo_password)

                if "failure" in communicate[1].split():
                    printer("Password incorrect.", foreground=FG().ERROR)
                else:
                    pass_ok = True

        reload_zsh()
        printer("Uninstall process finished.", foreground=FG().FINISH)
    except KeyboardInterrupt:
        reload_zsh()
        printer("Uninstall process finished.", foreground=FG().FINISH)


class UninstallCommand(Base):
    def __init__(self, home):
        Base.__init__(self, home)

    def run(self) -> None:
        checking_init(self.HOME)

        if not read_zshrc_omz(self.zsh_rc):
            title = f"Do you want to uninstall {package.info['name']}?"
            options = ["Yes", "No"]
            reply = pick(title, options, colorful=True, index=True)
            if reply is None or reply[0] == 1:
                printer("Whew! Thanks! :)", foreground=FG().GREEN)
                exit(0)
            remove_objects(objects=(self.init_file, self.data_root))
            uninstall_by_pip(packages=(package.info["name"],))
            rm_source_zshrc(self.zsh_rc)
            finished()
        else:
            title = "What did you want to uninstall?"
            options = [
                f"{package.info['name']}",
                f"{package.info['name']} and Oh My ZSH",
                "Cancel",
            ]
            reply = pick(title, options, colorful=True, index=True)

            # Cancel
            if reply is None or reply[0] == 2:
                printer("Whew! Thanks! :)", foreground=FG().GREEN)
                exit(0)

            # Remove default
            remove_objects(objects=(self.theme_file, self.init_file, self.data_root))
            uninstall_by_pip(packages=(package.info["name"],))
            change_theme_in_zshrc(self.zsh_rc, "robbyrussell")

            # ZSHPower and Oh My ZSH
            if reply[0] == 1:
                backup_file(self.zsh_rc, self.zsh_rc, date=True, extension=False)
                remove_objects(objects=(self.omz_root, self.zsh_rc))
                create_file(zshrc_sample, self.zsh_rc, force=True)

            finished()
