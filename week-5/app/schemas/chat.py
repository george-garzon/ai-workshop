from typing import Any

from pydantic import BaseModel, Field


class AgentRunRequest(BaseModel):
    instructions: str = Field(description="System-level guidance for the agent.")
    question: str = Field(description="The user's request.")


class AgentStep(BaseModel):
    iteration: int
    action: str | None = None
    tool_name: str | None = None
    tool_arguments: dict[str, Any] | None = None
    observation: Any | None = None
    error: str | None = None


class AgentRunResponse(BaseModel):
    response: str
    steps: list[AgentStep] = Field(default_factory=list)
