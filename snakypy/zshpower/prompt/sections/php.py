from subprocess import run
from snakypy.zshpower.prompt.sections.utils import Version


class Php(Version):
    def __init__(self):
        super(Php, self).__init__()
        self.files = ("composer.json",)
        self.extensions = (".php",)

    def get_version(
        self, config, reg_version, key="php", ext="php-", space_elem=" "
    ) -> str:
        return super().get(config, reg_version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, key="php", action=None) -> bool:
        version = run(
            """php -v 2>&1 | grep "^PHP\\s*[0-9.]\\+" | awk '{print $2}'""",
            capture_output=True,
            shell=True,
            text=True,
        ).stdout

        version_format = version.replace("\n", "")

        if version_format:
            return super().set(version_format, key, action)

        return False
