# Week 6 — LangGraph + Stateful Workflows

## Goal
Use an orchestration framework after understanding the underlying agent mechanics.

## Learn
- LangGraph nodes
- Edges
- State
- Conditional routing
- Persistence
- Checkpoints
- Tool nodes
- Human-in-the-loop
- Multi-agent concepts

## Build
Create a stateful research or document-analysis workflow.

Example:
```text
User request
    ↓
Analyze request
    ↓
Retrieve information
    ↓
Evaluate result
    ↓
Enough information?
 ↙               ↘
No                Yes
 ↓                  ↓
Retrieve again    Generate answer
```

Add:
- Persistent state
- Conditional branches
- Checkpoints
- Tool execution
- Human approval where appropriate

Integrate a useful LangGraph workflow into Project #1.

## Career Task
Begin applying to targeted AI engineering roles this week rather than waiting until the entire 12-week plan is complete.

## Checkpoint
You should be able to:
- Explain nodes, edges, and state
- Build conditional workflows
- Persist workflow state
- Explain what LangGraph provides beyond a plain Python agent loop
