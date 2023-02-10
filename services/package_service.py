from sqlalchemy_stuff.db_session import create_session
from sqlalchemy_stuff import package

def release_count():
    session = create_session()
    try:        
        return session.query(package.Release).count()
    except:
        print("fuck release_count query")
    finally:
        session.close()


def package_count():
    session = create_session()
    try:        
        return session.query(package.Package).count()
    except:
        print("fuck package_count query")
    finally:
        session.close()


def latest_packages(limit=5):
    session = create_session()
    try:        
        return session.query(package.Package).order_by("created_at").limit(limit).all()
    except:
        print("fuck latest_packages query")
    finally:
        session.close()


def get_package(pk=None):
    if not pk:return

    session = create_session()
    try:        
        return session.query(package.Package).get({"id": pk})
    except:
        print("fuck get_package query")
    finally:
        session.close()


def get_latest_release(package_id):
    if not package_id:return

    session = create_session()
    try:        
        return session.query(package.Release)\
            .filter(package.Release.package_id==package_id)\
            .order_by("created_at")\
            .limit(5)
    except:
        print("fuck get_package query")
    finally:
        session.close()
