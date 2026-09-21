from pathlib import Path

from app.services.conversation_store import ConversationStore
from app.services.openai_service import _response_input


def test_conversation_round_trip_and_openai_input(tmp_path: Path) -> None:
    store = ConversationStore(tmp_path)
    pdf_bytes = b"%PDF-1.4\nworkshop fixture"
    conversation = store.create("handbook.pdf", pdf_bytes)

    store.append_message(conversation, "user", "What is the policy?")
    store.append_message(
        conversation,
        "assistant",
        "The policy is described on page 2.",
        citation="handbook.pdf",
    )

    restored = store.get(conversation.id)
    assert restored.document.filename == "handbook.pdf"
    assert [message.role for message in restored.messages] == ["user", "assistant"]
    assert store.pdf_path(restored).read_bytes() == pdf_bytes
    assert store.list()[0].message_count == 2

    response_input = _response_input(restored, store.pdf_path(restored))
    file_part = response_input[0]["content"][0]
    assert file_part["type"] == "input_file"
    assert file_part["filename"] == "handbook.pdf"
    assert file_part["file_data"].startswith("data:application/pdf;base64,")
    assert response_input[-1] == {
        "role": "assistant",
        "content": "The policy is described on page 2.",
    }
