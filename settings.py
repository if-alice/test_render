from pydantic import BaseSettings


class Settings(BaseSettings):
    REDIS_URL: str
    POSTGRES_URL: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        frozen = True
