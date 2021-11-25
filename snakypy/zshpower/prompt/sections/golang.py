from subprocess import run

from snakypy.zshpower.config.base import Base
from snakypy.zshpower.prompt.sections.utils import Version


class Golang(Version, Base):
    def __init__(self):
        super(Golang, self).__init__()
        self.extensions = (".go",)
        self.files = ("go.mod", "glide.yaml")
        self.folders = ("Godeps",)

    def get_version(
        self, config, reg_version, key="golang", ext="go-", space_elem=" "
    ) -> str:
        return super().get(config, reg_version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, exec_="go", key="golang", action=None) -> bool:
        command = run("go version", capture_output=True, shell=True, text=True)
        version = command.stdout.replace("go", "").split(" ")[2]
        return super().set(command, version, exec_, key, action)
