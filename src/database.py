from sqlalchemy.orm import sessionmaker
from sqlmodel import Field, Session, SQLModel, create_engine, select

SQLALCHEMY_DATABASE_URL = "sqlite:///example.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
