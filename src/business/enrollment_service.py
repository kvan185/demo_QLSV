from src.data_access.enrollment_dao import (
    enroll_student,
    fetch_enrollments,
    delete_enrollment
)

def add_enrollment(student_id, course_class_id):
    if not student_id or not course_class_id:
        raise ValueError("Thiếu thông tin đăng ký")
    enroll_student(student_id, course_class_id)


def get_enrollments():
    return fetch_enrollments()


def remove_enrollment(student_id, course_class_id):
    delete_enrollment(student_id, course_class_id)
