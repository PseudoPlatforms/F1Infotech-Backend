from fastapi import APIRouter
from app.models.chat_models import ChatRequest
from app.services.conversation_engine import process_message

router = APIRouter()

@router.post("/chat")
def chat(request: ChatRequest):

    return process_message(
        request.session_id,
        request.message
    )