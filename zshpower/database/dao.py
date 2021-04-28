from sqlite3 import connect as connect_sqlite, Error
import sys
from os.path import join

from snakypy import printer, FG

from zshpower.config.base import Base
from zshpower import HOME


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
            sys.exit(1)

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

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()

    def query_one(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchone()
