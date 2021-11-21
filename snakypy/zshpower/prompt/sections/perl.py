from subprocess import run

from snakypy.zshpower.config.base import Base
from snakypy.zshpower.prompt.sections.utils import Version


class Perl(Version, Base):
    def __init__(self):
        super(Perl, self).__init__()
        self.extensions = (".pl",)

    def get_version(
        self, config, reg_version, key="perl", ext="pl-", space_elem=" "
    ) -> str:
        return super().get(config, reg_version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, exec_="perl", key="perl", action=None):
        command = run(
            # Model
            # perl -Mstrict -wall -e "print join('.', map {ord} split('', \$^V));"
            # perl -v | awk '/This/ {print $4}' | sed -e 's/v//'
            "perl -version | awk '/version/' 2>&1",
            capture_output=True,
            shell=True,
            text=True,
        )
        version = (
            command.stdout.split()[8].replace("v", "").replace("(", "").replace(")", "")
        )
        return super().set(command, version, exec_, key, action)
