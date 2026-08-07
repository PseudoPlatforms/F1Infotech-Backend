from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func

from app.database.database import Base


class RecentActivity(Base):
    __tablename__ = "recent_activity"

    id = Column(Integer, primary_key=True, index=True)
    admin_id = Column(Integer, nullable=False)
    module = Column(String(100), nullable=False)
    activity_type = Column(String(100), nullable=False)
    reference_id = Column(Integer, nullable=True)
    description = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())