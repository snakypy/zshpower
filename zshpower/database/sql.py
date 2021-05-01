def sql() -> dict:
    data = {
        "tbl_main": (
            "CREATE TABLE IF NOT EXISTS `main` ("
            "  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"
            "  name TEXT(100) NOT NULL,"
            "  version TEXT(50) NOT NULL,"
            "  date TIMESTAMP DEFAULT CURRENT_TIMESTAMP"
            ")"
        )
    }
    return data
