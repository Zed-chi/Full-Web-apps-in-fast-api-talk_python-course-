import sqlalchemy as sql
import sqlalchemy.orm as orm
from .base import SQLAlchemyBase


factory = None
engine = None


def global_init(db_file:str):
    global factory

    if factory: return

    if not db_file or not db_file.strip():
        raise Exception("no db file provided")
    db_url:str = f"sqlite:///{db_file.strip()}"
    engine = sql.create_engine(db_url, echo=True)
    factory = orm.sessionmaker(bind=engine)
    
    from . import package
    from . import account
    SQLAlchemyBase.metadata.create_all(engine)


def create_session():
    global factory
    if not factory:
        raise Exception("run global init")
    session = factory()
    session.expire_on_commit = False
    return session