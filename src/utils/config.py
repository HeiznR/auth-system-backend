from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_PORT: int
    DB_HOST: str
    PGADMIN_EMAIL: str
    PGADMIN_PASSWORD: str
    JWT_SECRET_KEY: str

    class Config:
        env_file = ".env"
