from datetime import datetime

import sqlalchemy as sql
import sqlalchemy.orm as orm

from .base import SQLAlchemyBase


class User(SQLAlchemyBase):
    __tablename__ = "users"
    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    name = sql.Column(sql.String)
    email = sql.Column(sql.String, unique=True)
    password = sql.Column(sql.String)
    last_login = sql.Column(sql.DateTime, default=datetime.now())
    created_at = sql.Column(sql.DateTime, default=datetime.now())

    package_id = sql.Column(
        sql.Integer, sql.ForeignKey("packages.id"), nullable=True
    )
    package = orm.relationship("Package", back_populates="author")
    maintained_packages = orm.relationship(
        "Package", secondary="user_maintain", back_populates="maintainers"
    )

    def __repr__(self) -> str:
        return f"Package {self.id}"


class UserMaintains(SQLAlchemyBase):
    __tablename__ = "user_maintain"

    id = sql.Column(sql.Integer, primary_key=True)
    user_id = sql.Column(sql.Integer, sql.ForeignKey("users.id"))
    project_id = sql.Column(sql.Integer, sql.ForeignKey("packages.id"))
