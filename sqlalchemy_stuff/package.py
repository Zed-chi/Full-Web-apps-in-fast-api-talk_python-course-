from datetime import datetime

import sqlalchemy as sql
import sqlalchemy.orm as orm

from .base import SQLAlchemyBase


class License(SQLAlchemyBase):
    __tablename__ = "licenses"
    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    name = sql.Column(sql.String, unique=True)
    description = sql.Column(sql.String)
    package_id = sql.Column(
        sql.Integer, sql.ForeignKey("packages.id"), nullable=True
    )
    package = orm.relationship("Package")

    def __repr__(self) -> str:
        return f"License {self.id}"


class Release(SQLAlchemyBase):
    __tablename__ = "releases"
    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    maj = sql.Column(sql.Integer, default=0)
    min = sql.Column(sql.Integer, default=0)
    build = sql.Column(sql.Integer, default=0)
    created_at = sql.Column(sql.DateTime, default=datetime.now(), index=True)
    comment = sql.Column(sql.Text, nullable=True)
    url = sql.Column(sql.String, nullable=True)
    size = sql.Column(sql.Integer, nullable=True)

    package_id = sql.Column(
        sql.Integer, sql.ForeignKey("packages.id"), nullable=True
    )
    package = orm.relationship("Package")

    def __repr__(self) -> str:
        return f"Release {self.id}"


class File(SQLAlchemyBase):
    __tablename__ = "files"
    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True)

    package_id = sql.Column(
        sql.Integer, sql.ForeignKey("packages.id"), nullable=True
    )
    package = orm.relationship("Package")

    release = orm.relationship("Release")
    release_id = sql.Column(
        sql.Integer, sql.ForeignKey("releases.id"), nullable=True
    )

    created_at = sql.Column(sql.DateTime, default=datetime.now(), index=True)

    def __repr__(self) -> str:
        return f"File {self.id}"


class Package(SQLAlchemyBase):
    __tablename__ = "packages"
    id = sql.Column(sql.String, primary_key=True, unique=True)
    created_at = sql.Column(sql.DateTime, default=datetime.now(), index=True)
    summary = sql.Column(sql.Text, nullable=True)
    description = sql.Column(sql.Text, nullable=True)

    author = orm.relationship("User", back_populates="package")
    maintainers = orm.relationship(
        "User", secondary="user_maintain", back_populates="maintained_packages"
    )

    home_page_url = sql.Column(sql.String, nullable=True)
    docs_url = sql.Column(sql.String, nullable=True)
    package_url = sql.Column(sql.String, nullable=True)

    license = orm.relationship("License", back_populates="package")
    releases = orm.relationship("Release", back_populates="package")

    def __repr__(self) -> str:
        return f"Package {self.id}"
