"""Exercise 5: separate human permission from model proposals.

Purpose
-------
The agent can propose sending a message, but application policy decides whether
that needs approval. This module answers the policy question and provides the
boundary where a real human decision would enter the system.

Build it yourself
-----------------
1. Implement requires_human_approval using the sensitive names in the registry.
   Tool validation is a separate step; an unknown tool is not safe merely because
   it is absent from the sensitive set.
2. Decide what the person needs to review: the tool name and exact arguments.
   Approval for one recipient/body must not authorize a different message.
3. For the first local version, make request_human_approval fail closed: when
   there is no actual human decision, return an unapproved result. In loop tests,
   substitute an async fake that explicitly approves or denies a known call.
4. Keep send_message simulated. A real HTTP approval flow is a later extension:
   store a pending action, return an identifier to a UI, and resume only after
   a verified human response. This scaffold supplies no persistence or resume API.
5. Avoid input() inside an async HTTP handler; it would block waiting for terminal
   input that the HTTP caller cannot provide. A separate CLI experiment can use
   terminal confirmation if you deliberately build one.

Check your work
---------------
send_message must require approval; read-only demo tools need not. With approval
denied or unavailable, verify that the agent never invokes the sending handler.
The model saying "approved" in its output is not a human decision.
"""

from app.models.agent import ToolCall


def requires_human_approval(tool_call: ToolCall) -> bool:
    """TODO: consult application-owned policy for this tool name."""
    raise NotImplementedError("Exercise 5: identify tools needing approval.")


async def request_human_approval(tool_call: ToolCall) -> bool:
    """TODO: return whether this exact action has explicit human approval.

    Until a real approval mechanism exists, the local implementation must leave
    the action unapproved. A boolean cannot distinguish pending from denied;
    explain that limitation in the stop message or extend the contract later.
    """
    raise NotImplementedError("Exercise 5: implement the approval boundary.")
