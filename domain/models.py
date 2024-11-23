from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column
from database import db
from datetime import datetime

class History(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    tool: Mapped[str] = mapped_column(String(255))
    input: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(DateTime)
