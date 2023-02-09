import hashlib

from fastapi import Request, Response

auth = "auth"


def set_auth(response: Response, user_id: str):
    hash_val = __hash_text(user_id)
    val = f"{user_id}:{hash_val}"
    response.set_cookie(auth, val, secure=False, httponly=True)


def get_user_id_from_auth_cookie(request: Request):
    print(f"===cooki {request.cookies} ===")
    if auth not in request.cookies:
        return
    val = request.cookies[auth]
    parts = val.split(":")
    if len(parts) != 2:
        return
    user_id, hash_val = parts
    hash_check = __hash_text(user_id)
    if hash_val != hash_check:
        return

    return request.cookies["auth"]


def __hash_text(text: str):
    text = f"some_{text}_some"
    return hashlib.sha512(text.encode("utf-8")).hexdigest()


def logout(response: Response):
    response.delete_cookie(auth)
