from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, Depends, HTTPException, status
from jose import jwt
from passlib.context import CryptContext
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.admin import Admin


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


SECRET_KEY = "f1infotech-super-secret-key-change-this"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


password_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


class SignupRequest(BaseModel):
    name: str
    email: EmailStr
    password: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


def hash_password(password: str) -> str:
    return password_context.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:
    return password_context.verify(
        plain_password,
        hashed_password
    )


def create_access_token(data: dict) -> str:
    payload = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload.update({
        "exp": expire
    })

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


@router.post(
    "/signup",
    status_code=status.HTTP_201_CREATED
)
def signup(
    request: SignupRequest,
    db: Session = Depends(get_db)
):
    existing_admin = (
        db.query(Admin)
        .filter(Admin.email == request.email)
        .first()
    )

    if existing_admin:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="An account with this email already exists"
        )

    new_admin = Admin(
        full_name=request.name,
        email=request.email,
        password=hash_password(request.password)
    )

    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)

    return {
        "message": "Account created successfully",
        "user": {
            "id": new_admin.id,
            "name": new_admin.full_name,
            "email": new_admin.email
        }
    }


@router.post("/login")
def login(
    request: LoginRequest,
    db: Session = Depends(get_db)
):
    admin = (
        db.query(Admin)
        .filter(Admin.email == request.email)
        .first()
    )

    if not admin:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    if not verify_password(
        request.password,
        admin.password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    access_token = create_access_token({
        "sub": str(admin.id),
        "email": admin.email
    })

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "id": admin.id,
            "name": admin.full_name,
            "email": admin.email
        }
    }