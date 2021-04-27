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

from subprocess import run
from zshpower.database.dao import DAO
from .lib.utils import Color
from .lib.utils import separator
from zshpower.utils.catch import find_objects
from os import getcwd as os_getcwd


class DockerGetVersion:
    def __init__(self, config, version, space_elem=" "):
        from .lib.utils import symbol_ssh, element_spacing

        self.config = config
        self.version = version
        self.space_elem = space_elem
        self.files = ("Dockerfile", "docker-compose.yml")
        self.extensions = ()
        self.folders = ()
        self.symbol = symbol_ssh(config["docker"]["symbol"], "dkr-")
        self.color = config["docker"]["color"]
        self.prefix_color = config["docker"]["prefix"]["color"]
        self.prefix_text = element_spacing(config["docker"]["prefix"]["text"])
        self.micro_version_enable = config["docker"]["version"]["micro"]["enable"]

    def __str__(self):
        docker_version = self.version

        if (
            docker_version
            and find_objects(
                os_getcwd(),
                files=self.files,
                folders=self.folders,
                extension=self.extensions,
            )
        ):
            prefix = f"{Color(self.prefix_color)}" f"{self.prefix_text}{Color().NONE}"
            return str(
                f"{separator(self.config)}{prefix}"
                f"{Color(self.color)}"
                f"{self.symbol}{docker_version}{self.space_elem}{Color().NONE}"
            )
        return ""


class DockerSetVersion(DAO):
    def __init__(self):
        DAO.__init__(self)

    def main(self, /, action=None):
        if action:
            docker_version = run(
                "docker version",
                capture_output=True,
                text=True,
                shell=True,
            ).stdout

            if not docker_version.replace("\n", ""):
                return False

            docker_version = docker_version.split("Version")[1].strip().split("\n")[0].replace(":", "").strip()

            if action == "insert":
                sql = f"""SELECT version FROM main WHERE name = 'docker';"""
                query = self.query(sql)

                if not query:
                    sql = f"""INSERT INTO main (name, version)
                    VALUES ('docker', '{docker_version}');"""
                    self.execute(sql)
                    self.commit()

            elif action == "update":
                sql = f"""UPDATE main SET version = '{docker_version}' WHERE name = 'docker';"""
                self.execute(sql)
                self.commit()

            self.connection.close()
            return True

        return False

