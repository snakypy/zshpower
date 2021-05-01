from subprocess import run
from zshpower.prompt.sections.lib.utils import Version


class Vagrant(Version):
    def __init__(self):
        super(Vagrant, self).__init__()
        self.files = ("Vagrantfile",)

    def get_version(self, config, version, key="vagrant", ext="vag-", space_elem=" "):
        return super().get(config, version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, key="vagrant", action=None):
        version = run("vagrant --version 2>&1", capture_output=True, shell=True, text=True)

        if not version.returncode == 0:
            return False

        version = version.stdout.split()[1].replace(" ", "")

        return super().set(version, key, action)
