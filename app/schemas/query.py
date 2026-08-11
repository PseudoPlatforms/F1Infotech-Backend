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


class QueryUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    company: Optional[str] = None
    message: Optional[str] = None
    status: Optional[str] = None


class QueryResponse(QueryCreate):
    id: int
    status: str
    created_at: datetime

    class Config:
        from_attributes = True