from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database.database import get_db
from app.models.opportunity import Opportunity
from app.schemas.opportunity import OpportunityCreate, OpportunityResponse

router = APIRouter(
    prefix="/opportunities",
    tags=["Opportunities"]
)

# POST API
@router.post("/", response_model=OpportunityResponse)
def create_opportunity(
    data: OpportunityCreate,
    db: Session = Depends(get_db)
):

    opportunity = Opportunity(**data.model_dump())

    db.add(opportunity)
    db.commit()
    db.refresh(opportunity)

    return opportunity


# GET API
@router.get("/")
def get_opportunities(db: Session = Depends(get_db)):
    return (
        db.query(Opportunity)
        .filter(Opportunity.status == "Active")
        .order_by(Opportunity.created_at.desc())
        .all()
    )