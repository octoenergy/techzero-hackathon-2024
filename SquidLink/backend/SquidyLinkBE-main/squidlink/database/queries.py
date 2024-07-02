from sqlalchemy.orm import Session

from squidlink.database import models as db_models
from squidlink import models


def get_projects(db: Session) -> list[db_models.Project]:
    """Retrieve all projects."""
    return db.query(db_models.Project).all()


def create_project(db: Session, project_data: models.WriteProject) -> models.ReadProject:
    skills = [
        db.query(db_models.Skill).get(skill_id) for skill_id in project_data.skills
    ]
    project = db_models.Project(
        name=project_data.name,
        facility_id=project_data.facility_id,
    )
    project.skills = skills
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


def get_facility(db: Session, facility_id: int) -> db_models.Facility | None:
    return db.query(db_models.Facility).filter(db_models.Facility.id == facility_id).first()


def create_facility(db: Session, facility_data: models.WriteFacility) -> models.ReadFacility:
    facility = db_models.Facility(
        name=facility_data.name,
        address_line_1=facility_data.address_line_1,
        address_line_2=facility_data.address_line_2,
        address_postcode=facility_data.address_postcode,
        address_city=facility_data.address_city,
        address_country=facility_data.address_country,
        bms=facility_data.bms,
        sector=db_models.FacilitySector.AGRICULTURE,
        floor_area_square_metres=facility_data.floor_area_square_metres,
    )
    db.add(facility)
    db.commit()
    db.refresh(facility)
    return facility


def get_contractor(db: Session, contractor_id: int) -> models.ReadContractor | None:
    return db.query(db_models.Contractor).filter(db_models.Contractor.id == contractor_id).first()


def create_contractor(db: Session, contractor_data: models.WriteContractor) -> models.ReadContractor:
    skills = [
        db.query(db_models.Skill).get(skill_id) for skill_id in contractor_data.skills
    ]
    contractor = db_models.Contractor(
        name=contractor_data.name,
        address_line_1=contractor_data.address_line_1,
        address_line_2=contractor_data.address_line_2,
        address_postcode=contractor_data.address_postcode,
        address_city=contractor_data.address_city,
        address_country=contractor_data.address_country,
    )
    contractor.skills = skills
    db.add(contractor)
    db.commit()
    db.refresh(contractor)
    return contractor


def get_bids(db: Session, project_id: int) -> list[models.ReadBid] | None:
    project = db.query(db_models.Project).get(project_id)
    if not project:
        return None
    return db.query(db_models.Bid).filter(db_models.Bid.project_id == project_id).all()


def create_bid(db: Session, bid_data: models.WriteBid) -> models.ReadBid:
    bid = db_models.Bid(
        project_id=bid_data.project_id,
        contractor_id=bid_data.contractor_id,
        price=bid_data.price,
        duration=bid_data.duration,
        site_inspection=bid_data.site_inspection,
        estimated_savings=bid_data.estimated_savings,
    )
    db.add(bid)
    db.commit()
    db.refresh(bid)
    return bid


def get_skills(db: Session) -> list[models.ReadSkill]:
    skills = db.query(db_models.Skill).all()
    return skills


def get_skill(skill_id: int, db: Session) -> models.ReadSkill | None:
    return db.query(db_models.Skill).get(skill_id)
