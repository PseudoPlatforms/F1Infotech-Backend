from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from typing import Optional



class QueryCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: Optional[str] = None
    company: str
    message: str


class QueryResponse(QueryCreate):
    id: int

    class Config:
        from_attributes = True


class QueryCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: Optional[str] = None
    company: str
    message: str


class QueryResponse(QueryCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True