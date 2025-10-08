import sqlite3

def save_telemetry(operation: str, placa: str, run_identifier: str, duration: int):
    conn = sqlite3.connect('./db/stress_db')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO telemetry (operation, duration, placa, run_identifier) VALUES (?, ?, ?, ?)",
        (operation, duration, placa, run_identifier)
    )
    conn.commit()
    conn.close()