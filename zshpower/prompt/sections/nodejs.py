from subprocess import run
from zshpower.prompt.sections.lib.utils import Version


class NodeJs(Version):
    def __init__(self):
        super(NodeJs, self).__init__()
        self.files = ("package.json",)
        self.folders = ("node_modules",)

    def get_version(self, config, version, key="nodejs", ext="node-", space_elem=" "):
        return super().get(config, version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, key="nodejs", action=None):
        version = run(
            "node -v 2>/dev/null", capture_output=True, shell=True, text=True
        ).stdout

        if not version.replace("\n", ""):
            return False

        version = version.replace("\n", "").split("v")[1]

        return super().set(version, key, action)
