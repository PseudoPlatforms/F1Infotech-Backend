from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
from sqlalchemy.sql import func

from app.database.database import Base


class Career(Base):
    __tablename__ = "careers"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String(100),
        nullable=False
    )

    email = Column(
        String(150),
        nullable=False
    )

    phone = Column(
        String(20),
        nullable=True
    )

    position = Column(
        String(150),
        nullable=True
    )

    experience = Column(
        String(50),
        nullable=True
    )

    current_company = Column(
        String(200),
        nullable=True
    )

    current_designation = Column(
        String(200),
        nullable=True
    )

    notice_period = Column(
        String(50),
        nullable=True
    )

    current_ctc = Column(
        String(50),
        nullable=True
    )

    expected_ctc = Column(
        String(50),
        nullable=True
    )

    message = Column(
        Text,
        nullable=True
    )

    resume_path = Column(
        String(500),
        nullable=True
    )

    resume_filename = Column(
        String(255),
        nullable=True
    )

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )