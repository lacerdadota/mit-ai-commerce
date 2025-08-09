from sqlmodel import Field
from app.models.schemas.user import UserBase


class User(UserBase, table=True):
    id: int = Field(primary_key=True)
    hashed_password: str = Field(nullable=False)
    email: str = Field(unique=True, index=True)

    def __repr__(self):
        return f"User(id={self.id}, username={self.username}, email={self.email})"
