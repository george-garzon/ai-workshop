# Agent Fundamentals

Run the API:

```bash
fastapi dev app/main.py
```

Example request:

```json
{
  "instructions": "Use the available tools when needed. Ask for approval before sensitive actions.",
  "question": "Look up the account and draft a response."
}
```

This week is intentionally scaffolded with empty functions so the agent loop can be implemented step by step.
