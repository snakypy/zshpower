from sys import exit
from sqlite3 import connect as connect_sqlite, Error
from os.path import join
from snakypy import printer, FG
from zshpower.config.base import Base
from zshpower import HOME
from zshpower.database.sql import sql


class DAO(Base):
    def __init__(self):
        try:
            Base.__init__(self, HOME)
            connection_data = join(HOME, self.data_root, self.database_name)
            self.conn = connect_sqlite(connection_data)
            self.get_cursor = self.conn.cursor()

        except Error:
            printer(
                "An error occurred while connecting to the database. Make sure that the SQLite database is turned on."
                "One way to resolve it is by running the command 'zshpower init [--omz]'",
                foreground=FG.ERROR,
            )
            exit(1)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self.connection.close()

    @property
    def connection(self):
        return self.conn

    @property
    def cursor(self):
        return self.get_cursor

    def commit(self):
        self.connection.commit()

    def execute(self, sql_, params=None):
        self.cursor.execute(sql_, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql_, params=None):
        self.cursor.execute(sql_, params or ())
        return self.fetchall()

    def query_one(self, sql_, params=None):
        self.cursor.execute(sql_, params or ())
        return self.fetchone()

    def create_table(self, tbl_name):
        try:
            self.execute(sql()[tbl_name])
            self.commit()
            self.connection.close()
            return True
        except FileNotFoundError:
            return False

    def select_columns(self, /, columns=(), table=None) -> dict:
        sql_ = f"SELECT {','.join(columns)} FROM {table};"
        # sql = sql.replace("(", "").replace(")", "").replace("'", "")
        try:
            query = self.query(sql_)
            data = {key: value for (key, value) in query}
            self.connection.close()
            return data
        except Exception:
            raise Exception("Error select in database.")

    def select_where(self, table, value, where, select=()):
        sql_ = f"SELECT {','.join(select)} FROM {table} WHERE {where} = '{value}';"
        try:
            data = self.query(sql_)
            self.commit()
            self.connection.close()
            return data
        except Exception:
            raise Exception("Error select data.")

    def insert(self, table, /, columns=(), values=()):
        sql_ = f"INSERT INTO {table} {columns} VALUES {values};"
        try:
            self.execute(sql_)
            self.commit()
            self.connection.close()
        except Exception:
            raise Exception("Error insert database.")

    def update(self, table, set_, version, where, value):
        sql_ = f"UPDATE {table} SET {set_} = '{version}' WHERE {where} = '{value}';"
        try:
            self.execute(sql_)
            self.commit()
            self.connection.close()
        except Exception:
            raise Exception("Error update database.")
