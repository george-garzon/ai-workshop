"""Exercise 3A: implement three small, deterministic local tools.

Purpose
-------
Each tool performs one concrete action and returns data. Tools do not choose
the next action, call the model, or manage the agent loop. Keeping them ordinary
Python functions makes them easy to understand and verify independently.

Build it yourself
-----------------
1. Create a tiny set of fictional documents and fictional account records in
   this file. A few dictionaries are enough; no database or web service is needed.
2. Implement search and lookup against those fixtures. Keep outputs compatible
   with JSON so they can become observations and API step summaries.
3. Implement send_message as a simulation that describes a proposed message and
   clearly reports a simulated status. Do not connect a real email or messaging
   service for this exercise.
4. Keep all three functions async to match the registry/dispatcher contract.
   Local dictionary operations need no await; real network I/O would later use
   a suitable async client rather than blocking this event loop.
5. Return useful, predictable data. A tool should not invent missing facts or
   hide failures inside prose that looks like a successful result.

Check your work
---------------
Call each function directly with a completed argument model before adding the
agent. Use asyncio.run in a small script or await in an async test. Verify repeat
calls with identical input give identical output. No API key should be needed.
"""

from typing import Any

from app.models.tools import (
    LookupAccountArgs,
    SearchKnowledgeBaseArgs,
    SendMessageArgs,
)


async def search_knowledge_base(args: SearchKnowledgeBaseArgs) -> dict[str, Any]:
    """TODO: search a few fictional notes using a simple text-matching rule.

    Decide whether matching means a substring or individual words and document
    your choice. Return a matches list with enough source information to explain
    a result, such as document id, title, and excerpt. No match should produce
    an empty list, not invented text. Test matching, mixed case, and no match.
    Embeddings or retrieval from earlier weeks are optional later extensions.
    """
    raise NotImplementedError("Exercise 3A: implement local knowledge search.")


async def lookup_account(args: LookupAccountArgs) -> dict[str, Any]:
    """TODO: look up a fictional account by its exact string identifier.

    Include an example account demo-001 so the README request can use it. Return
    a small record with fields such as account_id, name, and plan. For an unknown
    id, choose an explicit not-found result or a documented exception; keep
    services/tools.py consistent with that choice. Never substitute another id.
    """
    raise NotImplementedError("Exercise 3A: implement local account lookup.")


async def send_message(args: SendMessageArgs) -> dict[str, Any]:
    """TODO: simulate a send after the agent's approval gate permits this call.

    Return a clearly labeled simulated status and a summary of the fictional
    action. Do not claim actual delivery. This function does not collect approval;
    the agent controls that before dispatch. Use a fake recipient ending in
    example.test and verify that denied approval leaves this function uncalled.
    """
    raise NotImplementedError("Exercise 3A: implement a simulated message tool.")
