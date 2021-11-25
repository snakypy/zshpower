from subprocess import run

from snakypy.zshpower.config.base import Base
from snakypy.zshpower.prompt.sections.utils import Version


class Helm(Version, Base):
    def __init__(self):
        super(Helm, self).__init__()
        self.files = ("helmfile.yaml", "Chart.yaml")

    def get_version(
        self, config, reg_version, key="helm", ext="helm-", space_elem=" "
    ) -> str:
        return super().get(config, reg_version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, exec_="helm", key="helm", action=None) -> bool:
        command = run("helm version", capture_output=True, shell=True, text=True)
        version = command.stdout.split(":")[1].split('"')[1].replace("v", "")
        return super().set(command, version, exec_, key, action)
