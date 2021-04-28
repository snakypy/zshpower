def create_table(database, db_filepath):
    from os.path import exists

    if exists(db_filepath):
        database.execute(SQLTables()["main"])
        database.commit()
        database.connection.close()
        return True
    return False


class SQLTables:
    def __init__(self):
        self.tables = {
            f"main": (
                f"CREATE TABLE IF NOT EXISTS `main` ("
                "  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"
                "  name TEXT(100) NOT NULL,"
                "  version TEXT(50) NOT NULL,"
                "  date TIMESTAMP DEFAULT CURRENT_TIMESTAMP"
                ")"
            )
        }

    def __getitem__(self, item):
        return self.tables[item]


class SQLSelectVersionByName:
    def __init__(self, table, name):
        self.sql = f"""SELECT version FROM {table} WHERE name = '{name}';"""

    def __str__(self):
        return self.sql


class SQLInsert:
    def __init__(self, table, /, columns=(), values=()):
        self.sql = f"INSERT INTO {table} {columns} VALUES {values};"

    def __str__(self):
        return self.sql


class SQLUpdateVersionByName:
    def __init__(self, table, version, name):
        self.sql = f"UPDATE {table} SET version = '{version}' WHERE name = '{name}';"

    def __str__(self):
        return self.sql


class RetAllNameVersion:
    """
    Returns all records by name and version.
    """

    def __init__(self, database, /, columns=(), table=None):
        self.data = dict()
        if len(columns) == 2:
            sql = f"""SELECT {columns} FROM {table};"""
            sql = sql.replace("(", "").replace(")", "").replace("'", "")
            query = database.query(sql)
            self.data = {key: value for (key, value) in query}
            database.connection.close()

    def __getitem__(self, item):
        return self.data[item]

    def __repr__(self):
        return repr(self.data)
