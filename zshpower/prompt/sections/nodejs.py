class NodeJs:
    def __init__(self, config, version, space_elem=" "):
        from .lib.utils import symbol_ssh, element_spacing

        self.config = config
        self.version = version
        self.space_elem = space_elem
        self.files = ("package.json",)
        self.folders = ("node_modules",)
        self.symbol = symbol_ssh(self.config["nodejs"]["symbol"], "node-")
        self.color = self.config["nodejs"]["color"]
        self.prefix_color = self.config["nodejs"]["prefix"]["color"]
        self.prefix_text = element_spacing(self.config["nodejs"]["prefix"]["text"])
        self.micro_version_enable = self.config["nodejs"]["version"]["micro"]["enable"]

    # def get_version(self, space_elem=" "):
    #     from subprocess import run

    #     output = run(
    #         "node -v 2>/dev/null", capture_output=True, shell=True, text=True
    #     ).stdout

    #     nodejs_version = output.replace("\n", "")

    #     if not nodejs_version:
    #         return False

    #     nodejs_version = nodejs_version[1:].split(".")

    #     if not self.micro_version_enable:
    #         return f"{'{0[0]}.{0[1]}'.format(nodejs_version)}{space_elem}"
    #     return f"{'{0[0]}.{0[1]}.{0[2]}'.format(nodejs_version)}{space_elem}"

    def __str__(self):
        from .lib.utils import separator
        from zshpower.utils.catch import find_objects
        from os import getcwd as os_getcwd
        from .lib.utils import Color

        nodejs_version = self.version

        if (
            nodejs_version
            and find_objects(
                os_getcwd(),
                files=self.files,
                folders=self.folders,
            )
        ):

            prefix = f"{Color(self.prefix_color)}" f"{self.prefix_text}{Color().NONE}"

            return str(
                f"{separator(self.config)}{prefix}"
                f"{Color(self.color)}"
                f"{self.symbol}{nodejs_version}{self.space_elem}{Color().NONE}"
            )
        return ""


def nodejs(config):
    import concurrent.futures

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(NodeJs, config)
        return_value = future.result()
        return return_value
