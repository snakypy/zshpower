from subprocess import run

from snakypy.zshpower.prompt.sections.utils import Version


class Helm(Version):
    def __init__(self):
        super(Helm, self).__init__()
        self.files = ("helmfile.yaml", "Chart.yaml")

    def get_version(
        self, config, reg_version, key="helm", ext="helm-", space_elem=" "
    ) -> str:
        return super().get(config, reg_version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, key="helm", action=None) -> bool:
        version = run("helm version 2>&1", capture_output=True, shell=True, text=True)

        if version.returncode != 127 and version.returncode != 1:
            version_format = version.stdout.split(":")[1].split('"')[1].replace("v", "")
            return super().set(version_format, key, action)

        return False
