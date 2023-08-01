from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    token_expiry: int
    smtp_mail: str
    smtp_password: str

    class Config:
        env_file = ".env"


settings = Settings()
