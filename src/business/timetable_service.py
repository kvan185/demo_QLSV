from src.data_access.timetable_dao import (
    fetch_week_timetable,
    insert_schedule,
    fetch_schedules_by_class,
    check_schedule_conflict,
    fetch_exams_by_class,
    insert_exam
)

def get_week_timetable(student_id, max_periods=10):
    raw = fetch_week_timetable(student_id)

    # Khởi tạo lưới: day -> period -> text
    table = {
        day: {p: "" for p in range(1, max_periods + 1)}
        for day in range(2, 8)
    }

    for day, start, periods, course, room in raw:
        for p in range(start, start + periods):
            table[day][p] = f"{course}\n({room})"

    return table

def add_schedule(course_class_id, day, start, periods, room, total_sessions):
    if day < 2 or day > 7:
        raise ValueError("Thứ không hợp lệ")
    if start < 1 or periods < 1:
        raise ValueError("Tiết học không hợp lệ")

    insert_schedule(course_class_id, day, start, periods, room, total_sessions)


def get_schedules(course_class_id):
    return fetch_schedules_by_class(course_class_id)


def has_conflict(student_id, day, start, periods):
    return check_schedule_conflict(student_id, day, start, periods)

def get_exams(course_class_id):
    return fetch_exams_by_class(course_class_id)

def add_exam(course_class_id, date, time, duration, room, exam_type):
    insert_exam(course_class_id, date, time, duration, room, exam_type)