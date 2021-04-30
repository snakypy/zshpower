from zshpower.config.cron import cron_task, sync
from zshpower.prompt.sections.julia import Julia
from zshpower.prompt.sections.elixir import Elixir
from zshpower.prompt.sections.dotnet import Dotnet
from zshpower.prompt.sections.docker import Docker
from zshpower.config.base import Base
from snakypy.ansi import FG, NONE
from zshpower.prompt.sections.golang import Golang
from zshpower.prompt.sections.java import Java
from zshpower.database.dao import DAO
from zshpower.prompt.sections.dart import Dart
from zshpower.prompt.sections.nodejs import NodeJs
from zshpower.prompt.sections.php import Php
from zshpower.prompt.sections.ruby import Ruby
from zshpower.prompt.sections.rust import Rust
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
    create_file_superuser,
)


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

        tools_requirements("zsh", "vim", "git", "cut", "grep", "whoami")

        create_zshrc_not_exists(
            f". $HOME/.{package.info['pkg_name']}/init", self.zsh_rc
        )

        snakypy_path_create(self.config_root, self.data_root, self.cron_folder)

        create_config(config_content, self.config_file)

        snakypy_file_create(set_zshpower_content, self.init_file, force=True)

        # Create table and database if not exists
        DAO().create_table("main")

        # Insert database in database
        Dart().set_version(action="insert")
        Docker().set_version(action="insert")
        Dotnet().set_version(action="insert")
        Elixir().set_version(action="insert")
        Golang().set_version(action="insert")
        Java().set_version(action="insert")
        Julia().set_version(action="insert")
        NodeJs().set_version(action="insert")
        Php().set_version(action="insert")
        Ruby().set_version(action="insert")
        Rust().set_version(action="insert")

        if arguments["--omz"]:
            omz_install(self.omz_root)
            omz_install_plugins(self.omz_root, self.plugins)
            create_zshrc(zshrc_content, self.zsh_rc)
            change_theme_in_zshrc(self.zsh_rc, f"{package.info['pkg_name']}")
            add_plugins_zshrc(self.zsh_rc)
            snakypy_file_create(set_zshpower_content, self.theme_file, force=True)

        install_fonts(self.HOME)

        change_shell()

        try:
            create_file_superuser(
                context=(sync, cron_task),
                filepath=(self.script_sync, self.zshpower_task_file),
            )
            printer("Done!", foreground=FG.FINISH) if message else None

            if not arguments["--omz"] and not get_line_source(self.zsh_rc):
                printer(instruction_not_omz, foreground=FG.YELLOW)

            if reload:
                reload_zsh()
        except KeyboardInterrupt:
            printer("Canceled by user", foreground=FG.WARNING)
            printer("Done!", foreground=FG.FINISH) if message else None

            if not arguments["--omz"] and not get_line_source(self.zsh_rc):
                printer(instruction_not_omz, foreground=FG.YELLOW)

            if reload:
                reload_zsh()
