from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str = "Bearer"


class GetCurrentUserTokenSchema(BaseModel):
    email: str
    role: str
    expired_at: int
