class Golang:
    def __init__(self, config, version, space_elem=" "):
        from .lib.utils import symbol_ssh, element_spacing

        self.config = config
        self.version = version
        self.space_elem = space_elem
        self.extensions = (".go",)
        self.files = ("go.mod", "glide.yaml")
        self.folders = ("Godeps",)
        self.symbol = symbol_ssh(config["golang"]["symbol"], "go-")
        self.color = config["golang"]["color"]
        self.prefix_color = config["golang"]["prefix"]["color"]
        self.prefix_text = element_spacing(config["golang"]["prefix"]["text"])
        self.micro_version_enable = config["golang"]["version"]["micro"]["enable"]

    # def get_version(self, space_elem=" "):
    #     from subprocess import run

    #     output_version = run(
    #         "go version", capture_output=True, shell=True, text=True
    #     ).stdout

    #     if not output_version.replace("\n", ""):
    #         return False

    #     output_version = output_version.replace("go", "").split(" ")[2].split(".")

    #     if not self.micro_version_enable:
    #         return f"{'{0[0]}.{0[1]}'.format(output_version)}{space_elem}"
    #     return f"{'{0[0]}.{0[1]}.{0[2]}'.format(output_version)}{space_elem}"

    def __str__(self):
        from .lib.utils import Color, separator
        from zshpower.utils.catch import find_objects
        from os import getcwd as os_getcwd

        golang_version = self.version

        if (
            golang_version
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
                    f"{golang_version}{self.space_elem}{Color().NONE}"
                )
            )
        return ""


def golang(config):
    import concurrent.futures

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(Golang, config)
        return_value = future.result()
        return return_value
