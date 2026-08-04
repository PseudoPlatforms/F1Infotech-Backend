from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.query import Query
from app.schemas.query import QueryCreate, QueryResponse
from typing import List


router = APIRouter(
    prefix="/queries",
    tags=["Queries"]
)


@router.post("/", response_model=QueryResponse)
def create_query(data: QueryCreate, db: Session = Depends(get_db)):

    query = Query(
        first_name=data.first_name,
        last_name=data.last_name,
        email=data.email,
        phone=data.phone,
        company=data.company,
        message=data.message
    )

    db.add(query)
    db.commit()
    db.refresh(query)

    return query


@router.get("/", response_model=List[QueryResponse])
def get_all_queries(db: Session = Depends(get_db)):
    queries = db.query(Query).order_by(Query.id.desc()).all()
    return queries