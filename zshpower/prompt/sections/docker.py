from subprocess import run
from zshpower.prompt.sections.lib.utils import Version


class Docker(Version):
    def __init__(self):
        super(Docker, self).__init__()
        self.files = ("Dockerfile", "docker-compose.yml")

    def get_version(self, config, version, key="docker", ext="dkr-", space_elem=" "):
        return super().get(config, version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, key="docker", action=None):
        version = run(
            "docker version",
            capture_output=True,
            text=True,
            shell=True,
        )

        if version.returncode != 127 and version.returncode != 1:
            version = (
                version.stdout.split("Version")[1]
                .strip()
                .split("\n")[0]
                .replace(":", "")
                .strip()
            )
            return super().set(version, key, action)

        return False


# TODO: Get version Docker by Shell script (DEPRECATED)
# def docker_status():
#     from zshpower.utils.process import shell_command

#     cmd = """
#     state=$(docker info > /dev/null 2>&1)
#     if [[ $? -ne 0 ]]; then
#         echo "disabled"
#     fi
#     """
#     return shell_command(cmd)[0]
