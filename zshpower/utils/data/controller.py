def select_database_all(database):
    sql = """SELECT name, version FROM info;"""
    query = database.query(sql)
    data = {key: value for (key, value) in query}
    database.connection.close()
    return data
