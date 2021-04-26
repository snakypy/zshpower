def select_database_all(database, table_name):
    sql = f"""SELECT name, version FROM {table_name};"""
    query = database.query(sql)
    data = {key: value for (key, value) in query}
    database.connection.close()
    return data
