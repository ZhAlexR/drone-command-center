from typing import Type

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from backend.app.crud.user import create_user, get_user_by_email, create_role, get_roles
from backend.app.dependency import get_session
from backend.app.shemas.token_schema import Token
from backend.app.shemas.user_schema import UserCreateSchema, RoleSchema, UserLoginSchema
from backend.app.utils.auth import verify_password, create_access_token

auth_router = APIRouter()

@auth_router.post("/roles")
async def role_create(role_data: RoleSchema, session: AsyncSession = Depends(get_session)) -> dict:
    await create_role(role_data, session)
    return {"message": "Role '{}' created successfully".format(role_data.name)}

@auth_router.get("/roles")
async def role_list(session: AsyncSession = Depends(get_session)):
    return await get_roles(session)


@auth_router.post("/register")
async def register(user_data: UserCreateSchema, session: AsyncSession = Depends(get_session)) -> dict:
    await create_user(user=user_data, session=session)
    return {"message": "User '{}' created successfully".format(user_data.email)}


@auth_router.post("/login", response_model=Token)
async def login(user_data: UserLoginSchema, session: AsyncSession = Depends(get_session)) -> Type[Token]:
    user = await get_user_by_email(email=user_data.email, session=session)
    if not (user and verify_password(user_data.password, user.hashed_password)):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid credentials")
    return create_access_token(data={"sub": user.email})
