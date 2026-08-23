# Week 2 — Structured Output + Tool Calling

## Goal
Move beyond chat and make an LLM interact safely with application code.

## Learn
- Structured JSON outputs
- Pydantic response schemas
- Function/tool calling
- Tool selection
- Multiple tools
- Validation
- Retry strategies
- Parallel tool calls
- Deterministic workflows vs. agents

## Build
Create an application where a user can make a natural-language request and the model selects an appropriate tool.

Example:
```text
User request
    ↓
LLM
    ↓
Select tool + arguments
    ↓
Application validates arguments
    ↓
Execute tool/API
    ↓
Return structured result
    ↓
LLM generates final answer
```

Prefer a real API or business dataset instead of a toy weather example.

## Important Security Principle
The model may **request** that a tool be called. Your application remains responsible for:
- Authentication
- Authorization
- Argument validation
- Tool permissions
- Actual execution

## Checkpoint
You should be able to:
- Define structured model outputs
- Validate them with Pydantic
- Implement tool calling
- Explain tool calling vs. normal text generation
- Explain why the LLM should not directly control privileged actions
