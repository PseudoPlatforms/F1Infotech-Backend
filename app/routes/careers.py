from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.career import Career
from app.schemas.career import CareerCreate, CareerResponse
from typing import List


router = APIRouter(
    prefix="/careers",
    tags=["Careers"]
)


@router.post("/", response_model=CareerResponse)
def create_career(data: CareerCreate, db: Session = Depends(get_db)):

    career = Career(
        name=data.name,
        email=data.email,
        phone=data.phone,
        position=data.position,
        message=data.message
    )

    db.add(career)
    db.commit()
    db.refresh(career)

    return career

@router.get("/", response_model=List[CareerResponse])
def get_all_careers(db: Session = Depends(get_db)):
    careers = db.query(Career).order_by(Career.id.desc()).all()
    return careers