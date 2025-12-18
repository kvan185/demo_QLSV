from src.data_access.tuition_dao import (
    fetch_tuition_settings,
    calculate_course_fee
)


def get_tuition_settings():
    return fetch_tuition_settings()


def get_course_fee(course_id, system_id):
    return calculate_course_fee(course_id, system_id)
