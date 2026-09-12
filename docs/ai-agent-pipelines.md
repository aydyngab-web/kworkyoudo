# AI Agent Pipeline & Local AI Integration

Sanitized portfolio case based on a real automation project.

## Problem

Build a Telegram-controlled AI workflow where a language model can turn a user request into a structured plan and a local executor can carry out the approved steps.

## Architecture

```text
Telegram
   ↓
LLM Planner
   ↓
Structured / JSON Task Plan
   ↓
Local Agent Executor
   ↓
Tool / Computer Actions
   ↓
Step Results + Context
```

## Implemented concepts

- Telegram as the human-facing control layer
- LLM-based planning through an API
- Alternative local/model gateway configuration
- Task decomposition into smaller executable steps
- Structured plan exchange between planner and executor
- Context propagation between workflow steps
- Timeouts and stop-on-error behavior
- Local execution instead of requiring every action to run in a cloud service

## Model / integration experiments

The project explored more than one model path, including a Groq-hosted Llama configuration and a Nemotron-based local/gateway configuration. The engineering focus was the orchestration layer rather than dependence on one model vendor.

## Portfolio value

This case demonstrates AI-agent orchestration, LLM API integration, local AI workflows, structured outputs, Telegram automation and reliability controls.

## Security

Production tokens, machine-specific configuration and private endpoints are intentionally excluded from this portfolio description.
