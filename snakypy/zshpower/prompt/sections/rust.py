from subprocess import run

from snakypy.zshpower.config.base import Base
from snakypy.zshpower.prompt.sections.utils import Version


class Rust(Version, Base):
    def __init__(self):
        super(Rust, self).__init__()
        self.files = ("Cargo.toml",)
        self.extensions = (".rs",)

    def get_version(
        self, config, reg_version, key="rust", ext="rs-", space_elem=" "
    ) -> str:
        return super().get(config, reg_version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, exec_="rustc", key="rust", action=None):
        command = run("rustc --version", capture_output=True, shell=True, text=True)
        version = command.stdout.split(" ")[1].replace("\n", "")
        return super().set(command, version, exec_, key, action)
