# from zshpower.utils.check import is_tool

# # DEPRECATED
# def docker_status():
#     from zshpower.utils.process import shell_command

#     cmd = """
#     state=$(docker info > /dev/null 2>&1)
#     if [[ $? -ne 0 ]]; then
#         echo "disabled"
#     fi
#     """
#     return shell_command(cmd)[0]


class Docker:
    def __init__(self, config):
        from .lib.utils import symbol_ssh, element_spacing

        self.config = config
        self.search_f = ("Dockerfile", "docker-compose.yml")
        self.docker_version_enable = config["docker"]["version"]["enable"]
        self.docker_version_micro_enable = config["docker"]["version"]["micro"][
            "enable"
        ]
        self.docker_symbol = symbol_ssh(config["docker"]["symbol"], "dkr-")
        self.docker_color = config["docker"]["color"]
        self.docker_prefix_color = config["docker"]["prefix"]["color"]
        self.docker_prefix_text = element_spacing(config["docker"]["prefix"]["text"])

    def get_version(self, space_elem=" "):
        from subprocess import PIPE, Popen as subprocess_popen

        p = subprocess_popen(
            "docker version --format '{{.Server.Version}}'",
            shell=True,
            stdout=PIPE,
            stderr=PIPE,
            universal_newlines=True,
        )

        output, err = p.communicate()
        docker_v = output.replace("\n", "").split(".")

        if err:
            return False
        elif not self.docker_version_micro_enable:
            return f"{'.'.join(docker_v[:-1])}{space_elem}"
        return f"{'.'.join(docker_v)}{space_elem}"

    def __str__(self):
        from .lib.utils import Color
        from .lib.utils import separator
        from zshpower.utils.check import is_tool
        from zshpower.utils.catch import find_files
        from os import getcwd as os_getcwd

        docker_version = self.get_version()

        if is_tool("docker"):
            if (
                self.docker_version_enable
                and find_files(os_getcwd(), files=self.search_f)
                and docker_version
            ):
                docker_prefix = (
                    f"{Color(self.docker_prefix_color)}"
                    f"{self.docker_prefix_text}{Color().NONE}"
                )
                docker_export = (
                    f"{separator(self.config)}{docker_prefix}"
                    f"{Color(self.docker_color)}"
                    f"{self.docker_symbol}{docker_version}{Color().NONE}"
                )
                return str(docker_export)
        return ""
