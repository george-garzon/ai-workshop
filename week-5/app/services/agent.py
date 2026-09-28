from app.core.settings import settings
from app.models.agent import AgentState
from app.schemas import AgentRunRequest, AgentRunResponse
from app.services.approval import request_human_approval, requires_human_approval
from app.services.logging import (
    log_agent_decision,
    log_agent_start,
    log_agent_stop,
    log_tool_result,
)
from app.services.openai_service import choose_next_action, generate_final_answer
from app.services.tools import execute_tool


async def run_agent(request: AgentRunRequest) -> AgentRunResponse:
    state = create_initial_state(request)
    log_agent_start(state)

    while should_continue(state):
        decision = await choose_next_action(state)
        log_agent_decision(decision)

        if decision.action == "final":
            final_answer = decision.final_answer or await generate_final_answer(state)
            log_agent_stop(state, "final")
            return AgentRunResponse(response=final_answer)

        if decision.tool_call is None:
            raise ValueError("Tool decision did not include a tool call.")

        if requires_human_approval(decision.tool_call):
            approved = await request_human_approval(decision.tool_call)
            if not approved:
                log_agent_stop(state, "approval_denied")
                return AgentRunResponse(response="Action cancelled.")

        result = await execute_tool(decision.tool_call)
        log_tool_result(result)
        record_observation(state, result.model_dump())

    final_answer = await generate_final_answer(state)
    log_agent_stop(state, "max_iterations")
    return AgentRunResponse(response=final_answer)


def create_initial_state(request: AgentRunRequest) -> AgentState:
    return AgentState(
        instructions=request.instructions,
        question=request.question,
    )


def should_continue(state: AgentState) -> bool:
    return state.iteration < settings.max_agent_iterations


def record_observation(state: AgentState, observation: dict) -> None:
    state.iteration += 1
    state.observations.append(observation)
