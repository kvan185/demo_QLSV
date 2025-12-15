from src.data_access.db import get_connection

def fetch_courses(keyword="", order="ASC"):
    conn = get_connection()
    cursor = conn.cursor()

    sql = f"""
    SELECT id, course_code, course_name, credit
    FROM courses
    WHERE course_code LIKE %s OR course_name LIKE %s
    ORDER BY id {order}
    """

    like = f"%{keyword}%"
    cursor.execute(sql, (like, like))

    rows = cursor.fetchall()
    conn.close()
    return rows


def insert_course(code, name, credit):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO courses(course_code, course_name, credit) VALUES (%s, %s, %s)",
        (code, name, credit)
    )
    conn.commit()
    conn.close()


def update_course(id, code, name, credit):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE courses
        SET course_code=%s, course_name=%s, credit=%s
        WHERE id=%s
        """,
        (code, name, credit, id)
    )
    conn.commit()
    conn.close()
