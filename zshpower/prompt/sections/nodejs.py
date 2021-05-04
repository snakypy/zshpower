from subprocess import run
from zshpower.prompt.sections.lib.utils import Version
import concurrent.futures


class NodeJs(Version):
    def __init__(self):
        super(NodeJs, self).__init__()
        self.files = ("package.json",)
        self.folders = ("node_modules",)

    def get_version(self, config, register, key="nodejs", ext="node-", space_elem=" "):
        return super().get(config, register, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, key="nodejs", action=None):
        version = run("node -v 2>/dev/null", capture_output=True, shell=True, text=True)

        if version.returncode != 127 and version.returncode != 1:
            version = version.stdout.replace("\n", "").split("v")[1]
            return super().set(version, key, action)

        return False


def _nodejs(config, key):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(NodeJs().get_version, config, key)
        return_value = future.result()
        return return_value
