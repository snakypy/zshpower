from os.path import join
from snakypy.helpers.console import loading
from snakypy.zshpower.commands.lib.handle import records
from snakypy.zshpower import __version__
from snakypy.zshpower.config.cron import cron_content, sync_content
from snakypy.zshpower.config.base import Base
from snakypy.helpers.ansi import FG, NONE
from snakypy.zshpower.database.dao import DAO
from snakypy.helpers import printer
from snakypy.zshpower.config import package
from snakypy.helpers.path import create as snakypy_path_create
from snakypy.helpers.files import create_file
from snakypy.helpers.catches import tools_requirements
from snakypy.zshpower.utils.catch import get_line_source
from snakypy.zshpower.config.config import content as config_content
from snakypy.zshpower.config.zshrc import content as zshrc_content
from snakypy.zshpower.config.set_zshpower import content as set_zshpower_content
from snakypy.zshpower.utils.process import change_shell, reload_zsh
from snakypy.zshpower.utils.shift import (
    create_config,
    omz_install,
    omz_install_plugins,
    install_fonts,
    create_zshrc,
    change_theme_in_zshrc,
    add_plugins_zshrc,
    cron_task,
    remove_versions_garbage,
)

instruction_not_omz = f"""{FG().YELLOW}
********************** WARNING **********************
Add the following code to the {FG().MAGENTA}$HOME/.zshrc{NONE} {FG().YELLOW}file:

CODE: {FG().CYAN}source $HOME/.zshpower/{__version__}/init.sh {NONE}
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
            change_theme_in_zshrc(self.zsh_rc, f"{package.info['pkg_name']}")
            add_plugins_zshrc(self.zsh_rc)
            create_file(set_zshpower_content, self.theme_file, force=True)

        install_fonts(self.HOME)
        change_shell()
        remove_versions_garbage(join(self.HOME, f".{package.info['pkg_name']}"))

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
