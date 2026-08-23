# Week 9 — Production AI Engineering

## Goal
Turn your AI prototype into a system that could realistically serve users.

## Learn
- Redis caching
- Rate limiting
- Queues
- Background workers
- Model fallbacks
- Retries
- Timeouts
- API quotas
- Token budgets
- Prompt caching
- Streaming
- Structured logging
- Monitoring
- Secrets
- Authentication

## Build
Harden Project #1.

Add where appropriate:
- Redis caching
- Background document ingestion
- Rate limiting
- Timeouts
- Retries
- Structured logs
- Token telemetry
- Cost telemetry
- Model fallback strategy

## Cost Exercise
Estimate the cost of operating your application at realistic usage volumes.

Think about:
```text
users
× requests per user
× average input tokens
× average output tokens
× model pricing
```

Then identify ways to reduce cost without destroying answer quality.

## Checkpoint
You should be able to:
- Discuss latency/cost/quality tradeoffs
- Design retry/fallback behavior
- Explain caching opportunities
- Estimate AI infrastructure costs
- Discuss scaling an AI API to large user volumes
