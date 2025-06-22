from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    DATABASE_HOSTNAME: Optional[str] = "localhost"
    DATABASE_PORT: Optional[int] = 5432
    DATABASE_USERNAME: Optional[str] = "postgres"
    DATABASE_PASSWORD: Optional[str] = "postgres"
    DATABASE_NAME: Optional[str] = "FastApi"

    model_config = SettingsConfigDict(env_file=".env")
    

        
    @property
    def DATABASE_URL(self):
        return f"postgresql+psycopg2://{self.DATABASE_USERNAME}:{self.DATABASE_PASSWORD}@{self.DATABASE_HOSTNAME}:{self.DATABASE_PORT}/{self.DATABASE_NAME}"

settings = Settings()


