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

# 🧠 Ultimate Gym Escape Room  
**Autonomous AI Agent + Deterministic Docker Sandbox**

An experimental system where an AI agent autonomously navigates a constrained Linux environment to solve multi-step challenges using real command-line tools.

This project explores **agent reliability, tool use, and failure recovery** in a fully controlled, reproducible environment.

---

## 🚀 Overview

The system is composed of two parts:

### 🏋️ The "Ultimate Gym" (Sandbox Environment)
A deterministic Ubuntu-based Docker container containing structured challenges that require:
- File system navigation  
- Shell command composition  
- Environment inspection  
- Database querying (SQLite)  

### 🤖 The Agent System
A Python-based autonomous agent powered by an LLM (Claude 3.5 Sonnet) that:
- Interacts with Docker as its execution environment  
- Generates and runs shell commands  
- Iteratively reasons toward solutions  
- Handles failure through built-in safeguards  

---

## 🧩 What the Agent Solves

Inside the Gym, the agent must discover hidden values across three domains:

| Challenge | Skill Tested | Example Tooling |
|----------|-------------|----------------|
| Encoded File | File system + decoding | `cat`, `base64` |
| Environment Variable | System inspection | `env`, `grep` |
| Database Query | Structured data access | `sqlite3` |

The agent is not given explicit instructions — it must **infer and execute the correct sequence of commands**.

---

## 🏗️ Architecture Highlights

### Deterministic Sandbox Design
- Built on Docker for full isolation  
- Uses SQLite instead of external DB services  
- Ensures **fast startup + reproducibility**  
- Designed for scaling into RL or batch agent evaluation  

---

### Tool Execution Layer
- LLM outputs are translated into executable shell commands  
- Commands are wrapped in:

```bash
sh -c 'command'
