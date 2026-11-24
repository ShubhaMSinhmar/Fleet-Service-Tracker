from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from app.config import get_settings

settings = get_settings()


class Base(DeclarativeBase):
    """Every model inherits from this; Base.metadata knows all the tables."""


# TODO 1: build connect_args.
#   SQLite needs {"check_same_thread": False} (FastAPI may use another thread per request).
#   Any other database needs {}.
#   hint: settings.database_url.startswith("sqlite")

# TODO 2: engine = create_engine(settings.database_url, connect_args=...)

# TODO 3: SessionLocal = sessionmaker(bind=engine, autoflush=False)


# TODO 4: a FastAPI dependency that gives one session per request and always closes it.
#   hint: create SessionLocal(), `yield` it inside try, close it in finally.
def get_db() -> Generator[Session, None, None]: ...
