# app/schemas/chat.py
from pydantic import BaseModel

class ChatRequest(BaseModel):
    instructions: str
    question: str

class ChatResponse(BaseModel):
    response: str