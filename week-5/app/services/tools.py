from app.models.agent import ToolCall, ToolExecutionResult
from app.tools.registry import TOOL_ARGUMENT_MODELS, TOOL_REGISTRY


def validate_tool_call(tool_call: ToolCall):
    argument_model = TOOL_ARGUMENT_MODELS.get(tool_call.name)

    if argument_model is None:
        raise ValueError(f"Unknown tool: {tool_call.name}")

    return argument_model.model_validate(tool_call.arguments)


async def execute_tool(tool_call: ToolCall) -> ToolExecutionResult:
    raise NotImplementedError("Implement tool execution.")
