import asyncio
import os
from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock, patch


# Settings are created when the service module is imported. Unit tests use a
# placeholder because the OpenAI clients themselves are mocked below.
os.environ.setdefault("OPENAI_API_KEY", "test-api-key")

from app.services.openai_service import asyncopenai, clientopenai


class FakeAsyncStream:
    def __init__(self, events):
        self._events = iter(events)

    def __aiter__(self):
        return self

    async def __anext__(self):
        try:
            return next(self._events)
        except StopIteration:
            raise StopAsyncIteration


def test_asyncopenai_calls_client_and_combines_streamed_text():
    usage = SimpleNamespace(total_tokens=7)
    stream = FakeAsyncStream(
        [
            SimpleNamespace(type="response.output_text.delta", delta="Hello"),
            SimpleNamespace(type="response.output_text.delta", delta=" world"),
            SimpleNamespace(
                type="response.completed",
                response=SimpleNamespace(usage=usage),
            ),
        ]
    )
    mock_client = MagicMock()
    mock_client.responses.create = AsyncMock(return_value=stream)

    with patch("app.services.openai_service.AsyncOpenAI", return_value=mock_client):
        result = asyncio.run(
            asyncopenai(
                "Be concise.",
                "Say hello.",
                model="test-model",
                retries=1,
                timeout=2.0,
            )
        )

    assert result == {"response": "Hello world", "usage": usage}
    mock_client.responses.create.assert_called_once_with(
        model="test-model",
        instructions="Be concise.",
        input="Say hello.",
        stream=True,
        max_output_tokens=500,
    )


def test_clientopenai_calls_client_and_prints_each_stream_event():
    events = [
        SimpleNamespace(type="response.output_text.delta", delta="Hello"),
        SimpleNamespace(type="response.completed"),
    ]
    mock_client = MagicMock()
    mock_client.responses.create.return_value = events

    with (
        patch("app.services.openai_service.OpenAI", return_value=mock_client),
        patch("builtins.print") as mock_print,
    ):
        result = clientopenai(
            "Be concise.",
            "Say hello.",
            model="test-model",
            retries=1,
            timeout=2.0,
        )

    assert result is None
    mock_client.responses.create.assert_called_once_with(
        model="test-model",
        instructions="Be concise.",
        input="Say hello.",
        stream=True,
        max_output_tokens=500,
    )
    assert mock_print.call_args_list == [
        ((events[0],), {}),
        ((events[1],), {}),
    ]
