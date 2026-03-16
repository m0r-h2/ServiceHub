from backend.app.database.models import db_helper, Base
from backend.app.api_v1 import router_v1
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
from fastapi import FastAPI
from backend.app.render import router_render

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(
    title="Service Hub",
    lifespan=lifespan
)


# CORS
origins = [
    "http://localhost:8000",
    "http://127.0.0.1:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)



app.include_router(router=router_v1, prefix="/api/v1")
app.include_router(router=router_render)



app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

