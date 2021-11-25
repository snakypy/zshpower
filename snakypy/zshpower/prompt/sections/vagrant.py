from subprocess import run

from snakypy.zshpower.config.base import Base
from snakypy.zshpower.prompt.sections.utils import Version


class Vagrant(Version, Base):
    def __init__(self):
        super(Vagrant, self).__init__()
        self.files = ("Vagrantfile",)

    def get_version(
        self, config, reg_version, key="vagrant", ext="vag-", space_elem=" "
    ) -> str:
        return super().get(config, reg_version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, exec_="vagrant", key="vagrant", action=None):
        command = run("vagrant --version", capture_output=True, shell=True, text=True)
        version = command.stdout.split()[1].replace(" ", "")
        return super().set(command, version, exec_, key, action)
