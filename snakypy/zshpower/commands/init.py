from snakypy.helpers import printer
from snakypy.helpers.ansi import FG, NONE
from snakypy.helpers.catches import tools_requirements
from snakypy.helpers.files import create_file
from snakypy.helpers.path import create as snakypy_path_create

from snakypy.zshpower import __info__
from snakypy.zshpower.commands.utils.handle import records
from snakypy.zshpower.config.apply import content as set_zshpower_content
from snakypy.zshpower.config.base import Base
from snakypy.zshpower.config.config import content as config_content
from snakypy.zshpower.config.cron import cron_content, sync_content
from snakypy.zshpower.config.zshrc import content as zshrc_content
from snakypy.zshpower.database.dao import DAO
from snakypy.zshpower.utils.catch import get_line_source
from snakypy.zshpower.utils.modifiers import (
    add_plugins_zshrc,
    change_theme_in_zshrc,
    create_config,
    create_zshrc,
    cron_task,
    install_fonts,
    omz_install,
    omz_install_plugins,
)
from snakypy.zshpower.utils.process import change_shell, reload_zsh


class InitCommand(Base):
    def __init__(self, home):
        Base.__init__(self, home)
        self.instruction_not_omz = f"""{FG().YELLOW}
            ********************** WARNING **********************
            Add the following code to the {FG().MAGENTA}{home}/.zshrc{NONE} {FG().YELLOW}file:

            CODE: {FG().CYAN}source {self.init_file} {NONE}
            {FG().YELLOW}*****************************************************{NONE}
        """

    def run(self, arguments, *, reload=False, message=False) -> None:
        tools_requirements("bash", "zsh", "vim", "git", "cut", "grep", "whoami", "pwd")
        printer("Please wait ... assigning settings ...", foreground=FG().WARNING)
        snakypy_path_create(self.database_root, self.cache_root)
        create_config(config_content, self.config_file)

        if not arguments["--omz"]:
            create_file(set_zshpower_content, self.init_file, force=True)

        # Create table if not exists
        DAO().create_table(self.tbl_main)

        # Insert registers in database
        records("insert")

        if arguments["--omz"]:
            omz_install(self.omz_root, self.logfile)
            omz_install_plugins(self.omz_root, self.plugins, self.logfile)
            create_zshrc(zshrc_content, self.zsh_rc, self.logfile)
            change_theme_in_zshrc(self.zsh_rc, f"{__info__['pkg_name']}", self.logfile)
            add_plugins_zshrc(self.zsh_rc, self.logfile)
            create_file(set_zshpower_content, self.theme_file, force=True)

        # Install fonts
        install_fonts(self.HOME, self.logfile)

        # Change shell to ZSH
        change_shell(self.logfile)

        # Register log
        self.log.record("Initial settings applied", colorize=True, level="info")

        try:
            cron_task(
                sync_content, self.sync_path, cron_content, self.cron_path, self.logfile
            )
            printer("Done!", foreground=FG().FINISH) if message else None

            if not arguments["--omz"] and not get_line_source(
                self.zsh_rc, self.logfile
            ):
                printer(self.instruction_not_omz, foreground=FG().YELLOW)

            if reload:
                reload_zsh()
        except KeyboardInterrupt:
            printer("Canceled by user", foreground=FG().WARNING)
            printer("Done!", foreground=FG().FINISH) if message else None

            if not arguments["--omz"] and not get_line_source(
                self.zsh_rc, self.logfile
            ):
                printer(self.instruction_not_omz, foreground=FG().YELLOW)

            if reload:
                reload_zsh()
