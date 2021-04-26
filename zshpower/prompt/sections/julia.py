class Julia:
    def __init__(self, config, version, space_elem=" "):
        from .lib.utils import symbol_ssh, element_spacing

        self.config = config
        self.version = version
        self.space_elem = space_elem
        self.extensions = (".jl",)
        self.files = ()
        self.folders = ()
        self.symbol = symbol_ssh(config["julia"]["symbol"], "jl-")
        self.color = config["julia"]["color"]
        self.prefix_color = config["julia"]["prefix"]["color"]
        self.prefix_text = element_spacing(config["julia"]["prefix"]["text"])
        self.micro_version_enable = config["julia"]["version"]["micro"]["enable"]

    # def get_version2(self, space_elem=" "):
    #     from subprocess import run

    #     julia_version = run(
    #         "julia --version", capture_output=True, shell=True, text=True
    #     ).stdout

    #     if not julia_version.replace("\n", ""):
    #         return False

    #     julia_version = julia_version.replace("\n", "").split(" ")[2].split(".")

    #     if not self.micro_version_enable:
    #         return f"{'{0[0]}.{0[1]}'.format(julia_version)}{space_elem}"
    #     return f"{'{0[0]}.{0[1]}.{0[2]}'.format(julia_version)}{space_elem}"

    # def get_version(self, database, space_elem=" "):
    #     sql = """SELECT version FROM info WHERE name = 'julia';"""
    #     query = database.query(sql)[0][0]
    #     if query:
    #         julia_version = query.split(".")
    #         if not self.micro_version_enable:
    #             return f"{'{0[0]}.{0[1]}'.format(julia_version)}{space_elem}"
    #         return f"{'{0[0]}.{0[1]}.{0[2]}'.format(julia_version)}{space_elem}"
    #     return ""

    def __str__(self):
        from .lib.utils import Color, separator
        from zshpower.utils.catch import find_objects
        from os import getcwd as os_getcwd

        julia_version = self.version

        if (
            julia_version
            and find_objects(
                os_getcwd(),
                files=self.files,
                folders=self.folders,
                extension=self.extensions,
            )
        ):
            prefix = f"{Color(self.prefix_color)}{self.prefix_text}{Color().NONE}"

            print("JU")

            return str(
                (
                    f"{separator(self.config)}{prefix}"
                    f"{Color(self.color)}{self.symbol}"
                    f"{julia_version}{self.space_elem}{Color().NONE}"
                )
            )
        return ""


def julia(config):
    import concurrent.futures

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(Julia, config)
        return_value = future.result()
        return return_value


def register(database, /, option=None):
    from subprocess import run

    julia_version = run(
        "julia --version", capture_output=True, shell=True, text=True
    ).stdout

    if not julia_version.replace("\n", ""):
        return False

    julia_version = julia_version.replace("\n", "").split(" ")[2]

    if option:
        if option == "insert":
            sql = f"""INSERT INTO info (name, version) VALUES ('julia', '{julia_version}')"""
        elif option == "update":
            sql = f"""UPDATE info SET version = '{julia_version}' WHERE name = 'julia';"""
        database.execute(sql)
        database.commit()
        return True
    return
