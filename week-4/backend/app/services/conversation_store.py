import json
from datetime import UTC, datetime
from pathlib import Path
from uuid import UUID, uuid4

from app.schemas import ChatMessage, Conversation, ConversationSummary


class ConversationStore:
    def __init__(self, root: Path):
        self.root = root
        self.root.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def _validated_id(conversation_id: str) -> str:
        try:
            return str(UUID(conversation_id))
        except ValueError as error:
            raise FileNotFoundError("Conversation not found") from error

    def _directory(self, conversation_id: str) -> Path:
        return self.root / self._validated_id(conversation_id)

    def _metadata_path(self, conversation_id: str) -> Path:
        return self._directory(conversation_id) / "conversation.json"

    def create(self, filename: str, pdf_bytes: bytes) -> Conversation:
        conversation_id = str(uuid4())
        directory = self.root / conversation_id
        directory.mkdir(parents=True)
        stored_filename = "document.pdf"
        (directory / stored_filename).write_bytes(pdf_bytes)

        now = datetime.now(UTC)
        conversation = Conversation(
            id=conversation_id,
            document={
                "filename": filename,
                "stored_filename": stored_filename,
                "size": len(pdf_bytes),
            },
            created_at=now,
            updated_at=now,
        )
        self.save(conversation)
        return conversation

    def save(self, conversation: Conversation) -> None:
        directory = self._directory(conversation.id)
        directory.mkdir(parents=True, exist_ok=True)
        target = directory / "conversation.json"
        temporary = directory / "conversation.json.tmp"
        temporary.write_text(
            json.dumps(conversation.model_dump(mode="json"), indent=2),
            encoding="utf-8",
        )
        temporary.replace(target)

    def get(self, conversation_id: str) -> Conversation:
        path = self._metadata_path(conversation_id)
        if not path.is_file():
            raise FileNotFoundError("Conversation not found")
        return Conversation.model_validate_json(path.read_text(encoding="utf-8"))

    def pdf_path(self, conversation: Conversation) -> Path:
        path = self._directory(conversation.id) / conversation.document.stored_filename
        if not path.is_file():
            raise FileNotFoundError("Conversation PDF not found")
        return path

    def append_message(
        self,
        conversation: Conversation,
        role: str,
        text: str,
        citation: str | None = None,
    ) -> ChatMessage:
        message = ChatMessage(
            role=role,
            text=text,
            citation=citation,
            created_at=datetime.now(UTC),
        )
        conversation.messages.append(message)
        conversation.updated_at = message.created_at
        self.save(conversation)
        return message

    def list(self) -> list[ConversationSummary]:
        conversations: list[ConversationSummary] = []
        for path in self.root.glob("*/conversation.json"):
            try:
                conversation = Conversation.model_validate_json(path.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                continue
            conversations.append(ConversationSummary(
                id=conversation.id,
                filename=conversation.document.filename,
                created_at=conversation.created_at,
                updated_at=conversation.updated_at,
                message_count=len(conversation.messages),
            ))
        return sorted(conversations, key=lambda item: item.updated_at, reverse=True)
