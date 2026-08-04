from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func

from app.database.database import Base


class Opportunity(Base):

    __tablename__ = "opportunities"

    id = Column(Integer, primary_key=True, index=True)

    job_title = Column(String(255), nullable=False)

    department = Column(String(255), nullable=False)

    location = Column(String(255), nullable=False)

    experience = Column(String(100))

    employment_type = Column(String(100))

    salary = Column(String(100))

    description = Column(Text)

    requirements = Column(Text)

    status = Column(String(50), default="Active")

    created_at = Column(DateTime(timezone=True), server_default=func.now())