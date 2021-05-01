from subprocess import run
from zshpower.prompt.sections.lib.utils import Version


class Crystal(Version):
    def __init__(self):
        super(Crystal, self).__init__()
        self.extensions = (".cr",)
        self.files = ("shard.yml",)

    def get_version(self, config, version, key="crystal", ext="cr-", space_elem=" "):
        return super().get(config, version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, key="crystal", action=None):
        version = run(
            "crystal version 2>&1", capture_output=True, shell=True, text=True
        )

        if not version.returncode == 0:
            return False

        version = version.stdout.split()[1]

        return super().set(version, key, action)
