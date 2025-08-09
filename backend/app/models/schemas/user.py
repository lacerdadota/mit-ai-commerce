from sqlmodel import SQLModel
from typing import Optional


class UserBase(SQLModel):
    name: str
    email: str
    segment: str


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    id: int


class UserUpdate(UserBase):
    name: Optional[str]
    email: Optional[str]
    segment: Optional[str]
