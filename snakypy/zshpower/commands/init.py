from os import remove, symlink
from os.path import islink

from snakypy.helpers import printer
from snakypy.helpers.ansi import FG, NONE
from snakypy.helpers.catches import tools_requirements
from snakypy.helpers.files import create_file
from snakypy.helpers.path import create as snakypy_path_create

from snakypy.zshpower import __info__
from snakypy.zshpower.commands.utils.handle import records
from snakypy.zshpower.config.apply import zshpower_main
from snakypy.zshpower.config.base import Base
from snakypy.zshpower.config.config import config_content
from snakypy.zshpower.config.zshrc import zshrc_content
from snakypy.zshpower.database.dao import DAO
from snakypy.zshpower.utils.catch import get_line_source
from snakypy.zshpower.utils.modifiers import (
    add_plugins_zshrc,
    change_theme_in_zshrc,
    create_config,
    create_zshrc,
    install_fonts,
    omz_install,
    omz_install_plugins,
)
from snakypy.zshpower.utils.process import change_shell, reload_zsh


class InitCommand(Base):
    def __init__(self, home):
        Base.__init__(self, home)
        self.instruction_not_omz = f"""{FG().YELLOW}
            **************************** WARNING *******************************
            1- Add the following line of code to the {FG().MAGENTA}{home}/.zshrc{NONE}{FG().YELLOW} file:

            {FG().CYAN}source $HOME/.zshpower/lib/main.lib{NONE}

            {FG().YELLOW}2 - Then run the following command: {FG().CYAN}exec zsh{NONE}{FG().YELLOW}
            ********************************************************************{NONE}
        """

    def run(self, arguments, *, reload=False) -> None:
        tools_requirements("bash", "zsh", "vim", "git", "cut", "grep", "whoami", "pwd")
        printer("Wait a moment, creating initial settings...", foreground=FG().WARNING)
        snakypy_path_create(
            self.config_root, self.database_root, self.cache_root, self.lib_root
        )
        create_config(config_content, self.config_file)
        create_file(zshpower_main, self.lib_main, force=True)
        # Install with OMZ
        if arguments["--omz"]:
            omz_install(self.omz_root, self.logfile)
            omz_install_plugins(self.omz_root, self.plugins, self.logfile)
            create_zshrc(zshrc_content, self.zsh_rc, self.logfile)
            change_theme_in_zshrc(self.zsh_rc, f"{__info__['pkg_name']}", self.logfile)
            add_plugins_zshrc(self.zsh_rc, self.logfile)
            if islink(self.theme_symlink):
                remove(self.theme_symlink)
            symlink(self.lib_main, self.theme_symlink)
        # Install fonts
        install_fonts(self.HOME, self.logfile)
        # Changing shell to ZSH
        change_shell(self.logfile)
        printer("Settings finished!", foreground=FG().FINISH)

        printer("Generating database, wait...", foreground=FG().WARNING)
        # Create table in database if not exists
        DAO().create_table(self.tbl_main)
        # Insert registers in database
        records("insert")
        printer("Database generated!", foreground=FG().FINISH)

        # Register logs
        self.log.record("Initial settings applied", colorize=True, level="info")

        # Instruction ZSHPower without OMZ
        if not arguments["--omz"] and not get_line_source(self.zsh_rc, self.logfile):
            printer(self.instruction_not_omz, foreground=FG().YELLOW)

        # Reload terminal
        if arguments["--omz"] and reload:
            reload_zsh(sleep_timer=2, message=True)
