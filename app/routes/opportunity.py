from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database.database import get_db
from app.models.opportunity import Opportunity
from app.schemas.opportunity import (
    OpportunityCreate,
    OpportunityResponse
)


router = APIRouter(
    prefix="/opportunities",
    tags=["Opportunities"]
)


# =========================================================
# CREATE OPPORTUNITY
# =========================================================

@router.post(
    "/",
    response_model=OpportunityResponse
)
def create_opportunity(
    data: OpportunityCreate,
    db: Session = Depends(get_db)
):

    opportunity = Opportunity(
        **data.model_dump()
    )

    db.add(opportunity)
    db.commit()
    db.refresh(opportunity)

    return opportunity


# =========================================================
# GET ALL OPPORTUNITIES
# Admin panel
# =========================================================

@router.get(
    "/",
    response_model=List[OpportunityResponse]
)
def get_opportunities(
    db: Session = Depends(get_db)
):

    return (
        db.query(Opportunity)
        .order_by(Opportunity.created_at.desc())
        .all()
    )


# =========================================================
# GET SINGLE OPPORTUNITY
# =========================================================

@router.get(
    "/{opportunity_id}",
    response_model=OpportunityResponse
)
def get_opportunity(
    opportunity_id: int,
    db: Session = Depends(get_db)
):

    opportunity = (
        db.query(Opportunity)
        .filter(Opportunity.id == opportunity_id)
        .first()
    )

    if not opportunity:
        raise HTTPException(
            status_code=404,
            detail="Opportunity not found."
        )

    return opportunity


# =========================================================
# UPDATE OPPORTUNITY
# =========================================================

@router.put(
    "/{opportunity_id}",
    response_model=OpportunityResponse
)
def update_opportunity(
    opportunity_id: int,
    data: OpportunityCreate,
    db: Session = Depends(get_db)
):

    opportunity = (
        db.query(Opportunity)
        .filter(Opportunity.id == opportunity_id)
        .first()
    )

    if not opportunity:
        raise HTTPException(
            status_code=404,
            detail="Opportunity not found."
        )

    opportunity.job_title = data.job_title
    opportunity.department = data.department
    opportunity.location = data.location
    opportunity.experience = data.experience
    opportunity.employment_type = data.employment_type
    opportunity.salary = data.salary
    opportunity.description = data.description
    opportunity.requirements = data.requirements

    db.commit()
    db.refresh(opportunity)

    return opportunity


# =========================================================
# DELETE OPPORTUNITY
# =========================================================

@router.delete("/{opportunity_id}")
def delete_opportunity(
    opportunity_id: int,
    db: Session = Depends(get_db)
):

    opportunity = (
        db.query(Opportunity)
        .filter(Opportunity.id == opportunity_id)
        .first()
    )

    if not opportunity:
        raise HTTPException(
            status_code=404,
            detail="Opportunity not found."
        )

    db.delete(opportunity)
    db.commit()

    return {
        "message": "Opportunity deleted successfully."
    }