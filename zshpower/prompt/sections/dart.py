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

    def get_version(self, config, version, key="dart", ext="dt-", space_elem=" "):
        return super().get(config, version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, key="dart", action=None):
        version = run("dart --version 2>&1", capture_output=True, shell=True, text=True)

        if not version.returncode == 0:
            return False

        version = version.stdout.replace("\n", "").split(" ")[3]

        return super().set(version, key, action)


# from threading import Thread
# from time import sleep
#
# def a():
#     with open() as f:
#         f.write()
#     return "a"
#
#
# def b():
#     x = a()
#     return "b", x
#
#
# def c():
#     x = a()
#     return "c", x
#
# Thread(target=a).start()
# Thread(target=b).start()
# Thread(target=c).start()
