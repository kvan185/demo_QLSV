from src.data_access.student_dao import (
    fetch_all_students,
    fetch_students,
    fetch_all_students_simple,
    insert_student,
    update_student,
    delete_student,
    fetch_student_enrollments,
    insert_enrollment,
    delete_enrollment,
    fetch_students_by_class,
    fetch_student_by_id
)


# =======================
# STUDENT – FULL
# =======================

def get_all_students():
    return fetch_all_students()


def search_students(keyword="", class_id="", order="ASC"):
    return fetch_students(keyword, class_id, order)


# =======================
# STUDENT – COMBOBOX
# =======================

def get_all_students_for_combobox():
    return fetch_all_students_simple()

def get_students_for_combobox_by_class(class_id):
    """Sinh viên theo lớp cố vấn"""
    return fetch_students_by_class(class_id)

def add_student(student_code, full_name, birth_year, class_id):
    if not student_code or not full_name:
        raise ValueError("Thiếu thông tin sinh viên")
    insert_student(student_code, full_name, birth_year, class_id)

def edit_student(student_id, student_code, full_name, birth_year, class_id):
    update_student(student_id, student_code, full_name, birth_year, class_id)


def remove_student(student_id):
    delete_student(student_id)

def get_student_enrollments(student_id):
    return fetch_student_enrollments(student_id)


def enroll_course(student_id, course_class_id):
    insert_enrollment(student_id, course_class_id)


def unenroll_course(student_id, course_class_id):
    delete_enrollment(student_id, course_class_id)

def get_student_by_id(student_id):
    return fetch_student_by_id(student_id)