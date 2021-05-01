# perl -Mstrict -wall -e "print join('.', map {ord} split('', \$^V));"
# perl -v | awk '/This/ {print $4}' | sed -e 's/v//'

from subprocess import run
from zshpower.prompt.sections.lib.utils import Version


class Perl(Version):
    def __init__(self):
        super(Perl, self).__init__()
        self.extensions = (".pl",)

    def get_version(self, config, version, key="perl", ext="pl-", space_elem=" "):
        return super().get(config, version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, key="perl", action=None):
        version = run(
            "perl -version | awk '/version/' 2>&1",
            capture_output=True,
            text=True,
            shell=True,
        ).stdout

        if not version.replace("\n", ""):
            return False

        version = version.split()[8].replace("v", "").replace("(", "").replace(")", "")

        return super().set(version, key, action)
