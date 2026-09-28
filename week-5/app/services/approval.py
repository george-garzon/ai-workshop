from app.models.agent import ToolCall
from app.tools.registry import SENSITIVE_TOOLS


def requires_human_approval(tool_call: ToolCall) -> bool:
    return tool_call.name in SENSITIVE_TOOLS


async def request_human_approval(tool_call: ToolCall) -> bool:
    raise NotImplementedError("Implement human approval.")
