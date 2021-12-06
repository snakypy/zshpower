from subprocess import run

from snakypy.zshpower.config.base import Base
from snakypy.zshpower.prompt.sections.utils import Version


class NodeJs(Version, Base):
    def __init__(self, *args):
        super(NodeJs, self).__init__()
        self.args: tuple = args
        self.key = "nodejs"
        self.app_executable = "node"
        self.shorten = "node-"
        self.finder = {
            "extensions": [".js"],
            "folders": ["node_modules"],
            "files": ["package.json"],
        }

    def get_version(self, space_elem: str = " ") -> str:
        # args[0]: dict = config file (toml)
        # args[1]: dict = database registers
        return super().get(
            self.args[0], self.args[1], self.key, self.shorten, space_elem=space_elem
        )

    def set_version(self, action: str = "") -> bool:
        command = run("node -v", capture_output=True, shell=True, text=True)
        version = command.stdout.replace("\n", "").split("v")[1]
        return super().set(
            command, version, self.app_executable, self.key, action=action
        )

    def __str__(self):
        return self.get_version()


# def _nodejs(config, key):
#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         future = executor.submit(NodeJs().get_version, config, key)
#         return_value = future.result()
#         return return_value
