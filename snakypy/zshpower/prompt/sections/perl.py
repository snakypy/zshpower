from subprocess import run

from snakypy.zshpower.config.base import Base
from snakypy.zshpower.prompt.sections.utils import Version


class Perl(Version, Base):
    def __init__(self, *args):
        super(Perl, self).__init__()
        self.args: tuple = args
        self.key = "perl"
        self.app_executable = "perl"
        self.shorten = "pl-"
        self.extensions = (".pl",)

    def get_version(self, space_elem: str = " ") -> str:
        return super().get(
            self.args[0], self.args[1], self.key, self.shorten, space_elem=space_elem
        )

    def set_version(self, action: str = "") -> bool:
        command = run(
            # Model
            # perl -Mstrict -wall -e "print join('.', map {ord} split('', \$^V));"
            # perl -v | awk '/This/ {print $4}' | sed -e 's/v//'
            f"{self.app_executable} -version | awk '/version/' 2>&1",
            capture_output=True,
            shell=True,
            text=True,
        )
        version = (
            command.stdout.split()[8].replace("v", "").replace("(", "").replace(")", "")
        )
        return super().set(
            command, version, self.app_executable, self.key, action=action
        )

    def __str__(self):
        return self.get_version()
