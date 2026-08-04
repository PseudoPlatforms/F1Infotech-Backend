from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class OpportunityCreate(BaseModel):

    job_title: str

    department: str

    location: str

    experience: Optional[str] = None

    employment_type: Optional[str] = None

    salary: Optional[str] = None

    description: Optional[str] = None

    requirements: Optional[str] = None


class OpportunityResponse(OpportunityCreate):

    id: int

    status: str

    created_at: datetime

    class Config:

        from_attributes = True