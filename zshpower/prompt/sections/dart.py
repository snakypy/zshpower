from subprocess import run
from zshpower.prompt.sections.lib.utils import Version


class Dart(Version):
    def __init__(self):
        super(Dart, self).__init__()
        self.extensions = (".dart",)
        self.files = (
            "pubspec.yaml",
            "config.src.yaml",
            "analysis_options.yaml",
        )

    def get_version(
        self, config, reg_version, key="dart", ext="dt-", space_elem=" "
    ) -> str:
        return super().get(config, reg_version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, key="dart", action=None) -> bool:
        version = run("dart --version 2>&1", capture_output=True, shell=True, text=True)

        if not version.returncode == 0:
            return False

        version_format = version.stdout.replace("\n", "").split(" ")[3]

        return super().set(version_format, key, action)
