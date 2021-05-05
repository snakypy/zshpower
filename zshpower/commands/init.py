from os.path import join
from snakypy.console import loading
from zshpower.prompt.sections.gulp import Gulp

from zshpower.database.sql import sql
from zshpower import __version__
from zshpower.prompt.sections.zig import Zig
from zshpower.prompt.sections.vagrant import Vagrant
from zshpower.prompt.sections.ocaml import Ocaml
from zshpower.prompt.sections.nim import Nim
from zshpower.prompt.sections.kotlin import Kotlin
from zshpower.prompt.sections.helm import Helm
from zshpower.prompt.sections.erlang import Erlang
from zshpower.prompt.sections.deno import Deno
from zshpower.prompt.sections.crystal import Crystal
from zshpower.prompt.sections.cmake import CMake
from zshpower.prompt.sections.perl import Perl
from zshpower.config.cron import cron_content, sync_content
from zshpower.prompt.sections.julia import Julia
from zshpower.prompt.sections.elixir import Elixir
from zshpower.prompt.sections.dotnet import Dotnet
from zshpower.prompt.sections.docker import Docker
from zshpower.config.base import Base
from snakypy.ansi import FG, NONE
from zshpower.prompt.sections.golang import Golang
from zshpower.prompt.sections.java import Java
from zshpower.prompt.sections.scala import Scala
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
    cron_task,
    remove_versions_garbage,
)
from concurrent.futures import ThreadPoolExecutor


instruction_not_omz = f"""{FG.YELLOW}
********************** WARNING **********************
Add the following code to the {FG.MAGENTA}$HOME/.zshrc{NONE} {FG.YELLOW}file:

CODE: {FG.CYAN}source $HOME/.zshpower/{__version__}/init.sh {NONE}
{FG.YELLOW}*****************************************************{NONE}
"""


class InitCommand(Base):
    def __init__(self, home):
        Base.__init__(self, home)

    def run(self, arguments, *, reload=False, message=False):
        # threaded_start = time.time()

        # printer("Please wait ... assigning settings ...", foreground=FG.WARNING)
        tools_requirements("zsh", "vim", "git", "cut", "grep", "whoami")
        # create_zshrc_not_exists(
        #     f". $HOME/.{package.info['pkg_name']}/{__version__}/init.sh", self.zsh_rc
        # )
        snakypy_path_create(self.data_root)
        create_config(config_content, self.config_file)
        snakypy_file_create(set_zshpower_content, self.init_file, force=True)
        # Create table and database if not exists
        DAO().create_table([item for item in sql().keys()][0])
        with ThreadPoolExecutor(max_workers=27) as executor:
            executor.submit(Dart().set_version, action="insert")
            executor.submit(Docker().set_version, action="insert")
            executor.submit(Dotnet().set_version, action="insert")
            executor.submit(Elixir().set_version, action="insert")
            executor.submit(Golang().set_version, action="insert")
            executor.submit(Gulp().set_version, action="insert")
            executor.submit(Java().set_version, action="insert")
            executor.submit(Julia().set_version, action="insert")
            executor.submit(NodeJs().set_version, action="insert")
            executor.submit(Php().set_version, action="insert")
            executor.submit(Ruby().set_version, action="insert")
            executor.submit(Rust().set_version, action="insert")
            executor.submit(Scala().set_version, action="insert")
            executor.submit(Perl().set_version, action="insert")
            executor.submit(CMake().set_version, action="insert")
            executor.submit(Crystal().set_version, action="insert")
            executor.submit(Deno().set_version, action="insert")
            executor.submit(Erlang().set_version, action="insert")
            executor.submit(Helm().set_version, action="insert")
            executor.submit(Kotlin().set_version, action="insert")
            executor.submit(Nim().set_version, action="insert")
            executor.submit(Ocaml().set_version, action="insert")
            executor.submit(Vagrant().set_version, action="insert")
            executor.submit(Zig().set_version, action="insert")
            loading(
                set_time=0.040,
                bar=False,
                header="ZSHPower is creating the database. Wait a moment...",
                foreground=FG.QUESTION,
            )

        if arguments["--omz"]:
            omz_install(self.omz_root)
            omz_install_plugins(self.omz_root, self.plugins)
            create_zshrc(zshrc_content, self.zsh_rc)
            change_theme_in_zshrc(self.zsh_rc, f"{package.info['pkg_name']}")
            add_plugins_zshrc(self.zsh_rc)
            snakypy_file_create(set_zshpower_content, self.theme_file, force=True)

        install_fonts(self.HOME)
        change_shell()
        remove_versions_garbage(join(self.HOME, f".{package.info['pkg_name']}"))

        try:
            cron_task(sync_content, self.sync_path, cron_content, self.cron_path)
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
