from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class ToolCall(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    arguments: dict[str, Any] = Field(default_factory=dict)


class AgentDecision(BaseModel):
    model_config = ConfigDict(extra="forbid")

    action: Literal["tool", "final", "approval_required"]
    final_answer: str | None = None
    tool_call: ToolCall | None = None
    reason: str | None = None


class AgentState(BaseModel):
    instructions: str
    question: str
    iteration: int = 0
    observations: list[dict[str, Any]] = Field(default_factory=list)
    pending_approval: ToolCall | None = None


class ToolExecutionResult(BaseModel):
    tool_name: str
    output: Any | None = None
    error: str | None = None
