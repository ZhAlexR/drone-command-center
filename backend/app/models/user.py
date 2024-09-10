from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column

from backend.app.models.base import BaseModel


class Role(BaseModel):
    __tablename__ = 'roles'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: str = mapped_column(String(30), unique=True)

    users: Mapped[list["User"]] = relationship(back_populates="role")

    def __repr__(self) -> str:
        return f"<Role(name={self.name})>"

class User(BaseModel):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(30), unique=True, index=True)
    email: str = mapped_column(unique=True, index=True)
    hashed_password: Mapped[str]
    is_active: Mapped[bool] = mapped_column(default=True)
    role_id: Mapped[int] = mapped_column(ForeignKey('roles.id'))

    role: Mapped["Role"] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"<User(username={self.email})>"
