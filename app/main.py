from contextlib import asynccontextmanager
from pathlib import Path
from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.config import settings
from app.db import Base, engine, get_db
from app.models import Project
from app.schemas import ProjectCreate, ProjectRead, ProjectUpdate


@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title=settings().app_name, version="0.1.0", lifespan=lifespan)


@app.get("/", include_in_schema=False)
def dashboard():
    return FileResponse(Path(__file__).parent / "static" / "index.html")


@app.get("/static/{asset}", include_in_schema=False)
def static_asset(asset: str):
    if asset not in {"style.css", "app.js"}:
        raise HTTPException(status_code=404, detail="Asset not found")
    return FileResponse(Path(__file__).parent / "static" / asset)


@app.get("/api/health")
def health():
    return {"status": "ok", "app": settings().app_name, "version": "0.1.0"}


@app.get("/api/projects", response_model=list[ProjectRead])
def list_projects(db: Session = Depends(get_db)):
    return list(db.scalars(select(Project).order_by(Project.created_at.desc())).all())


@app.post("/api/projects", response_model=ProjectRead, status_code=201)
def create_project(payload: ProjectCreate, db: Session = Depends(get_db)):
    item = Project(**payload.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@app.get("/api/projects/{project_id}", response_model=ProjectRead)
def get_project(project_id: str, db: Session = Depends(get_db)):
    item = db.get(Project, project_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return item


@app.patch("/api/projects/{project_id}", response_model=ProjectRead)
def update_project(project_id: str, payload: ProjectUpdate, db: Session = Depends(get_db)):
    item = db.get(Project, project_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Project not found")
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item


@app.get("/api/publishing/policy")
def publishing_policy():
    return {"publishing_enabled": False, "default_visibility": "private", "human_approval_required": True}
