from enum import Enum

from sqlalchemy import (
    Column,
    Enum as DbEnum,
    Integer,
    String,
    ForeignKey,
    Float,
    DateTime,
    Table,
    Boolean,
)
from sqlalchemy.orm import relationship, Session

from squidlink.database.database import Base


class FacilitySector(Enum):
    """Available facility sectors."""
    # TODO specify
    AGRICULTURE = "AGRICULTURE"
    COMMERCIAL = "COMMERCIAL"
    INDUSTRIAL = "INDUSTRIAL"
    RESIDENTIAL = "RESIDENTIAL"
    OTHER = "OTHER"


class Facility(Base):
    """SQL data model for a Facility."""
    __tablename__ = "facilities"

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String, nullable=False)

    address_line_1 = Column(String)
    address_line_2 = Column(String)
    address_postcode = Column(String)
    address_city = Column(String)
    address_country = Column(String)

    bms = Column(String)
    sector = Column(DbEnum(FacilitySector, nullable=False))
    floor_area_square_metres = Column(Integer)

    meter_readings = relationship("MeterReading", back_populates="facility")
    projects = relationship("Project", back_populates="facility")


class MeterReadingType(Enum):
    """Available meter reading types."""
    ELECTRICITY = "ELECTRICITY"
    GAS = "GAS"


class MeterReadingUnit(Enum):
    """Available meter reading units."""
    KWH = "KWH"


class MeterReadingDataSource(Enum):
    """Available meter reading data sources."""
    OCTOPUS_API = "OCTOPUS_API"


class MeterReading(Base):
    """SQL data model for a meter reading."""
    __tablename__ = "meter_readings"

    id = Column(Integer, nullable=False, primary_key=True)

    facility_id = Column(Integer, ForeignKey("facilities.id", ondelete="CASCADE"), nullable=False)
    facility = relationship(Facility, back_populates="meter_readings")

    data_source = Column(DbEnum(MeterReadingDataSource, nullable=False))
    type = Column(DbEnum(MeterReadingType, nullable=False))
    consumption = Column(Float, nullable=False)
    unit = Column(DbEnum(MeterReadingUnit, nullable=False))

    interval_start = Column(DateTime, nullable=False)
    interval_end = Column(DateTime, nullable=False)


contractors_skills_pivot = Table(
    'contractors_skills', Base.metadata,
    Column('contractor_id', Integer, ForeignKey('contractors.id'), primary_key=True),
    Column('skill_id', Integer, ForeignKey('skills.id'), primary_key=True)
)


projects_skills_pivot = Table(
    'projects_skills', Base.metadata,
    Column('project_id', Integer, ForeignKey('projects.id'), primary_key=True),
    Column('skill_id', Integer, ForeignKey('skills.id'), primary_key=True)
)


class Contractor(Base):
    """SQL data model for a Contractor."""
    __tablename__ = "contractors"

    id = Column(Integer, nullable=False, primary_key=True)

    skills = relationship("Skill", secondary=contractors_skills_pivot, back_populates='contractors')
    bids = relationship("Bid", back_populates='contractor')

    name = Column(String, nullable=False)
    address_line_1 = Column(String)
    address_line_2 = Column(String)
    address_postcode = Column(String)
    address_city = Column(String)
    address_country = Column(String)


class Skill(Base):
    """SQL data model for a Skill."""
    __tablename__ = "skills"

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String, nullable=False)

    contractors = relationship('Contractor', secondary=contractors_skills_pivot, back_populates='skills')
    projects = relationship('Project', secondary=projects_skills_pivot, back_populates='skills')


class Project(Base):
    """SQL data model for a Project."""
    __tablename__ = "projects"

    id = Column(Integer, nullable=False, primary_key=True)

    facility_id = Column(Integer, ForeignKey("facilities.id", ondelete="CASCADE"), nullable=False)
    facility = relationship(Facility, back_populates="projects")

    skills = relationship("Skill", secondary=projects_skills_pivot, back_populates="projects")
    bids = relationship("Bid", back_populates="project")

    name = Column(String, nullable=False)


class Bid(Base):
    """SQL data model for a Bid."""
    __tablename__ = "bids"

    id = Column(Integer, nullable=False, primary_key=True)

    contractor_id = Column(Integer, ForeignKey("contractors.id", ondelete="CASCADE"), nullable=False)
    contractor = relationship(Contractor, back_populates="bids")

    project_id = Column(Integer, ForeignKey("projects.id", ondelete="CASCADE"), nullable=False)
    project = relationship(Project, back_populates="bids")

    price = Column(Integer, nullable=False)
    duration = Column(Integer, nullable=False)
    site_inspection = Column(Boolean, nullable=False)
    estimated_savings = Column(Integer)
