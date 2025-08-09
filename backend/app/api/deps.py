from fastapi import Depends
from sqlmodel import Session
from app.db.session import get_session


def get_db(session: Session = Depends(get_session)):
    return session
