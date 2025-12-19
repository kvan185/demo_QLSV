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

#=========================
# DÙNG CHO ASSIGN ADVISOR
#=========================
def fetch_all_teachers():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, full_name
        FROM teachers
        ORDER BY full_name
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows

def fetch_classes_without_advisor():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, class_name
        FROM classes
        WHERE advisor_id IS NULL
        ORDER BY class_name
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows

def fetch_all_classes_with_advisor():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            c.id,
            c.class_name,
            c.major,
            t.full_name AS advisor_name
        FROM classes c
        LEFT JOIN teachers t ON c.advisor_id = t.id
        ORDER BY c.class_name
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows

def fetch_teachers_without_class():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, full_name
        FROM teachers
        WHERE id NOT IN (
            SELECT advisor_id FROM classes WHERE advisor_id IS NOT NULL
        )
        ORDER BY full_name
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows


def assign_advisor(class_id, teacher_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE classes
        SET advisor_id=%s
        WHERE id=%s
    """, (teacher_id, class_id))

    conn.commit()
    conn.close()

def fetch_advisor_class(teacher_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, class_name, major
        FROM classes
        WHERE advisor_id=%s
        ORDER BY class_name
    """, (teacher_id,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def fetch_teachers_full():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, teacher_code, full_name
        FROM teachers
        ORDER BY full_name
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows

def fetch_teachers_simple():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, full_name
        FROM teachers
        ORDER BY full_name
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows