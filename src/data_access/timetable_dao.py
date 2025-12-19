from src.data_access.db import get_connection


def fetch_week_timetable(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    SELECT
        cs.day_of_week,
        cs.start_period,
        cs.periods,
        c.course_name,
        cs.room
    FROM enrollments e
    JOIN course_classes cc ON e.course_class_id = cc.id
    JOIN courses c ON cc.course_id = c.id
    JOIN class_schedules cs ON cs.course_class_id = cc.id
    WHERE e.student_id = %s
    ORDER BY cs.day_of_week, cs.start_period
    """

    cursor.execute(sql, (student_id,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def insert_schedule(course_class_id, day, start_period, periods, room, total_sessions):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO class_schedules
    (course_class_id, day_of_week, start_period, periods, room, total_sessions)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (
        course_class_id,
        day,
        start_period,
        periods,
        room,
        total_sessions
    ))
    conn.commit()
    conn.close()


def fetch_schedules_by_class(course_class_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT day_of_week, start_period, periods, room, total_sessions
        FROM class_schedules
        WHERE course_class_id=%s
        ORDER BY day_of_week, start_period
    """, (course_class_id,))

    rows = cursor.fetchall()
    conn.close()
    return rows


def check_schedule_conflict(student_id, day, start, periods):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    SELECT 1
    FROM enrollments e
    JOIN class_schedules cs ON e.course_class_id = cs.course_class_id
    WHERE e.student_id = %s
      AND cs.day_of_week = %s
      AND (
            cs.start_period < %s + %s
        AND %s < cs.start_period + cs.periods
      )
    LIMIT 1
    """
    cursor.execute(sql, (student_id, day, start, periods, start))
    conflict = cursor.fetchone() is not None
    conn.close()
    return conflict

def insert_exam(course_class_id, exam_date, start_time, duration, room, exam_type):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO exam_schedules
    (course_class_id, exam_date, start_time, duration, room, exam_type)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (
        course_class_id,
        exam_date,
        start_time,
        duration,
        room,
        exam_type
    ))
    conn.commit()
    conn.close()


def fetch_exams_by_class(course_class_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT exam_date, start_time, duration, room, exam_type
        FROM exam_schedules
        WHERE course_class_id=%s
        ORDER BY exam_date, start_time
    """, (course_class_id,))

    rows = cursor.fetchall()
    conn.close()
    return rows

def insert_exam(course_class_id, date, time, duration, room, exam_type):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO exam_schedules
    (course_class_id, exam_date, start_time, duration, room, exam_type)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (
        course_class_id,
        date,
        time,
        duration,
        room,
        exam_type
    ))
    conn.commit()
    conn.close()

def check_exam_conflict(student_id, exam_date, start_time, duration):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    SELECT 1
    FROM enrollments e
    JOIN exam_schedules ex ON e.course_class_id = ex.course_class_id
    WHERE e.student_id = %s
      AND ex.exam_date = %s
      AND (
            ex.start_time < ADDTIME(%s, SEC_TO_TIME(%s*60))
        AND %s < ADDTIME(ex.start_time, SEC_TO_TIME(ex.duration*60))
      )
    LIMIT 1
    """
    cursor.execute(sql, (
        student_id,
        exam_date,
        start_time,
        duration,
        start_time
    ))
    conflict = cursor.fetchone() is not None
    conn.close()
    return conflict
