from src.data_access.class_dao import fetch_advisor_class, remove_advisor
from src.data_access.teacher_dao import (
    insert_teacher,
    update_teacher,
    fetch_teachers,
    fetch_teachers_full,
    fetch_teachers_without_class,
    assign_advisor,
    fetch_advisor_class,
    fetch_all_teachers,
    fetch_all_classes_with_advisor,
    fetch_teachers_simple,
    fetch_classes_without_advisor,
    fetch_teacher_by_id
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

def get_all_classes_status():
    """
    Trả về:
    id, class_name, major, advisor_name (None nếu chưa có)
    """
    return fetch_all_classes_with_advisor()

def get_classes_need_advisor():
    return fetch_classes_without_advisor()


def get_available_teachers():
    return fetch_teachers_without_class()


def set_advisor(class_id, teacher_id):
    if not class_id or not teacher_id:
        raise ValueError("Thiếu thông tin gán cố vấn")

    assign_advisor(class_id, teacher_id)

def get_advisor_class(teacher_id):
    """
    Return: (class_id, class_name) hoặc None
    """
    rows = fetch_advisor_class(teacher_id)

    if not rows:
        return None

    class_id, class_name, *_ = rows[0]
    return class_id, class_name


def set_advisor_for_class(class_id, teacher_id):
    if not class_id or not teacher_id:
        raise ValueError("Thiếu thông tin gán cố vấn")

    assign_advisor(class_id, teacher_id)


def unset_advisor_for_class(class_id):
    remove_advisor(class_id)
    
def get_all_teachers():
    """id, teacher_code, full_name"""
    return fetch_teachers_full()

def get_teachers_for_combobox():
    """id, full_name"""
    return fetch_teachers_simple()

def get_teacher_by_id(teacher_id):
    return fetch_teacher_by_id(teacher_id)