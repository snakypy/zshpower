from sqlite3 import connect as connect_sqlite
import sys
from os.path import join
from zshpower.config.base import Base


class Database(Base):

    def __init__(self, home):
        try:
            Base.__init__(self, home)
            connection_data = join(home, self.data_root, self.database_name)
            self.conn = connect_sqlite(connection_data)
            self.get_cursor = self.conn.cursor()

        except Exception:
            msg = 'A connection error has occurred.' \
                  f' Check connectivity data ({join(self.data_root, "database.sqlite3")})' \
                  ' make sure database is powered on, or if there is a database.'
            print(msg)
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
