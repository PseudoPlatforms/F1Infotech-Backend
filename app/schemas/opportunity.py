from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class OpportunityCreate(BaseModel):
    job_title: str
    department: Optional[str] = ""
    location: Optional[str] = ""
    experience: Optional[str] = ""
    employment_type: Optional[str] = ""
    salary: Optional[str] = ""
    description: Optional[str] = ""
    requirements: Optional[str] = ""


class OpportunityResponse(BaseModel):
    id: int
    job_title: str
    department: Optional[str] = None
    location: Optional[str] = None
    experience: Optional[str] = None
    employment_type: Optional[str] = None
    salary: Optional[str] = None
    description: Optional[str] = None
    requirements: Optional[str] = None
    status: Optional[str] = None
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True