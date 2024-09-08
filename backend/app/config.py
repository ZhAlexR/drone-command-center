from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str = "postgresql://user:password@localhost/dbname"
    jwt_secret_key: str = "secret_key_here"
    jwt_algorithm: str = "HS256"
    jwt_access_token_expire_minutes: int = 30

settings = Settings()
