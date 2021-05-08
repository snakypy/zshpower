def sql() -> dict:
    data: dict = {
        "tbl_main": (
            "CREATE TABLE IF NOT EXISTS `tbl_main` ("
            "  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"
            "  name TEXT(20) NOT NULL,"
            "  version TEXT(20) NOT NULL,"
            "  date TIMESTAMP DEFAULT CURRENT_TIMESTAMP"
            ")"
        )
    }
    return data
