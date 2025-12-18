from src.data_access.db import get_connection


def insert_semester(name, start_date, end_date):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO semesters (name, start_date, end_date)
    VALUES (%s, %s, %s)
    """
    cursor.execute(sql, (name, start_date, end_date))
    conn.commit()
    conn.close()


def update_semester(id, name, start_date, end_date):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    UPDATE semesters
    SET name=%s, start_date=%s, end_date=%s
    WHERE id=%s
    """
    cursor.execute(sql, (name, start_date, end_date, id))
    conn.commit()
    conn.close()


def fetch_semesters(keyword="", order="ASC"):
    if order not in ("ASC", "DESC"):
        order = "ASC"

    conn = get_connection()
    cursor = conn.cursor()

    sql = f"""
    SELECT id, name, start_date, end_date
    FROM semesters
    WHERE name LIKE %s
    ORDER BY id {order}
    LIMIT 25
    """

    like = f"%{keyword}%"
    cursor.execute(sql, (like,))
    rows = cursor.fetchall()
    conn.close()
    return rows


def fetch_all_semesters():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, name FROM semesters ORDER BY start_date"
    )
    rows = cursor.fetchall()
    conn.close()
    return rows
