"""Exercise 7: isolate the model provider behind two async functions.

Purpose
-------
This is the only module that should need the OpenAI client. It translates your
own AgentState into model input and turns model output into your own contracts.
Keeping that boundary small lets you test the agent with fake decisions first.

Build it yourself
-----------------
1. Start with an async fake in your tests that returns a predetermined decision.
   You can complete and verify the agent loop before integrating a live model.
2. When ready for live calls, obtain settings lazily and create/reuse an async
   client with an appropriate lifecycle. Avoid network calls during import.
3. Build input from the question, caller guidance, previous observations, and
   the permitted tool descriptions in registry.py. Keep application-owned rules
   separate from caller guidance and treat tool output as data, not instructions.
4. For the first version, request one structured decision matching AgentDecision.
   The model proposes a name/arguments or a final answer; Python validates it
   and controls execution. The tool catalog describes choices, not permission.
5. Use the structured-output facilities of your installed SDK and validate the
   result against AgentDecision. Inspect the SDK's supported format when you
   implement this; these exercises deliberately do not provide a provider call.
   Native function-call events use a different shape and would need a separate
   adapter rather than being treated directly as AgentDecision objects.
6. Apply the configured model/output budget. Handle refusals, missing output,
   malformed decisions, timeouts, and provider errors explicitly. Do not silently
   convert a failed call into a fabricated successful answer.
7. Implement final-answer generation using the collected observations with tool
   execution disabled. Summarize what actually happened, including unavailable
   information and failures. This function must not restart the agent loop.

Check your work
---------------
With a fake client, inspect that a second decision sees the first observation.
Verify malformed decisions are rejected. Test that an answer cannot claim a
message was sent when the tool only simulated it or approval was denied.
Only after offline checks pass, try a small live request with a low attempt
limit. Live calls require valid credentials and can incur provider charges.
"""

from app.models.agent import AgentDecision, AgentState


async def choose_next_action(state: AgentState) -> AgentDecision:
    """TODO: request, parse, and validate exactly one proposed next action.

    Read the current state without modifying its counter or executing tools.
    The caller owns those responsibilities. Return an AgentDecision instance,
    not a provider response object or an unchecked JSON string.
    """
    raise NotImplementedError("Exercise 7: implement the model decision boundary.")


async def generate_final_answer(state: AgentState) -> str:
    """TODO: return a plain-language answer grounded in this run's observations.

    If no useful observations exist, say what is unknown. Keep this to one
    bounded summarization call without new actions; the agent decides when it
    is appropriate to call this function.
    """
    raise NotImplementedError("Exercise 7: implement final-answer generation.")
