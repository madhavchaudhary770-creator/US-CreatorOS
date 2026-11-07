from datetime import datetime, timezone
from uuid import uuid4
from sqlalchemy import Boolean, DateTime, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from app.db import Base


class Project(Base):
    __tablename__ = "projects"
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid4()))
    title: Mapped[str] = mapped_column(String(160), nullable=False)
    format: Mapped[str] = mapped_column(String(16), default="short", nullable=False)
    niche: Mapped[str] = mapped_column(String(120), default="AI tools", nullable=False)
    audience: Mapped[str] = mapped_column(String(80), default="United States", nullable=False)
    status: Mapped[str] = mapped_column(String(24), default="idea", nullable=False)
    brief: Mapped[str] = mapped_column(Text, default="", nullable=False)
    script: Mapped[str] = mapped_column(Text, default="", nullable=False)
    approval_required: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
