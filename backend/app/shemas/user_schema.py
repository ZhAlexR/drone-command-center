from pydantic import BaseModel


class RoleSchema(BaseModel):
    name: str


class UserCreateSchema(BaseModel):
    username: str
    email: str
    password: str
    role_id: int


class UserLoginSchema(BaseModel):
    email: str
    password: str
