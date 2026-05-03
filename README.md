# Deeptune Hackathon: AI Agent & Sandbox Environment

This repository contains a complete, functional prototype of an Agentic AI system and its corresponding evaluation environment ("The Gym"). It demonstrates a firm understanding of LLM Tool Calling (ReAct patterns), Docker environment isolation, and resilient system engineering.

## 📁 Repository Structure
This project is structured as a **Monorepo** to enforce a strict separation of concerns between the infrastructure (The Gym) and the application logic (The Agent).

```text
deeptune-hackathon/
├── gym-escape-room/                 # The deterministic RL evaluation environment
│   └── Dockerfile                   # The blueprint containing 3 hidden puzzles
│
└── agent-system/                    # The AI solver 
    ├── pyproject.toml               # uv package dependencies
    ├── agent_tools.py               # Docker tooling (The Agent's "hands")
    ├── agent_brain.py               # The main ReAct loop using Anthropic API
    ├── agent_mock_escape_room.py    # Local API mock for the escape room puzzle
    └── agent_mock_loop_breaker.py   # Local API mock demonstrating circuit breakers
