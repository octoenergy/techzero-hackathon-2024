from .db import db
from sqlalchemy import Integer, String, Boolean, ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column

class SupplierConsumerPartnerships(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    supplier_id: Mapped[int] = mapped_column(ForeignKey("supplier_business.id"))
    consumer_id: Mapped[int] = mapped_column(ForeignKey("consumer_business.id"))
    relationship_start_date = mapped_column(Date())
    relationship_end_date = mapped_column(Date())
    relationship_state: Mapped[str]