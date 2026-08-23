# Week 7 — MCP (Model Context Protocol)

## Goal
Understand how AI applications can use a standardized interface to external tools and resources.

## Learn
- MCP architecture
- MCP servers
- MCP clients
- Tools
- Resources
- Prompts
- Authentication
- Authorization
- Security boundaries

## Build
Create your own MCP server around a useful application or dataset.

Example:
```text
Cruise MCP Server

Tools:
- search_cruises()
- get_ship()
- get_itinerary()
- get_price()
- get_ports()
```

Connect an AI client to your server and demonstrate tool execution.

## Security
Do not assume MCP makes integrations automatically safe.

Your server should still enforce:
- Authentication
- Authorization
- Input validation
- Tool-level permissions
- Rate limits where appropriate
- Safe error handling

## Checkpoint
You should be able to:
- Explain MCP in an interview
- Build a basic MCP server
- Expose useful tools/resources
- Connect an AI client
- Explain MCP security boundaries
