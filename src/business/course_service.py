from src.data_access.course_dao import (
    fetch_courses,
    insert_course,
    update_course
)

def get_courses(keyword="", order="ASC"):
    return fetch_courses(keyword, order)

def add_course(code, name, credit):
    if not code or not name:
        raise ValueError("Mã môn và tên môn không được rỗng")
    if credit <= 0:
        raise ValueError("Số tín chỉ phải > 0")
    insert_course(code, name, credit)

def edit_course(id, code, name, credit):
    if not code or not name:
        raise ValueError("Mã môn và tên môn không được rỗng")
    if credit <= 0:
        raise ValueError("Số tín chỉ phải > 0")
    update_course(id, code, name, credit)

def get_all_courses():
    return fetch_courses()