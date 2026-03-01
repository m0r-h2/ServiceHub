from pydantic_settings import BaseSettings
from pydantic import BaseModel
from sqlalchemy import URL


class SqlalchemyConfig(BaseModel):
    echo: bool = True



class DatabaseConfig(BaseModel):
    database: str = "service_hub_db"
    username: str = "service_hub_user"
    host: str = "localhost"
    port: int = 5432
    password: str = "23458945"

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


settings = Settings()