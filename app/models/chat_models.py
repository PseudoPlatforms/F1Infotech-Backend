from pydantic import BaseModel

class ChatRequest(BaseModel):
    session_id: str
    message: str


class ChatResponse(BaseModel):
    message: str
    options: list[str]
    state: str
    input_type: str