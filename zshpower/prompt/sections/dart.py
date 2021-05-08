class Dart:
    def __init__(self, config):
        from .lib.utils import symbol_ssh, element_spacing

        self.config = config
        self.extensions = (".dart",)
        self.files = (
            "pubspec.yaml",
            "config.src.yaml",
            "analysis_options.yaml",
        )
        self.folders = ()
        self.symbol = symbol_ssh(config["dart"]["symbol"], "dart-")
        self.color = config["dart"]["color"]
        self.prefix_color = config["dart"]["prefix"]["color"]
        self.prefix_text = element_spacing(config["dart"]["prefix"]["text"])
        self.micro_version_enable = config["dart"]["version"]["micro"]["enable"]

    def get_version(self, space_elem=" "):
        from subprocess import run

        dart_version = run(
            "dart --version 2>&1", capture_output=True, shell=True, text=True
        )

        if not dart_version.returncode == 0:
            return False

        dart_version = dart_version.stdout.replace("\n", "").split(" ")[3].split(".")

        if not self.micro_version_enable:
            return f"{'{0[0]}.{0[1]}'.format(dart_version)}{space_elem}"
        return f"{'{0[0]}.{0[1]}.{0[2]}'.format(dart_version)}{space_elem}"

    def __str__(self):
        from .lib.utils import Color, separator
        from zshpower.utils.catch import find_objects
        from os import getcwd as os_getcwd

        dart_version = self.get_version()

        if dart_version and find_objects(
            os_getcwd(),
            files=self.files,
            folders=self.folders,
            extension=self.extensions,
        ):
            prefix = f"{Color(self.prefix_color)}{self.prefix_text}{Color().NONE}"

            return str(
                (
                    f"{separator(self.config)}{prefix}"
                    f"{Color(self.color)}{self.symbol}"
                    f"{dart_version}{Color().NONE}"
                )
            )
        return ""


def dart(config):
    import concurrent.futures

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(Dart, config)
        return_value = future.result()
        return return_value
