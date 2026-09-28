from app.models.agent import AgentDecision, AgentState, ToolExecutionResult


def log_agent_start(state: AgentState) -> None:
    pass


def log_agent_decision(decision: AgentDecision) -> None:
    pass


def log_tool_result(result: ToolExecutionResult) -> None:
    pass


def log_agent_stop(state: AgentState, reason: str) -> None:
    pass
