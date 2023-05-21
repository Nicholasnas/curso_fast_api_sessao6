from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = '/ap1/v1'
    DB_URL: str = 'sqlite+aiosqlite:///faculdade.db'
    DBBaseModel = declarative_base()

    # segredo usado na geração de tokens
    JWT_SECRET:str = 'js1D14EdOxj0TXjmDP3H_ZPyVKFufAh6fnXWPvMLQ64'
    """
    import secrets
    token = secrets.token_urlsafe(32)
    """
    ALGORITHM:str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 *  24 * 7  # uma semana
    
    
    class Config:
        case_sensitive = True


settings: Settings = Settings()

