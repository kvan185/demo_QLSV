from src.data_access.class_dao import (
    fetch_classes,
    insert_class,
    update_class,
    fetch_all_course_classes
)

def get_classes(keyword="", order="ASC"):
    return fetch_classes(keyword, order)

def add_class(name, major):
    if not name:
        raise ValueError("Tên lớp không được rỗng")
    insert_class(name, major)

def edit_class(id, name, major):
    if not name:
        raise ValueError("Tên lớp không được rỗng")
    update_class(id, name, major)

def get_all_course_classes():
    return fetch_all_course_classes()