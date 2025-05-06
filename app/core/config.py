
import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str = os.getenv("OPENAI_API_KEY")
    redis_url: str = os.getenv("REDIS_URL")
    db_url: str = os.getenv("DATABASE_URL")

settings = Settings()
