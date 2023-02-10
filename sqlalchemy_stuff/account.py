import sqlalchemy as sql
from datetime import datetime
from .base import SQLAlchemyBase

class User(SQLAlchemyBase):
    __tablename__ = "accounts"
    id = sql.Column(sql.String, primary_key=True, unique=True)
    name = sql.Column(sql.String)
    email = sql.Column(sql.String, unique=True)
    password = sql.Column(sql.String)
    last_login = sql.Column(sql.DateTime, default=datetime.now())
    created_at = sql.Column(sql.DateTime, default=datetime.now())


    def __repr__(self) -> str:
        return f"Package {self.id}"
