from sqlalchemy_stuff import package
from sqlalchemy_stuff.db_session import create_session


def release_count():
    session = create_session()
    try:
        return session.query(package.Release).count()
    finally:
        session.close()


def package_count():
    session = create_session()
    try:
        return session.query(package.Package).count()
    finally:
        session.close()


def latest_packages(limit=5):
    session = create_session()
    try:
        return (
            session.query(package.Package)
            .order_by("created_at")
            .limit(limit)
            .all()
        )
    finally:
        session.close()


def get_package(pk=None):
    if not pk:
        return

    session = create_session()
    try:
        return session.query(package.Package).get({"id": pk})
    finally:
        session.close()


def get_latest_release(package_id):
    if not package_id:
        return

    session = create_session()
    try:
        return (
            session.query(package.Release)
            .filter(package.Release.package_id == package_id)
            .order_by("created_at")
            .limit(5)
        )
    finally:
        session.close()
