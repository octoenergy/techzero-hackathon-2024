"""Main module for the SquidLink API."""

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from squidlink import models
from squidlink.database.database import get_db
from squidlink.database import queries
from squidlink.plots.viz_class import Facility as FacilityViz

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/projects")
def read_projects(db: Session = Depends(get_db)) -> list[models.ReadProject]:
    """Retrieve all projects."""
    return queries.get_projects(db)


@app.post("/project")
def create_project(project: models.WriteProject, db: Session = Depends(get_db)) -> models.ReadProject:
    """Creates a new Project."""
    return queries.create_project(db, project)


@app.get("/facility/{facility_id}")
def read_facility(facility_id: int, db: Session = Depends(get_db)) -> models.ReadFacility:
    """Retrieve a facility by ID."""
    facility = queries.get_facility(db, facility_id)
    if not facility:
        raise HTTPException(404)
    return facility


@app.post("/facility")
def create_facility(facility: models.WriteFacility, db: Session = Depends(get_db)) -> models.ReadFacility:
    """Create a new facility."""
    return queries.create_facility(db, facility)


@app.get("/contractor/{contractor_id}")
def read_contractor(contractor_id: int, db: Session = Depends(get_db)) -> models.ReadContractor:
    """Retrieve a contractor by ID."""
    contractor = queries.get_contractor(db, contractor_id)
    if not contractor:
        raise HTTPException(404)
    return contractor


@app.post("/contractor")
def create_contractor(contractor: models.WriteContractor, db: Session = Depends(get_db)) -> models.ReadContractor:
    """Create a new contractor."""
    return queries.create_contractor(db, contractor)


@app.get("/bids/{project_id}")
def read_bids(project_id: int, db: Session = Depends(get_db)) -> list[models.ReadBid]:
    """Retrieve all bids for a project."""
    bids = queries.get_bids(db, project_id)
    if bids is None:
        raise HTTPException(404)
    return bids


@app.post("/bid")
def create_bid(bid: models.WriteBid, db: Session = Depends(get_db)) -> models.ReadBid:
    """Create a new bid for a project."""
    return queries.create_bid(db, bid)


@app.get("/skills")
def read_skills(db: Session = Depends(get_db)) -> list[models.ReadSkill]:
    """Retrieve all skills."""
    return queries.get_skills(db)


@app.get("/skill/{skill_id}")
def read_skills(skill_id: int, db: Session = Depends(get_db)) -> models.ReadSkill:
    """Retrieve a skill by id."""
    skill = queries.get_skill(skill_id, db)
    if skill is None:
        raise HTTPException(404)
    return skill


@app.get("/facility/{facility_id}/avg-elec-data")
def read_facility_avg_elec(facility_id: int) -> str:
    """Retrieve a plot for a facility."""
    viz = FacilityViz(facility_id)
    return viz.viz_avg_elec_data()


@app.get("/facility/{facility_id}/avg-elec-and-carbon-data")
def read_facility_avg_elec_and_carbon(facility_id: int) -> str:
    """Retrieve a plot for a facility."""
    viz = FacilityViz(facility_id)
    return viz.viz_avg_elec_and_carbon_data()


@app.get("/facility/{facility_id}/overall-chart")
def read_facility_overall(facility_id: int) -> str:
    """Retrieve a plot for a facility."""
    viz = FacilityViz(facility_id)
    return viz.viz_overall_chart()
