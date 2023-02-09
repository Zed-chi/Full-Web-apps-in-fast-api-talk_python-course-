from typing import Optional

from models import account
from settings import db


def user_count():
    return db.count("users")


def get_user(pk=None):
    if not pk:
        return
    db.get("users", pk=pk)


def create_user(name, email, password):
    user = account.User(name=name, email=email, hashed_pass=password)
    db.add("users", user.to_dict())
    return user


def login_user(email, password):
    user: Optional[dict] = db.get("users", email)
    print(f"=== {user} ===")
    if not user:
        return
    if user["password"] == password:
        return user
