from src.data_access.student_dao import insert_student, fetch_students, update_student, fetch_all_students
from src.data_access.class_dao import fetch_classes_for_student

def add_student(code, name, year, class_id):
    if year < 1990:
        raise ValueError("Năm sinh không hợp lệ")

    insert_student(code, name, year, class_id)


def get_all_students():
    return fetch_all_students()

def get_students(keyword="", class_id="", order=""):
    return fetch_students(keyword, class_id, order)

def edit_student(id, code, name, year, class_id):
    if not code or not name:
        raise ValueError("Dữ liệu không hợp lệ")
    update_student(id, code, name, year, class_id)

def get_class():
    return fetch_classes_for_student()