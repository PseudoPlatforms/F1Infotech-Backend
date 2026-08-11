from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.chat import router as chat_router
from app.routes import recent_activities

from app.database.database import Base, engine
from app.database.models import Lead

from app.routes.careers import router as careers_router
from app.routes.queries import router as queries_router
from app.models.query import Query
from app.routes.opportunity import router as opportunities_router

from app.models.admin import Admin
from app.routes.auth import router as auth_router
from fastapi.staticfiles import StaticFiles
from pathlib import Path


# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(title="F1 InfoTech Chatbot")
UPLOAD_DIRECTORY = Path("uploads")
UPLOAD_DIRECTORY.mkdir(parents=True, exist_ok=True)

app.mount(
    "/uploads",
    StaticFiles(directory=str(UPLOAD_DIRECTORY)),
    name="uploads"
)


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==============================
# ROUTES
# ==============================

app.include_router(chat_router)

app.include_router(careers_router)

app.include_router(queries_router)

app.include_router(opportunities_router)

app.include_router(auth_router)

# IMPORTANT: Recent Activities
app.include_router(recent_activities.router)


# ==============================
# HOME
# ==============================

@app.get("/")
def home():
    return {
        "message": "Chatbot Running Successfully"
    }