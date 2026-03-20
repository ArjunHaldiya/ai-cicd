# CI/CD Pipeline

An autonomous code review pipeline that uses multi-agent AI to block bad code from being deployed. Every pull request is automatically reviewed by three parallel AI agents before merging is allowed.

## How It Works

```
Pull Request
     │
     ▼
┌────────────────────────┐
│   Orchestrator         │  coordinates all agents in parallel
└────────────────────────┘
     │          │          │
     ▼          ▼          ▼
Security    Performance   Style
 Agent        Agent       Agent
     │          │          │
     └────┬─────┘          │
          ▼                ▼
      ❌ BLOCKED      ✅ APPROVED
      (any failure)   (all pass)
```

Each agent runs **simultaneously** via `ThreadPoolExecutor` — total review time equals the slowest agent, not the sum of all three.

## Agents

| Agent | Checks For |
|---|---|
| Security | Hardcoded secrets, SQL injection, unsafe imports, missing input validation |
| Performance | Nested loops, inefficient data structures, redundant computations |
| Style | Naming conventions, missing docstrings, code formatting |

## Stack

- **Python** — orchestrator + agents
- **Mistral** — AI model powering each agent
- **GitHub Actions** — CI/CD trigger on every PR
- **MCP** — exposes the pipeline as a tool for AI assistants

## Setup

```bash
git clone https://github.com/your-username/ai-cicd-pipeline
cd ai-cicd-pipeline
pip install -r requirements.txt
```

Create a `.env` file:
```
MODEL_API=your-api-key-here
```

## Usage

**Run locally:**
```bash
python3 pipeline.py
```

**Use as MCP tool:**
```bash
python3 mcp_server.py
```

**CI/CD:** Automatic on every pull request via GitHub Actions. Failed reviews block the merge.

## Adding a New Agent

1. Create `agents/new_agent.py` inheriting the same pattern
2. Add it to `orchestrator.py`
3. All three (or more) must pass for deployment

## Production Notes

- API calls use retry with exponential backoff (3 attempts, 1/2/4s delays)
- JSON parse failures return structured error dicts — pipeline never crashes
- API keys stored in `.env` locally and GitHub Secrets in CI/CD
- Never commit `.env` — it's in `.gitignore`