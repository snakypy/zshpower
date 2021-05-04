import sys
from sqlite3 import OperationalError
from threading import Thread
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

    def main(self):
        try:
            checking_init(self.HOME)
            # Docker().set_version(action="update")
            # Dart().set_version(action="update")
            # Dotnet().set_version(action="update")
            # Elixir().set_version(action="update")
            # Golang().set_version(action="update")
            # Java().set_version(action="update")
            # Julia().set_version(action="update")
            # NodeJs().set_version(action="update")
            # Php().set_version(action="update")
            # Ruby().set_version(action="update")
            # Rust().set_version(action="update")
            # Scala().set_version(action="update")
            # Perl().set_version(action="update")
            # CMake().set_version(action="update")
            # Crystal().set_version(action="update")
            # Deno().set_version(action="update")
            # Erlang().set_version(action="update")
            # Helm().set_version(action="update")
            # Kotlin().set_version(action="update")
            # Nim().set_version(action="update")
            # Ocaml().set_version(action="update")
            # Vagrant().set_version(action="update")
            # Zig().set_version(action="update")

            Thread(target=Dart().set_version, kwargs={"action": "update"}).start()
            Thread(target=Docker().set_version, kwargs={"action": "update"}).start()
            Thread(target=Dotnet().set_version, kwargs={"action": "update"}).start()
            Thread(target=Elixir().set_version, kwargs={"action": "update"}).start()
            Thread(target=Golang().set_version, kwargs={"action": "update"}).start()
            Thread(target=Java().set_version, kwargs={"action": "update"}).start()
            Thread(target=Julia().set_version, kwargs={"action": "update"}).start()
            Thread(target=NodeJs().set_version, kwargs={"action": "update"}).start()
            Thread(target=Php().set_version, kwargs={"action": "update"}).start()
            Thread(target=Ruby().set_version, kwargs={"action": "update"}).start()
            Thread(target=Rust().set_version, kwargs={"action": "update"}).start()
            Thread(target=Scala().set_version, kwargs={"action": "update"}).start()
            Thread(target=Perl().set_version, kwargs={"action": "update"}).start()
            Thread(target=CMake().set_version, kwargs={"action": "update"}).start()
            Thread(target=Crystal().set_version, kwargs={"action": "update"}).start()
            Thread(target=Deno().set_version, kwargs={"action": "update"}).start()
            Thread(target=Erlang().set_version, kwargs={"action": "update"}).start()
            Thread(target=Helm().set_version, kwargs={"action": "update"}).start()
            Thread(target=Kotlin().set_version, kwargs={"action": "update"}).start()
            Thread(target=Nim().set_version, kwargs={"action": "update"}).start()
            Thread(target=Ocaml().set_version, kwargs={"action": "update"}).start()
            Thread(target=Vagrant().set_version, kwargs={"action": "update"}).start()
            Thread(target=Zig().set_version, kwargs={"action": "update"}).start()
            loading(
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
