from pathlib import Path
from shutil import copyfileobj
from typing import List
from uuid import uuid4

from fastapi import (
    APIRouter,
    Depends,
    File,
    Form,
    HTTPException,
    UploadFile,
    status,
)
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.career import Career
from app.schemas.career import CareerResponse, CareerUpdate

router = APIRouter(
    prefix="/careers",
    tags=["Careers"]
)


# Resume upload directory
RESUME_DIRECTORY = Path("uploads/resumes")

RESUME_DIRECTORY.mkdir(
    parents=True,
    exist_ok=True
)


ALLOWED_RESUME_EXTENSIONS = {
    ".pdf",
    ".doc",
    ".docx"
}

MAX_RESUME_SIZE = 5 * 1024 * 1024


@router.post(
    "/",
    response_model=CareerResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_career(
    name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(""),
    position: str = Form(""),
    experience: str = Form(""),
    current_company: str = Form(""),
    current_designation: str = Form(""),
    notice_period: str = Form(""),
    current_ctc: str = Form(""),
    expected_ctc: str = Form(""),
    message: str = Form(""),
    resume: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    original_filename = resume.filename or ""

    file_extension = Path(
        original_filename
    ).suffix.lower()

    if file_extension not in ALLOWED_RESUME_EXTENSIONS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=(
                "Only PDF, DOC and DOCX resume files "
                "are allowed."
            )
        )

    await resume.seek(0)

    file_content = await resume.read()

    if len(file_content) > MAX_RESUME_SIZE:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Resume size must not exceed 5 MB."
        )

    unique_filename = (
        f"{uuid4().hex}{file_extension}"
    )

    resume_file_path = (
        RESUME_DIRECTORY /
        unique_filename
    )

    try:
        with resume_file_path.open("wb") as output_file:
            output_file.write(file_content)

        career = Career(
            name=name.strip(),
            email=email.strip(),
            phone=phone.strip() or None,
            position=position.strip() or None,
            experience=experience.strip() or None,
            current_company=(
                current_company.strip() or None
            ),
            current_designation=(
                current_designation.strip() or None
            ),
            notice_period=(
                notice_period.strip() or None
            ),
            current_ctc=(
                current_ctc.strip() or None
            ),
            expected_ctc=(
                expected_ctc.strip() or None
            ),
            message=message.strip() or None,
            resume_path=str(resume_file_path),
            resume_filename=original_filename
        )

        db.add(career)
        db.commit()
        db.refresh(career)

        return career

    except Exception as error:
        db.rollback()

        if resume_file_path.exists():
            resume_file_path.unlink()

        print(
            "Career application error:",
            repr(error)
        )

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to save career application."
        ) from error

    finally:
        await resume.close()


@router.get(
    "/",
    response_model=List[CareerResponse]
)
def get_all_careers(
    db: Session = Depends(get_db)
):
    return (
        db.query(Career)
        .order_by(Career.id.desc())
        .all()
    )


# =========================================================
# UPDATE CAREER APPLICATION
# =========================================================

@router.put(
    "/{career_id}",
    response_model=CareerResponse
)
def update_career(
    career_id: int,
    data: CareerUpdate,
    db: Session = Depends(get_db)
):
    career = (
        db.query(Career)
        .filter(Career.id == career_id)
        .first()
    )

    if not career:
        raise HTTPException(
            status_code=404,
            detail="Career application not found."
        )

    career.name = data.name
    career.email = data.email
    career.phone = data.phone
    career.position = data.position
    career.experience = data.experience
    career.current_company = data.current_company
    career.current_designation = data.current_designation
    career.notice_period = data.notice_period
    career.current_ctc = data.current_ctc
    career.expected_ctc = data.expected_ctc
    career.message = data.message

    db.commit()
    db.refresh(career)

    return career