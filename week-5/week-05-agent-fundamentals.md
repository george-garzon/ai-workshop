# Week 5 — Agent Fundamentals

## Goal
Understand what an AI agent actually is before relying on agent frameworks.

## Learn
- Agent loops
- Tools
- State
- Memory
- Planning
- Routing
- Retries
- Loops
- Human approval
- Deterministic vs. agentic workflows

## Build
Implement a small agent loop yourself in Python.

```text
User
 ↓
LLM
 ↓
Choose action
 ↓
Call permitted tool
 ↓
Observe result
 ↓
Need another action?
 ↙             ↘
Yes             No
 ↓               ↓
Continue       Final answer
```

Give the agent only a small, controlled set of tools.

Add:
- Maximum iteration count
- Tool validation
- Error handling
- Logging
- Human approval for sensitive actions

## Questions to Answer
- When should I use an agent?
- When is a normal workflow better?
- What happens if an agent gets stuck in a loop?
- Who controls tool permissions?
- What state needs to survive between steps?

## Checkpoint
You should be able to:
- Build a basic agent loop without a framework
- Explain agent vs. workflow
- Explain state and tool execution
- Prevent uncontrolled loops
- Restrict agent capabilities
