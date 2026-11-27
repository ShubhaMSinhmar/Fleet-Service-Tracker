from fastapi import FastAPI

from app import models  # noqa: F401
from app.database import Base, engine
from app.routers import auth

app = FastAPI(
    title="BMW Fleet & Service Tracker",
    description="Unofficial fan project. Not affiliated with BMW. Sample data.",
)
app.include_router(auth.router)

Base.metadata.create_all(bind=engine)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
