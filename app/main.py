from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.chat import router as chat_router

from app.database.database import Base, engine
from app.database.models import Lead

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="F1 InfoTech Chatbot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)


@app.get("/")
def home():
    return {
        "message": "Chatbot Running Successfully"
    }