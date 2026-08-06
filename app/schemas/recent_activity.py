from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class RecentActivityCreate(BaseModel):
    admin_id: int
    module: str
    activity_type: str
    reference_id: Optional[int] = None
    description: str


class RecentActivityResponse(RecentActivityCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True