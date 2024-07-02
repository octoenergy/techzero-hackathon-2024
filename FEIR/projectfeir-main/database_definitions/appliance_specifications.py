from .db import db
from sqlalchemy import Integer, String, Boolean, ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column

class ApplianceSpecifications(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    brand: Mapped[str]
    model_name: Mapped[str]
    product_type: Mapped[str]
    energy_consumption: Mapped[int]
    energy_consumption_units: Mapped[str]
    capacity: Mapped[int]
    capacity_units: Mapped[str]
    