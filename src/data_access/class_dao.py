from src.data_access.db import get_connection


# =======================
# CLASS – FULL DATA
# =======================

def fetch_classes(keyword="", order="ASC"):
    conn = get_connection()
    cursor = conn.cursor()

    sql = f"""
        SELECT
            c.id,
            c.class_name,
            c.major,
            t.full_name AS advisor_name
        FROM classes c
        LEFT JOIN teachers t ON c.advisor_id = t.id
        WHERE c.class_name LIKE %s
        ORDER BY c.class_name {order}
    """

    cursor.execute(sql, (f"%{keyword}%",))
    rows = cursor.fetchall()
    conn.close()
    return rows


# =======================
# CLASS – COMBOBOX
# =======================

def fetch_classes_simple():
    """Dùng cho combobox"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, class_name
        FROM classes
        ORDER BY class_name
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows


# =======================
# CRUD
# =======================

def insert_class(class_name, major):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO classes (class_name, major)
        VALUES (%s, %s)
    """, (class_name, major))

    conn.commit()
    conn.close()


def update_class(class_id, class_name, major):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE classes
        SET class_name=%s,
            major=%s
        WHERE id=%s
    """, (class_name, major, class_id))

    conn.commit()
    conn.close()


def delete_class(class_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM classes WHERE id=%s", (class_id,))
    conn.commit()
    conn.close()


# =======================
# ADVISOR (CỐ VẤN)
# =======================

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


def remove_advisor(class_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE classes
        SET advisor_id=NULL
        WHERE id=%s
    """, (class_id,))

    conn.commit()
    conn.close()


def fetch_advisor_class(teacher_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, class_name
        FROM classes
        WHERE advisor_id=%s
    """, (teacher_id,))

    rows = cursor.fetchall()
    conn.close()
    return rows
