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

    # def get_version(self, space_elem=" "):
    #     from subprocess import run

    #     docker_version = run(
    #         "docker version --format '{{.Server.Version}}'",
    #         capture_output=True,
    #         text=True,
    #         shell=True,
    #     ).stdout

    #     if not docker_version.replace("\n", ""):
    #         return False

    #     docker_version = docker_version.replace("\n", "").split(".")

    #     if not self.micro_version_enable:
    #         return f"{'{0[0]}.{0[1]}'.format(docker_version)}{space_elem}"
    #     return f"{'{0[0]}.{0[1]}.{0[2]}'.format(docker_version)}{space_elem}"

    # def get_version(self, database, space_elem=" "):
    #     sql = """SELECT version FROM info WHERE name = 'docker';"""
    #     query = database.query(sql)[0][0]
    #     if query:
    #         julia_version = query.split(".")
    #         if not self.micro_version_enable:
    #             return f"{'{0[0]}.{0[1]}'.format(julia_version)}{space_elem}"
    #         return f"{'{0[0]}.{0[1]}.{0[2]}'.format(julia_version)}{space_elem}"
    #     return ""

    def __str__(self):
        from .lib.utils import Color
        from .lib.utils import separator
        from zshpower.utils.catch import find_objects
        from os import getcwd as os_getcwd

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


def docker(config):
    import concurrent.futures

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(Docker, config)
        return_value = future.result()
        return return_value


def register(database, /, option=None):
    from subprocess import run

    docker_version = run(
        "docker version --format '{{.Server.Version}}'",
        capture_output=True,
        text=True,
        shell=True,
    ).stdout

    if not docker_version.replace("\n", ""):
        return False

    docker_version = docker_version.replace("\n", "")

    if option:
        if option == "insert":
            sql = f"""INSERT INTO info (name, version) VALUES ('docker', '{docker_version}')"""
        elif option == "update":
            sql = f"""UPDATE info SET version = '{docker_version}' WHERE name = 'docker';"""
        database.execute(sql)
        database.commit()
        return True
    return
