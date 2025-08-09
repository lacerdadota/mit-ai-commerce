from sqlmodel import SQLModel
from app.db.session import engine


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
