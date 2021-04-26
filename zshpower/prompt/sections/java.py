class Java:
    def __init__(self, config, version, space_elem=" "):
        from .lib.utils import symbol_ssh, element_spacing

        self.config = config
        self.version = version
        self.space_elem = space_elem
        self.extensions = (".java",)
        self.files = ()
        self.folders = ()
        self.symbol = symbol_ssh(config["java"]["symbol"], "java-")
        self.color = config["java"]["color"]
        self.prefix_color = config["java"]["prefix"]["color"]
        self.prefix_text = element_spacing(config["java"]["prefix"]["text"])
        self.version_enable = config["java"]["version"]["enable"]
        self.micro_version_enable = config["java"]["version"]["micro"]["enable"]

    # def get_version(self, space_elem=" "):
    #     from subprocess import run

    #     java_version = run(
    #         """java -version 2>&1 | awk -F '"' '/version/ {print $2}'""",
    #         capture_output=True,
    #         shell=True,
    #         text=True,
    #     ).stdout

    #     if not java_version.replace("\n", ""):
    #         return False

    #     java_version = java_version.replace("\n", "").split("_")[0].split(".")

    #     if not self.micro_version_enable:
    #         return f"{'{0[0]}.{0[1]}'.format(java_version)}{space_elem}"
    #     return f"{'{0[0]}.{0[1]}.{0[2]}'.format(java_version)}{space_elem}"

    def __str__(self):
        from .lib.utils import Color, separator
        from zshpower.utils.catch import find_objects
        from os import getcwd as os_getcwd

        java_version = self.version

        if (
            self.version_enable
            and java_version
            and find_objects(
                os_getcwd(),
                files=self.files,
                folders=self.folders,
                extension=self.extensions,
            )
        ):
            prefix = f"{Color(self.prefix_color)}{self.prefix_text}{Color().NONE}"

            return str(
                (
                    f"{separator(self.config)}{prefix}"
                    f"{Color(self.color)}{self.symbol}"
                    f"{java_version}{self.space_elem}{Color().NONE}"
                )
            )
        return ""


def java(config):
    import concurrent.futures

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(Java, config)
        return_value = future.result()
        return return_value
