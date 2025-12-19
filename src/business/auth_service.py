from src.data_access.auth_dao import find_user, insert_user
import hashlib


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def login(username, password):
    user = find_user(username)
    if not user:
        raise ValueError("Sai tài khoản")

    if user[2] != hash_password(password):
        raise ValueError("Sai mật khẩu")

    return {
        "id": user[0],
        "username": user[1],
        "role": user[3],
        "ref_id": user[4]
    }


def register(username, password, role, ref_id=None):
    if find_user(username):
        raise ValueError("Tài khoản đã tồn tại")

    insert_user(
        username,
        hash_password(password),
        role,
        ref_id
    )
