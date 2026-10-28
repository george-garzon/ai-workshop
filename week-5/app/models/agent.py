"""Exercise 1B: model the agent's internal working data.

Purpose
-------
These objects connect the decision service, loop, approval checks, and tool
executor. They are internal contracts, separate from the public HTTP schemas.
Agreeing on their shapes first makes each later function easier to implement.

Build it yourself
-----------------
1. Implement ToolCall, then AgentDecision, then AgentState and ToolExecutionResult.
2. Use Literal for a fixed set of action names and ConfigDict(extra="forbid")
   where unexpected model-generated fields should be rejected.
3. Give mutable collections a default_factory. Each run needs independent state.
4. Validate relationships between decision fields: a tool action must include
   a tool call. Use a model validator or an explicit check at the loop boundary.
5. Keep state local to one run. Persistent memory across requests is a separate
   feature, so no global AgentState object should be created here.

Check your work
---------------
An unknown action should fail. A tool action without a tool_call should fail.
Two new states must not share observations. Explain why observations contain
tool results while AgentRunResponse.steps describes the run for a client.
"""
from typing import Literal
from pydantic import BaseModel, Field


class ToolCall(BaseModel):
    """TODO: add name and arguments.

    name: required nonblank string; the executor later checks registry membership.
    arguments: dictionary from strings to JSON-compatible values, initially empty.

    Example data: name="lookup_account", arguments={"account_id": "demo-001"}.
    A correctly shaped ToolCall is only a proposal, not permission to execute.
    """

    name: str
    arguments: dict[str,str]


class AgentDecision(BaseModel):
    """TODO: define one proposed next action.

    action: one of "tool", "final", or "approval_required".
    final_answer: optional string; a final action can use it or ask the separate
        final-answer service to summarize existing observations when it is absent.
    tool_call: optional ToolCall; required for tool and approval_required actions.
    reason: optional short action explanation, not a private reasoning transcript.

    Reject contradictory combinations, such as a final action carrying a tool
    call. An approval_required action pauses for a human; the model cannot grant
    approval itself. Application policy must also check ordinary tool actions.
    """

    action: Literal["tool", "final", "approval_required"] = Field(
        default="final",
        description="The action to perform"
    )
    final_answer: str | None = Field(default=None)
    tool_call: ToolCall | None = Field(default=None)
    reason: str | None = Field(default=None)


class AgentState(BaseModel):
    """TODO: define the working state for one user request.

    instructions: required string copied from the request.
    question: required string copied from the request.
    iteration: nonnegative integer, initially 0; count decision attempts, including
        unsuccessful attempts, so errors cannot bypass the iteration limit.
    observations: fresh list of dictionaries holding tool outputs and errors.
    pending_approval: optional ToolCall, initially None, identifying a paused action.

    The run's AgentStep list can be maintained separately in run_agent. If you
    choose to store it here instead, document that decision consistently.
    """

    instructions: str
    question: str
    iteration: int = Field(ge=0)
    observations: dict
    pending_approval: ToolCall | None = Field(default=None)

class ToolExecutionResult(BaseModel):
    """TODO: provide one consistent result shape for every tool.

    tool_name: required string recording which tool was attempted.
    output: optional JSON-compatible result, initially None.
    error: optional readable failure message, initially None.

    For this exercise, success has output with no error; failure has an error
    with no output. Never disguise a failed tool as an empty successful result.
    """

    tool_name: str
    output: str | None = Field(default=None)
    error: str | None = Field(default=None)
