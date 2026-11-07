from datetime import datetime
from typing import Literal
from pydantic import BaseModel, Field


class ProjectCreate(BaseModel):
    title: str = Field(min_length=1, max_length=160)
    format: Literal["short", "long"] = "short"
    niche: str = Field(default="AI tools", max_length=120)
    audience: str = Field(default="United States", max_length=80)
    brief: str = Field(default="", max_length=5000)


class ProjectUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=160)
    status: Literal["idea", "research", "script", "production", "review", "approved"] | None = None
    brief: str | None = Field(default=None, max_length=5000)
    script: str | None = Field(default=None, max_length=20000)


class ProjectRead(BaseModel):
    id: str
    title: str
    format: str
    niche: str
    audience: str
    status: str
    brief: str
    script: str
    approval_required: bool
    created_at: datetime

    model_config = {"from_attributes": True}
