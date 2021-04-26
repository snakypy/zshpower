from zshpower import HOME
from zshpower.config.base import Base
from snakypy.ansi import FG, NONE
from zshpower.utils.data.generators import Manager
from zshpower.utils.data.database import Database
from zshpower.utils.data.generators import create_table
from os.path import join


instruction_not_omz = f"""{FG.YELLOW}
********************** WARNING **********************
Add the following code to the {FG.MAGENTA}$HOME/.zshrc{NONE} {FG.YELLOW}file:

CODE: {FG.CYAN}source $HOME/.zshpower/init {NONE}
{FG.YELLOW}*****************************************************{NONE}
"""


class InitCommand(Base):
    def __init__(self, home):
        Base.__init__(self, home)

    def main(self, arguments, *, reload=False, message=False):
        from snakypy import printer
        from zshpower.config import package
        from snakypy.path import create as snakypy_path_create
        from snakypy.file import create as snakypy_file_create
        from zshpower.utils.check import tools_requirements
        from zshpower.utils.catch import get_line_source
        from zshpower.config.config import content as config_content
        from zshpower.config.zshrc import content as zshrc_content
        from zshpower.config.set_zshpower import content as set_zshpower_content
        from zshpower.utils.process import change_shell, reload_zsh
        from zshpower.utils.shift import (
            create_config,
            omz_install,
            omz_install_plugins,
            install_fonts,
            create_zshrc,
            change_theme_in_zshrc,
            add_plugins_zshrc,
            create_zshrc_not_exists,
        )

        tools_requirements("zsh", "vim", "git", "cut", "grep")

        create_zshrc_not_exists(
            f". $HOME/.{package.info['pkg_name']}/init", self.zsh_rc
        )

        snakypy_path_create(self.config_root, self.data_root)

        create_config(config_content, self.config_file)

        snakypy_file_create(set_zshpower_content, self.init_file, force=True)

        # Create table and database if not exists
        create_table(Database(HOME), join(HOME, self.data_root, self.database_name))

        # Insert registers in database
        Manager(Database(HOME)).dart("insert")
        Manager(Database(HOME)).docker("update")
        Manager(Database(HOME)).dotnet("insert")
        Manager(Database(HOME)).elixir("insert")

        if arguments["--omz"]:
            omz_install(self.omz_root)
            omz_install_plugins(self.omz_root, self.plugins)
            create_zshrc(zshrc_content, self.zsh_rc)
            change_theme_in_zshrc(self.zsh_rc, f"{package.info['pkg_name']}")
            add_plugins_zshrc(self.zsh_rc)
            snakypy_file_create(set_zshpower_content, self.theme_file, force=True)

        install_fonts(self.HOME)

        change_shell()

        printer("Done!", foreground=FG.FINISH) if message else None

        if not arguments["--omz"] and not get_line_source(self.zsh_rc):
            printer(instruction_not_omz, foreground=FG.YELLOW)

        reload_zsh() if reload else None
