from .db import db
from sqlalchemy import Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

class ConsumerBusiness(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    business_type: Mapped[str]
    name: Mapped[str]
    
    