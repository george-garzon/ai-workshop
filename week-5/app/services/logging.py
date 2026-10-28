"""Exercise 6: make the agent's behavior observable.

Purpose
-------
Logs help you understand why a run stopped or which tool failed. They are for
the developer; the steps list in an API response is a separate client-facing
summary. This module centralizes logging so other services do not scatter print
statements throughout the loop.

Build it yourself
-----------------
1. Use Python's standard logging module and create a named logger for this module.
2. Configure log level/format once at the application entry point when wiring it;
   do not repeatedly configure the root logger inside these functions.
3. Implement the four events below. Use consistent field labels so the sequence
   of decisions and tool outcomes is easy to follow.
4. Log metadata, not API keys, complete prompts, message bodies, or account data.
   Prefer tool names, action types, attempt counts, and success/failure labels.
5. Return None; logging should not change state, choose actions, or execute tools.

Check your work
---------------
Capture logs for a fake run and verify start, decision, result, and stop appear
in order. Include an error case. Check that secrets and message bodies do not
appear. Later, add a run identifier if concurrent requests become hard to trace.
"""

from app.models.agent import AgentDecision, AgentState, ToolExecutionResult


def log_agent_start(state: AgentState) -> None:
    """TODO: log a start event with safe metadata, such as the initial counter."""
    raise NotImplementedError("Exercise 6: log the start of a run.")


def log_agent_decision(decision: AgentDecision) -> None:
    """TODO: log the action and tool name, handling decisions without a tool."""
    raise NotImplementedError("Exercise 6: log a decision.")


def log_tool_result(result: ToolExecutionResult) -> None:
    """TODO: log the tool name and whether it succeeded; omit raw payloads."""
    raise NotImplementedError("Exercise 6: log a tool outcome.")


def log_agent_stop(state: AgentState, reason: str) -> None:
    """TODO: log the attempt count and reason (final, limit, unapproved, error)."""
    raise NotImplementedError("Exercise 6: log why a run stopped.")
