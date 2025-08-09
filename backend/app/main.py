from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.router import router
from contextlib import asynccontextmanager

from app.db.init import create_db_and_tables


@asynccontextmanager
async def startup_event():
    if settings.env == "dev":
        create_db_and_tables()
    yield


app = FastAPI(title=settings.app_name,
              env=settings.env,
              lifespan=startup_event)

origins = settings.cors_origins or []
app.add_middleware(CORSMiddleware,
                   allow_origins=[*origins, '*'],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])

app.include_router(router)


@app.get("/", tags=["health"])
def health():
    return {"status": "ok"}
