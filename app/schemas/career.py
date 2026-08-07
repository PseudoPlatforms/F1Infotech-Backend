from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class CareerResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: Optional[str] = None
    position: Optional[str] = None
    experience: Optional[str] = None
    current_company: Optional[str] = None
    current_designation: Optional[str] = None
    notice_period: Optional[str] = None
    current_ctc: Optional[str] = None
    expected_ctc: Optional[str] = None
    message: Optional[str] = None
    resume_path: Optional[str] = None
    resume_filename: Optional[str] = None
    created_at: datetime
class CareerUpdate(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    position: Optional[str] = None
    experience: Optional[str] = None
    current_company: Optional[str] = None
    current_designation: Optional[str] = None
    notice_period: Optional[str] = None
    current_ctc: Optional[str] = None
    expected_ctc: Optional[str] = None
    message: Optional[str] = None
    class Config:
        from_attributes = True