import concurrent.futures
from subprocess import run

from snakypy.zshpower.config.base import Base
from snakypy.zshpower.prompt.sections.utils import Version


class NodeJs(Version, Base):
    def __init__(self):
        super(NodeJs, self).__init__()
        self.files = ("package.json",)
        self.folders = ("node_modules",)

    def get_version(
        self, config, reg_version, key="nodejs", ext="node-", space_elem=" "
    ) -> str:
        return super().get(config, reg_version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, exec_="node", key="nodejs", action=None):
        command = run("node -v", capture_output=True, shell=True, text=True)
        version = command.stdout.replace("\n", "").split("v")[1]
        return super().set(command, version, exec_, key, action)


def _nodejs(config, key):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(NodeJs().get_version, config, key)
        return_value = future.result()
        return return_value
