from .db import db
from sqlalchemy import Integer, String, Boolean, ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column

class AuditOutcome(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    consumer_id: Mapped[int] = mapped_column(ForeignKey("consumer_business.id"))
    audit_date = mapped_column(Date())
    score: Mapped[int]