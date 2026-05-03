# Deeptune Hackathon Test: AI Agent & Sandbox Environment

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
```

## 🧠 Ultimate Gym Escape Room  
**Autonomous AI Agent + Deterministic Docker Sandbox**

An AI agent that navigates a constrained Linux environment to solve multi-step challenges using real shell tools—focused on **reliability, tool use, and failure recovery**.

---

## 🚀 Overview

**🏋️ Gym (Sandbox):**  
Deterministic Docker environment with challenges involving:
- File system navigation  
- Shell commands  
- Environment variables  
- SQLite queries  

**🤖 Agent System:**  
LLM-powered agent (Claude 3.5 Sonnet) that:
- Executes commands via Docker  
- Iteratively reasons toward solutions  
- Recovers from failure with built-in safeguards  

---

## 🧩 Challenges

| Challenge | Skill | Tools |
|----------|------|------|
| Encoded File | Decoding | `cat`, `base64` |
| Env Variable | Inspection | `env`, `grep` |
| Database | Querying | `sqlite3` |

The agent must infer and execute the correct command sequence autonomously.

---

## 🏗️ Architecture

**Deterministic Sandbox**
- Docker-based isolation  
- SQLite for fast, reproducible runs  

**Tool Execution**
- LLM outputs → shell commands  
- Supports chaining via:

```bash
sh -c 'command'
```
