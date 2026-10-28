# Week 5: build an agent yourself

This app is now a learning scaffold. The completed agent loop, validation logic,
route wiring, model fields, and populated registry have been cleared. Each Python
file explains its purpose, what you need to implement, how it connects to the
other files, and how to check your work. Function signatures and model names
remain as a starting structure; the solutions are yours to write.

**Start with [app/schemas/chat.py](app/schemas/chat.py), then follow the build order
below.** Read one file's instructions, implement a small piece, and verify it
before moving on. You do not need a real model or API key for the first stages.

## What works at the starting point

- `app/main.py` creates a minimal FastAPI application; `/docs` can open.
- `/health` and `/api/agent` are intentionally not registered yet and return 404.
- Exercise functions raise `NotImplementedError` with the exercise to complete.
- Pydantic classes are empty shells. They import, but do not yet validate the
  documented fields. A successful import does not mean a model is finished.
- The tool registry is empty. No tools are available until you populate it.
- Configuration loading, model calls, and tool execution are not implemented.

The dependency declarations and environment template remain, with explanatory
comments. The original [lesson](week-05-agent-fundamentals.md) and your notes in
`topics/` remain as learning references. Package `__init__.py` files explain
their roles; most need no executable code. Previous tracked code remains in Git
history if you later want to compare your approach.

## How the pieces fit together

```text
HTTP JSON request
    |
    v
main.py -> api/routes/chat.py -> services/agent.py
                 |                    |
        schemas/chat.py        working AgentState
                                      |
                         services/openai_service.py
                            proposes AgentDecision
                                      |
                  validate tool + check approval policy
                                      |
                           services/tools.py
                                      |
                         tools/registry.py selects
                                      |
                         tools/sample_tools.py runs
                                      |
                          record the observation
                                      |
                    another bounded decision or stop
                                      |
                      AgentRunResponse -> HTTP JSON
```

The model chooses a proposed next step. Your Python code owns the available
tools, argument validation, approval requirements, and stopping rules. State
holds information for one run; persistent memory across runs is a later feature.

## File map

| File | Responsibility | What you will build |
| --- | --- | --- |
| `app/schemas/chat.py` | Public JSON contracts | Request, execution step, and response fields and validation |
| `app/models/agent.py` | Internal agent contracts | Tool call, decision, state, and result models |
| `app/models/tools.py` | Inputs accepted by each tool | Required fields and rejection of invalid/extra arguments |
| `app/core/settings.py` | Environment-backed configuration | Settings fields, positive limits, and lazy loading |
| `app/tools/sample_tools.py` | Concrete local actions | Fictional note search, account lookup, and simulated sending |
| `app/tools/registry.py` | Available capabilities | Name-to-handler/model mappings, descriptions, and sensitive names |
| `app/services/tools.py` | Shared tool execution mechanics | Validation, dispatch, awaiting handlers, and result normalization |
| `app/services/approval.py` | Human permission boundary | Sensitive-tool checks and an explicit approval contract |
| `app/services/logging.py` | Developer-facing execution events | Start, decision, tool outcome, and stop logs |
| `app/services/openai_service.py` | Model-provider boundary | One validated decision or one final summary per call |
| `app/services/agent.py` | Coordination and stopping rules | Bounded loop, observations, approval gate, and steps |
| `app/api/routes/chat.py` | HTTP-facing handlers | Service delegation, appropriate errors, and health response |
| `app/main.py` | Application entry point | Route registration and application setup |
| `app/**/__init__.py` | Python package boundaries | Understand imports; keep these files minimal |
| `tests/__init__.py` | Testing roadmap and package marker | Add your own test modules as you finish features |
| `pyproject.toml` | Project metadata and dependencies | Understand the environment; retain setup while learning |
| `.env.example` | Non-secret configuration template | Copy to `.env` and supply local values when needed |
| `topics/*.md` | Your short conceptual notes | Revisit and expand them as each concept becomes concrete |
| `week-05-agent-fundamentals.md` | Original assignment and checkpoint | Use it to assess your understanding at the end |

## Suggested build order

1. **Define your data (1A–1C).** Complete the public schemas, agent models, and
   tool argument models. Construct valid examples and deliberately invalid ones.
   Check that two independent states do not share their observations list.
2. **Load settings (2).** Add configuration fields and validate positive numeric
   limits. Call the loader only when needed. Offline checks can supply explicit
   dummy credentials to settings without ever constructing a live API client.
3. **Write local tools and register them (3A–3B).** Use fictional records, including
   account `demo-001`. Choose and document predictable result shapes. Sending
   stays simulated. Check that every registered name has an argument model and
   description, and that `send_message` is marked sensitive.
4. **Validate and dispatch (4).** Call a known tool with valid arguments. Then try
   an unknown tool, a missing argument, and an unexpected argument. None of those
   invalid cases should reach a handler.
5. **Add the approval boundary (5).** Default to leaving an action unapproved when
   there is no human decision. Use explicit approve/deny fakes in tests. A real
   approval UI, persistence, and resume endpoint are optional later work.
6. **Add logs (6).** Capture useful event metadata without raw credentials or
   message content. Distinguish developer logs from the client-visible steps.
7. **Understand the model boundary (7).** First use a fake async decision source
   in your checks. Save live SDK integration until your loop works offline.
8. **Build the loop (8).** Start with an immediate final answer. Next add one tool
   followed by a final answer. Then cover approval, errors, and the iteration
   limit. Count every decision attempt, and retain steps on every return path.
9. **Implement handlers (9).** Keep HTTP concerns here and agent behavior in the
   service. Health must not depend on model credentials or tool execution.
10. **Wire the app (10).** Register routes before including the router. Check
    `/docs`, `/health`, and a request to `/api/agent` using your fake agent first.
11. **Finish checks and try a live model (11).** Follow the testing ideas in
    `tests/__init__.py`, then complete live model integration in exercise 7.
    Start with a small read-only task and a low iteration limit.

For each stage, explain the input, output, caller, and failure cases aloud before
coding. If you cannot explain a function yet, sketch a concrete example first.
The in-file docstrings give contracts and hints without the completed algorithms.

## Running the scaffold

From the repository root, enter this week's directory. Other weeks also contain
an `app` package, so use `week-5` as your working directory in PyCharm too.

Using the project's uv setup:

```bash
cd week-5
uv sync
uv run uvicorn app.main:app --reload
```

The project declares Python 3.14 or newer. If you use an already configured
environment instead, install this project's declared dependencies there and
run `python -m uvicorn app.main:app --reload` with that interpreter. The command
uses Uvicorn directly, which is already declared as a dependency.

Open `http://127.0.0.1:8000/docs`. Initially, no application endpoints appear;
that is expected until exercise 10. Starting the scaffold does not call an LLM.

When you implement configuration, copy `.env.example` to `.env` inside `week-5`
and fill in your own values. Keep real credentials out of source control and
logs. A real key is only needed for live provider integration.

After implementing and wiring the API, try this JSON in `POST /api/agent`:

```json
{
  "instructions": "Use the available tools when needed. Ask for approval before sensitive actions.",
  "question": "Look up account demo-001 and summarize its plan."
}
```

Expected behavior: the agent uses your local account lookup, observes its actual
result, and returns an answer with a steps list. A stubbed decision sequence makes
this predictable during testing; a live model may choose a different sequence.
Caller instructions are guidance, and must not override application policy.

## Checking your progress

Standard-library tests need no extra test framework. Once you write your tests:

```bash
uv run python -m unittest discover -s tests -v
```

Before adding test modules, this command discovers zero tests; that does not
verify the implementation. If you choose FastAPI's TestClient later, add its
required `httpx` dependency to your development setup. Keep all automated checks
offline by substituting the provider and any approval decision.

- [ ] Blank/invalid input is rejected before the agent begins.
- [ ] Unknown tools and invalid arguments never reach a handler.
- [ ] One tool result becomes an observation visible to the next decision.
- [ ] Unapproved sensitive actions never execute.
- [ ] Repeated decisions and errors cannot bypass the iteration budget.
- [ ] Normal, failed, unapproved, and limited runs preserve their steps.
- [ ] Requests have independent state; imports do not require credentials.
- [ ] Simulated sending is never described as real delivery.
- [ ] The API routes appear correctly and health works without a model call.

When these are complete, revisit the original lesson's questions and explain
which decisions in your app are deterministic and which are made by the model.
