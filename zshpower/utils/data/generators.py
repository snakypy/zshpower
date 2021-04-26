from subprocess import run


def create_table(database, db_filepath):
    from os.path import exists

    if exists(db_filepath):
        database.execute("""
            CREATE TABLE IF NOT EXISTS info (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                version TEXT NOT NULL,
                date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """)
        database.commit()
        database.connection.close()
        return True
    return False


class Manager:
    def __init__(self, database):
        self.database = database

    def dart(self, /, option=None):

        if option:
            dart_version = run(
                "dart --version 2>&1", capture_output=True, shell=True, text=True
            )

            if not dart_version.returncode == 0:
                return False

            dart_version = dart_version.stdout.replace("\n", "").split(" ")[3]

            if option == "insert":
                sql = """SELECT version FROM info WHERE name = 'dart';"""
                query = self.database.query(sql)

                if not query:
                    sql = f"""INSERT INTO info (name, version)
                    VALUES ('dart', '{"{0[0]}.{0[1]}.{0[2]}".format(dart_version)}');"""
                    self.database.execute(sql)
                    self.database.commit()

            elif option == "update":
                sql = f"""UPDATE info SET version = '{dart_version}' WHERE name = 'dart';"""
                self.database.execute(sql)
                self.database.commit()

            self.database.connection.close()

    def docker(self, /, option=None):

        if option:
            docker_version = run(
                "docker version --format '{{.Server.Version}}'",
                capture_output=True,
                text=True,
                shell=True,
            ).stdout

            if not docker_version.replace("\n", ""):
                return False

            docker_version = docker_version.replace("\n", "")

            if option == "insert":
                sql = """SELECT version FROM info WHERE name = 'docker';"""
                query = self.database.query(sql)

                if not query:
                    sql = f"""INSERT INTO info (name, version)
                    VALUES ('docker', '{"{0[0]}.{0[1]}.{0[2]}".format(docker_version)}');"""
                    self.database.execute(sql)
                    self.database.commit()

            elif option == "update":
                sql = f"""UPDATE info SET version = '{docker_version}' WHERE name = 'docker';"""
                self.database.execute(sql)
                self.database.commit()

            self.database.connection.close()

    def dotnet(self, /, option=None):

        if option:
            dotnet_version = run(
                "dotnet --version 2>/dev/null", capture_output=True, shell=True, text=True
            ).stdout

            if not dotnet_version.replace("\n", ""):
                return False

            dotnet_version = dotnet_version.replace("\n", "")

            if option == "insert":
                sql = """SELECT version FROM info WHERE name = 'dotnet';"""
                query = self.database.query(sql)

                if not query:
                    sql = f"""INSERT INTO info (name, version)
                    VALUES ('dotnet', '{"{0[0]}.{0[1]}.{0[2]}".format(dotnet_version)}');"""
                    self.database.execute(sql)
                    self.database.commit()

            elif option == "update":
                sql = f"""UPDATE info SET version = '{dotnet_version}' WHERE name = 'dotnet';"""
                self.database.execute(sql)
                self.database.commit()

            self.database.connection.close()

    def elixir(self, /, option=None):

        if option:
            elixir_version = run(
                "elixir -v 2>/dev/null | grep 'Elixir' | cut -d ' ' -f2",
                capture_output=True,
                shell=True,
                text=True,
            ).stdout

            if not elixir_version.replace("\n", ""):
                return False

            elixir_version = elixir_version.replace("\n", "")

            if option == "insert":
                sql = """SELECT version FROM info WHERE name = 'elixir';"""
                query = self.database.query(sql)

                if not query:
                    sql = f"""INSERT INTO info (name, version)
                    VALUES ('elixir', '{"{0[0]}.{0[1]}.{0[2]}".format(elixir_version)}');"""
                    self.database.execute(sql)
                    self.database.commit()

            elif option == "update":
                sql = f"""UPDATE info SET version = '{elixir_version}' WHERE name = 'elixir';"""
                self.database.execute(sql)
                self.database.commit()

            self.database.connection.close()
