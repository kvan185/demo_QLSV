from src.data_access.grade_dao import (
    fetch_grades,
    insert_grade,
    update_grade
)

def get_grades(keyword="", order="ASC"):
    return fetch_grades(keyword, order)

def add_grade(student_id, course_id, score):
    if score < 0 or score > 10:
        raise ValueError("Điểm phải từ 0 đến 10")
    insert_grade(student_id, course_id, score)

def edit_grade(student_id, course_id, score):
    if score < 0 or score > 10:
        raise ValueError("Điểm phải từ 0 đến 10")
    update_grade(student_id, course_id, score)
