from os.path import join

from snakypy.helpers import printer
from snakypy.helpers.ansi import FG, NONE
from snakypy.helpers.catches import tools_requirements
from snakypy.helpers.console import loading
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
from snakypy.zshpower.utils.process import change_shell, reload_zsh
from snakypy.zshpower.utils.shift import (
    add_plugins_zshrc,
    change_theme_in_zshrc,
    create_config,
    create_zshrc,
    cron_task,
    install_fonts,
    omz_install,
    omz_install_plugins,
    remove_versions_garbage,
)

instruction_not_omz = f"""{FG().YELLOW}
********************** WARNING **********************
Add the following code to the {FG().MAGENTA}$HOME/.zshrc{NONE} {FG().YELLOW}file:

CODE: {FG().CYAN}source $HOME/.zshpower/{__info__["version"]}/init.sh {NONE}
{FG().YELLOW}*****************************************************{NONE}
"""


class InitCommand(Base):
    def __init__(self, home):
        Base.__init__(self, home)

    def run(self, arguments, *, reload=False, message=False) -> None:
        printer("Please wait ... assigning settings ...", foreground=FG().WARNING)
        tools_requirements("bash", "zsh", "vim", "git", "cut", "grep", "whoami", "pwd")
        snakypy_path_create(self.data_root)
        create_config(config_content, self.config_file)
        create_file(set_zshpower_content, self.init_file, force=True)
        # Create table if not exists
        DAO().create_table(self.tbl_main)
        # Insert registers
        records("insert")
        loading(
            set_time=0.040,
            bar=False,
            header="ZSHPower is creating the database. Wait a moment...",
            foreground=FG().QUESTION,
        )

        if arguments["--omz"]:
            omz_install(self.omz_root)
            omz_install_plugins(self.omz_root, self.plugins)
            create_zshrc(zshrc_content, self.zsh_rc)
            change_theme_in_zshrc(self.zsh_rc, f"{__info__['pkg_name']}")
            add_plugins_zshrc(self.zsh_rc)
            create_file(set_zshpower_content, self.theme_file, force=True)

        install_fonts(self.HOME)
        change_shell()
        remove_versions_garbage(join(self.HOME, f".{__info__['pkg_name']}"))

        try:
            cron_task(sync_content, self.sync_path, cron_content, self.cron_path)
            printer("Done!", foreground=FG().FINISH) if message else None

            if not arguments["--omz"] and not get_line_source(self.zsh_rc):
                printer(instruction_not_omz, foreground=FG().YELLOW)

            if reload:
                reload_zsh()
        except KeyboardInterrupt:
            printer("Canceled by user", foreground=FG().WARNING)
            printer("Done!", foreground=FG().FINISH) if message else None

            if not arguments["--omz"] and not get_line_source(self.zsh_rc):
                printer(instruction_not_omz, foreground=FG().YELLOW)

            if reload:
                reload_zsh()
