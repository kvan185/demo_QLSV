from src.data_access.grade_dao import  fetch_grades, insert_grade, update_grade, update_grade_rule, fetch_grade_rules, insert_grade_rule, check_rule_exists

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

def add_or_update_rule(course_id, min_score, pass_score):
    if min_score < 0 or pass_score > 10:
        raise ValueError("Điểm phải trong khoảng 0 – 10")
    if min_score > pass_score:
        raise ValueError("Điểm tối thiểu phải ≤ điểm đạt")

    if check_rule_exists(course_id):
        update_grade_rule(course_id, min_score, pass_score)
    else:
        insert_grade_rule(course_id, min_score, pass_score)


def get_grade_rules(keyword=""):
    return fetch_grade_rules(keyword)
