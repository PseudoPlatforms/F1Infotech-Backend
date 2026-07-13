from app.database.database import SessionLocal
from app.database.models import Lead


def save_lead(name, email, phone, service):

    db = SessionLocal()

    try:

        lead = Lead(
            name=name,
            email=email,
            phone=phone,
            service=service
        )

        db.add(lead)
        db.commit()

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()