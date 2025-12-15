from src.data_access.db import get_connection

def insert_student(code, name, year, class_id):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO students (student_code, full_name, birth_year, class_id)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(sql, (code, name, year, class_id))

    conn.commit()
    conn.close()


def fetch_all_students():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()

    conn.close()
    return result

def fetch_students(keyword="", class_id=None, order="ASC"):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    SELECT id, student_code, full_name, birth_year, class_id
    FROM students
    WHERE (full_name LIKE %s OR student_code LIKE %s)
    """
    params = [f"%{keyword}%", f"%{keyword}%"]

    if class_id:
        sql += " AND class_id = %s"
        params.append(class_id)

    sql += f" ORDER BY id {order}"

    cursor.execute(sql, tuple(params))
    rows = cursor.fetchall()

    conn.close()
    return rows


def fetch_all_students():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()

    conn.close()
    return result

def update_student(id, code, name, year, class_id):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    UPDATE students
    SET student_code=%s, full_name=%s, birth_year=%s, class_id=%s
    WHERE id=%s
    """
    cursor.execute(sql, (code, name, year, class_id, id))
    conn.commit()
    conn.close()
