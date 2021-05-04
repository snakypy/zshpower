from subprocess import run
from zshpower.prompt.sections.lib.utils import Version


class Php(Version):
    def __init__(self):
        super(Php, self).__init__()
        self.files = ("composer.json",)
        self.extensions = (".php",)

    def get_version(self, config, version, key="php", ext="php-", space_elem=" "):
        return super().get(config, version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, key="php", action=None):
        version = run(
            """php -v 2>&1 | grep "^PHP\\s*[0-9.]\\+" | awk '{print $2}'""",
            capture_output=True,
            shell=True,
            text=True,
        ).stdout

        version = version.replace("\n", "")

        if version:
            return super().set(version, key, action)

        return False
