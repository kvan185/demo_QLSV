from src.data_access.db import get_connection


def insert_teacher(code, name, degree):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO teachers (teacher_code, full_name, degree)
    VALUES (%s, %s, %s)
    """
    cursor.execute(sql, (code, name, degree))
    conn.commit()
    conn.close()


def update_teacher(id, code, name, degree):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    UPDATE teachers
    SET teacher_code=%s, full_name=%s, degree=%s
    WHERE id=%s
    """
    cursor.execute(sql, (code, name, degree, id))
    conn.commit()
    conn.close()


def fetch_teachers(keyword="", order="ASC"):
    if order not in ("ASC", "DESC"):
        order = "ASC"

    conn = get_connection()
    cursor = conn.cursor()

    sql = f"""
    SELECT id, teacher_code, full_name, degree
    FROM teachers
    WHERE teacher_code LIKE %s OR full_name LIKE %s
    ORDER BY id {order}
    LIMIT 25
    """

    like = f"%{keyword}%"
    cursor.execute(sql, (like, like))
    rows = cursor.fetchall()
    conn.close()
    return rows


def fetch_all_teachers():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, teacher_code, full_name FROM teachers ORDER BY full_name"
    )
    rows = cursor.fetchall()
    conn.close()
    return rows
