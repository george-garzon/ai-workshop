from app.models.agent import AgentDecision, AgentState


async def choose_next_action(state: AgentState) -> AgentDecision:
    raise NotImplementedError("Implement LLM decision step.")


async def generate_final_answer(state: AgentState) -> str:
    raise NotImplementedError("Implement final answer generation.")
