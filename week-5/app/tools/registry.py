from typing import Any, Awaitable, Callable

from app.models.tools import (
    LookupAccountArgs,
    SearchKnowledgeBaseArgs,
    SendMessageArgs,
)
from app.tools.sample_tools import (
    lookup_account,
    search_knowledge_base,
    send_message,
)

ToolHandler = Callable[[Any], Awaitable[Any]]

TOOL_REGISTRY: dict[str, ToolHandler] = {
    "search_knowledge_base": search_knowledge_base,
    "lookup_account": lookup_account,
    "send_message": send_message,
}

TOOL_ARGUMENT_MODELS = {
    "search_knowledge_base": SearchKnowledgeBaseArgs,
    "lookup_account": LookupAccountArgs,
    "send_message": SendMessageArgs,
}

SENSITIVE_TOOLS = {
    "send_message",
}

TOOL_SCHEMAS = [
    {
        "type": "function",
        "name": "search_knowledge_base",
        "description": "Search internal documents or notes.",
        "parameters": SearchKnowledgeBaseArgs.model_json_schema(),
        "strict": False,
    },
    {
        "type": "function",
        "name": "lookup_account",
        "description": "Look up account details by account id.",
        "parameters": LookupAccountArgs.model_json_schema(),
        "strict": False,
    },
    {
        "type": "function",
        "name": "send_message",
        "description": "Send a message. This requires human approval.",
        "parameters": SendMessageArgs.model_json_schema(),
        "strict": False,
    },
]
