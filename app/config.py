import os


class Settings:
    DB_URL: str = os.getenv(
        "DATABASE_URL", "postgresql://bakeryops_user:mysecretpassword@localhost/bakeryops_db"
    )
    SECRET_KEY: str = os.getenv("SECRET_KEY", "secretkey")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30


settings = Settings()
