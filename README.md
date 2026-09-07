# Zero Trust for AI Agents

Experimental research on applying Zero-Trust security principles to
tool-using AI agents.

## Research Question

Can runtime authorization and risk-aware policy enforcement prevent
AI agents from converting malicious or untrusted context into
unauthorized consequential actions ? 

## Motivation

Modern AI agents can interact with external tools, APIs, databases,
files, and other systems. Authentication and static authorization
can establish who an agent is and what capabilities it possesses,
but they do not necessarily determine whether a specific action
should be allowed in its current context.

This project investigates whether Zero-Trust principles can be
extended from identity and access control toward runtime,
action-level authorization for AI agents.

## Experimental Architecture

```text
User
  |
  v
AI Agent
  |
  v
Security Layer
  |
  v
MCP Server
  |
  +---- Tool A
  +---- Tool B
  +---- Tool C