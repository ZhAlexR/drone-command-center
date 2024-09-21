from datetime import datetime, timedelta, UTC

import jwt

from passlib.context import CryptContext
from backend.app.config import settings
from backend.app.shemas.token_schema import Token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_access_token(data: dict):
    data_to_encode = data.copy()
    expire = datetime.now(UTC) + timedelta(minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
    data_to_encode.update({"exp": expire})
    return jwt.encode(
        payload=data_to_encode,
        key=settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM,
    )


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)
