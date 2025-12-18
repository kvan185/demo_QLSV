from src.data_access.db import get_connection


def fetch_tuition_settings():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, system_name, price_per_credit, coefficient
        FROM tuition_settings
        ORDER BY system_name
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows


def calculate_course_fee(course_id, system_id):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    SELECT
        c.credit,
        t.price_per_credit,
        t.coefficient
    FROM courses c, tuition_settings t
    WHERE c.id = %s AND t.id = %s
    """
    cursor.execute(sql, (course_id, system_id))
    credit, price, coef = cursor.fetchone()
    conn.close()

    return credit * price * coef
