from src.data_access.course_class_dao import (
    insert_course_class,
    update_course_class,
    fetch_course_classes,
    fetch_all_course_classes
)


def add_course_class(course_id, teacher_id, semester, school_year):
    if not course_id or not teacher_id:
        raise ValueError("Thiếu môn học hoặc giáo viên")
    insert_course_class(course_id, teacher_id, semester, school_year)


def edit_course_class(id, course_id, teacher_id, semester, school_year):
    if not id:
        raise ValueError("Chưa chọn lớp học phần")
    update_course_class(id, course_id, teacher_id, semester, school_year)


def get_course_classes(keyword="", order="ASC"):
    return fetch_course_classes(keyword, order)


def get_all_course_classes():
    return fetch_all_course_classes()
