from .db import db
from sqlalchemy import Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

class ConsumerSite(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    business_id: Mapped[int] = mapped_column(ForeignKey("consumer_business.id"))
    site_type: Mapped[str]
    number_of_employees: Mapped[int]
    name: Mapped[str]
    