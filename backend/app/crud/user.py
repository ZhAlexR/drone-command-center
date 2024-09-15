from typing import Type, Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.models.user import User, Role
from backend.app.utils.auth import get_password_hash
from backend.app.shemas import user_schema


async def create_role(role: user_schema.RoleSchema, session: AsyncSession) -> Role:
    new_role = Role(name=role.name)
    session.add(new_role)
    await session.commit()
    await session.refresh(new_role)
    return new_role

async def get_roles(session: AsyncSession) -> Sequence[Role]:
    roles = await session.execute(select(Role))
    return roles.scalars().all()


async def create_user(user: user_schema.UserCreateSchema, session: AsyncSession) -> User:
    user_data = user.model_dump()
    user_data["hashed_password"] = get_password_hash(user_data["password"])
    user_data.pop("password")

    new_user = User(**user_data)
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user

async def get_user_by_email(session: AsyncSession, email: str) -> Type[User]:
    user = await session.execute(select(User).where(User.email == email))
    return user.scalar()
