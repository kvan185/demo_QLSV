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

def insert_course_class(course_id, teacher_id, semester, school_year):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO course_classes (course_id, teacher_id, semester, school_year)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(sql, (course_id, teacher_id, semester, school_year))
    conn.commit()
    conn.close()


def update_course_class(id, course_id, teacher_id, semester, school_year):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    UPDATE course_classes
    SET course_id=%s, teacher_id=%s, semester=%s, school_year=%s
    WHERE id=%s
    """
    cursor.execute(sql, (course_id, teacher_id, semester, school_year, id))
    conn.commit()
    conn.close()


def fetch_course_classes(keyword="", order="ASC"):
    if order not in ("ASC", "DESC"):
        order = "ASC"

    conn = get_connection()
    cursor = conn.cursor()

    sql = f"""
    SELECT
        cc.id,
        c.course_name,
        t.full_name,
        cc.semester,
        cc.school_year
    FROM course_classes cc
    JOIN courses c ON cc.course_id = c.id
    JOIN teachers t ON cc.teacher_id = t.id
    WHERE c.course_name LIKE %s
       OR t.full_name LIKE %s
    ORDER BY cc.id {order}
    LIMIT 25
    """

    like = f"%{keyword}%"
    cursor.execute(sql, (like, like))
    rows = cursor.fetchall()
    conn.close()
    return rows


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
