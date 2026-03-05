from contextlib import asynccontextmanager
from fastapi import FastAPI
from backend.app.database.models import db_helper, Base
from backend.app.api_v1 import router as router_v1



@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(
    title="Service Hub",
    lifespan=lifespan
)

app.include_router(router=router_v1, prefix="/api/v1")