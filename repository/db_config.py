import sqlite3
from typing import Tuple

def connect_to_db(db_path: str = "../db/stress_db") -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def get_cursor(conn: sqlite3.Connection) -> sqlite3.Cursor:
    return conn.cursor()

def execute_dml(conn: sqlite3.Connection, query: str, params: Tuple = ()):
    cursor = get_cursor(conn)
    cursor.execute(query, params)
    conn.commit()
    rows = cursor.fetchall()
    cursor.close()
    close_connection(conn)
    return rows

def execute_ddl(conn: sqlite3.Connection, query: str, params: Tuple = ()):
    cursor = get_cursor(conn)
    cursor.execute(query, params)
    conn.commit()
    cursor.close()
    close_connection(conn)

def close_connection(conn: sqlite3.Connection) -> None:
    conn.close()


for row in execute_dml(connect_to_db('./db/stress_db'), "SELECT * FROM auth_credentials"):
    print(row.keys())