from contextlib import suppress
from os import remove, symlink
from os.path import islink, join
from sys import stdout

from snakypy.helpers import printer
from snakypy.helpers.ansi import FG, NONE
from snakypy.helpers.files import backup_file, create_file
from snakypy.helpers.os import remove_objects
from snakypy.helpers.path import create as create_path

from snakypy.zshpower import __info__
from snakypy.zshpower.commands.utils.handle import records
from snakypy.zshpower.config.base import Base
from snakypy.zshpower.config.bootstrap import bootstrap
from snakypy.zshpower.config.config import config_content
from snakypy.zshpower.config.zshrc import zshrc_content, zshrc_sample
from snakypy.zshpower.database.dao import DAO
from snakypy.zshpower.utils.catch import get_line, get_zsh_theme
from snakypy.zshpower.utils.check import tools_requirements
from snakypy.zshpower.utils.modifiers import (
    add_plugins,
    change_theme,
    create_toml,
    create_zshrc,
    install_fonts,
    install_plugins,
    omz_install,
    remove_lines,
)
from snakypy.zshpower.utils.process import change_shell, reload_zsh


class InitCommand(Base):
    def __init__(self, home):
        Base.__init__(self, home)
        self.instruction_not_omz = f"""{FG().YELLOW}
            **************************** WARNING *******************************
            1- Add the following line of code to the {FG().MAGENTA}{home}/.zshrc{NONE}{FG().YELLOW} file:

            {FG().CYAN}eval "$(zshpower init --path)"{NONE}

            {FG().YELLOW}2 - Then run the following command: {FG().CYAN}exec zsh{NONE}{FG().YELLOW}
            ********************************************************************{NONE}
        """

    def run(self, arguments, *, reload=False) -> None:
        tools_requirements("bash", "zsh", "vim", "git", "cut", "grep", "whoami", "pwd")

        # If there is, an exception will not pop.
        with suppress(FileExistsError):
            create_file(zshrc_sample, self.zsh_rc)

        # Returns only the path
        if arguments["--path"]:
            stdout.write(
                join(f'[[ -d "{self.lib_root}" ]] && source $HOME', self.source_code)
            )
        else:
            printer(
                "Wait a moment, creating initial settings...", foreground=FG().QUESTION
            )
            create_path(
                self.config_root, self.database_root, self.cache_root, self.lib_root
            )
            create_toml(config_content, self.config_file)
            create_file(bootstrap, self.lib_main, force=True)
            # Install with OMZ
            if arguments["--omz"]:
                remove_lines(
                    self.zsh_rc,
                    self.logfile,
                    lines=('eval "\\$\\(zshpower init --path\\)"',),
                )
                omz_install(self.omz_root, self.logfile)
                install_plugins(self.omz_root, self.plugins, self.logfile)
                create_zshrc(zshrc_content, self.zsh_rc, self.logfile)
                change_theme(self.zsh_rc, f"{__info__['pkg_name']}", self.logfile)
                add_plugins(self.zsh_rc, self.logfile)
                if islink(self.theme_symlink):
                    remove(self.theme_symlink)
                symlink(self.lib_main, self.theme_symlink)
            # Install fonts
            install_fonts(self.HOME, self.logfile)
            # Changing shell to ZSH
            change_shell(self.logfile)
            printer("Settings finished!", foreground=FG().FINISH)

            # printer("Generating database, wait...", foreground=FG().QUESTION)
            # Create table in database if not exists
            DAO().create_table(self.tbl_main)
            # Insert registers in database
            records("insert", "Generating database, wait ...", FG().QUESTION)
            printer("Database generated!", foreground=FG().FINISH)

            # Register logs
            self.log.record("Initial settings applied", colorize=True, level="info")

            # Create new .zshrc and Instruction ZSHPower without OMZ
            if not arguments["--omz"]:
                if get_zsh_theme(self.zsh_rc, self.logfile):
                    backup_file(self.zsh_rc, self.zsh_rc, date=True, extension=False)
                    remove_objects(objects=(self.zsh_rc,))
                    create_file(zshrc_sample, self.zsh_rc, force=True)
                line = 'eval "\\$\\(zshpower init --path\\)"'
                if not get_line(self.zsh_rc, line, self.logfile):
                    printer(self.instruction_not_omz, foreground=FG().YELLOW)

            # Reload terminal
            if arguments["--omz"] and reload:
                reload_zsh(sleep_timer=2, message=True)
