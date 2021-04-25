from zshpower.prompt.sections.package import Rust


class Ruby:
    def __init__(self, config):
        from .lib.utils import symbol_ssh, element_spacing

        self.config = config
        self.files = ("Gemfile", "Rakefile")
        self.extensions = (".rb",)
        self.folders = ()
        self.symbol = symbol_ssh(config["ruby"]["symbol"], "rb-")
        self.color = config["ruby"]["color"]
        self.prefix_color = config["ruby"]["prefix"]["color"]
        self.prefix_text = element_spacing(config["ruby"]["prefix"]["text"])
        self.micro_version_enable = config["ruby"]["version"]["micro"]["enable"]

    def get_version(self, space_elem=" "):
        from subprocess import run

        ruby_version = run(
            "ruby --version 2>/dev/null", capture_output=True, shell=True, text=True
        ).stdout

        if not ruby_version.replace("\n", ""):
            return False

        # E.g: ['3', '0', '1p64']
        ruby_version = ruby_version.replace("\n", " ").split(" ")[1].split(".")

        # Format version. Remove p64. E.g: ['3', '0', '1']
        ruby_version.append(ruby_version[2].split("p")[0])
        ruby_version.pop(2)

        if not self.micro_version_enable:
            return f"{'{0[0]}.{0[1]}'.format(ruby_version)}{space_elem}"
        return f"{'{0[0]}.{0[1]}.{0[2]}'.format(ruby_version)}{space_elem}"

    def __str__(self):
        from .lib.utils import Color, separator
        from zshpower.utils.catch import find_objects
        from os import getcwd as os_getcwd

        ruby_version = self.get_version()

        if (
            ruby_version
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
                    f"{self.get_version()}{Color().NONE}"
                )
            )
        return ""


def ruby(config):
    import concurrent.futures

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(Ruby, config)
        return_value = future.result()
        return return_value
