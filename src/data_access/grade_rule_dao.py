from src.data_access.db import get_connection


def insert_grade_rule(course_id, min_score, pass_score):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO grade_rules (course_id, min_score, pass_score)
    VALUES (%s, %s, %s)
    """
    cursor.execute(sql, (course_id, min_score, pass_score))
    conn.commit()
    conn.close()


def update_grade_rule(course_id, min_score, pass_score):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    UPDATE grade_rules
    SET min_score=%s, pass_score=%s
    WHERE course_id=%s
    """
    cursor.execute(sql, (min_score, pass_score, course_id))
    conn.commit()
    conn.close()


def fetch_grade_rules(keyword=""):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    SELECT
        c.course_name,
        gr.min_score,
        gr.pass_score,
        gr.course_id
    FROM grade_rules gr
    JOIN courses c ON gr.course_id = c.id
    WHERE c.course_name LIKE %s
    ORDER BY c.course_name
    """

    like = f"%{keyword}%"
    cursor.execute(sql, (like,))
    rows = cursor.fetchall()
    conn.close()
    return rows


def check_rule_exists(course_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT 1 FROM grade_rules WHERE course_id=%s",
        (course_id,)
    )
    exists = cursor.fetchone() is not None
    conn.close()
    return exists
