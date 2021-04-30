from subprocess import run
from zshpower.prompt.sections.lib.utils import Version


class Ruby(Version):
    def __init__(self):
        super(Ruby, self).__init__()
        self.files = ("Gemfile", "Rakefile")
        self.extensions = (".rb",)

    def get_version(self, config, version, key="ruby", ext="rb-", space_elem=" "):
        return super().get(config, version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, key="ruby", action=None):
        version = run(
            "ruby --version 2>/dev/null", capture_output=True, shell=True, text=True
        ).stdout

        version = version.replace("\n", " ").split(" ")[1].split("p")[0]

        if not version:
            return False

        return super().set(version, key, action)
