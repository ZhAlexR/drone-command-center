from typing import AsyncGenerator, Type

import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from starlette import status

from backend.app.config import settings
from backend.app.database import async_session
from backend.app.shemas.token_schema import GetCurrentUserTokenSchema

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

async def get_session() -> AsyncGenerator:
    async with async_session() as session:
        yield session


async def get_current_user(token: str = Depends(oauth2_scheme)) -> GetCurrentUserTokenSchema:
    try:
        token_data = jwt.decode(
        jwt=token,
        key=settings.JWT_SECRET_KEY,
        algorithms=[settings.JWT_ALGORITHM],
    )
        schema = GetCurrentUserTokenSchema(
            email=token_data["sub"],
            role = token_data["role"],
            expired_at = token_data["exp"],
        )
        return schema
    except JWTError:
        HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

class RoleChecker:
    def __init__(self, allowed_roles: list):
        self.allowed_roles = allowed_roles

    def __call__(self, current_user: GetCurrentUserTokenSchema = Depends(get_current_user)):
        if current_user.role not in self.allowed_roles:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions.")
        return True