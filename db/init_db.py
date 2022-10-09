import sqlite3

def init_db_exec():
    connection = sqlite3.connect("./db/database.db")

    with open("./migrations/create.sql") as f:
        connection.executescript(f.read())

    connection.close()