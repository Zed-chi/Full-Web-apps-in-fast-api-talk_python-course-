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
        return session.query(account.User).get({"email": email})
    finally:
        session.close()


def create_user(name, email, password):
    session = create_session()
    try:
        user = account.User()
        user.email = email
        user.name = name
        user.password = sha512_crypt.hash(password, rounds=HASH_ROUNDS)
        session.add(user)
        session.commit()
    finally:
        session.close()


def login_user(email, password):
    session = create_session()
    try:
        user = session.query(account.User).get({"email": email})
        if not user:
            return
        if sha512_crypt.verify(password, user.password):
            pass
    finally:
        session.close()
