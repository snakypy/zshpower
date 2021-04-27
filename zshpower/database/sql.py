def select_all(database, columns=(), table=None):
    if table is not None and columns:
        sql = f"""SELECT {columns} FROM {table};"""
        sql = sql.replace("(", "").replace(")", "").replace("'", "")
        query = database.query(sql)
        data = {key: value for (key, value) in query}
        database.connection.close()
        return data
    return


# class SQLBase:
#     def __int__(self):
#         self.tbl_name = "zshpower"


class SQLTables:
    def __init__(self):
        self.tables = {f'main': (
            f"CREATE TABLE IF NOT EXISTS `main` ("
            "  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"
            "  name TEXT(100) NOT NULL,"
            "  version TEXT(50) NOT NULL,"
            "  date TIMESTAMP DEFAULT CURRENT_TIMESTAMP"
            ")")}

    def __getitem__(self, key):
        return self.tables[key]


class SQLSelectVersionByName:
    def __init__(self, table, name):
        self.sql = f"""SELECT version FROM {table} WHERE name = '{name}';"""

    def __str__(self):
        return self.sql


class SQLInsert:
    def __init__(self, table, /, columns=(), values=()):
        self.sql = f"""INSERT INTO {table} {columns} VALUES {values};"""

    def __str__(self):
        return self.sql


class SQLUpdateVersionByName:
    def __init__(self, table, version, name):
        self.sql = f"""UPDATE {table} SET version = '{version}' WHERE name = '{name}';"""

    def __str__(self):
        return self.sql


