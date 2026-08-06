from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from app.database.database import get_db
from app.models.recent_activity import RecentActivity
from app.schemas.recent_activity import (
    RecentActivityCreate,
    RecentActivityResponse
)

router = APIRouter(
    prefix="/recent-activities",
    tags=["Recent Activities"]
)


# -----------------------------
# login
# -----------------------------
@router.post("/login")
def admin_login(db: Session = Depends(get_db)):

    activity = RecentActivity(
        admin_id=1,
        module="Login",
        activity_type="LOGIN",
        reference_id=1,
        description="Administrator logged in"
    )

    db.add(activity)
    db.commit()

    return {
        "success": True,
        "message": "Login activity recorded"
    }



# -----------------------------
# logout
# -----------------------------
@router.post("/logout")
def admin_logout(db: Session = Depends(get_db)):

    activity = RecentActivity(
        admin_id=1,
        module="Login",
        activity_type="LOGOUT",
        reference_id=1,
        description="Administrator logged out"
    )

    db.add(activity)
    db.commit()

    return {
        "success": True,
        "message": "Logout activity recorded"
    }



# -----------------------------
# add opportunity
# -----------------------------
@router.post("/add-opportunity")
def add_opportunity_activity(
    opportunity_id: int,
    job_title: str,
    db: Session = Depends(get_db)
):

    activity = RecentActivity(
        admin_id=1,
        module="Opportunity",
        activity_type="ADD_OPPORTUNITY",
        reference_id=opportunity_id,
        description=f"Added opportunity '{job_title}'"
    )

    db.add(activity)
    db.commit()

    return {
        "success": True,
        "message": "Activity recorded"
    }



# -----------------------------
# delete opportunity
# -----------------------------
@router.post("/delete-opportunity")
def delete_opportunity_activity(
    opportunity_id: int,
    job_title: str,
    db: Session = Depends(get_db)
):

    activity = RecentActivity(
        admin_id=1,
        module="Opportunity",
        activity_type="DELETE_OPPORTUNITY",
        reference_id=opportunity_id,
        description=f"Deleted opportunity '{job_title}'"
    )

    db.add(activity)
    db.commit()

    return {
        "success": True,
        "message": "Activity recorded"
    }



# -----------------------------
# resolve query
# -----------------------------
@router.post("/resolve-query")
def resolve_query_activity(
    query_id: int,
    customer_name: str,
    db: Session = Depends(get_db)
):

    activity = RecentActivity(
        admin_id=1,
        module="Query",
        activity_type="RESOLVE_QUERY",
        reference_id=query_id,
        description=f"Resolved query from {customer_name}"
    )

    db.add(activity)
    db.commit()

    return {
        "success": True,
        "message": "Activity recorded"
    }



# -----------------------------
# Add Recent Activity
# -----------------------------
@router.post("/", response_model=RecentActivityResponse)
def add_recent_activity(
    data: RecentActivityCreate,
    db: Session = Depends(get_db)
):

    activity = RecentActivity(
        admin_id=data.admin_id,
        module=data.module,
        activity_type=data.activity_type,
        reference_id=data.reference_id,
        description=data.description
    )

    db.add(activity)
    db.commit()
    db.refresh(activity)

    return activity


# -----------------------------
# Get All Activities
# -----------------------------
@router.get("/")
def get_recent_activities(db: Session = Depends(get_db)):

    activities = (
        db.query(RecentActivity)
        .order_by(RecentActivity.created_at.desc())
        .all()
    )

    response = []

    now = datetime.now()

    for activity in activities:

        seconds = int((now - activity.created_at).total_seconds())

        if seconds < 60:
            time = f"{seconds} seconds ago"

        elif seconds < 3600:
            minutes = seconds // 60
            time = f"{minutes} minute{'s' if minutes != 1 else ''} ago"

        elif seconds < 86400:
            hours = seconds // 3600
            time = f"{hours} hour{'s' if hours != 1 else ''} ago"

        elif seconds < 2592000:
            days = seconds // 86400
            time = f"{days} day{'s' if days != 1 else ''} ago"

        elif seconds < 31536000:
            months = seconds // 2592000
            time = f"{months} month{'s' if months != 1 else ''} ago"

        else:
            years = seconds // 31536000
            time = f"{years} year{'s' if years != 1 else ''} ago"

        response.append({
            "id": activity.id,
            "admin_id": activity.admin_id,
            "module": activity.module,
            "activity_type": activity.activity_type,
            "reference_id": activity.reference_id,
            "description": activity.description,
            "created_at": activity.created_at,
            "time": time
        })

    return response


# -----------------------------
# Dashboard Latest Activities
# -----------------------------
@router.get("/latest")
def get_latest_activities(db: Session = Depends(get_db)):

    activities = (
        db.query(RecentActivity)
        .order_by(RecentActivity.created_at.desc())
        .limit(10)
        .all()
    )

    response = []

    now = datetime.now()

    for activity in activities:

        seconds = int((now - activity.created_at).total_seconds())

        if seconds < 60:
            time = f"{seconds} seconds ago"

        elif seconds < 3600:
            minutes = seconds // 60
            time = f"{minutes} minute{'s' if minutes != 1 else ''} ago"

        elif seconds < 86400:
            hours = seconds // 3600
            time = f"{hours} hour{'s' if hours != 1 else ''} ago"

        elif seconds < 2592000:
            days = seconds // 86400
            time = f"{days} day{'s' if days != 1 else ''} ago"

        elif seconds < 31536000:
            months = seconds // 2592000
            time = f"{months} month{'s' if months != 1 else ''} ago"

        else:
            years = seconds // 31536000
            time = f"{years} year{'s' if years != 1 else ''} ago"

        response.append({
            "id": activity.id,
            "module": activity.module,
            "activity_type": activity.activity_type,
            "description": activity.description,
            "time": time
        })

    return response