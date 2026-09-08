import json
from typing import Any

from openai import AsyncOpenAI

from app.core.settings import settings
from app.models import DocumentByIdArgs
from app.tools import fetch_document_by_id, fetch_documents


TOOLS = [
    {
        "type": "function",
        "name": "search_documents",
        "description": (
            "List all available documents and their metadata. Use this first "
            "to decide which document best matches the user's question."
        ),
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False,
        },
        "strict": True,
    },
    {
        "type": "function",
        "name": "search_document_by_file_id",
        "description": (
            "Read the selected PDF and return the chunks most relevant to "
            "the user's question. Call this after search_documents."
        ),
        "parameters": DocumentByIdArgs.model_json_schema(),
        "strict": True,
    },
]


async def execute_tool(tool_call) -> dict[str, Any]:
    if tool_call.name == "search_documents":
        result = await fetch_documents()
    elif tool_call.name == "search_document_by_file_id":
        raw_arguments = json.loads(tool_call.arguments)
        arguments = DocumentByIdArgs.model_validate(raw_arguments)
        result = await fetch_document_by_id(arguments)
    else:
        raise ValueError(f"Unknown tool: {tool_call.name}")

    return {
        "type": "function_call_output",
        "call_id": tool_call.call_id,
        "output": json.dumps(result, default=str),
    }


async def asyncopenai(
    instructions: str,
    question: str,
    model: str = "gpt-5.5",
    retries: int = 5,
    timeout: float = 60.0,
):
    tool_instructions = f"""{instructions}

Use search_documents first to inspect the available document catalog. Select the
document whose metadata best matches the user's question. Then call
search_document_by_file_id with that document's ID and the user's original
question. Answer only from the relevant_chunks returned by that tool. If no
document or chunk contains the answer, say that the available documents do not
provide enough information. Never invent document content.
"""

    async with AsyncOpenAI(
        api_key=settings.openai_api_key,
        max_retries=retries,
        timeout=timeout,
    ) as client:
        response = await client.responses.create(
            model=model,
            instructions=tool_instructions,
            input=question,
            tools=TOOLS,
            tool_choice={"type": "function", "name": "search_documents"},
            parallel_tool_calls=False,
            max_output_tokens=500,
        )

        for _ in range(6):
            tool_calls = [
                item
                for item in response.output
                if item.type == "function_call"
            ]

            if not tool_calls:
                return {
                    "response": response.output_text,
                    "usage": response.usage,
                }

            tool_outputs = [
                await execute_tool(tool_call)
                for tool_call in tool_calls
            ]

            response = await client.responses.create(
                model=model,
                instructions=tool_instructions,
                previous_response_id=response.id,
                input=tool_outputs,
                tools=TOOLS,
                tool_choice="auto",
                parallel_tool_calls=False,
                max_output_tokens=500,
            )

    raise RuntimeError("The model exceeded the maximum number of tool turns")
