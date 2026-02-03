import sqlite3
from pathlib import Path
from werkzeug.security import generate_password_hash, check_password_hash

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "taskscore.db"

WEEKDAYS = [
    "Montag 💼",
    "Dienstag 📊",
    "Mittwoch ⏳",
    "Donnerstag 🎯",
    "Freitag 🏁",
    "Samstag 🕺",
    "Sonntag 🌿",
]

def get_connection():
    return sqlite3.connect(DB_PATH)

def _column_exists(conn, table, column):
    cols = conn.execute(f"PRAGMA table_info({table})").fetchall()
    return any(c[1] == column for c in cols)

def _ensure_column(conn, table, column_sql):
   
    col_name = column_sql.split()[0]
    if not _column_exists(conn, table, col_name):
        conn.execute(f"ALTER TABLE {table} ADD COLUMN {column_sql}")


def init_db():
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password_hash TEXT NOT NULL
            )
            """
        )

        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS user_stats (
                user_id INTEGER PRIMARY KEY,
                done_score INTEGER NOT NULL DEFAULT 0
            )
            """
        )

        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                weekday TEXT NOT NULL,
                points_total INTEGER NOT NULL DEFAULT 0,
                status TEXT NOT NULL DEFAULT 'OPEN',
                user_id INTEGER
            )
            """
        )

        _ensure_column(conn, "tasks", "rewarded INTEGER NOT NULL DEFAULT 0")
        _ensure_column(conn, "tasks", "user_id INTEGER")

        conn.execute("UPDATE tasks SET rewarded = 0 WHERE rewarded IS NULL")

       
        conn.execute(
            """
            INSERT OR IGNORE INTO user_stats (user_id, done_score)
            SELECT id, 0 FROM users
            """
        )

def create_user(username, password):
    username = (username or "").strip()

    if len(username) < 3:
        return False, "Benutzername muss mindestens 3 Zeichen haben."
    if len(password) < 4:
        return False, "Passwort muss mindestens 4 Zeichen haben."

    pw_hash = generate_password_hash(password)

    try:
        with get_connection() as conn:
            cur = conn.execute(
                "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                (username, pw_hash),
            )
            user_id = cur.lastrowid
            conn.execute(
                "INSERT OR IGNORE INTO user_stats (user_id, done_score) VALUES (?, 0)",
                (user_id,),
            )
        return True, "OK"
    except sqlite3.IntegrityError:
        return False, "Benutzername ist bereits vergeben."

def verify_user(username, password):
    username = (username or "").strip()

    with get_connection() as conn:
        row = conn.execute(
            "SELECT id, password_hash FROM users WHERE username = ?",
            (username,),
        ).fetchone()

    if not row:
        return None

    user_id, pw_hash = row
    return user_id if check_password_hash(pw_hash, password) else None

def get_user_done_score(user_id):
    with get_connection() as conn:
        row = conn.execute(
            "SELECT done_score FROM user_stats WHERE user_id = ?",
            (user_id,),
        ).fetchone()
    return row[0] if row else 0

def get_all_tasks(user_id):
    with get_connection() as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            """
            SELECT id, title, description, weekday, points_total, status
            FROM tasks
            WHERE user_id = ?
            ORDER BY
              CASE weekday
                WHEN 'Montag 💼' THEN 1
                WHEN 'Dienstag 📊' THEN 2
                WHEN 'Mittwoch ⏳' THEN 3
                WHEN 'Donnerstag 🎯' THEN 4
                WHEN 'Freitag 🏁' THEN 5
                WHEN 'Samstag 🕺' THEN 6
                WHEN 'Sonntag 🌿' THEN 7
              END,
              id ASC
            """,
            (user_id,),
        ).fetchall()

    return [dict(r) for r in rows]

def insert_task(title, description, weekday, points_total, user_id):
    with get_connection() as conn:
        conn.execute(
            """
            INSERT INTO tasks (title, description, weekday, points_total, user_id, rewarded)
            VALUES (?, ?, ?, ?, ?, 0)
            """,
            (title, description, weekday, points_total, user_id),
        )

def get_total_points(user_id):
    with get_connection() as conn:
        value = conn.execute(
            "SELECT SUM(points_total) FROM tasks WHERE user_id = ?",
            (user_id,),
        ).fetchone()[0]
    return value or 0

def get_done_points(user_id):
    with get_connection() as conn:
        value = conn.execute(
            "SELECT SUM(points_total) FROM tasks WHERE status = 'DONE' AND user_id = ?",
            (user_id,),
        ).fetchone()[0]
    return value or 0

def get_weekly_points(user_id):
    weekly = {day: 0 for day in WEEKDAYS}

    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT weekday, SUM(points_total)
            FROM tasks
            WHERE user_id = ?
            GROUP BY weekday
            """,
            (user_id,),
        ).fetchall()

    for weekday, total in rows:
        if weekday in weekly:
            weekly[weekday] = total or 0

    return weekly

def toggle_task_status(task_id, user_id):
    with get_connection() as conn:
        row = conn.execute(
            "SELECT status, rewarded FROM tasks WHERE id = ? AND user_id = ?",
            (task_id, user_id),
        ).fetchone()

        if not row:
            return

        status, rewarded = row
        new_status = "DONE" if status != "DONE" else "OPEN"

        conn.execute(
            "UPDATE tasks SET status = ? WHERE id = ? AND user_id = ?",
            (new_status, task_id, user_id),
        )

        if new_status == "DONE" and (rewarded is None or rewarded == 0):
            conn.execute(
                "UPDATE tasks SET rewarded = 1 WHERE id = ? AND user_id = ?",
                (task_id, user_id),
            )
            conn.execute(
                "UPDATE user_stats SET done_score = done_score + 1 WHERE user_id = ?",
                (user_id,),
            )

def delete_task(task_id, user_id):
    with get_connection() as conn:
        conn.execute(
            "DELETE FROM tasks WHERE id = ? AND user_id = ?",
            (task_id, user_id),
        )