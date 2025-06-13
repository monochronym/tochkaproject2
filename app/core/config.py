from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    """Настройки приложения"""
    DATABASE_URL: str
    SECRET_KEY: str
    ADMIN_API_KEY: str
    
    # Настройки SSL/TLS
    SSL_KEYFILE: Optional[str] = None
    SSL_CERTFILE: Optional[str] = None
    
    class Config:
        env_file = ".env"

settings = Settings(DATABASE_URL="postgresql://postgres:VXhvCqFkIPqsYOpYeAPEXEqBvlcvQJbP@trolley.proxy.rlwy.net:26708/railway", SECRET_KEY="gV64m9aIzFG4qpgVphvQbPQrtAO0nM-7YwwOvu0XPt5KJOjAy4AfgLkqJXYEt", ADMIN_API_KEY="b2b11fae-e2a5-4274-bd10-4ef170eb4b52") 
