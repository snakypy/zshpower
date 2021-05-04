from subprocess import run
from zshpower.prompt.sections.lib.utils import Version


class Rust(Version):
    def __init__(self):
        super(Rust, self).__init__()
        self.files = ("Cargo.toml",)
        self.extensions = (".rs",)

    def get_version(self, config, version, key="rust", ext="rs-", space_elem=" "):
        return super().get(config, version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, key="rust", action=None):
        version = run("rustc --version", capture_output=True, shell=True, text=True)

        if version.returncode != 127 and version.returncode != 1:
            version = version.stdout.split(" ")[1].replace("\n", "")
            return super().set(version, key, action)

        return False
