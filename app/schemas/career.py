from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class CareerCreate(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    position: Optional[str] = None
    message: Optional[str] = None


class CareerResponse(CareerCreate):
    id: int

    class Config:
        from_attributes = True
class CareerResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str | None = None
    position: str | None = None
    message: str | None = None
    created_at: datetime

    class Config:
        from_attributes = True