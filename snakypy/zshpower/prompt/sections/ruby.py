from subprocess import run

from snakypy.zshpower.prompt.sections.utils import Version
from snakypy.zshpower.config.base import Base


class Ruby(Version, Base):
    def __init__(self):
        super(Ruby, self).__init__()
        self.files = ("Gemfile", "Rakefile")
        self.extensions = (".rb",)

    def get_version(
        self, config, reg_version, key="ruby", ext="rb-", space_elem=" "
    ) -> str:
        return super().get(config, reg_version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, exec="ruby", key="ruby", action=None):
        command = run("ruby --version", capture_output=True, shell=True, text=True)
        version = command.stdout.replace("\n", " ").split(" ")[1].split("p")[0]
        return super().set(command, version, exec, key, action)
