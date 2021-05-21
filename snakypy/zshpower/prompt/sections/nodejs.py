import concurrent.futures
from subprocess import run

from snakypy.zshpower.prompt.sections.utils import Version


class NodeJs(Version):
    def __init__(self):
        super(NodeJs, self).__init__()
        self.files = ("package.json",)
        self.folders = ("node_modules",)

    def get_version(
        self, config, reg_version, key="nodejs", ext="node-", space_elem=" "
    ) -> str:
        return super().get(config, reg_version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, key="nodejs", action=None) -> bool:
        version = run("node -v 2>/dev/null", capture_output=True, shell=True, text=True)

        if version.returncode != 127 and version.returncode != 1:
            version_format = version.stdout.replace("\n", "").split("v")[1]
            return super().set(version_format, key, action)

        return False


def _nodejs(config, key):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(NodeJs().get_version, config, key)
        return_value = future.result()
        return return_value
