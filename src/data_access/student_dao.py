from src.data_access.db import get_connection


# =======================
# STUDENT – FULL DATA
# =======================

def fetch_all_students():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            s.id,
            s.student_code,
            s.full_name,
            s.birth_year,
            c.class_name
        FROM students s
        LEFT JOIN classes c ON s.class_id = c.id
        ORDER BY s.full_name
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows


def fetch_students(keyword="", class_id="", order="ASC"):
    conn = get_connection()
    cursor = conn.cursor()

    sql = f"""
        SELECT
            s.id,
            s.student_code,
            s.full_name,
            s.birth_year,
            c.class_name
        FROM students s
        LEFT JOIN classes c ON s.class_id = c.id
        WHERE s.full_name LIKE %s
    """

    params = [f"%{keyword}%"]

    if class_id:
        sql += " AND s.class_id = %s"
        params.append(class_id)

    sql += f" ORDER BY s.full_name {order}"

    cursor.execute(sql, tuple(params))
    rows = cursor.fetchall()
    conn.close()
    return rows


# =======================
# STUDENT – COMBOBOX
# =======================

def fetch_all_students_simple():
    """Dùng cho combobox"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, full_name
        FROM students
        ORDER BY full_name
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows


# =======================
# CRUD
# =======================

def insert_student(student_code, full_name, birth_year, class_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO students (student_code, full_name, birth_year, class_id)
        VALUES (%s, %s, %s, %s)
    """, (student_code, full_name, birth_year, class_id))

    conn.commit()
    conn.close()


def update_student(student_id, student_code, full_name, birth_year, class_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE students
        SET student_code=%s,
            full_name=%s,
            birth_year=%s,
            class_id=%s
        WHERE id=%s
    """, (student_code, full_name, birth_year, class_id, student_id))

    conn.commit()
    conn.close()


def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE id=%s", (student_id,))
    conn.commit()
    conn.close()


# =======================
# ENROLLMENT (ĐĂNG KÝ HP)
# =======================

def fetch_student_enrollments(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            cc.id,
            c.course_name,
            cc.semester,
            cc.school_year
        FROM enrollments e
        JOIN course_classes cc ON e.course_class_id = cc.id
        JOIN courses c ON cc.course_id = c.id
        WHERE e.student_id = %s
    """, (student_id,))

    rows = cursor.fetchall()
    conn.close()
    return rows


def insert_enrollment(student_id, course_class_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO enrollments (student_id, course_class_id)
        VALUES (%s, %s)
    """, (student_id, course_class_id))

    conn.commit()
    conn.close()


def delete_enrollment(student_id, course_class_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM enrollments
        WHERE student_id=%s AND course_class_id=%s
    """, (student_id, course_class_id))

    conn.commit()
    conn.close()
