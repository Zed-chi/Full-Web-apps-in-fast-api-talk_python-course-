from typing import Optional

from passlib.handlers.sha2_crypt import sha512_crypt

from settings import HASH_ROUNDS
from sqlalchemy_stuff import account
from sqlalchemy_stuff.db_session import create_session


def user_count():
    session = create_session()
    try:
        return session.query(account.User).count()
    finally:
        session.close()


def get_user(pk=None) -> Optional[account.User]:
    if not pk:
        return
    session = create_session()
    try:
        return session.query(account.User).get({"id": pk})
    finally:
        session.close()


def get_user_by_email(email=None):
    if not email:
        return
    session = create_session()
    try:
        return (
            session.query(account.User)
            .filter(account.User.email == email)
            .first()
        )
    finally:
        session.close()


def create_user(name, email, password):
    print(f"=== pass {password}")
    session = create_session()
    try:
        user = account.User()
        user.email = email
        user.name = name
        # ignore
        user.password = sha512_crypt.hash(password, rounds=HASH_ROUNDS)
        session.add(user)
        session.commit()
        return user
    finally:
        session.close()


def login_user(email, password):
    session = create_session()
    try:
        user = (
            session.query(account.User)
            .filter(account.User.email == email)
            .first()
        )
        if not user:
            return
        if sha512_crypt.verify(password, str(user.password)):
            return user
    finally:
        session.close()
