from src.data_access.db import get_connection

def fetch_classes_for_student():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, class_name FROM classes ORDER BY class_name")
    rows = cursor.fetchall()

    conn.close()
    return rows

def fetch_classes(keyword="", order="ASC"):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    SELECT id, class_name, major
    FROM classes
    WHERE class_name LIKE %s OR major LIKE %s
    ORDER BY id {}
    """.format(order)

    like = f"%{keyword}%"
    cursor.execute(sql, (like, like))

    rows = cursor.fetchall()
    conn.close()
    return rows


def insert_class(name, major):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO classes(class_name, major) VALUES (%s, %s)",
        (name, major)
    )
    conn.commit()
    conn.close()


def update_class(id, name, major):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE classes SET class_name=%s, major=%s WHERE id=%s",
        (name, major, id)
    )
    conn.commit()
    conn.close()