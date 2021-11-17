import sqlite3
from textwrap import dedent
from typing import Any

from snakypy.helpers import FG, NONE

from snakypy.zshpower import HOME
from snakypy.zshpower.config.base import Base
from snakypy.zshpower.database.sql import sql


class DAO(Base):
    def __init__(self):
        try:
            Base.__init__(self, HOME)
            self.conn = sqlite3.connect(self.database_path)
            self.get_cursor = self.conn.cursor()

        except sqlite3.Error:
            message = dedent(
                f"""\n\n{FG().RED}
                An error occurred while connecting to the database. Make sure that the SQLite database is turned on.
                One way to resolve it is by running the command "zshpower init [--omz]".{NONE}
            """
            )
            self.log.record(message, colorize=True, level="critical")
            raise sqlite3.Error(message)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.commit()
        self.connection.close()

    @property
    def connection(self) -> sqlite3.Connection:
        return self.conn

    @property
    def cursor(self) -> sqlite3.Cursor:
        return self.get_cursor

    def commit(self):
        self.connection.commit()

    def execute(self, sql_, params=None):
        self.cursor.execute(sql_, params or ())

    def fetchall(self) -> list:
        return self.cursor.fetchall()

    def fetchone(self) -> Any:
        return self.cursor.fetchone()

    def query(self, sql_, params=None) -> list:
        self.cursor.execute(sql_, params or ())
        return self.fetchall()

    def query_one(self, sql_, params=None) -> Any:
        self.cursor.execute(sql_, params or ())
        return self.fetchone()

    def create_table(self, tbl_name) -> bool:
        try:
            self.execute(sql()[tbl_name])
            self.commit()
            self.connection.close()
            return True
        except (sqlite3.DatabaseError, sqlite3.DataError):
            return False

    def select_columns(self, /, columns=(), table=None) -> dict:
        sql_ = f"SELECT {','.join(columns)} FROM {table};"
        query = self.query(sql_)
        data = {key: value for (key, value) in query}
        self.connection.close()
        return data

    def select_where(self, table, value, where, select=()) -> list:
        sql_ = f"SELECT {','.join(select)} FROM {table} WHERE {where} = '{value}';"
        data = self.query(sql_)
        self.commit()
        self.connection.close()
        return data

    def insert(self, table, /, columns=(), values=()) -> bool:
        sql_ = f"INSERT INTO {table} {columns} VALUES {values};"
        try:
            self.execute(sql_)
            self.commit()
            self.connection.close()
            return True
        except Exception:
            raise Exception("Error insert database.")

    def update(self, table, set_, version, where, value) -> bool:
        sql_ = f"UPDATE {table} SET {set_} = '{version}' WHERE {where} = '{value}';"
        try:
            self.execute(sql_)
            self.commit()
            self.connection.close()
            return True
        except sqlite3.OperationalError as err:
            raise sqlite3.OperationalError(
                "Error writing to table. Table does not exist.", err
            )
