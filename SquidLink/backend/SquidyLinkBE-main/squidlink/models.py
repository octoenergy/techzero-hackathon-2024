from datetime import datetime

from pydantic import BaseModel

from squidlink.database.models import (
    FacilitySector,
    MeterReadingType,
    MeterReadingUnit,
    MeterReadingDataSource
)


class ReadFacility(BaseModel):
    id: int
    name: str

    address_line_1: str | None
    address_line_2: str | None
    address_postcode: str | None
    address_city: str | None
    address_country: str | None

    bms: str | None
    sector: FacilitySector
    floor_area_square_metres: int | None

    class Config:
        orm_mode = True
        from_attributes = True


class WriteFacility(BaseModel):
    name: str

    address_line_1: str | None
    address_line_2: str | None
    address_postcode: str | None
    address_city: str | None
    address_country: str | None

    bms: str | None
    sector: FacilitySector
    floor_area_square_metres: int | None

    class Config:
        orm_mode = True


class ReadSkill(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class ReadContractor(BaseModel):
    id: int
    name: str

    address_line_1: str | None
    address_line_2: str | None
    address_postcode: str | None
    address_city: str | None
    address_country: str | None

    class Config:
        orm_mode = True


class WriteContractor(BaseModel):
    name: str
    address_line_1: str | None
    address_line_2: str | None
    address_postcode: str | None
    address_city: str | None
    address_country: str | None

    skills: list[int]

    class Config:
        orm_mode = True


class ReadProject(BaseModel):
    """Pydantic model for reading a Project."""
    id: int
    name: str

    facility_id: int

    class Config:
        orm_mode = True


class WriteProject(BaseModel):
    """Pydantic model for writing a Project."""
    name: str
    facility_id: int

    skills: list[int]

    class Config:
        orm_mode = True


class ReadBid(BaseModel):
    """Pydantic model for reading a Bid."""
    id: int

    contractor_id: int
    project_id: int

    price: int
    duration: int
    site_inspection: bool
    estimated_savings: int | None

    class Config:
        orm_mode = True


class WriteBid(BaseModel):
    """Pydantic model for writing a Bid."""
    contractor_id: int
    project_id: int

    price: int
    duration: int
    site_inspection: bool
    estimated_savings: int | None

    class Config:
        orm_mode = True


class ReadMeterReading(BaseModel):
    id: int

    facility_id: int

    data_source: MeterReadingDataSource
    type: MeterReadingType
    consumption: float
    unit: MeterReadingUnit

    interval_start: datetime
    interval_end: datetime

    class Config:
        orm_mode = True


class ReadSkill(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
