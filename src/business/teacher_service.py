from src.data_access.teacher_dao import (
    insert_teacher,
    update_teacher,
    fetch_teachers,
    fetch_all_teachers
)


def add_teacher(code, name, degree):
    if not code or not name:
        raise ValueError("Mã GV và tên không được để trống")
    insert_teacher(code, name, degree)


def edit_teacher(id, code, name, degree):
    if not id:
        raise ValueError("Chưa chọn giáo viên")
    update_teacher(id, code, name, degree)


def get_teachers(keyword="", order="ASC"):
    return fetch_teachers(keyword, order)


def get_all_teachers():
    return fetch_all_teachers()
