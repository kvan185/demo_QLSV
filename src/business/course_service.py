from src.data_access.course_dao import fetch_courses, insert_course, update_course
from src.data_access.course_dao import insert_course_class, fetch_course_classes, update_course_class, fetch_all_course_classes

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
