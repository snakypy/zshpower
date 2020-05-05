from os import getcwd
from subprocess import check_output
from os.path import isfile, join
from .lib.utils import Color, symbol_ssh, separator, element_spacing
from zshpower.utils.check import is_tool
from zshpower.utils.process import shell_command


def docker_status():
    cmd = """
    state=$(docker info > /dev/null 2>&1)
    if [[ $? -ne 0 ]]; then
        echo "disabled"
    fi
    """
    return shell_command("docker", cmd)[0]


class Docker(Color):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.dockerfile = join(getcwd(), "Dockerfile")
        self.docker_compose = join(getcwd(), "docker-compose.yml")
        self.docker_version_enable = config["docker"]["version"]["enable"]
        self.docker_version_micro_enable = config["docker"]["version"]["micro"][
            "enable"
        ]
        self.docker_symbol = symbol_ssh(config["docker"]["symbol"], "Dkr-")
        self.docker_color = config["docker"]["color"]
        self.docker_prefix_color = config["docker"]["prefix"]["color"]
        self.docker_prefix_text = element_spacing(config["docker"]["prefix"]["text"])

    def get_version(self, space_elem=" "):
        docker_v = (
            check_output(
                "docker version --format '{{.Server.Version}}'",
                shell=True,
                universal_newlines=True,
            )
            .replace("\n", "")
            .split(".")
        )
        if not self.docker_version_micro_enable:
            return f"{'.'.join(docker_v[:-1])}{space_elem}"
        return f"{'.'.join(docker_v)}{space_elem}"

    def __str__(self):
        if (
            is_tool("docker")
            and self.docker_version_enable
            and not docker_status() == "disabled"
        ):
            if isfile(self.dockerfile) or isfile(self.docker_compose):
                docker_prefix = (
                    f"{Color(self.docker_prefix_color)}"
                    f"{self.docker_prefix_text}{Color().NONE}"
                )
                docker_export = (
                    f"{separator(self.config)}{docker_prefix}"
                    f"{Color(self.docker_color)}"
                    f"{self.docker_symbol}{self.get_version()}{Color().NONE}"
                )
                return str(docker_export)
        return ""
