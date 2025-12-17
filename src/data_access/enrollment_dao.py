from src.data_access.db import get_connection

def enroll_student(student_id, course_class_id):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO enrollments (student_id, course_class_id)
    VALUES (%s, %s)
    """
    cursor.execute(sql, (student_id, course_class_id))
    conn.commit()
    conn.close()


def fetch_enrollments():
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    SELECT s.student_code, s.full_name,
           c.course_name, cc.semester, cc.school_year
    FROM enrollments e
    JOIN students s ON e.student_id = s.id
    JOIN course_classes cc ON e.course_class_id = cc.id
    JOIN courses c ON cc.course_id = c.id
    """
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.close()
    return rows


def delete_enrollment(student_id, course_class_id):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    DELETE FROM enrollments
    WHERE student_id=%s AND course_class_id=%s
    """
    cursor.execute(sql, (student_id, course_class_id))
    conn.commit()
    conn.close()
