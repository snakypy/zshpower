import sys
from sqlite3 import OperationalError

from snakypy import FG
from snakypy.console import loading, printer

from zshpower.utils.check import checking_init
from zshpower.prompt.sections.rust import RustSetVersion
from zshpower.prompt.sections.ruby import RubySetVersion
from zshpower.prompt.sections.php import PhpSetVersion
from zshpower.prompt.sections.nodejs import NodeJsSetVersion
from zshpower.prompt.sections.julia import JuliaSetVersion
from zshpower.prompt.sections.java import JavaSetVersion
from zshpower.prompt.sections.golang import GolangSetVersion
from zshpower.prompt.sections.elixir import ElixirSetVersion
from zshpower.prompt.sections.docker import DockerSetVersion
from zshpower.prompt.sections.dotnet import DotnetSetVersion
from zshpower.prompt.sections.dart import DartSetVersion
from zshpower.config.base import Base


class Sync(Base):
    def __init__(self, home):
        Base.__init__(self, home)

    def main(self):
        try:
            checking_init(self.HOME)
            DockerSetVersion().main(action="update")
            DartSetVersion().main(action="update")
            DotnetSetVersion().main(action="update")
            ElixirSetVersion().main(action="update")
            GolangSetVersion().main(action="update")
            JavaSetVersion().main(action="update")
            JuliaSetVersion().main(action="update")
            NodeJsSetVersion().main(action="update")
            PhpSetVersion().main(action="update")
            RubySetVersion().main(action="update")
            RustSetVersion().main(action="update")
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
