from .db import db
from sqlalchemy import Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

class SupplierProduct(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    manufacturer_id: Mapped[int] = mapped_column(ForeignKey("supplier_business.id"))
    product_name: Mapped[str]
    product_type: Mapped[str]
    units_available: Mapped[int]
    units_consumed: Mapped[int]
    normal_cost: Mapped[int]
    financing_type_available: Mapped[str]