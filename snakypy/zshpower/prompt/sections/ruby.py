from subprocess import run
from snakypy.zshpower.prompt.sections.lib.utils import Version


class Ruby(Version):
    def __init__(self):
        super(Ruby, self).__init__()
        self.files = ("Gemfile", "Rakefile")
        self.extensions = (".rb",)

    def get_version(
        self, config, reg_version, key="ruby", ext="rb-", space_elem=" "
    ) -> str:
        return super().get(config, reg_version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, key="ruby", action=None) -> bool:
        version = run(
            "ruby --version 2>/dev/null",
            capture_output=True,
            shell=True,
            text=True,
        )

        if version.returncode != 127 and version.returncode != 1:
            version_format = (
                version.stdout.replace("\n", " ").split(" ")[1].split("p")[0]
            )
            return super().set(version_format, key, action)
        return False
