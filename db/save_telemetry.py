import sqlite3

def save_telemetry(operation: str, placa: str, run_identifier: str, duration: int):
    try:
        conn = sqlite3.connect('./db/stress_db')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO telemetry (operation, duration, placa, run_identifier) VALUES (?, ?, ?, ?)",
            (operation, duration, placa, run_identifier)
        )
        conn.commit()
    except Exception as e:
        # Log the error, print, or just silently pass to not affect other executions
        print(f"Warning: Failed to save telemetry: {e}")
    finally:
        try:
            conn.close()
        except Exception:
            pass