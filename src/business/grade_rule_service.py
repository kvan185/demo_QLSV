from src.data_access.grade_rule_dao import (
    insert_grade_rule,
    update_grade_rule,
    fetch_grade_rules,
    check_rule_exists
)


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
