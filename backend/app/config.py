import os
from functools import cached_property

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_TYPE: str
    DATABASE_DRIVER: str
    DATABASE_USERNAME: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_PORT: int
    DATABASE_NAME: str
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str



    model_config = SettingsConfigDict(env_file=os.path.join(os.path.dirname(__file__), "../.env"))

    @cached_property
    def database_url(self) -> str:
        return (f"{self.DATABASE_TYPE}+{self.DATABASE_DRIVER}://"
                f"{self.DATABASE_USERNAME}:{self.DATABASE_PASSWORD}"
                f"@{self.DATABASE_HOST}:{self.DATABASE_PORT}/{self.DATABASE_NAME}")


settings = Settings()

print(settings.database_url)