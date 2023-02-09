from fastapi import Request, Response

auth = "qwe"


def set_auth(response: Response, user_id: int):
    response.set_cookie(auth, str(user_id), secure=False, httponly=True)


def get_user_id_from_auth_cookie(request: Request):
    if auth not in request.cookies:
        return
    return int(request.cookies["auth_key"])
