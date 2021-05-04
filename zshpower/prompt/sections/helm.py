from subprocess import run
from zshpower.prompt.sections.lib.utils import Version


class Helm(Version):
    def __init__(self):
        super(Helm, self).__init__()
        self.files = ("helmfile.yaml", "Chart.yaml")

    def get_version(self, config, version, key="helm", ext="helm-", space_elem=" "):
        return super().get(config, version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, key="helm", action=None):
        version = run("helm version 2>&1", capture_output=True, shell=True, text=True)

        if version.returncode != 127 and version.returncode != 1:
            version = version.stdout.split(":")[1].split('"')[1].replace("v", "")
            return super().set(version, key, action)

        return False
