import sqlite3

def save_telemetry(db_path: str, operation: str, duration: float):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO telemetry (operation, duration) VALUES (?, ?)",
        (operation, duration)
    )
    conn.commit()
    conn.close()
