from subprocess import run


def create_table(database, table_name, db_filepath):
    from os.path import exists

    if exists(db_filepath):
        database.execute(f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
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

    def dart(self, table_name, /, option=None):

        if option:
            dart_version = run(
                "dart --version 2>&1", capture_output=True, shell=True, text=True
            )

            if not dart_version.returncode == 0:
                return False

            dart_version = dart_version.stdout.replace("\n", "").split(" ")[3]

            if option == "insert":
                sql = f"""SELECT version FROM {table_name} WHERE name = 'dart';"""
                query = self.database.query(sql)

                if not query:
                    sql = f"""INSERT INTO {table_name} (name, version)
                    VALUES ('dart', '{dart_version}');"""
                    self.database.execute(sql)
                    self.database.commit()

            elif option == "update":
                sql = f"""UPDATE {table_name} SET version = '{dart_version}' WHERE name = 'dart';"""
                self.database.execute(sql)
                self.database.commit()

            self.database.connection.close()

    def docker(self, table_name, /, option=None):

        if option:
            docker_version = run(
                "docker version",
                capture_output=True,
                text=True,
                shell=True,
            ).stdout

            if not docker_version.replace("\n", ""):
                return False

            docker_version = docker_version.split("Version")[1].strip().split("\n")[0].replace(":", "").strip()

            if option == "insert":
                sql = f"""SELECT version FROM {table_name} WHERE name = 'docker';"""
                query = self.database.query(sql)

                if not query:
                    sql = f"""INSERT INTO {table_name} (name, version)
                    VALUES ('docker', '{docker_version}');"""
                    self.database.execute(sql)
                    self.database.commit()

            elif option == "update":
                sql = f"""UPDATE {table_name} SET version = '{docker_version}' WHERE name = 'docker';"""
                self.database.execute(sql)
                self.database.commit()

            self.database.connection.close()

    def dotnet(self, table_name, /, option=None):

        if option:
            dotnet_version = run(
                "dotnet --version 2>/dev/null", capture_output=True, shell=True, text=True
            ).stdout

            if not dotnet_version.replace("\n", ""):
                return False

            dotnet_version = dotnet_version.replace("\n", "")

            if option == "insert":
                sql = f"""SELECT version FROM {table_name} WHERE name = 'dotnet';"""
                query = self.database.query(sql)

                if not query:
                    sql = f"""INSERT INTO {table_name} (name, version)
                    VALUES ('dotnet', '{dotnet_version}');"""
                    self.database.execute(sql)
                    self.database.commit()

            elif option == "update":
                sql = f"""UPDATE {table_name} SET version = '{dotnet_version}' WHERE name = 'dotnet';"""
                self.database.execute(sql)
                self.database.commit()

            self.database.connection.close()

    def elixir(self, table_name, /, option=None):

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
                sql = f"""SELECT version FROM {table_name} WHERE name = 'elixir';"""
                query = self.database.query(sql)

                if not query:
                    sql = f"""INSERT INTO {table_name} (name, version)
                    VALUES ('elixir', '{elixir_version}');"""
                    self.database.execute(sql)
                    self.database.commit()

            elif option == "update":
                sql = f"""UPDATE {table_name} SET version = '{elixir_version}' WHERE name = 'elixir';"""
                self.database.execute(sql)
                self.database.commit()

            self.database.connection.close()

    def golang(self, table_name, /, option=None):

        if option:
            golang_version = run(
                "go version", capture_output=True, shell=True, text=True
            ).stdout

            if not golang_version.replace("\n", ""):
                return False

            golang_version = golang_version.replace("go", "").split(" ")[2]

            if option == "insert":
                sql = f"""SELECT version FROM {table_name} WHERE name = 'golang';"""
                query = self.database.query(sql)

                if not query:
                    sql = f"""INSERT INTO {table_name} (name, version)
                    VALUES ('golang', '{golang_version}');"""
                    self.database.execute(sql)
                    self.database.commit()

            elif option == "update":
                sql = f"""UPDATE {table_name} SET version = '{golang_version}' WHERE name = 'golang';"""
                self.database.execute(sql)
                self.database.commit()

            self.database.connection.close()

    def java(self, table_name, /, option=None):

        if option:
            java_version = run(
                """java -version 2>&1 | awk -F '"' '/version/ {print $2}'""",
                capture_output=True,
                shell=True,
                text=True,
            ).stdout

            if not java_version.replace("\n", ""):
                return False

            java_version = java_version.replace("\n", "").split("_")[0]

            if option == "insert":
                sql = f"""SELECT version FROM {table_name} WHERE name = 'java';"""
                query = self.database.query(sql)

                if not query:
                    sql = f"""INSERT INTO {table_name} (name, version)
                    VALUES ('java', '{java_version}');"""
                    self.database.execute(sql)
                    self.database.commit()

            elif option == "update":
                sql = f"""UPDATE {table_name} SET version = '{java_version}' WHERE name = 'java';"""
                self.database.execute(sql)
                self.database.commit()

            self.database.connection.close()

    def julia(self, table_name, /, option=None):

        if option:
            julia_version = run(
                "julia --version", capture_output=True, shell=True, text=True
            ).stdout

            if not julia_version.replace("\n", ""):
                return False

            julia_version = julia_version.replace("\n", "").split(" ")[2]

            if option == "insert":
                sql = f"""SELECT version FROM {table_name} WHERE name = 'julia';"""
                query = self.database.query(sql)

                if not query:
                    sql = f"""INSERT INTO {table_name} (name, version)
                    VALUES ('julia', '{julia_version}');"""
                    self.database.execute(sql)
                    self.database.commit()

            elif option == "update":
                sql = f"""UPDATE {table_name} SET version = '{julia_version}' WHERE name = 'julia';"""
                self.database.execute(sql)
                self.database.commit()

            self.database.connection.close()

    def nodejs(self, table_name, /, option=None):

        if option:
            nodejs_version = run(
                "node -v 2>/dev/null", capture_output=True, shell=True, text=True
            ).stdout

            if not nodejs_version.replace("\n", ""):
                return False

            nodejs_version = nodejs_version[1:].replace("\n", "")

            if option == "insert":
                sql = f"""SELECT version FROM {table_name} WHERE name = 'nodejs';"""
                query = self.database.query(sql)

                if not query:
                    sql = f"""INSERT INTO {table_name} (name, version)
                    VALUES ('nodejs', '{nodejs_version}');"""
                    self.database.execute(sql)
                    self.database.commit()

            elif option == "update":
                sql = f"""UPDATE {table_name} SET version = '{nodejs_version}' WHERE name = 'nodejs';"""
                self.database.execute(sql)
                self.database.commit()

            self.database.connection.close()

    def php(self, table_name, /, option=None):

        if option:
            php_version = run(
                """php -v 2>&1 | grep "^PHP\\s*[0-9.]\\+" | awk '{print $2}'""",
                capture_output=True,
                shell=True,
                text=True,
            ).stdout

            php_version = php_version.replace("\n", "")

            if not php_version:
                return False

            if option == "insert":
                sql = f"""SELECT version FROM {table_name} WHERE name = 'php';"""
                query = self.database.query(sql)

                if not query:
                    sql = f"""INSERT INTO {table_name} (name, version)
                    VALUES ('php', '{php_version}');"""
                    self.database.execute(sql)
                    self.database.commit()

            elif option == "update":
                sql = f"""UPDATE {table_name} SET version = '{php_version}' WHERE name = 'php';"""
                self.database.execute(sql)
                self.database.commit()

            self.database.connection.close()

    def ruby(self, table_name, /, option=None):

        if option:
            ruby_version = run(
                "ruby --version 2>/dev/null", capture_output=True, shell=True, text=True
            ).stdout

            if not ruby_version.replace("\n", ""):
                return False

            ruby_version = ruby_version.replace("\n", " ").split(" ")[1].split("p")[0]

            if option == "insert":
                sql = f"""SELECT version FROM {table_name} WHERE name = 'ruby';"""
                query = self.database.query(sql)

                if not query:
                    sql = f"""INSERT INTO {table_name} (name, version)
                    VALUES ('ruby', '{ruby_version}');"""
                    self.database.execute(sql)
                    self.database.commit()

            elif option == "update":
                sql = f"""UPDATE {table_name} SET version = '{ruby_version}' WHERE name = 'ruby';"""
                self.database.execute(sql)
                self.database.commit()

            self.database.connection.close()

    def rust(self, table_name, /, option=None):

        if option:
            rust_version = run(
                "rustc --version", capture_output=True, shell=True, text=True
            ).stdout

            if not rust_version.replace("\n", ""):
                return False

            rust_version = rust_version.split(" ")[1].replace("\n", "")

            if option == "insert":
                sql = f"""SELECT version FROM {table_name} WHERE name = 'rust';"""
                query = self.database.query(sql)

                if not query:
                    sql = f"""INSERT INTO {table_name} (name, version)
                    VALUES ('rust', '{rust_version}');"""
                    self.database.execute(sql)
                    self.database.commit()

            elif option == "update":
                sql = f"""UPDATE {table_name} SET version = '{rust_version}' WHERE name = 'rust';"""
                self.database.execute(sql)
                self.database.commit()

            self.database.connection.close()
