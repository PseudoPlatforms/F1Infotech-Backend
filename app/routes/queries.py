from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database.database import get_db
from app.models.query import Query
from app.schemas.query import (
    QueryCreate,
    QueryUpdate,
    QueryResponse
)


router = APIRouter(
    prefix="/queries",
    tags=["Queries"]
)


# =========================================================
# CREATE QUERY
# =========================================================

@router.post("/", response_model=QueryResponse)
def create_query(
    data: QueryCreate,
    db: Session = Depends(get_db)
):

    query = Query(
        first_name=data.first_name,
        last_name=data.last_name,
        email=data.email,
        phone=data.phone,
        company=data.company,
        message=data.message,
        status="pending"
    )

    db.add(query)
    db.commit()
    db.refresh(query)

    return query


# =========================================================
# GET ALL QUERIES
# =========================================================

@router.get("/", response_model=List[QueryResponse])
def get_all_queries(
    db: Session = Depends(get_db)
):

    queries = (
        db.query(Query)
        .order_by(Query.id.desc())
        .all()
    )

    return queries


# =========================================================
# GET SINGLE QUERY / VIEW QUERY
# =========================================================

@router.get("/{query_id}", response_model=QueryResponse)
def get_query_by_id(
    query_id: int,
    db: Session = Depends(get_db)
):

    query = (
        db.query(Query)
        .filter(Query.id == query_id)
        .first()
    )

    if not query:
        raise HTTPException(
            status_code=404,
            detail="Query not found"
        )

    return query


# =========================================================
# UPDATE QUERY / EDIT QUERY
# =========================================================

@router.put("/{query_id}", response_model=QueryResponse)
def update_query(
    query_id: int,
    data: QueryUpdate,
    db: Session = Depends(get_db)
):

    query = (
        db.query(Query)
        .filter(Query.id == query_id)
        .first()
    )

    if not query:
        raise HTTPException(
            status_code=404,
            detail="Query not found"
        )

    update_data = data.model_dump(
        exclude_unset=True
    )

    # Validate status if frontend sends status
    if "status" in update_data:

        status = update_data["status"]

        if status is not None:

            status = status.strip().lower()

            if status not in [
                "pending",
                "resolved"
            ]:
                raise HTTPException(
                    status_code=400,
                    detail="Invalid status"
                )

            update_data["status"] = status


    # Update only fields received from frontend
    for field, value in update_data.items():
        setattr(query, field, value)


    db.commit()
    db.refresh(query)

    return query


# =========================================================
# UPDATE QUERY STATUS
# =========================================================

@router.put("/{query_id}/status")
def update_query_status(
    query_id: int,
    status: str,
    db: Session = Depends(get_db)
):

    query = (
        db.query(Query)
        .filter(Query.id == query_id)
        .first()
    )

    if not query:
        raise HTTPException(
            status_code=404,
            detail="Query not found"
        )


    status = status.strip().lower()


    if status not in [
        "pending",
        "resolved"
    ]:

        raise HTTPException(
            status_code=400,
            detail="Invalid status"
        )


    query.status = status

    db.commit()
    db.refresh(query)


    return {
        "message": "Status updated successfully",
        "id": query.id,
        "status": query.status
    }


# =========================================================
# DELETE QUERY
# =========================================================

@router.delete("/{query_id}")
def delete_query(
    query_id: int,
    db: Session = Depends(get_db)
):

    query = (
        db.query(Query)
        .filter(Query.id == query_id)
        .first()
    )


    if not query:
        raise HTTPException(
            status_code=404,
            detail="Query not found"
        )


    db.delete(query)
    db.commit()


    return {
        "message": "Query deleted successfully",
        "id": query_id
    }