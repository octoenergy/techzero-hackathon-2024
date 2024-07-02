from .db import db
from sqlalchemy import Integer, String, Boolean, ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column

class SupplierConsumerTransaction(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    relationship_id: Mapped[int] = mapped_column(ForeignKey("supplier_consumer_partnerships.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("supplier_product.id"))
    product_count: Mapped[int]
    financing_type: Mapped[str]
    date_completed = mapped_column(Date())
    
    