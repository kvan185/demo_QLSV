from src.data_access.db import get_connection


def find_user(username):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, username, password, role, ref_id FROM users WHERE username=%s",
        (username,)
    )
    user = cursor.fetchone()
    conn.close()
    return user


def insert_user(username, password, role, ref_id=None):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO users(username, password, role, ref_id)
        VALUES (%s, %s, %s, %s)
    """, (username, password, role, ref_id))

    conn.commit()
    conn.close()
