import sys
from concurrent.futures.thread import ThreadPoolExecutor
from sqlite3 import OperationalError
from snakypy import FG
from snakypy.console import loading, printer
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
from zshpower.utils.check import checking_init
from zshpower.prompt.sections.rust import Rust
from zshpower.prompt.sections.ruby import Ruby
from zshpower.prompt.sections.php import Php
from zshpower.prompt.sections.nodejs import NodeJs
from zshpower.prompt.sections.julia import Julia
from zshpower.prompt.sections.java import Java
from zshpower.prompt.sections.scala import Scala
from zshpower.prompt.sections.golang import Golang
from zshpower.prompt.sections.elixir import Elixir
from zshpower.prompt.sections.docker import Docker
from zshpower.prompt.sections.dotnet import Dotnet
from zshpower.prompt.sections.dart import Dart
from zshpower.config.base import Base


class Sync(Base):
    def __init__(self, home):
        Base.__init__(self, home)

    def run(self):
        try:
            checking_init(self.HOME)
            with ThreadPoolExecutor(max_workers=25) as executor:
                executor.submit(Dart().set_version, action="update")
                executor.submit(Docker().set_version, action="update")
                executor.submit(Dotnet().set_version, action="update")
                executor.submit(Elixir().set_version, action="update")
                executor.submit(Golang().set_version, action="update")
                executor.submit(Java().set_version, action="update")
                executor.submit(Julia().set_version, action="update")
                executor.submit(NodeJs().set_version, action="update")
                executor.submit(Php().set_version, action="update")
                executor.submit(Ruby().set_version, action="update")
                executor.submit(Rust().set_version, action="update")
                executor.submit(Scala().set_version, action="update")
                executor.submit(Perl().set_version, action="update")
                executor.submit(CMake().set_version, action="update")
                executor.submit(Crystal().set_version, action="update")
                executor.submit(Deno().set_version, action="update")
                executor.submit(Erlang().set_version, action="update")
                executor.submit(Helm().set_version, action="update")
                executor.submit(Kotlin().set_version, action="update")
                executor.submit(Nim().set_version, action="update")
                executor.submit(Ocaml().set_version, action="update")
                executor.submit(Vagrant().set_version, action="update")
                executor.submit(Zig().set_version, action="update")
                loading(
                    set_time=0.040,
                    bar=False,
                    header="Synchronizing versions with database ...",
                    foreground=FG.QUESTION,
                )

            printer("Done!", foreground=FG.FINISH)
        except OperationalError:
            printer("The database does not exist or is corrupted.", foreground=FG.ERROR)
            loading(
                set_time=0.03,
                bar=False,
                header="[Restoring database ...]",
                foreground=FG.CYAN,
            )
            sys.exit(1)
