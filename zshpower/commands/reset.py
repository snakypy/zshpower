from concurrent.futures.thread import ThreadPoolExecutor

from zshpower.prompt.sections.gulp import Gulp

from zshpower.database.sql import sql

from zshpower.database.dao import DAO

from zshpower.utils.process import reload_zsh
from zshpower.utils.check import checking_init
from zshpower.utils.shift import create_config
from zshpower.config.config import content as config_content
from snakypy.console import loading
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
from zshpower.prompt.sections.julia import Julia
from zshpower.prompt.sections.elixir import Elixir
from zshpower.prompt.sections.dotnet import Dotnet
from zshpower.prompt.sections.docker import Docker
from zshpower.config.base import Base
from snakypy.ansi import FG
from zshpower.prompt.sections.golang import Golang
from zshpower.prompt.sections.java import Java
from zshpower.prompt.sections.scala import Scala
from zshpower.prompt.sections.dart import Dart
from zshpower.prompt.sections.nodejs import NodeJs
from zshpower.prompt.sections.php import Php
from zshpower.prompt.sections.ruby import Ruby
from zshpower.prompt.sections.rust import Rust
from snakypy import printer


class ResetCommand(Base):
    def __init__(self, home):
        Base.__init__(self, home)

    def run(self, arguments) -> None:
        checking_init(self.HOME)
        if arguments["--config"]:
            create_config(config_content, self.config_file, force=True)
            printer("Reset process finished.", foreground=FG.FINISH)
            reload_zsh()
        elif arguments["--db"]:
            DAO().create_table([item for item in sql().keys()][0])
            with ThreadPoolExecutor(max_workers=27) as executor:
                executor.submit(Dart().set_version, action="insert")
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
                    set_time=0.050,
                    bar=False,
                    header="ZSHPower Restoring the database ...",
                    foreground=FG.QUESTION,
                )
                printer("Done!", foreground=FG.FINISH)
