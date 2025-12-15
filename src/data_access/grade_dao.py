from src.data_access.db import get_connection


def fetch_grades(keyword="", order="ASC"):
    conn = get_connection()
    cursor = conn.cursor()

    sql = f"""
    SELECT g.student_id, s.full_name, c.course_name, g.score
    FROM grades g
    JOIN students s ON g.student_id = s.id
    JOIN courses c ON g.course_id = c.id
    WHERE s.full_name LIKE %s OR c.course_name LIKE %s
    ORDER BY g.student_id {order}
    """

    like = f"%{keyword}%"
    cursor.execute(sql, (like, like))
    rows = cursor.fetchall()
    conn.close()
    return rows


def insert_grade(student_id, course_id, score):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO grades(student_id, course_id, score) VALUES (%s, %s, %s)",
        (student_id, course_id, score)
    )
    conn.commit()
    conn.close()


def update_grade(student_id, course_id, score):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE grades SET score=%s WHERE student_id=%s AND course_id=%s",
        (score, student_id, course_id)
    )
    conn.commit()
    conn.close()
