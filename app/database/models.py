from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime

from datetime import datetime

from app.database.database import Base


class Lead(Base):

    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100))

    email = Column(String(150))

    phone = Column(String(20))

    service = Column(String(200))

    created_at = Column(DateTime, default=datetime.utcnow)