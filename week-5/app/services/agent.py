"""Exercise 8: build the bounded observe/decide/act loop.

Purpose
-------
This is the coordinator. It owns the order of operations, working state,
iteration limit, approval gate, and execution trace. The model proposes actions;
Python code decides whether those actions may run. This file should not contain
provider-specific API calls or the actual search/account/message implementations.

Build it yourself, in small increments
-------------------------------------
1. Implement the three helpers at the bottom first.
2. Create fresh state and a separate list of AgentStep records for each request.
   Log the start. Use a fake decision function that immediately returns a final
   answer so you can finish one run without paying for a model call.
3. Add a loop that checks should_continue before each decision attempt. Increment
   state.iteration exactly once BEFORE requesting the decision, even if it fails.
   Record the action or error in a step with that iteration number.
4. Handle a final action by using its answer, or generating an answer from the
   state if one is missing. Return AgentRunResponse with all collected steps.
5. Handle a tool action by checking that a ToolCall exists and validating it
   through services/tools.py. Do not execute unknown or malformed calls.
6. Before execution, consult requires_human_approval even if the model called the
   action an ordinary tool action. Also honor an explicit approval_required
   decision. Store the pending call, ask the approval service, and stop with a
   clear response if it is not approved. Keep prior steps in that response.
7. Execute only an allowed call with any required approval. Clear pending_approval
   after approval, record the tool result in state, and add its safe details to
   the step. The next decision must see that observation, including any error.
8. When the iteration budget is exhausted, return an honest stop message plus
   steps. Optionally summarize observations once with tools disabled. That final
   summary call is separate from the decision budget; document it if you add it.
9. Log a stop reason for each exit. Give errors an explicit path: either stop
   with a useful explanation or retry within the same fixed budget. Start by
   stopping on decision/provider errors; add bounded retries only after that works.

Check your work without a real model
-----------------------------------
- Fake decisions [lookup_account, final] should execute one tool and return two
  steps; the second decision should receive the lookup observation.
- Repeated tool decisions must stop at the configured number of attempts.
- Invalid decisions or tool errors must never create an unbounded loop.
- A denied send_message request must never reach the tool handler.
- A model-proposed approval_required action must use the approval path too.
- Two requests must have independent observations and steps.

Read topics/01_Agent_Loops.md, 03_State.md, 08_Loops.md, and 09_Human_Approval.md.
"""

from typing import Any

from app.models.agent import AgentState
from app.schemas.chat import AgentRunRequest, AgentRunResponse


async def run_agent(request: AgentRunRequest) -> AgentRunResponse:
    """TODO: coordinate a bounded run using the steps above.

    Add service imports as you connect each piece. Await async decisions,
    approvals, and tool execution. Every return path must include the trace;
    avoid returning a success-looking answer after an unhandled tool failure.
    """
    raise NotImplementedError("Exercise 8: implement the agent loop.")


def create_initial_state(request: AgentRunRequest) -> AgentState:
    """TODO: copy instructions/question into a new state with zero attempts.

    Its observations should be empty and pending_approval should be None.
    Do not make an LLM call or load global mutable state in this helper.
    """
    raise NotImplementedError("Exercise 8: initialize per-request state.")


def should_continue(state: AgentState) -> bool:
    """TODO: compare the attempt count with the configured iteration limit.

    Obtain configuration through core/settings.py. This helper only answers a
    question; it must not increment counters or mutate the state. With a limit
    of 3, counts 0, 1, and 2 permit a new attempt; count 3 does not.
    """
    raise NotImplementedError("Exercise 8: enforce the iteration budget.")


def record_observation(state: AgentState, observation: dict[str, Any]) -> None:
    """TODO: append a tool result dictionary to this state's observations.

    Keep successful output and error details distinguishable. Do not increment
    iteration here: run_agent already counts every decision attempt, including
    attempts that produce no observation. This function returns no value.
    """
    raise NotImplementedError("Exercise 8: record a tool observation.")
