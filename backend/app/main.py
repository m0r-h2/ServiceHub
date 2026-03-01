from contextlib import asynccontextmanager

from backend.app.database.models import db_helper, Base
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(
    title="Service_Hub",
    lifespan=lifespan
)
