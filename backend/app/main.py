from fastapi import FastAPI

# This import looks unused, but it is what registers the tables on Base.metadata.
from app import models  # noqa: F401
from app.database import Base, engine

app = FastAPI(
    title="BMW Fleet & Service Tracker",
    description="Unofficial fan project. Not affiliated with BMW. Sample data.",
)

# TODO 1: create all tables that Base knows about.
#   hint: Base.metadata.create_all(bind=engine)

# TODO 2: GET /health that returns {"status": "ok"}
