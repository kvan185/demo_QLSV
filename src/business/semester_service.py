from src.data_access.semester_dao import (
    insert_semester,
    update_semester,
    fetch_semesters,
    fetch_all_semesters
)


def add_semester(name, start_date, end_date):
    if not name:
        raise ValueError("Tên học kỳ không được để trống")
    if start_date > end_date:
        raise ValueError("Ngày bắt đầu phải trước ngày kết thúc")
    insert_semester(name, start_date, end_date)


def edit_semester(id, name, start_date, end_date):
    if not id:
        raise ValueError("Chưa chọn học kỳ")
    update_semester(id, name, start_date, end_date)


def get_semesters(keyword="", order="ASC"):
    return fetch_semesters(keyword, order)


def get_all_semesters():
    return fetch_all_semesters()
