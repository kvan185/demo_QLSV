from src.data_access.class_dao import (
    fetch_classes,
    fetch_classes_simple,
    insert_class,
    update_class,
    delete_class,
    assign_advisor,
    remove_advisor,
    fetch_advisor_class
)

# =======================
# CLASS – FULL
# =======================

def get_classes(keyword="", order="ASC"):
    return fetch_classes(keyword, order)


# =======================
# CLASS – COMBOBOX
# =======================

def get_classes_for_combobox():
    """id, class_name"""
    return fetch_classes_simple()


# =======================
# CRUD
# =======================

def add_class(class_name, major):
    if not class_name:
        raise ValueError("Tên lớp không được để trống")
    insert_class(class_name, major)


def edit_class(class_id, class_name, major):
    update_class(class_id, class_name, major)


def remove_class(class_id):
    delete_class(class_id)


# =======================
# ADVISOR
# =======================

def set_advisor(class_id, teacher_id):
    assign_advisor(class_id, teacher_id)


def unset_advisor(class_id):
    remove_advisor(class_id)


def get_advisor_class(teacher_id):
    return fetch_advisor_class(teacher_id)
