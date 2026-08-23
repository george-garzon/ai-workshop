# Week 10 — AI Security

## Goal
Learn how to safely expose data and tools to an LLM-powered application.

## Learn
- Prompt injection
- Indirect prompt injection
- Data exfiltration
- Jailbreak concepts
- Tool permission boundaries
- PII handling
- Tenant isolation
- RAG authorization
- Malicious uploaded documents
- Output validation
- Secrets management

## Build
Threat-model Project #1 and implement important controls.

### Safer Architecture
```text
User
 ↓
Authentication
 ↓
Authorization
 ↓
Application / AI orchestration
 ↓
Restricted tool layer
 ↓
Database / external APIs
```

Do **not** use the LLM itself as the authorization layer.

## Security Tasks
- Permission-aware retrieval
- Tenant isolation
- Allow-listed tools
- Validate all tool arguments
- Treat model output as untrusted
- Protect secrets from model context
- Require human approval for sensitive actions
- Test malicious instructions inside uploaded documents

## Checkpoint
You should be able to:
- Explain direct and indirect prompt injection
- Explain why an LLM cannot enforce authorization
- Secure RAG retrieval by user/tenant
- Restrict agent tools
- Discuss common AI application attack paths
