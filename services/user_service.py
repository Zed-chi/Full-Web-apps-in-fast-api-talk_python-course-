from typing import Optional
from sqlalchemy_stuff.db_session import create_session
from sqlalchemy_stuff import account
from models import account as acc_model
from settings import db


def user_count():
    session = create_session()
    try:        
        return session.query(account.User).count()
    except:
        print("fuck relesase query")
    finally:
        session.close()


def get_user(pk=None):
    if not pk:
        return
    session = create_session()
    try:        
        return session.query(account.User).get({"id":pk})
    except:
        print("fuck relesase query")
    finally:
        session.close()


def get_user_by_email(email=None):
    if not email:
        return
    session = create_session()
    try:        
        return session.query(account.User).get({"email":email})
    except:
        print("fuck relesase query")
    finally:
        session.close()

def create_user(name, email, password):
    session = create_session()
    try:        
        user = account.User()
        user.email = email
        user.name = name
        user.password = password
        session.add(user)
        session.commit()        
    except:
        print("fuck relesase query")
    finally:
        session.close()


def login_user(email, password):
    session = create_session()
    try:        
        user = session.query(account.User).get({"email":email})
        if not user:
            return
        if user.password == password:
            pass
    except:
        print("fuck relesase query")
    finally:
        session.close()
