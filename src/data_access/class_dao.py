from src.data_access.db import get_connection


# =========================
# DÙNG CHO STUDENT FORM
# =========================
def fetch_classes_for_student():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, class_name FROM classes ORDER BY class_name"
    )
    rows = cursor.fetchall()
    conn.close()
    return rows


# =========================
# DÙNG CHO CLASS FORM (SEARCH + SORT)
# =========================
def fetch_classes(keyword="", order="ASC"):
    if order not in ("ASC", "DESC"):
        order = "ASC"

    conn = get_connection()
    cursor = conn.cursor()

    sql = f"""
    SELECT id, class_name, major
    FROM classes
    WHERE class_name LIKE %s OR major LIKE %s
    ORDER BY id {order}
    LIMIT 25
    """

    like = f"%{keyword}%"
    cursor.execute(sql, (like, like))
    rows = cursor.fetchall()
    conn.close()
    return rows


# =========================
# THÊM LỚP
# =========================
def insert_class(class_name, major):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO classes (class_name, major) VALUES (%s, %s)",
        (class_name, major)
    )
    conn.commit()
    conn.close()


# =========================
# CẬP NHẬT LỚP
# =========================
def update_class(id, class_name, major):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE classes SET class_name=%s, major=%s WHERE id=%s",
        (class_name, major, id)
    )
    conn.commit()
    conn.close()


# =========================
# DÙNG CHO ENROLLMENT
# =========================
def fetch_all_course_classes():
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    SELECT
        cc.id,
        c.course_name,
        cc.semester,
        cc.school_year
    FROM course_classes cc
    JOIN courses c ON cc.course_id = c.id
    ORDER BY c.course_name
    """

    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.close()
    return rows
