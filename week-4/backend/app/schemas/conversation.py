from datetime import datetime

from pydantic import BaseModel, Field


class DocumentInfo(BaseModel):
    filename: str
    stored_filename: str
    size: int


class ChatMessage(BaseModel):
    role: str = Field(pattern="^(user|assistant)$")
    text: str
    created_at: datetime
    citation: str | None = None


class Conversation(BaseModel):
    id: str
    document: DocumentInfo
    created_at: datetime
    updated_at: datetime
    messages: list[ChatMessage] = Field(default_factory=list)


class ConversationSummary(BaseModel):
    id: str
    filename: str
    created_at: datetime
    updated_at: datetime
    message_count: int


class MessageRequest(BaseModel):
    message: str = Field(min_length=1, max_length=8000)
