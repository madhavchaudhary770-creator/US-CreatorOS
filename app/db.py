from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from app.config import settings

cfg = settings()
if cfg.database_url.startswith("sqlite:///"):
    db_path = cfg.database_url.removeprefix("sqlite:///")
    if db_path != ":memory:":
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)
kwargs = {"connect_args": {"check_same_thread": False}} if cfg.database_url.startswith("sqlite") else {}
engine = create_engine(cfg.database_url, future=True, pool_pre_ping=True, **kwargs)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
