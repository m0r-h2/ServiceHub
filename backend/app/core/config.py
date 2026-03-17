from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pydantic import BaseModel
from sqlalchemy import URL
import os
import dotenv

class SqlalchemyConfig(BaseModel):
    echo: bool = True


load_dotenv()



class AuthConfig(BaseModel):
    secret_key: str = os.getenv("SECRET_KEY")
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 120




class DatabaseConfig(BaseModel):
    database: str = os.getenv("SERVICE__HUB__DB__NAME")
    username: str = os.getenv("SERVICE__HUB__DB__USERNAME")
    host: str = os.getenv("SERVICE__HUB__DB__HOST")
    port: int = os.getenv("SERVICE__HUB__DB__PORT")
    password: str = os.getenv("SERVICE__HUB__DB__PASSWORD")

    @property
    def async_url_pg(self):
        return URL.create(
            drivername="postgresql+asyncpg",
            database=self.database,
            username=self.username,
            host=self.host,
            port=self.port,
            password=self.password
        )

    sqlalchemy: SqlalchemyConfig = SqlalchemyConfig()


class Settings(BaseSettings):
    db: DatabaseConfig = DatabaseConfig()
    auth: AuthConfig = AuthConfig()


settings = Settings()