import sys
from sqlite3 import OperationalError
from snakypy import FG
from snakypy.console import loading, printer
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
            Docker().set_version(action="update")
            Dart().set_version(action="update")
            Dotnet().set_version(action="update")
            Elixir().set_version(action="update")
            Golang().set_version(action="update")
            Java().set_version(action="update")
            Julia().set_version(action="update")
            NodeJs().set_version(action="update")
            Php().set_version(action="update")
            Ruby().set_version(action="update")
            Rust().set_version(action="update")
            Scala().set_version(action="update")
            Perl().set_version(action="update")
            loading(
                set_time=0.03,
                bar=False,
                header="[Synchronizing versions with database ...]",
                foreground=FG.CYAN,
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
