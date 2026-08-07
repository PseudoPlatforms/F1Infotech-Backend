from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class QueryCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: Optional[str] = None
    company: str
    message: str


class QueryResponse(QueryCreate):
    id: int
    status: str
    created_at: datetime

    class Config:
        from_attributes = True